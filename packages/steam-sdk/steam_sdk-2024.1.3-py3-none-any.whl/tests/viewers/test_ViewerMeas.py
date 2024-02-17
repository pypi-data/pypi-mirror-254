import unittest
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import sys
# np.set_printoptions(threshold=sys.maxsize)

from pathlib import Path
from steam_sdk.viewers.ViewerMeas import ViewerMeas
from steam_sdk.parsers.ParserTdms import ParserTdms
from steam_sdk.plotters.PlotterModel import PlotterModel


class TestDictionaryMeasurementReader(unittest.TestCase):

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

        # Close all figures
        plt.close('all')


    def test_read_testCampaign(self, maximum_allowed_rel_error=1e-6):
        # Assign
        #path_meas = Path(r'\\eosproject-smb\eosproject\s\sm18-magnettest\Data_TDMS') # use for data from server
        path_meas = Path('input')
        path_infotestCampaign = Path('test_infoTestCampaigns.csv')
        list_testCampaigns = ['test_measurement_data', 'possible_next_testCampaign']
        path_output = Path('output')

        VM = ViewerMeas(path_meas, path_output, path_infotestCampaign, list_testCampaigns)

        # Act: 2 TDMS file in testCampaign-folder (test_measurement_data) are used
        VM.read_testCampaign(VM.list_testCampaigns[0], flag_save=1)

        # reference data: use the ParserTdms to generate .csv files that got the data from the ParserTdms methods
        dict_tdms_header = {VM.list_groupnames[0]: ['IDCCT_HF','Vmag','Vsum','P3','P2','P4','P1','Vsum','Vsum','Vsum','Vsum']}
        dict_tdms_header_csv = {VM.list_groupnames[0]: ['IDCCT_HF', 'Vmag', 'Vsum', 'P3', 'P2', 'P4', 'P1', 'Vsum', 'Vsum', 'Vsum', 'Vsum', 'timeVector']}
        testCampaign_path = Path(path_meas, list_testCampaigns[0])
        for file in os.listdir(testCampaign_path):
            PT = ParserTdms(Path(testCampaign_path, file))
            PT.appendColumnToSignalData(dict_tdms_header)
            #Get time vector
            timeVector = PT.get_timeVector(VM.list_groupnames[0], 'IDCCT_HF')
            PT.signal_data = np.column_stack((PT.signal_data, timeVector))
            # Write to csv
            reference_output = Path(path_output, file.replace('.tdms', '') + '_ref.csv')
            PT.writeTdmsToCsv(reference_output, dict_tdms_header_csv)

        # Assert data in classes
        for file_VM, file_PT in zip(VM.tdms_file_names_dict[list_testCampaigns[0]], os.listdir(testCampaign_path)):
            PT = ParserTdms(Path(testCampaign_path, file_PT))
            PT.appendColumnToSignalData(dict_tdms_header)
            for signal_name_VM, data_PT in zip(dict_tdms_header[VM.list_groupnames[0]], PT.signal_data.T):
                data_signal_VM = VM.data_dict[list_testCampaigns[0]][file_VM][signal_name_VM]
                np.testing.assert_allclose(data_PT, data_signal_VM, rtol=1e-5, atol=0)

        # Assert for both csv files that are generated
        data_generated_1 = np.genfromtxt(Path(path_output, 'test_TDMSfile.csv'), dtype=float, delimiter=',', skip_header=1)
        data_reference_1 = np.genfromtxt(Path(path_output, 'test_TDMSfile_ref.csv'), dtype=float, delimiter=',', skip_header=1)
        data_generated_2 = np.genfromtxt(Path(path_output, 'test_TDMSfile2.csv'), dtype=float, delimiter=',', skip_header=1)
        data_reference_2 = np.genfromtxt(Path(path_output, 'test_TDMSfile2_ref.csv'), dtype=float, delimiter=',', skip_header=1)

        # Check that the number of elements in the generated matrix is the same as in the reference file
        if data_generated_1.size != data_reference_1.size:
            raise Exception('Generated csv file does not have the correct size.')

        if data_generated_2.size != data_reference_2.size:
            raise Exception('Generated csv file does not have the correct size.')

        # 1. file
        relative_differences_1 = np.abs(
            data_generated_1 - data_reference_1) / data_reference_1 # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference_1 = np.max(np.max(relative_differences_1))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference_1,
                               delta=maximum_allowed_rel_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(Path(path_output, 'test_TDMSfile.csv'), Path(path_output, 'test_TDMSfile_ref.csv'),
                                                                max_relative_difference_1 * 100))

        # 2. file
        relative_differences_2 = np.abs(
            data_generated_2 - data_reference_2) / data_reference_2  # Matrix with absolute values of relative differences between the two matrices
        max_relative_difference_2 = np.max(np.max(relative_differences_2))  # Maximum relative difference in the matrix
        self.assertAlmostEqual(0, max_relative_difference_2,
                               delta=maximum_allowed_rel_error)  # Check that the maximum relative difference is below
        print("Files {} and {} differ by less than {}%.".format(Path(path_output, 'test_TDMSfile2.csv'), Path(path_output, 'test_TDMSfile2_ref.csv'),
                                                                max_relative_difference_2 * 100))

    def test_identify_signals(self):
        # Assign
        #path_meas = Path(r'\\eosproject-smb\eosproject\s\sm18-magnettest\Data_TDMS') # use for data from server
        path_meas = Path('input')
        path_infotestCampaign = Path('test_infoTestCampaigns.csv')
        list_testCampaigns = ['test_measurement_data']
        path_output = Path('output')

        VM = ViewerMeas(path_meas, path_output, path_infotestCampaign, list_testCampaigns)
        data_infotestCampaign = pd.read_csv(VM.path_infotestCampaign, header=0)

        # Act
        signalsToRead_group = VM.identify_signals(VM.list_testCampaigns[0], VM.list_groupnames[0], data_infotestCampaign)

        # Reference
        signalsToRead_group_ref = ['IDCCT_HF','Vmag','Vsum','P3','P2','P4','P1','Vsum','Vsum','Vsum','Vsum']

        # Assert
        self.assertListEqual(signalsToRead_group,signalsToRead_group_ref)

    def test_plot_meas(self):
        """
            This is a potential example of a plot with the VieaerMeas class.
            For the class (ViewerMeas = VM) you need:
                                    - path where the data of the testCampaign is stored (so folder, where all of the testCampaigns are stored, not the data of one testCampaign)
                                    - path where the output of data of the testCampaigns are stored
                                    - path where infotestCampaign is stored
                                    - list with the testCampaigns one wants to examine
            x-data: timeVector can be obtained VM.data_dict[name_testCampaign][name_tdmsfile]['timeVector']
            y-data: signal can be obtained VM.data_dict[name_testCampaign][name_tdmsfile]['signal_name']
        """

        # Assign
        #path_meas = Path(r'\\eosproject-smb\eosproject\s\sm18-magnettest\Data_TDMS') # use for data from server
        path_meas = Path('input')
        path_infotestCampaign = Path('test_infoTestCampaigns.csv')
        list_testCampaigns = ['test_measurement_data', 'HCMQXFM001-CR000072']
        path_output = Path('output')

        # Act
        VM = ViewerMeas(path_meas,path_output,path_infotestCampaign,list_testCampaigns)
        VM.read_testCampaign(list_testCampaigns[0], flag_save=False)
        tdms_file_name = VM.tdms_file_names_dict[list_testCampaigns[0]][0]  #tdms file which should later be compared to the simulation
        timeVector = VM.data_dict[list_testCampaigns[0]][tdms_file_name]['timeVector']
        y_data = VM.data_dict[list_testCampaigns[0]][tdms_file_name]

        # Plot initialization

        data = [{'x': timeVector.tolist(), 'y': list(y_data.values())[0].tolist(), 'z': list(range(len(timeVector)))},
                {'x': timeVector.tolist(), 'y': list(y_data.values())[1].tolist(), 'z': list(range(len(timeVector)))},
                {'x': timeVector.tolist(), 'y': list(y_data.values())[2].tolist(), 'z': list(range(len(timeVector)))},
                {'x': timeVector.tolist(), 'y': list(y_data.values())[3].tolist(), 'z': list(range(len(timeVector)))},
                ]
        len_data = len(data)
        titles = []
        for i in range(5):
            titles.append('Plot_{}'.format(i))
        labels = [
            {'x': 'Time [s]', 'y': 'Current [kA]', 'z': ''},
            {'x': 'Time [s]', 'y': 'Voltage [V]', 'z': ''},
            {'x': 'Time [s]', 'y': 'Voltage [V]', 'z': ''},
            {'x': 'Time [s]', 'y': 'Voltage [V]', 'z': ''},
            ]
        types = ['plot']* len_data
        texts = [{'x': [0], 'y': [0], 't': []}] * len_data
        legends = []
        for i in range(5):
            legends.append(list(y_data.keys())[i])
        style = [{'color': 'red', 'cmap': None, 'psize': 5, 'pstyle': '|'},
                 {'color': 'red', 'cmap': None, 'psize': 5, 'pstyle': '-'},
                 {'color': 'green', 'cmap': None, 'psize': 5,'pstyle': '+'},
                 {'color': 'blue', 'cmap': None, 'psize': 1, 'pstyle': '-.'},]
        window = [1,2,3,3,]
        scale = ['auto'] * len_data
        size = [12, 5]
        order = [3,1]

        VM.plot_ViewerMeas(data, titles, labels, types, texts, size, legends, style, window, scale, order)






