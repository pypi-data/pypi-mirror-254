"""
This test will check the result of combine model applying EDCR knowing the constraint
The prediction is before and after running with LTN, from BCE, Soft marginal with lr = 1e-04 and lr = 3e-06
"""
import sys
import unittest
import os
import math
import numpy as np
from EDCR_pipeline import run_EDCR_pipeline
from vit_pipeline import get_and_print_metrics
from data_preprocessing import get_num_inconsistencies
import utils
from itertools import product

combined = True
conditions_from_main = True
consistency_constraint = True

acc_err_margin = 0.005
inconsistency_err_margin = 0.005

class Test_before_edcr(unittest.TestCase):
    
    # loss and lrs
    baseline = "base" # ["base", "LTN"]
    loss = "BCE" # ["BCE", 'soft_marginal']
    lr = "1e-04" # [1e-04, 3e-06]
    optimize = "accuracy" # ["accuracy", "inconsistency"]

    @classmethod
    def setUpClass(cls) -> None:
        super(Test_before_edcr, cls).setUpClass()
        
        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        pred_path = {
            "BCE_0.0001": ["combined_results/vit_b_16_BCE_test_fine_pred_lr0.0001_e19.npy",
                           "combined_results/vit_b_16_BCE_test_coarse_pred_lr0.0001_e19.npy"], 
            "BCE_3e-06": ["combined_results/vit_b_16_BCE_test_fine_pred_lr3e-06_e19.npy",
                          "combined_results/vit_b_16_BCE_test_coarse_pred_lr3e-06_e19.npy"], 
            "LTN_BCE_0.0001_accuracy": ["combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.3_batch_size_512_step_size_1_scheduler_gamma_0.3_fine_pred.npy",
                                        "combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.3_batch_size_512_step_size_1_scheduler_gamma_0.3_coarse_pred.npy"], 
            "LTN_BCE_0.0001_inconsistency": ["combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.9_batch_size_512_step_size_1_scheduler_gamma_0.3_fine_pred.npy",
                                             "combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.9_batch_size_512_step_size_1_scheduler_gamma_0.3_coarse_pred.npy"], 
            "LTN_BCE_3e-06_accuracy": ["combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_0.8_batch_size_512_step_size_2_scheduler_gamma_0.1_fine_pred.npy",
                                       "combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_0.8_batch_size_512_step_size_2_scheduler_gamma_0.1_coarse_pred.npy",], 
            "LTN_BCE_3e-06_inconsistency": ["combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.1_fine_pred.npy",
                                            "combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.1_coarse_pred.npy"], 
            "soft_marginal_0.0001": ["combined_results/vit_b_16_soft_marginal_test_fine_pred_lr0.0001_e19.npy",
                                     "combined_results/vit_b_16_soft_marginal_test_coarse_pred_lr0.0001_e19.npy"], 
            "soft_marginal_3e-06": ["combined_results/vit_b_16_soft_marginal_test_fine_pred_lr3e-06_e19.npy",
                                    "combined_results/vit_b_16_soft_marginal_test_coarse_pred_lr3e-06_e19.npy"], 
            "LTN_soft_marginal_0.0001_accuracy": ["combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_1_scheduler_gamma_0.1_fine_pred.npy",
                                                  "combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_1_scheduler_gamma_0.1_coarse_pred.npy"], 
            "LTN_soft_marginal_0.0001_inconsistency": ["combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.4_batch_size_512_step_size_1_scheduler_gamma_0.1_fine_pred.npy",
                                                       "combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.4_batch_size_512_step_size_1_scheduler_gamma_0.1_coarse_pred.npy"], 
            "LTN_soft_marginal_3e-06_accuracy": ["combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_2_scheduler_gamma_0.8_fine_pred.npy",
                                                 "combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_2_scheduler_gamma_0.8_coarse_pred.npy"], 
            "LTN_soft_marginal_3e-06_inconsistency": ["combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.8_fine_pred.npy",
                                                      "combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.8_coarse_pred.npy"], 
        }
        cls.expected_result = {
            "BCE_0.0001": [0.6897, 0.8427, 0.0376],
            "BCE_3e-06": [0.5842, 0.8186, 0.0728],
            "LTN_BCE_0.0001_accuracy": [0.7027, 0.8593, 0.0296],
            "LTN_BCE_0.0001_inconsistency": [0.7070, 0.8507, 0.0228],
            "LTN_BCE_3e-06_accuracy": [0.6070, 0.8328, 0.0512],
            "LTN_BCE_3e-06_inconsistency": [0.6027, 0.8260, 0.0469],
            "soft_marginal_0.0001": [0.6477, 0.8396, 0.0315],
            "soft_marginal_3e-06": [0.5965, 0.8353, 0.0666],
            "LTN_soft_marginal_0.0001_accuracy": [0.7027, 0.8550, 0.0321],
            "LTN_soft_marginal_0.0001_inconsistency": [0.6950, 0.8575, 0.0271],
            "LTN_soft_marginal_3e-06_accuracy": [0.6151, 0.8470, 0.0635],
            "LTN_soft_marginal_3e-06_inconsistency": [0.6064, 0.8427, 0.0512],
        }

        model_name = f"{cls.baseline}_{cls.loss}_{cls.lr}_{cls.optimize}" if cls.baseline == "LTN" else f"{cls.loss}_{cls.lr}" 
        fine_prediction = np.load(pred_path[model_name][0])
        coarse_prediction = np.load(pred_path[model_name][1])
        test_fine_accuracy, \
        test_coarse_accuracy = get_and_print_metrics(fine_prediction,
                                                      coarse_prediction,
                                                      loss=cls.loss,
                                                      model_name="vit_b_16",
                                                      lr=cls.lr)
        inconsistency = get_num_inconsistencies(fine_prediction, coarse_prediction) / len(fine_prediction)
        cls.result.append([model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency])
        
    def test_fine_accuracy(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_accuracy = cls.expected_result[model_name][0]  # Adjust if needed
            cls.assertTrue(
                math.fabs(test_fine_accuracy - expected_accuracy) < acc_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_accuracy:.4f}, Actual: {test_fine_accuracy:.4f}"
            )

    def test_coarse_accuracy(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_accuracy = cls.expected_result[model_name][1]  # Adjust if needed
            cls.assertTrue(
                math.fabs(test_coarse_accuracy - expected_accuracy) < acc_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_accuracy:.4f}, Actual: {test_coarse_accuracy:.4f}"
            )

    def test_inconsistency(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_inconsistency = cls.expected_result[model_name][2]  # Adjust if needed
            cls.assertTrue(
                math.fabs(inconsistency - expected_inconsistency) < inconsistency_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_inconsistency:.4f}, Actual: {inconsistency:.4f}"
            )

class Test_after_edcr(unittest.TestCase):
    
    # loss and lrs
    baseline = "base" # ["base", "LTN"]
    loss = "BCE" # ["BCE", 'soft_marginal']
    lr = "1e-04" # [1e-04, 3e-06]
    optimize = "accuracy" # ["accuracy", "inconsistency"]

    @classmethod
    def setUpClass(cls) -> None:
        super(Test_after_edcr, cls).setUpClass()
        
        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        pred_path = {
            "BCE_0.0001": ["combined_results/vit_b_16_BCE_test_fine_pred_lr0.0001_e19.npy",
                           "combined_results/vit_b_16_BCE_test_coarse_pred_lr0.0001_e19.npy"], 
            "BCE_3e-06": ["combined_results/vit_b_16_BCE_test_fine_pred_lr3e-06_e19.npy",
                          "combined_results/vit_b_16_BCE_test_coarse_pred_lr3e-06_e19.npy"], 
            "LTN_BCE_0.0001_accuracy": ["combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.3_batch_size_512_step_size_1_scheduler_gamma_0.3_fine_pred.npy",
                                        "combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.3_batch_size_512_step_size_1_scheduler_gamma_0.3_coarse_pred.npy"], 
            "LTN_BCE_0.0001_inconsistency": ["combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.9_batch_size_512_step_size_1_scheduler_gamma_0.3_fine_pred.npy",
                                             "combined_results/vit_b_16_lr0.0001_LTN_BCE_beta_0.9_batch_size_512_step_size_1_scheduler_gamma_0.3_coarse_pred.npy"], 
            "LTN_BCE_3e-06_accuracy": ["combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_0.8_batch_size_512_step_size_2_scheduler_gamma_0.1_fine_pred.npy",
                                       "combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_0.8_batch_size_512_step_size_2_scheduler_gamma_0.1_coarse_pred.npy",], 
            "LTN_BCE_3e-06_inconsistency": ["combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.1_fine_pred.npy",
                                            "combined_results/vit_b_16_lr3e-06_LTN_BCE_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.1_coarse_pred.npy"], 
            "soft_marginal_0.0001": ["combined_results/vit_b_16_soft_marginal_test_fine_pred_lr0.0001_e19.npy",
                                     "combined_results/vit_b_16_soft_marginal_test_coarse_pred_lr0.0001_e19.npy"], 
            "soft_marginal_3e-06": ["combined_results/vit_b_16_soft_marginal_test_fine_pred_lr3e-06_e19.npy",
                                    "combined_results/vit_b_16_soft_marginal_test_coarse_pred_lr3e-06_e19.npy"], 
            "LTN_soft_marginal_0.0001_accuracy": ["combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_1_scheduler_gamma_0.1_fine_pred.npy",
                                                  "combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_1_scheduler_gamma_0.1_coarse_pred.npy"], 
            "LTN_soft_marginal_0.0001_inconsistency": ["combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.4_batch_size_512_step_size_1_scheduler_gamma_0.1_fine_pred.npy",
                                                       "combined_results/vit_b_16_lr0.0001_LTN_soft_marginal_beta_0.4_batch_size_512_step_size_1_scheduler_gamma_0.1_coarse_pred.npy"], 
            "LTN_soft_marginal_3e-06_accuracy": ["combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_2_scheduler_gamma_0.8_fine_pred.npy",
                                                 "combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_0.5_batch_size_512_step_size_2_scheduler_gamma_0.8_coarse_pred.npy"], 
            "LTN_soft_marginal_3e-06_inconsistency": ["combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.8_fine_pred.npy",
                                                      "combined_results/vit_b_16_lr3e-06_LTN_soft_marginal_beta_1.0_batch_size_512_step_size_2_scheduler_gamma_0.8_coarse_pred.npy"], 
        }
        cls.expected_result = {
            "BCE_0.0001": [0.6854, 0.8445, 0.0167],
            "BCE_3e-06": [0.5928, 0.8304, 0.0481],
            "LTN_BCE_0.0001_accuracy": [0.7187, 0.8680, 0.0117],
            "LTN_BCE_0.0001_inconsistency": [0.7224, 0.8575, 0.0086],
            "LTN_BCE_3e-06_accuracy": [0.6151, 0.8421, 0.0327],
            "LTN_BCE_3e-06_inconsistency": [0.6076, 0.8334, 0.0142],
            "soft_marginal_0.0001": [0.6626, 0.8464, 0.0099],
            "soft_marginal_3e-06": [0.6089, 0.8421, 0.0364],
            "LTN_soft_marginal_0.0001_accuracy": [0.7187, 0.8674, 0.0099],
            "LTN_soft_marginal_0.0001_inconsistency": [0.7101, 0.8674, 0.0086],
            "LTN_soft_marginal_3e-06_accuracy": [0.6280, 0.8563, 0.0370],
            "LTN_soft_marginal_3e-06_inconsistency": [0.6181, 0.8563, 0.0259],
        }

        model_name = f"{cls.baseline}_{cls.loss}_{cls.lr}_{cls.optimize}" if cls.baseline == "LTN" else f"{cls.loss}_{cls.lr}" 
        
            
        print(utils.red_text(f'\nconditions_from_secondary={not conditions_from_main}, '
                            f'conditions_from_main={conditions_from_main}\n' +
                            f'combined={combined}\n' + '#' * 100 + '\n'))

        
        test_fine_accuracy, test_coarse_accuracy, inconsistency= run_EDCR_pipeline(main_lr=cls.lr,
                                                                                    combined=combined,
                                                                                    loss=cls.loss,
                                                                                    conditions_from_secondary=not conditions_from_main,
                                                                                    conditions_from_main=conditions_from_main,
                                                                                    consistency_constraints=consistency_constraint,
                                                                                    multiprocessing=True,
                                                                                    main_fine_path=pred_path[model_name][0],
                                                                                    main_coarse_path=pred_path[model_name][1],
                                                                                    secondary_fine_path=pred_path[model_name][0],
                                                                                    secondary_coarse_path=pred_path[model_name][1])
        cls.result.append([model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency])
        

    def test_fine_accuracy(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_accuracy = cls.expected_result[model_name][0]  # Adjust if needed
            cls.assertTrue(
                math.fabs(test_fine_accuracy - expected_accuracy) < acc_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_accuracy:.4f}, Actual: {test_fine_accuracy:.4f}"
            )

    def test_coarse_accuracy(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_accuracy = cls.expected_result[model_name][1]  # Adjust if needed
            cls.assertTrue(
                math.fabs(test_coarse_accuracy - expected_accuracy) < acc_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_accuracy:.4f}, Actual: {test_coarse_accuracy:.4f}"
            )

    def test_inconsistency(cls):
        for model_name, test_fine_accuracy, test_coarse_accuracy, inconsistency in cls.result:
            expected_inconsistency = cls.expected_result[model_name][2]  # Adjust if needed
            cls.assertTrue(
                math.fabs(inconsistency - expected_inconsistency) < inconsistency_err_margin,
                f"The accuracy for fine grain with model {model_name} is wrong. Expected: {expected_inconsistency:.4f}, Actual: {inconsistency:.4f}"
            )

    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        Test_before_edcr.optimize = sys.argv.pop()
        Test_before_edcr.lr = float(sys.argv.pop())
        Test_before_edcr.loss = sys.argv.pop()
        Test_before_edcr.baseline = sys.argv.pop()

        Test_after_edcr.optimize = Test_before_edcr.optimize
        Test_after_edcr.lr = Test_before_edcr.lr
        Test_after_edcr.loss = Test_before_edcr.loss
        Test_after_edcr.baseline = Test_before_edcr.baseline
    

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_before_edcr))
    runner = unittest.TextTestRunner(failfast=True).run(suite)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_after_edcr))
    runner = unittest.TextTestRunner(failfast=True).run(suite)