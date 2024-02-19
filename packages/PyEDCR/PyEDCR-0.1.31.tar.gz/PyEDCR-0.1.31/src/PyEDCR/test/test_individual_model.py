"""
This test will check the result of individual model 
The prediction is from Cross Entropy with lr = 1e-04 and lr = 1e-06
"""

import unittest
import sys
import math
import numpy as np
from EDCR_pipeline import run_EDCR_pipeline, load_priors
from vit_pipeline import get_and_print_metrics
from data_preprocessing import get_num_inconsistencies
import utils

acc_err_margin = 0.005
inconsistency_err_margin = 0.005

class Test_before_edcr(unittest.TestCase):
    

    # loss and lrs
    lr = 1e-04 # [1e-04, 1e-06]

    @classmethod
    def setUpClass(cls) -> None:
        super(Test_before_edcr, cls).setUpClass()
        

        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        cls.expected_result = {
            "individual_0.0001": [0.6798, 0.8285, 0.1567],
            "individual_1e-06": [0.5787, 0.7977, 0.1690],
        }

        model_name = "individual_" + str(cls.lr)
        fine_prediction = np.load(f"individual_results/vit_b_16_test_pred_lr{cls.lr}_e19_fine_individual.npy")
        coarse_prediction = np.load(f"individual_results/vit_b_16_test_pred_lr{cls.lr}_e19_coarse_individual.npy")
        test_fine_accuracy, \
        test_coarse_accuracy = get_and_print_metrics(fine_prediction,
                                                            coarse_prediction,
                                                            loss="",
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

class Test_after_edcr_main(unittest.TestCase):
    
    lr = 1e-04
    
    @classmethod
    def setUpClass(cls) -> None:
        super(Test_after_edcr_main, cls).setUpClass()
        

        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        cls.expected_result = {
            "individual_0.0001": [0.7033, 0.8421, 0.0981],
            "individual_1e-06": [0.5965, 0.8063, 0.0944],
        }

        model_name = "individual" + "_" + str(cls.lr)
        combined = False
        conditions_from_main = True
        print(utils.red_text(f'\nconditions_from_secondary={not conditions_from_main}, '
                            f'conditions_from_main={conditions_from_main}\n' +
                            f'combined={combined}\n' + '#' * 100 + '\n'))

        
        test_fine_accuracy, test_coarse_accuracy, inconsistency= run_EDCR_pipeline(main_lr=cls.lr,
                                                                                    combined=combined,
                                                                                    loss="CE",
                                                                                    conditions_from_secondary=not conditions_from_main,
                                                                                    conditions_from_main=conditions_from_main,
                                                                                    consistency_constraints=False,
                                                                                    multiprocessing=True)
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

class Test_after_edcr_secondary(unittest.TestCase):
    
    lr = 1e-04 # [1e-04, 1e-06]
    
    @classmethod
    def setUpClass(cls) -> None:
        super(Test_after_edcr_secondary, cls).setUpClass()

        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        cls.expected_result = {
            "individual_0.0001": [0.7027, 0.8433, 0.1240],
            "individual_1e-06": [0.5978, 0.8118, 0.1246],
        }

        model_name = "individual" + "_" + str(cls.lr)
        combined = False
        conditions_from_main = False
        print(utils.red_text(f'\nconditions_from_secondary={not conditions_from_main}, '
                            f'conditions_from_main={conditions_from_main}\n' +
                            f'combined={combined}\n' + '#' * 100 + '\n'))

        
        test_fine_accuracy, test_coarse_accuracy, inconsistency= run_EDCR_pipeline(main_lr=cls.lr,
                                                                                    combined=combined,
                                                                                    loss="CE",
                                                                                    conditions_from_secondary=not conditions_from_main,
                                                                                    conditions_from_main=conditions_from_main,
                                                                                    consistency_constraints=False,
                                                                                    multiprocessing=True)
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
        
        lr = float(sys.argv.pop())
        condition = sys.argv.pop()
        Test_before_edcr.lr = lr
        Test_after_edcr_main.lr = lr
        Test_after_edcr_secondary.lr = lr


    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_before_edcr))
    runner = unittest.TextTestRunner(failfast=True).run(suite)

    if condition == "main":
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(Test_after_edcr_main))
        runner = unittest.TextTestRunner(failfast=True).run(suite)

    elif condition == "secondary":
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(Test_after_edcr_secondary))
        runner = unittest.TextTestRunner(failfast=True).run(suite)
    
    else:
        print("condition from main and secondary only")