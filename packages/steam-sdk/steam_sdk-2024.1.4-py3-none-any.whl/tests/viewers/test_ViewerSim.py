import unittest
import os
import matplotlib.pyplot as plt
from pathlib import Path

from steam_sdk.viewers.ViewerSim import ViewerSim
from steam_sdk.viewers.ViewerMeas import ViewerMeas


class TestDictionarySimulationReader(unittest.TestCase):

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

    def test_read_sim(self):
        # Assign
        name_file = 'SimulationResults_LEDET_12.mat'
        path_sim = os.path.join('input\\test_simulation_data\SimulationResults_LEDET_')
        list_Signals = ['I_CoilSections', 'time_vector'] # ï»¿
        model_name = 'MBRD'
        simNumber = ['10', '12']
        path_output = Path('output')
        file_type = name_file.split('.')[1]  #preferred

        VS = ViewerSim(path_sim, model_name, simNumber, path_output, list_Signals, file_type)
        VS.read_simulationSignals()
        timeVector = []
        y_data = []
        data = []
        for n in range(len(simNumber)):
            timeVector.append(list(VS.simulationSignalsToPlot.loc['time_vector_' + simNumber[n]]))
            y_data.append(list(VS.simulationSignalsToPlot.loc['I_CoilSections_' + simNumber[n]]))
            data.append({'x': timeVector[n], 'y': y_data[n], 'z': list(range(len(timeVector[n])))})
        len_data = len(data)
        titles = ['Discharges MBRD'] * len_data
        labels = [{'x': 'x', 'y': 'y', 'z': ''}] * len_data
        types = ['plot'] * len_data
        texts = [{'x': [0], 'y': [0], 't': []}] * len_data
        legends = []
        for i in range(len_data):
            legends.append('I_discharge_'+str(i))
        style = [{'color': 'red', 'cmap': None, 'psize': 5, 'pstyle': '-'}] * len(data)
        window = [1] * len(data)
        scale = ['auto'] * len_data
        size = [12, 5]
        order = [1,1]

        VS.plot_ViewerSim(data, titles, labels, types, texts, size, legends, style, window, scale, order)

    def test_compare(self):
        # Assign
        name_file = 'SimulationResults_LEDET_12.mat'
        path_sim = os.path.join('input\\test_simulation_data\SimulationResults_LEDET_')
        list_Signals = ['I_CoilSections', 'time_vector']
        model_name = 'MBRD'
        simNumber = ['10']
        path_output = Path('output')
        file_type = name_file.split('.')[1]

        VS = ViewerSim(path_sim, model_name, simNumber, path_output, list_Signals, file_type)
        VS.read_simulationSignals()
        timeVector = []
        y_data = []
        data = []

        path_meas = Path('input')
        path_infotestCampaign = Path('test_infoTestCampaigns.csv')
        list_testCampaigns = ['test_simulation_data', 'HCMQXFM001-CR000072']
        list_testCampaigns = ['test_measurement_data', 'HCMQXFM001-CR000072']
        path_output = Path('output')

        # Act
        VM = ViewerMeas(path_meas, path_output, path_infotestCampaign, list_testCampaigns)
        VM.read_testCampaign(list_testCampaigns[0], flag_save=False)
        tdms_file_name = VM.tdms_file_names_dict[list_testCampaigns[0]][0]  # tdms file which should later be compared to the simulation

        for n in range(len(simNumber)):
            timeVector.append(list(VS.simulationSignalsToPlot.loc['time_vector_' + simNumber[n]]))
            timeVector.append(list(VM.data_dict[list_testCampaigns[0]][tdms_file_name]['timeVector']))

            y_data.append(list(VS.simulationSignalsToPlot.loc['I_CoilSections_' + simNumber[n]]))
            meas = VM.data_dict[list_testCampaigns[0]][tdms_file_name]
            y_data.append(list(meas.values())[1].tolist())

            for m in range(len(y_data)):
                data.append({'x': timeVector[m], 'y': y_data[m], 'z': list(range(len(timeVector[m])))})

        len_data = len(data)
        titles = ['Discharges MBRD'] * len_data
        labels = [{'x': 'x', 'y': 'y', 'z': ''}] * len_data
        types = ['plot'] * len_data
        texts = [{'x': [0], 'y': [0], 't': []}] * len_data
        legends = []
        for i in range(len_data):
            legends.append('I_discharge_' + str(i))
        style = [{'color': 'red', 'cmap': None, 'psize': 5, 'pstyle': '-'}] * len(data)
        window = [1] * len(data)
        scale = ['auto'] * len_data
        size = [12, 5]
        order = [1, 1]

        VS.plot_ViewerSim(data, titles, labels, types, texts, size, legends, style, window, scale, order)






