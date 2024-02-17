import unittest
import os
from steam_sdk.parsers.ParserMat import get_signals_from_mat, get_signals_from_mat_to_dict
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


    def test_read_mat(self):
        # arrange
        file_name = os.path.join('input', 'TEST_FILE.mat')
        selected_signals = ['time_vector', 'I_CoilSections', 'HotSpotT']

        # act
        df_signals = get_signals_from_mat(file_name, selected_signals)


    def test_check_mat(self, max_relative_error=1e-6):
        # arrange
        file_name = os.path.join('input', 'TEST_FILE.mat')
        selected_signals = ['time_vector', 'I_CoilSections']#, 'HotSpotT']
        output_path = os.path.join('output', 'testmat.csv')
        reference_path = os.path.join('references', 'testmat_REFERENCE.csv')

        # act
        df_signals = get_signals_from_mat(file_name, selected_signals)

        #assert
        # dictionary = df_signals.to_dict('list')
        # sio.savemat('output\\testmat.mat', dictionary)
        df_signals.to_csv(output_path, index=False)

        data_generated = np.genfromtxt(output_path, dtype=float, delimiter=',', skip_header=1)
        data_reference = np.genfromtxt(reference_path, dtype=float, delimiter=',', skip_header=1)

        # Check that the number of elements in the generated matrix is the same as in the reference file
        if data_generated.size != data_reference.size:
            raise Exception('Generated csv file does not have the correct size.')

        data_generated[data_generated == 0] = 1e-12
        data_reference[data_reference == 0] = 1e-12

        relative_differences = np.abs(data_generated - data_reference) / data_reference  # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference = np.max(np.max(relative_differences))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference, delta=max_relative_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(output_path, reference_path, max_relative_difference * 100))



    def test_read_mat_columns(self, max_relative_error=1e-6):
        # arrange
        file_name = os.path.join('input', 'TEST_FILE.mat')
        selected_signals = ['time_vector', 'I_QH(:,2)']
        output_path = os.path.join('output', 'testmat_columns.csv')
        reference_path = os.path.join('references', 'testcsv_columns_REFERENCE.csv')

        # act
        df_signals = get_signals_from_mat(file_name, selected_signals)

        # assert
        df_signals.to_csv(output_path, index=False)
        data_generated = np.genfromtxt(output_path, dtype=float, delimiter=',', skip_header=1)
        data_reference = np.genfromtxt(reference_path, dtype=float, delimiter=',', skip_header=1)

        # Check that the number of elements in the generated matrix is the same as in the reference file
        if data_generated.size != data_reference.size:
            raise Exception('Generated csv file does not have the correct size.')

        # Substitute 0 with small value to avoid error when dividing by zero
        data_generated[data_generated == 0] = 1e-12
        data_reference[data_reference == 0] = 1e-12

        relative_differences = np.abs(data_generated - data_reference) / data_reference  # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference = np.max(np.max(relative_differences))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference, delta=max_relative_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(output_path, reference_path,max_relative_difference * 100))

    def test_read_mat_structure(self, max_relative_error=1e-6):
        # arrange
        file_name = os.path.join('input', 'read_mat', 'TestFile_SimulationResults_LEDET_0.mat')
        selected_signals = ['var_int', 'var_string', 'time_vector','model_data', 'time_vector', 'model_geometry']
        output_path = os.path.join('output', 'testmat_structure.csv')
        reference_path = os.path.join('references', 'testmat_structure_REFERENCE.csv')

        # act
        df_signals = get_signals_from_mat_to_dict(file_name, selected_signals)

        # assert
        df_signals.to_csv(output_path, index=False)
        data_generated = np.genfromtxt(output_path, dtype=float, delimiter=',', skip_header=1)
        data_reference = np.genfromtxt(reference_path, dtype=float, delimiter=',', skip_header=1)

        # Check that the number of elements in the generated matrix is the same as in the reference file
        if data_generated.size != data_reference.size:
            raise Exception('Generated csv file does not have the correct size.')

        # Substitute 0 with small value to avoid error when dividing by zero
        data_generated[data_generated == 0] = 1e-12
        data_reference[data_reference == 0] = 1e-12

        relative_differences = np.abs(data_generated - data_reference) / data_reference  # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference = np.max(np.max(relative_differences))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference, delta=max_relative_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(output_path, reference_path,max_relative_difference * 100))

