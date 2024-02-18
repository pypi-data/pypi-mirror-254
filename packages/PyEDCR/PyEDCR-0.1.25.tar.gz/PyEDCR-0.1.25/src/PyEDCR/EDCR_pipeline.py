import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import multiprocessing as mp
import multiprocessing.managers
import warnings

warnings.filterwarnings('ignore')

import vit_pipeline
import utils
import data_preprocessing
import context_handlers

figs_folder = 'figs/'

main_model_name = 'vit_b_16'
main_lr = 0.0001
epochs_num = 20

secondary_model_name = 'vit_l_16'
secondary_lr = 0.0001

num_epsilons = 40
combined = True
conditions_from_main = True
loss = "BCE"

dist = 0.005

combined_caption = 'without_constraint'
main_coarse_path = None
main_fine_path = None
secondary_coarse_path = None
secondary_fine_path = None

def get_binary_condition_values(example_index: int,
                                fine_cla_datas: np.array,
                                coarse_cla_datas: np.array):
    res = []
    for fine_i, fine_cls in enumerate(fine_cla_datas[:, example_index].astype(int)):
        for coarse_i, coarse_cls in enumerate(coarse_cla_datas[:, example_index].astype(int)):
            pred = int(fine_cls & coarse_cls)
            consistent = int(pred & (data_preprocessing.fine_to_course_idx[fine_i] == coarse_i))
            res += [pred, consistent]

    return res


def get_unary_condition_values(example_index: int,
                               cla_datas: np.array):
    return [int(cls[example_index]) for cls in cla_datas]


def get_scores(y_true: np.array,
               y_pred: np.array):
    try:
        y_actual = y_true
        y_hat = y_pred
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        for i in range(len(y_hat)):
            if y_actual[i] == y_hat[i] == 1:
                TP += 1
            if y_hat[i] == 1 and y_actual[i] != y_hat[i]:
                FP += 1
            if y_actual[i] == y_hat[i] == 0:
                TN += 1
            if y_hat[i] == 0 and y_actual[i] != y_hat[i]:
                FN += 1
        # print(f"TP:{TP}, FP:{FP}, TN:{TN}, FN:{FN}")

        pre = precision_score(y_true, y_pred)
        rec = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        acc = accuracy_score(y_true, y_pred)
        return [pre, rec, f1, acc]
    except:
        pre = accuracy_score(y_true, y_pred)
        rec = recall_score(y_true, y_pred, average='macro')
        f1 = f1_score(y_true, y_pred, average='macro')
        acc = accuracy_score(y_true, y_pred)

        return [pre, rec, f1, acc]


def generate_chart(n_classes: int,
                   charts: list) -> list:
    all_charts = [[] for _ in range(n_classes)]

    for data in charts:
        for count, jj in enumerate(all_charts):
            # pred, corr, tp, fp, cond1, cond2 ... condn
            each_items = []
            for d in data[:2]:
                if d == count:
                    each_items.append(1)
                else:
                    each_items.append(0)

            if each_items[0] == 1 and each_items[1] == 1:
                each_items.append(1)
            else:
                each_items.append(0)
            if each_items[0] == 1 and each_items[1] == 0:
                each_items.append(1)
            else:
                each_items.append(0)

            each_items.extend(data[2:])
            jj.append(each_items)

    return all_charts


def DetUSMPosRuleSelect(i: int,
                        all_charts: list):
    chart = all_charts[i]
    chart = np.array(chart)
    rule_indexs = [i for i in range(4, len(chart[0]))]
    each_sum = np.sum(chart, axis=0)
    tpi = each_sum[2]
    fpi = each_sum[3]
    pi = tpi * 1.0 / (tpi + fpi)

    pb_scores = []
    for ri in rule_indexs:
        posi = np.sum(chart[:, 1] * chart[:, ri], axis=0)
        bodyi = np.sum(chart[:, ri], axis=0)
        score = posi * 1.0 / bodyi
        if score > pi:
            pb_scores.append((score, ri))
    pb_scores = sorted(pb_scores)
    cci = []
    ccn = pb_scores
    for (score, ri) in pb_scores:

        cii = 0
        for (cs, ci) in cci:
            cii = cii | chart[:, ci]
        POScci = np.sum(cii * chart[:, 1], axis=0)
        BODcci = np.sum(cii, axis=0)
        POSccij = np.sum((cii | chart[:, ri]) * chart[:, 1], axis=0)
        BODccij = np.sum((cii | chart[:, ri]), axis=0)

        cni = 0
        cnij = 0
        for (cs, ci) in ccn:
            cni = (cni | chart[:, ci])
            if ci == ri:
                continue
            cnij = (cnij | chart[:, ci])
        POScni = np.sum(cni * chart[:, 1], axis=0)
        BODcni = np.sum(cni, axis=0)
        POScnij = np.sum(cnij * chart[:, 1], axis=0)
        BODcnij = np.sum(cnij, axis=0)

        a = POSccij * 1.0 / (BODccij + 0.001) - POScci * 1.0 / (BODcci + 0.001)
        b = POScnij * 1.0 / (BODcnij + 0.001) - POScni * 1.0 / (BODcni + 0.001)
        if a >= b:
            cci.append((score, ri))
        else:
            ccn.remove((score, ri))

    cii = 0
    for (cs, ci) in cci:
        cii = cii | chart[:, ci]
    POScci = np.sum(cii * chart[:, 1], axis=0)
    BODcci = np.sum(cii, axis=0)
    new_pre = POScci * 1.0 / (BODcci + 0.001)
    if new_pre < pi:
        cci = []
    cci = [c[1] for c in cci]
    # print(f"class{count}, cci:{cci}, new_pre:{new_pre}, pre:{pi}")

    return cci


def GreedyNegRuleSelect(i: int,
                        epsilon: float,
                        all_charts: list):
    chart = all_charts[i]
    chart = np.array(chart)
    rule_indexs = [i for i in range(4, len(chart[0]))]
    each_sum = np.sum(chart, axis=0)
    tpi = each_sum[2]
    fpi = each_sum[3]
    pi = tpi * 1.0 / (tpi + fpi)
    ri = tpi * 1.0 / each_sum[1]
    ni = each_sum[0]
    quantity = epsilon * ni * pi / ri
    # print(f"class{count}, quantity:{quantity}")

    NCi = []
    NCn = []
    for rule in rule_indexs:
        negi_score = np.sum(chart[:, 2] * chart[:, rule])
        if negi_score < quantity:
            NCn.append(rule)

    with context_handlers.WrapTQDM(total=len(NCn)) as progress_bar:
        while NCn:
            best_score = -1
            best_index = -1
            for c in NCn:
                tem_cond = 0
                for cc in NCi:
                    tem_cond |= chart[:, cc]
                tem_cond |= chart[:, c]
                posi_score = np.sum(chart[:, 3] * tem_cond)
                if best_score < posi_score:
                    best_score = posi_score
                    best_index = c
            NCi.append(best_index)
            NCn.remove(best_index)
            tem_cond = 0
            for cc in NCi:
                tem_cond |= chart[:, cc]
            tmp_NCn = []
            for c in NCn:
                tem = tem_cond | chart[:, c]
                negi_score = np.sum(chart[:, 2] * tem)
                if negi_score < quantity:
                    tmp_NCn.append(c)
            NCn = tmp_NCn

            if utils.is_local():
                time.sleep(0.1)
                progress_bar.update(1)

        # print(f"class:{i}, NCi:{NCi}")

    return NCi


def ruleForNPCorrection_worker(i: int,
                               chart: list,
                               epsilon: float,
                               all_charts: list[list],
                               main_granularity: str,
                               run_positive_rules: bool,
                               total_results: multiprocessing.managers.ListProxy,
                               shared_index: multiprocessing.managers.ValueProxy,
                               error_detections: multiprocessing.managers.DictProxy,
                               consistency_constraints_for_main_model: dict[str, set]
                               ):
    chart = np.array(chart)
    NCi = GreedyNegRuleSelect(i=i,
                              epsilon=epsilon,
                              all_charts=all_charts)
    neg_i_count = 0
    pos_i_count = 0

    predict_result = np.copy(chart[:, 0])
    tem_cond = np.zeros_like(chart[:, 0])

    for cc in NCi:
        tem_cond |= chart[:, cc]

    classes = data_preprocessing.fine_grain_classes if main_granularity == 'fine' \
        else data_preprocessing.coarse_grain_classes
    curr_class = classes[i]

    recovered = set()

    if np.sum(tem_cond) > 0:
        for example_index, example_values in enumerate(chart):
            if tem_cond[example_index] and predict_result[example_index]:
                neg_i_count += 1
                predict_result[example_index] = 0

                condition_values = example_values[4:]

                if main_granularity == 'coarse':
                    fine_grain_condition_values = condition_values[:len(data_preprocessing.fine_grain_classes)]
                    fine_grain_prediction = data_preprocessing.fine_grain_classes[
                        np.argmax(fine_grain_condition_values)]
                    derived_coarse_grain_prediction = data_preprocessing.fine_to_coarse[fine_grain_prediction]

                    if derived_coarse_grain_prediction != curr_class:
                        recovered = recovered.union({fine_grain_prediction})
                else:
                    coarse_grain_condition_values = condition_values[len(data_preprocessing.fine_grain_classes):
                                                                     len(data_preprocessing.fine_grain_classes) +
                                                                     len(data_preprocessing.coarse_grain_classes)]
                    coarse_grain_prediction = data_preprocessing.coarse_grain_classes[
                        np.argmax(coarse_grain_condition_values)]
                    derived_coarse_grain_prediction = data_preprocessing.fine_to_coarse[curr_class]

                    if coarse_grain_prediction != derived_coarse_grain_prediction:
                        recovered = recovered.union({coarse_grain_prediction})

    if curr_class in consistency_constraints_for_main_model:
        all_possible_constraints = len(consistency_constraints_for_main_model[curr_class])
        error_detections[curr_class] = round(len(recovered) / all_possible_constraints * 100, 2)

    CCi = DetUSMPosRuleSelect(i=i,
                              all_charts=all_charts) if run_positive_rules else []
    tem_cond = np.zeros_like(chart[:, 0])

    for cc in CCi:
        tem_cond |= chart[:, cc]

    if np.sum(tem_cond) > 0:
        for example_index, cv in enumerate(chart):
            if tem_cond[example_index] and not predict_result[example_index]:
                pos_i_count += 1
                predict_result[example_index] = 1
                total_results[example_index] = i

    scores_cor = get_scores(chart[:, 1], predict_result)

    if not utils.is_local():
        shared_index.value += 1
        print(f'Completed {shared_index.value}/{len(all_charts)}')

    return scores_cor + [neg_i_count,
                         pos_i_count,
                         len(NCi),
                         len(CCi)]


def ruleForNPCorrectionMP(all_charts: list[list],
                          true_data: np.array,
                          pred_data: np.array,
                          main_granularity: str,
                          epsilon: float,
                          consistency_constraints_for_main_model: dict[str, set],
                          run_positive_rules: bool = True):
    manager = mp.Manager()
    shared_results = manager.list(pred_data)
    error_detections = manager.dict({})
    shared_index = manager.Value('i', 0)

    args_list = [(i,
                  chart,
                  epsilon,
                  all_charts,
                  main_granularity,
                  run_positive_rules,
                  shared_results,
                  shared_index,
                  error_detections,
                  consistency_constraints_for_main_model)
                 for i, chart in enumerate(all_charts)]

    # Create a pool of processes and map the function with arguments
    processes_num = min(len(all_charts), mp.cpu_count())

    with mp.Pool(processes_num) as pool:
        print(f'Num of processes: {processes_num}')
        results = pool.starmap(ruleForNPCorrection_worker, args_list)

    shared_results = np.array(list(shared_results))
    error_detections_values = np.array(list(dict(error_detections).values()))

    error_detections_mean = np.mean(error_detections_values)
    print(f'Mean error detections found for {main_granularity}-grain: {error_detections_mean}')

    results = [item for sublist in results for item in sublist]

    results.extend(get_scores(y_true=true_data,
                              y_pred=shared_results))
    posterior_acc = accuracy_score(y_true=true_data,
                                   y_pred=shared_results)

    # retrieve_error_detection_rule(error_detections)

    return results, posterior_acc, shared_results, error_detections_mean


def ruleForNPCorrection(all_charts: list,
                        true_data,
                        pred_data,
                        epsilon: float,
                        run_positive_rules: bool = True):
    results = []
    total_results = np.copy(pred_data)
    print(len(all_charts))

    for i, chart in enumerate(all_charts):
        with ((context_handlers.TimeWrapper(s=f'Class {i} is done'))):
            chart = np.array(chart)
            NCi = GreedyNegRuleSelect(i=i,
                                      epsilon=epsilon,
                                      all_charts=all_charts)
            neg_i_count = 0
            pos_i_count = 0

            predict_result = np.copy(chart[:, 0])
            tem_cond = np.zeros_like(chart[:, 0])

            for cc in NCi:
                tem_cond |= chart[:, cc]

            if np.sum(tem_cond) > 0:
                for ct, cv in enumerate(chart):
                    if tem_cond[ct] and predict_result[ct]:
                        neg_i_count += 1
                        predict_result[ct] = 0

            CCi = DetUSMPosRuleSelect(i=i,
                                      all_charts=all_charts) if run_positive_rules else []
            tem_cond = np.zeros_like(chart[:, 0])

            for cc in CCi:
                tem_cond |= chart[:, cc]

            if np.sum(tem_cond) > 0:
                for ct, cv in enumerate(chart):
                    if tem_cond[ct] and not predict_result[ct]:
                        pos_i_count += 1
                        predict_result[ct] = 1
                        total_results[ct] = i

            scores_cor = get_scores(chart[:, 1], predict_result)
            results.extend(scores_cor + [neg_i_count,
                                         pos_i_count,
                                         len(NCi),
                                         len(CCi)])

    results.extend(get_scores(true_data, total_results))
    posterior_acc = accuracy_score(true_data, total_results)

    return results, posterior_acc, total_results, None

def plot(df: pd.DataFrame,
         classes: list,
         col_num: int,
         x_values: pd.Series,
         main_granularity: str,
         main_model_name: str,
         main_lr: float,
         secondary_model_name: str,
         secondary_lr: float,
         folder: str,
         pipeline_results_across_epsilon: dict):
    average_precision = pd.Series(data=0,
                                  index=x_values.index)
    average_recall = pd.Series(data=0,
                               index=x_values.index)
    average_f1_score = pd.Series(data=0,
                                 index=x_values.index)
    average_accuracy = pd.Series(data=0,
                                 index=x_values.index)
    result_inconsistencies = []

    for i in range(len(classes)):
        df_i = df.iloc[0:, 1 + i * col_num:1 + (i + 1) * col_num]

        added_str = f'.{i}' if i else ''
        precision_i = df_i[f'pre']
        recall_i = df_i[f'recall']
        f1_score_i = df_i[f'F1']
        accuracy_score_i = df_i['acc']

        average_precision += precision_i
        average_recall += recall_i
        average_f1_score += f1_score_i
        average_accuracy += accuracy_score_i

        # Calculate the limit using the base recall value and formula
        base_recall = recall_i.iloc[0]  # Get the base recall value from the first index
        limit = pd.Series([base_recall * (1 - dist * epsilon) for epsilon in range(0, num_epsilons + 1)])

        plt.plot(x_values,
                 precision_i,
                 label='precision')
        plt.plot(x_values,
                 recall_i,
                 label='recall')
        plt.plot(x_values,
                 f1_score_i,
                 label='f1')
        plt.plot(x_values,
                 accuracy_score_i,
                 label='accuracy')
        
        plt.plot(x_values, 
                 limit, 
                 label='recall limit',
                 color='green', linestyle='--')

        plt.title(f'{main_granularity.capitalize()}-grain class #{i}-{classes[i]}, '
                  f'Main: {main_model_name}, lr: {main_lr}'
                  f', secondary: {secondary_model_name}, lr: {secondary_lr}'
                  )
        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.savefig(f'{folder}/cls{i}.png')
        plt.clf()
        plt.cla()

    for i in range(num_epsilons + 1):
        fine_predictions = pipeline_results_across_epsilon['fine'][i]
        coarse_predictions = pipeline_results_across_epsilon['coarse'][i]
        inconsistency = data_preprocessing.get_num_inconsistencies(fine_predictions,
                                                               coarse_predictions) / len(fine_predictions)
        result_inconsistencies.append([inconsistency])

    # Calculate the limit using the base recall value and formula
    base_recall = average_recall.iloc[0]  # Get the base recall value from the first index
    limit = pd.Series([base_recall * (1 - dist * epsilon) for epsilon in range(0, num_epsilons + 1)])

    inconsistency = pd.Series(1 - np.array(result_inconsistencies)[:,0])
    average_best_result = (average_accuracy + average_f1_score) / 2 - inconsistency

    plt.plot(x_values,
             average_precision / len(classes),
             label='average precision')
    plt.plot(x_values,
             average_recall / len(classes),
             label='average recall')
    plt.plot(x_values,
             average_f1_score / len(classes),
             label='average f1')
    plt.plot(x_values,
             average_accuracy / len(classes),
             label='average accuracy')
    plt.plot(x_values, 
             inconsistency, 
             label='consistency',
             color='red', linestyle='--')
    plt.plot(x_values, 
             limit / len(classes), 
             label='recall reduction threshold',
             color='green', linestyle='--')
    
    if conditions_from_main == True:
        folder = (f'{figs_folder}/{"combine_" + combined_caption if combined else "individual_"}main_{loss}_{main_model_name}_lr{main_lr}')
        plt.title(f'{"combine" + combined_caption if combined else "individual"}_{main_granularity}_main_{loss}_{main_model_name}_lr{main_lr}\n')
    else:
        folder = (f'{figs_folder}/{"combine_" + combined_caption if combined else "individual_"}main_{loss}_{main_model_name}_lr{main_lr}'
                    f'_secondary_{secondary_model_name}_lr{secondary_lr}')
        plt.title(f'{"combine" + combined_caption if combined else "individual"}_{main_granularity}_main_{loss}_{main_model_name}_lr{main_lr}\n'
                    f'_secondary_{secondary_model_name}_lr{secondary_lr}')
    
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.savefig(f'{folder}/average_{main_granularity}_old.png')
    plt.clf()
    plt.cla()

    average_best_result.to_csv(f'{folder}/average_{main_granularity}_old.csv')


def retrieve_error_detection_rule(error_detections):
    for coarse_grain_label, coarse_grain_label_data in error_detections.items():
        for fine_grain_label in coarse_grain_label_data.keys():
            print(f'error <- predicted_coarse_grain = {coarse_grain_label} '
                  f'and predicted_fine_grain = {fine_grain_label}')


def rearrange_for_condition_values(arr: np.array) -> np.array:
    return np.eye(np.max(arr) + 1)[arr].T

def load_priors(main_lr,
                loss: str,
                combined: bool,
                main_fine_path: str,
                main_coarse_path: str,
                secondary_fine_path: str,
                secondary_coarse_path: str) -> (np.array, np.array):
    if main_fine_path is not None:
        main_model_fine_path = main_fine_path
        main_model_coarse_path = main_coarse_path
        secondary_model_fine_path = secondary_fine_path
        secondary_model_coarse_path = secondary_coarse_path

        main_fine_data = np.load(main_model_fine_path)
        main_coarse_data = np.load(main_model_coarse_path)

        secondary_fine_data = np.load(secondary_model_fine_path)
        secondary_coarse_data = np.load(secondary_model_coarse_path)

    elif combined:
        loss_str = f'{loss}_' if (loss == 'soft_marginal' and combined) else 'BCE_'
        main_model_fine_path = f'{main_model_name}_{loss_str}test_fine_pred_lr{main_lr}_e{epochs_num - 1}.npy'
        main_model_coarse_path = f'{main_model_name}_{loss_str}test_coarse_pred_lr{main_lr}_e{epochs_num - 1}.npy'
        secondary_model_fine_path = main_model_fine_path
        secondary_model_coarse_path = main_model_coarse_path

        path = vit_pipeline.combined_results_path if combined else vit_pipeline.individual_results_path

        main_fine_data = np.load(os.path.join(path, main_model_fine_path))
        main_coarse_data = np.load(os.path.join(path, main_model_coarse_path))

        secondary_fine_data = np.load(os.path.join(path, secondary_model_fine_path))
        secondary_coarse_data = np.load(os.path.join(path, secondary_model_coarse_path))
    else:
        loss_str = f'{loss}_' if (loss == 'soft_marginal' and combined) else 'BCE_'
        main_model_fine_path = (f'{main_model_name}_test_pred_lr{main_lr}_e{epochs_num - 1}'
                                f'_fine_individual.npy')
        main_model_coarse_path = (f'{main_model_name}_test_pred_lr{main_lr}_e{epochs_num - 1}'
                                  f'_coarse_individual.npy')
        secondary_model_fine_path = (f'{secondary_model_name}_test_pred_lr{secondary_lr}'
                                 f'_e9_fine_individual.npy')
        secondary_model_coarse_path = (f'{secondary_model_name}_test_pred_lr{secondary_lr}'
                                    f'_e9_coarse_individual.npy')
        
        path = vit_pipeline.combined_results_path if combined else vit_pipeline.individual_results_path
        
        main_fine_data = np.load(os.path.join(path, main_model_fine_path))
        main_coarse_data = np.load(os.path.join(path, main_model_coarse_path))

        secondary_fine_data = np.load(os.path.join(path, secondary_model_fine_path))
        secondary_coarse_data = np.load(os.path.join(path, secondary_model_coarse_path))

    vit_pipeline.get_and_print_metrics(fine_predictions=main_fine_data,
                                       coarse_predictions=main_coarse_data,
                                       loss=loss,
                                       combined=combined,
                                       model_name=main_model_name,
                                       lr=main_lr)

    consistency_constraints_for_main_model = {}

    for fine_prediction_index, coarse_prediction_index in zip(main_fine_data, main_coarse_data):
        fine_prediction = data_preprocessing.fine_grain_classes[fine_prediction_index]
        coarse_prediction = data_preprocessing.coarse_grain_classes[coarse_prediction_index]

        if data_preprocessing.fine_to_coarse[fine_prediction] != coarse_prediction:
            if coarse_prediction not in consistency_constraints_for_main_model:
                consistency_constraints_for_main_model[coarse_prediction] = {fine_prediction}
            else:
                consistency_constraints_for_main_model[coarse_prediction] = (
                    consistency_constraints_for_main_model[coarse_prediction].union({fine_prediction}))

            if fine_prediction not in consistency_constraints_for_main_model:
                consistency_constraints_for_main_model[fine_prediction] = {coarse_prediction}
            else:
                consistency_constraints_for_main_model[fine_prediction] = (
                    consistency_constraints_for_main_model[fine_prediction].union({coarse_prediction}))

    # for coarse_prediction, fine_grain_inconsistencies in consistency_constraints_for_main_model.items():
    #     assert len(set(data_preprocessing.coarse_to_fine[coarse_prediction]).
    #                intersection(fine_grain_inconsistencies)) == 0

    # print([f'{k}: {len(v)}' for k, v in consistency_constraints_for_main_model.items()])

    return (main_fine_data, main_coarse_data, secondary_fine_data, secondary_coarse_data,
            consistency_constraints_for_main_model)


def get_conditions_data(main_fine_data: np.array,
                        main_coarse_data: np.array,
                        secondary_fine_data: np.array) -> dict[str, dict[str, np.array]]:
    condition_datas = {}

    for main_or_secondary in ['main',
                              'secondary'
                              ]:
        take_conditions_from = main_fine_data if main_or_secondary == 'main' else secondary_fine_data

        for granularity in data_preprocessing.granularities:
            if main_or_secondary not in condition_datas:
                condition_datas[main_or_secondary] = {}

            cla_data = main_fine_data if granularity == 'fine' else main_coarse_data
            condition_datas[main_or_secondary][granularity] = rearrange_for_condition_values(cla_data)

        derived_coarse = np.array([data_preprocessing.fine_to_course_idx[fine_grain_prediction]
                                   for fine_grain_prediction in take_conditions_from])

        condition_datas[main_or_secondary]['fine_to_coarse'] = rearrange_for_condition_values(derived_coarse)

    return condition_datas


def run_EDCR_for_granularity(main_lr,
                             main_granularity: str,
                             main_fine_data: np.array,
                             main_coarse_data: np.array,
                             condition_datas: dict[str, dict[str, np.array]],
                             conditions_from_secondary: bool,
                             conditions_from_main: bool,
                             consistency_constraints: bool,
                             multiprocessing: bool,
                             consistency_constraints_for_main_model: dict[str, set]) -> np.array:
    with ((context_handlers.TimeWrapper())):
        if main_granularity == 'fine':
            classes = data_preprocessing.fine_grain_classes
            true_data = data_preprocessing.true_fine_data
            pred_data = main_fine_data
        else:
            classes = data_preprocessing.coarse_grain_classes
            true_data = data_preprocessing.true_coarse_data
            pred_data = main_coarse_data

        examples_num = true_data.shape[0]

        charts = [[pred_data[example_index], true_data[example_index]] +
                  ((
                           get_unary_condition_values(example_index=example_index,
                                                      cla_datas=condition_datas['main']['fine'])
                           +
                           get_unary_condition_values(example_index=example_index,
                                                      cla_datas=condition_datas['main']['coarse'])
                           +
                           (get_binary_condition_values(example_index=example_index,
                                                        fine_cla_datas=condition_datas['main']['fine'],
                                                        coarse_cla_datas=condition_datas['main']['coarse'])
                            if consistency_constraints else [])
                   ) if conditions_from_main else [])
                  +
                  (
                      (
                              get_unary_condition_values(example_index=example_index,
                                                         cla_datas=condition_datas['secondary']['fine'])
                              +
                              get_unary_condition_values(example_index=example_index,
                                                         cla_datas=condition_datas['secondary']['coarse'])
                      )
                      if conditions_from_secondary else [])
                  for example_index in range(examples_num)]

        all_charts = generate_chart(n_classes=len(classes),
                                    charts=charts)

        results = []
        result0 = [0]
        prediction = []

        print(f'Started EDCR pipeline for the {main_granularity}-grain main classes...'
              # f', secondary: {secondary_model_name}, lr: {secondary_lr}\n'
              )

        for count, chart in enumerate(all_charts):
            chart = np.array(chart)
            result0.extend(get_scores(chart[:, 1], chart[:, 0]))
            result0.extend([0, 0, 0, 0])

        result0.extend(get_scores(true_data, pred_data))
        results.append(result0)
        prediction.append(pred_data.reshape(1, -1))

        # posterior_acc = 0
        total_results = np.zeros_like(pred_data)

        epsilons = [dist * i for i in range(1, num_epsilons + 1, 1)]

        for epsilon in epsilons:
            result, posterior_acc, total_results, error_detections_mean = ruleForNPCorrectionMP(
                all_charts=all_charts,
                true_data=true_data,
                pred_data=pred_data,
                main_granularity=main_granularity,
                epsilon=epsilon,
                consistency_constraints_for_main_model=consistency_constraints_for_main_model
            ) if multiprocessing else ruleForNPCorrection(all_charts=all_charts,
                                                          true_data=true_data,
                                                          pred_data=pred_data,
                                                          epsilon=epsilon)

            results.append([epsilon] + result)
            prediction.append(total_results.reshape(1, -1))
            print(posterior_acc)
            print(error_detections_mean)

        prediction_across_epsilon = np.concatenate(prediction, axis=0)

        prior_acc = 0
        print(f'\nSaved plots for main: {main_granularity}-grain {main_model_name}, lr={main_lr}'
              # f', secondary: {secondary_model_name}, lr={secondary_lr}'
              f'\nPrior acc:{prior_acc}, post acc: {posterior_acc}')

        col = ['pre', 'recall', 'F1', 'acc', 'NSC', 'PSC', 'NRC', 'PRC']
        df = pd.DataFrame(results, columns=['epsilon'] + col * len(classes) + ['pre', 'recall', 'F1', 'acc'])

        # df.to_csv(results_file)
        # df = pd.read_csv(results_file)

        # if conditions_from_main == True:
        #     folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}')
        # else:
        #     folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}'
        #                 f'_secondary_{secondary_model_name}_lr{secondary_lr}')
            
        if conditions_from_main == True:
            folder = (f'{figs_folder}/{"combine_" + combined_caption if combined else "individual_"}main_{loss}_{main_model_name}_lr{main_lr}')
            
        else:
            folder = (f'{figs_folder}/{"combine_" + combined_caption if combined else "individual_"}main_{loss}_{main_model_name}_lr{main_lr}'
                        f'_secondary_{secondary_model_name}_lr{secondary_lr}')
            
    
        utils.create_directory(folder)

        # plot(df=df,
        #      classes=classes,
        #      col_num=len(col),
        #      x_values=df['epsilon'][0:],
        #      main_granularity=main_granularity,
        #      main_model_name=main_model_name,
        #      main_lr=main_lr,
        #      secondary_model_name=secondary_model_name,
        #      secondary_lr=secondary_lr,
        #      folder=folder)


        np.save(f'{folder}/results.npy', total_results)

        # Save the DataFrame to an Excel file
        df.to_excel(f'{folder}/results.xlsx')

        print(f'\nCompleted {main_granularity}-grain EDCR run'
              # f'saved error detections and corrections to {folder}\n'
              )
        
        plot_args = [
            df, 
            classes, 
            len(col), 
            df['epsilon'], 
            main_granularity, 
            main_model_name, 
            main_lr, 
            secondary_model_name,
            secondary_lr,
            folder]

    return total_results, error_detections_mean, prediction_across_epsilon, plot_args


# def plot_everything(pipeline_results_across_epsilon):
    
#     x_values = pd.Series([epsilon * dist for epsilon in range(0, num_epsilons + 1)])
#     result_coarse = []
#     result_fine = []
#     result_inconsistencies = []
#     result_best = []
#     result_table = []
#     # Calculate the limit using the base recall value and formula
#     for i in range(num_epsilons + 1):
#         fine_predictions = pipeline_results_across_epsilon['fine'][i]
#         coarse_predictions = pipeline_results_across_epsilon['coarse'][i]

#         fine_accuracy = accuracy_score(y_true=data_preprocessing.true_fine_data,
#                                         y_pred=fine_predictions)
#         coarse_accuracy = accuracy_score(y_true=data_preprocessing.true_coarse_data,
#                                             y_pred=coarse_predictions)
        
#         fine_f1 = f1_score(y_true=data_preprocessing.true_fine_data,
#                                 y_pred=fine_predictions,
#                                 labels=range(len(data_preprocessing.fine_grain_classes)),
#                                 average='macro')
#         coarse_f1 = f1_score(y_true=data_preprocessing.true_coarse_data,
#                                 y_pred=coarse_predictions,
#                                 labels=range(len(data_preprocessing.coarse_grain_classes)),
#                                 average='macro')
        
#         fine_recall = recall_score(y_true=data_preprocessing.true_fine_data,
#                                     y_pred=fine_predictions,
#                                     labels=range(len(data_preprocessing.fine_grain_classes)),
#                                     average='macro')
#         coarse_recall = recall_score(y_true=data_preprocessing.true_coarse_data,
#                                     y_pred=coarse_predictions,
#                                     labels=range(len(data_preprocessing.coarse_grain_classes)),
#                                     average='macro')
        
#         fine_precision = precision_score(y_true=data_preprocessing.true_fine_data,
#                                         y_pred=fine_predictions,
#                                         labels=range(len(data_preprocessing.fine_grain_classes)),
#                                         average='macro')
#         coarse_precision = precision_score(y_true=data_preprocessing.true_coarse_data,
#                                         y_pred=coarse_predictions,
#                                         labels=range(len(data_preprocessing.coarse_grain_classes)),
#                                         average='macro')
        
#         inconsistency = data_preprocessing.get_num_inconsistencies(fine_predictions,
#                                                                coarse_predictions) / len(fine_predictions)
        
#         result_coarse.append([coarse_accuracy, coarse_f1, coarse_recall, coarse_precision])
#         result_fine.append([fine_accuracy, fine_f1, fine_recall, fine_precision])
#         result_inconsistencies.append([inconsistency])
#         result_best.append(fine_accuracy + coarse_accuracy + fine_f1 + coarse_f1 - inconsistency)
#         result_table.append([i * dist, fine_accuracy, fine_f1, coarse_accuracy, coarse_f1, inconsistency])

#     result_coarse = np.array(result_coarse)
#     result_fine = np.array(result_fine)
#     result_inconsistencies = np.array(result_inconsistencies)

#     plt.plot(x_values,
#              pd.Series(result_coarse[:,0]),
#              label='average coarse accuracy')
#     plt.plot(x_values,
#              pd.Series(result_coarse[:,1]),
#              label='average coarse f1')
#     plt.plot(x_values,
#              pd.Series(result_coarse[:,2]),
#              label='average coarse recall')
#     plt.plot(x_values,
#              pd.Series(result_coarse[:,3]),
#              label='average coarse precision')
    
#     plt.plot(x_values, 
#              pd.Series(1 - result_inconsistencies[:,0]), 
#              label='consistency',
#              color='red', linestyle='--')
    
#     # Calculate the limit using the base recall value and formula
#     base_coarse_recall = result_coarse[0,3]  # Get the base recall value from the first index
#     limit_coarse_recall = pd.Series([base_coarse_recall * (1 - dist * epsilon) for epsilon in range(0, num_epsilons + 1)])
    
#     plt.plot(x_values, 
#              limit_coarse_recall, 
#              label='recall reduction threshold',
#              color='blue', linestyle='--')

    
#     if conditions_from_main == True:
#         folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}')
#         plt.title(f'{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}')
#     else:
#         folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}'
#                     f'_secondary_{secondary_model_name}_lr{secondary_lr}')
#         plt.title(f'{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}'
#                     f'_secondary_{secondary_model_name}_lr{secondary_lr}')
#     plt.legend()
#     plt.tight_layout()
#     plt.grid()
#     plt.savefig(f'{folder}/average_coarse.png')
#     plt.clf()
#     plt.cla()


#     plt.plot(x_values,
#              pd.Series(result_fine[:,0]),
#              label='average fine accuracy')
#     plt.plot(x_values,
#              pd.Series(result_fine[:,1]),
#              label='average fine f1')
#     plt.plot(x_values,
#              pd.Series(result_fine[:,2]),
#              label='average fine recall')
#     plt.plot(x_values,
#              pd.Series(result_fine[:,3]),
#              label='average fine precision')
    
#     plt.plot(x_values, 
#              pd.Series(1 - result_inconsistencies[:,0]), 
#              label='consistency',
#              color='red', linestyle='--')
#     # Calculate the limit using the base recall value and formula
#     base_fine_recall = result_fine[0,3]  # Get the base recall value from the first index
#     limit_fine_recall = pd.Series([base_fine_recall * (1 - dist * epsilon) for epsilon in range(0, num_epsilons + 1)])

#     plt.plot(x_values, 
#              limit_fine_recall, 
#              label='recall reduction threshold',
#              color='green', linestyle='--')
    
#     if conditions_from_main == True:
#         folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}')
#         plt.title(f'{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}')
#     else:
#         folder = (f'{figs_folder}/{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}'
#                     f'_secondary_{secondary_model_name}_lr{secondary_lr}')
#         plt.title(f'{"combine" if combined else "individual"}_main_{loss}_{main_model_name}_lr{main_lr}'
#                     f'_secondary_{secondary_model_name}_lr{secondary_lr}')
#     plt.legend()
#     plt.tight_layout()
#     plt.grid()
#     plt.savefig(f'{folder}/average_fine.png')
#     plt.clf()
#     plt.cla()

#     # Define column names
#     column_names = ['epsilon', 'fine_accuracy', 'fine_f1', 'coarse_accuracy', 'coarse_f1', 'inconsistency']

#     # Create DataFrame
#     df = pd.DataFrame(result_table, columns=column_names)

#     # Save the DataFrame as a CSV file
#     df.to_csv(f'{folder}/result_table_with_epsilon.csv', index=False)

#     print("DataFrame saved successfully!")
    
def run_EDCR_pipeline(main_lr,
                      combined: bool,
                      loss: str,
                      conditions_from_secondary: bool,
                      conditions_from_main: bool,
                      consistency_constraints: bool,
                      main_fine_path: str = None,
                      main_coarse_path: str = None,
                      secondary_fine_path: str = None,
                      secondary_coarse_path: str = None,
                      multiprocessing: bool = True):
    (main_fine_data, main_coarse_data, secondary_fine_data, secondary_coarse_data,
     consistency_constraints_for_main_model) = load_priors(main_lr,
                                                           loss,
                                                           combined,
                                                           main_fine_path,
                                                           main_coarse_path,
                                                           secondary_fine_path,
                                                           secondary_coarse_path)

    condition_datas = get_conditions_data(main_fine_data=main_fine_data,
                                          main_coarse_data=main_coarse_data,
                                          secondary_fine_data=secondary_fine_data)
    pipeline_results = {}
    plot_args = {}
    error_detections = []
    pipeline_results_across_epsilon = {}

    for main_granularity in data_preprocessing.granularities:
        res = (
            run_EDCR_for_granularity(main_lr=main_lr,
                                     main_granularity=main_granularity,
                                     main_fine_data=main_fine_data,
                                     main_coarse_data=main_coarse_data,
                                     condition_datas=condition_datas,
                                     conditions_from_secondary=conditions_from_secondary,
                                     conditions_from_main=conditions_from_main,
                                     consistency_constraints=consistency_constraints,
                                     multiprocessing=multiprocessing,
                                     consistency_constraints_for_main_model=consistency_constraints_for_main_model))
        pipeline_results[main_granularity] = res[0]
        pipeline_results_across_epsilon[main_granularity] = res[2]
        plot_args[main_granularity] = res[3]
        if multiprocessing:
            error_detections += [res[1]]

    if multiprocessing:
        error_detections = np.mean(np.array(error_detections))
        print(utils.green_text(f'Mean error detections found {np.mean(error_detections)}'))

    vit_pipeline.get_and_print_metrics(fine_predictions=pipeline_results['fine'],
                                       coarse_predictions=pipeline_results['coarse'],
                                       loss=loss,
                                       prior=False,
                                       combined=combined,
                                       model_name=main_model_name,
                                       lr=main_lr)
    
    plot(df=plot_args['fine'][0],
        classes=plot_args['fine'][1],
        col_num=plot_args['fine'][2],
        x_values=plot_args['fine'][3],
        main_granularity=plot_args['fine'][4],
        main_model_name=plot_args['fine'][5],
        main_lr=plot_args['fine'][6],
        secondary_model_name=plot_args['fine'][7],
        secondary_lr=plot_args['fine'][8],
        folder=plot_args['fine'][9],
        pipeline_results_across_epsilon=pipeline_results_across_epsilon)
    
    plot(df=plot_args['coarse'][0],
        classes=plot_args['coarse'][1],
        col_num=plot_args['coarse'][2],
        x_values=plot_args['coarse'][3],
        main_granularity=plot_args['coarse'][4],
        main_model_name=plot_args['coarse'][5],
        main_lr=plot_args['coarse'][6],
        secondary_model_name=plot_args['coarse'][7],
        secondary_lr=plot_args['coarse'][8],
        folder=plot_args['coarse'][9],
        pipeline_results_across_epsilon=pipeline_results_across_epsilon)
    
    # plot_everything(pipeline_results_across_epsilon)


if __name__ == '__main__':
    print(utils.red_text(f'\nconditions_from_secondary={not conditions_from_main}, '
                         f'conditions_from_main={conditions_from_main}\n' +
                         f'combined={combined}\n' + '#' * 100 + '\n'))

    run_EDCR_pipeline(main_lr=main_lr,
                      combined=combined,
                      loss=loss,
                      conditions_from_secondary=not conditions_from_main,
                      conditions_from_main=conditions_from_main,
                      consistency_constraints=False,
                      main_coarse_path=main_coarse_path,
                      main_fine_path=main_fine_path,
                      secondary_coarse_path=secondary_coarse_path,
                      secondary_fine_path=secondary_fine_path,
                      multiprocessing=True)
