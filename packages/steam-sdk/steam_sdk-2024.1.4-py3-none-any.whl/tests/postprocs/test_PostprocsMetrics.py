import unittest
import os
import numpy as np

from steam_sdk.postprocs.PostprocsMetrics import PostprocsMetrics


class TestPostprocsMetrics(unittest.TestCase):

    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.current_path = os.getcwd()
        os.chdir(os.path.dirname(__file__))  # move to the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('\nTest is run from folder: {}'.format(os.getcwd()))

    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder


    def test_peak_value(self):

        """
            function to test the peak value function
        """

        # arrange
        metrics_to_do = ['max']
        var_to_interpolate = [0, 4, 6, 3.78, 2, 100.1, 6]

        # act
        metrics = PostprocsMetrics(metrics_to_do = metrics_to_do, var_to_interpolate = var_to_interpolate)
        peak_value = metrics.metrics_result

        # assert
        peak_reference = 100.1

        self.assertEqual(peak_value[0], peak_reference)
        print("The peak value is calculated correctly with {}.".format(peak_reference))

    def test_maximum_absolute_error(self):

        """
            function to test the maximum absolute error function
        """

        # arrange
        metrics_to_do = ['maximum_abs_error']
        var_to_interpolate = [0, 4, 6, 3.78, 2, 100.1, 6]
        var_to_interpolate_ref = [1, 15, 6, 200, 10, 9, 5]
        time_vector = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        time_vector_ref = [0, 0.5, 1, 1.5, 2, 2.5, 3]

        # act
        metrics = PostprocsMetrics(metrics_to_do = metrics_to_do, var_to_interpolate = var_to_interpolate, var_to_interpolate_ref = var_to_interpolate_ref, time_vector = time_vector, time_vector_ref = time_vector_ref)
        max_absolute_error = metrics.metrics_result[0]

        # assert
        max_absolute_error_reference = 196.22

        self.assertEqual(max_absolute_error, max_absolute_error_reference)
        print("The maximum_absolute_error is calculated correctly with {}.".format(max_absolute_error_reference))

    def test_RMSE(self):

        """
            function to test the RMSE function
        """

        # arrange
        metrics_to_do = ['RMSE']
        var_to_interpolate = [0.1, 1.2, 4.2, 5, 1.9, 10.1, 2.5]
        var_to_interpolate_ref = [0, 1.3, 4, 5, 2, 10, 2]
        time_vector = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        time_vector_ref = [0, 0.5, 1, 1.5, 2, 2.5, 3]

        # act
        metrics = PostprocsMetrics(metrics_to_do = metrics_to_do, var_to_interpolate = var_to_interpolate, var_to_interpolate_ref = var_to_interpolate_ref, time_vector = time_vector, time_vector_ref = time_vector_ref)
        RMSE = metrics.metrics_result[0]

        # assert
        RMSE_reference = 0.217124

        self.assertAlmostEqual(RMSE, RMSE_reference, delta = 1e-6)
        print("The RMSE is calculated correctly with {}.".format(RMSE_reference))

    def test_RMSE_ratio(self):

        """
            function to test the RMSE_ratio function
        """

        # arrange
        metrics_to_do = ['RMSE_ratio']
        var_to_interpolate = [0.1, 1.2, 4.2, 5, 1.9, 10.1, 2.5]
        var_to_interpolate_ref = [0, 1.3, 4, 5, 2, 10, 2]
        time_vector = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        time_vector_ref = [0, 0.5, 1, 1.5, 2, 2.5, 3]

        # act
        metrics = PostprocsMetrics(metrics_to_do = metrics_to_do, var_to_interpolate = var_to_interpolate, var_to_interpolate_ref = var_to_interpolate_ref, time_vector = time_vector, time_vector_ref = time_vector_ref)
        RMSE_ratio = metrics.metrics_result[0]

        # assert
        RMSE_ratio_reference = 0.0217124

        self.assertAlmostEqual(RMSE_ratio, RMSE_ratio_reference, delta = 1e-6)
        print("The RMSE_ratio is calculated correctly with {}.".format(RMSE_ratio_reference))

    def test_multiple(self):

        """
            function to test multiple functions which are part of PostprocsMetrics
        """

        # arrange
        metrics_to_do = ['quench_load', 'quench_load_error', 'RMSE']
        var_to_interpolate = [0.1, 1.2, 4.2, 5, 1.9, 10.1, 2.5]
        var_to_interpolate_ref = [0, 1.3, 4, 5, 2, 10, 2]
        time_vector = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        time_vector_ref = [0, 0.5, 1, 1.5, 2, 2.5, 3]

        # act
        metrics = PostprocsMetrics(metrics_to_do = metrics_to_do, var_to_interpolate = var_to_interpolate, var_to_interpolate_ref = var_to_interpolate_ref, time_vector = time_vector, time_vector_ref = time_vector_ref)
        metrics_result = metrics.metrics_result

        # assert
        metrics_result_reference = [74.855, 1.510001, 0.217124]

        np.testing.assert_almost_equal(metrics_result, metrics_result_reference, 6)
        print("The metric results are calculated correctly with {}.".format(metrics_result_reference))