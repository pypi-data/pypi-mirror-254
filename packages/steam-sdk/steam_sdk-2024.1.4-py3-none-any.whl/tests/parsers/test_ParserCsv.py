import unittest
import os
import csv
from steam_sdk.parsers.ParserCsv import get_signals_from_csv
from steam_sdk.parsers.ParserCsv import load_global_parameters_from_csv
from tests.TestHelpers import assert_equal_yaml
import numpy as np

class TestParserCsv(unittest.TestCase):

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


    def test_read_csv(self, max_relative_error=1e-6):
        # arrange
        file_name = os.path.join('input', 'TEST_FILE.csv')
        selected_signals = ['time_vector', 'I_CoilSections_1']
        output_path = os.path.join('output', 'testcsv.csv')
        reference_path = os.path.join('references', 'testcsv_REFERENCE.csv')

        # act
        df_signals = get_signals_from_csv(file_name, selected_signals)

        # assert
        df_signals.to_csv(output_path, index=False)

        data_generated = np.genfromtxt(output_path, dtype=float, delimiter=',', skip_header=1)
        data_reference = np.genfromtxt(reference_path, dtype=float, delimiter=',', skip_header=1)

        # Check that the number of elements in the generated matrix is the same as in the reference file
        if data_generated.size != data_reference.size:
            raise Exception('Generated csv file does not have the correct size.')

        relative_differences = np.abs(data_generated - data_reference) / data_reference  # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference = np.max(np.max(relative_differences))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference, delta=max_relative_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(output_path, reference_path,max_relative_difference * 100))

    def test_check_global_parameters_from_csv_table(self):
        #arrange
        reference_file = os.path.join('references', 'load_parameters_from_csv',
                                      'reference_file_load_parameters_from_csv.yaml')  # this is a  yaml model file with manually edited glocal parameters

        filename=os.path.join('input', 'load_parameters_from_csv', 'input_test_load_parameters_from_csv.csv')
        circuit_name="RCS.A12B1"
        steam_models_path='../builders/model_library'
        case_model="circuit"

        #act
        expected_file = load_global_parameters_from_csv(filename, circuit_name, steam_models_path, case_model) # this file will be written by the test. Its name is written programmatically

        #assert
        assert_equal_yaml(reference_file, expected_file)
