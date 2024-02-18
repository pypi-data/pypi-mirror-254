"""
This test will check the result of combine model applying EDCR without knowing the constraint
The prediction is from BCE, Soft marginal with lr = 1e-04 and lr = 3e-06
"""

import unittest
import sys
import math
import numpy as np
from EDCR_pipeline import run_EDCR_pipeline
from vit_pipeline import get_and_print_metrics
from data_preprocessing import get_num_inconsistencies
import utils

combined = True
conditions_from_main = True
consistency_constraint = False

acc_err_margin = 0.005
inconsistency_err_margin = 0.005

class Test_before_edcr(unittest.TestCase):
    
    # loss and lrs
    loss = "BCE" # ["BCE", 'soft_marginal']
    lr = 1e-04 # [1e-04, 3e-06]

    @classmethod
    def setUpClass(cls) -> None:
        super(Test_before_edcr, cls).setUpClass()
        
        

        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        cls.expected_result = {
            "BCE_0.0001": [0.6897, 0.8427, 0.0376],
            "BCE_3e-06": [0.5842, 0.8186, 0.0728],
            "soft_marginal_0.0001": [0.6477, 0.8396, 0.0315],
            "soft_marginal_3e-06": [0.5965, 0.8353, 0.0666]
        }

        model_name = str(cls.loss) + "_" + str(cls.lr)
        fine_prediction = np.load(f"combined_results/vit_b_16_{cls.loss}_test_fine_pred_lr{cls.lr}_e19.npy")
        coarse_prediction = np.load(f"combined_results/vit_b_16_{cls.loss}_test_coarse_pred_lr{cls.lr}_e19.npy")
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
    loss = "BCE" # ["BCE", 'soft_marginal']
    lr = 1e-04 # [1e-04, 3e-06]
    
    @classmethod
    def setUpClass(cls) -> None:
        super(Test_after_edcr, cls).setUpClass()
        
        # loss and lrs
        losses = ["BCE", "soft_marginal"]
        lrs = [1e-04, 3e-06]

        # format of result: test_fine_accuracy, test_coarse_accuracy, inconsistency
        cls.result = []
        cls.expected_result = {
            "BCE_0.0001": [0.7014, 0.8427, 0.0457],
            "BCE_3e-06": [0.5830, 0.8217, 0.0580],
            "soft_marginal_0.0001": [0.6484, 0.8408, 0.0216],
            "soft_marginal_3e-06": [0.5978, 0.8402, 0.0518]
        }

        
        model_name = str(cls.loss) + "_" + str(cls.lr)
        
        print(utils.red_text(f'\nconditions_from_secondary={not conditions_from_main}, '
                            f'conditions_from_main={conditions_from_main}\n' +
                            f'combined={combined}\n' + '#' * 100 + '\n'))

        
        test_fine_accuracy, test_coarse_accuracy, inconsistency= run_EDCR_pipeline(main_lr=cls.lr,
                                                                                    combined=combined,
                                                                                    loss=cls.loss,
                                                                                    conditions_from_secondary=not conditions_from_main,
                                                                                    conditions_from_main=conditions_from_main,
                                                                                    consistency_constraints=consistency_constraint,
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
        Test_before_edcr.lr = float(sys.argv.pop())
        Test_before_edcr.loss = sys.argv.pop()

        Test_after_edcr.lr = Test_before_edcr.lr
        Test_after_edcr.loss = Test_before_edcr.loss
    

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_before_edcr))
    runner = unittest.TextTestRunner(failfast=True).run(suite)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Test_after_edcr))
    runner = unittest.TextTestRunner(failfast=True).run(suite)