import unittest
import os
import matplotlib.pyplot as plt
import numpy as np

from steam_sdk.parsers.CSD_Reader import CSD_read
from steam_sdk.utils.misc import displayWaitAndClose


class TestCSDReader(unittest.TestCase):

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


    def test_read_csd_timeDomain(self):
        # arrange
        file_name = os.path.join('input', 'test_csd_time.csd')
        selected_signals = ['I(r1_warm)', 'I(x_MB1.L1)']

        # act
        csd = CSD_read(file_name)
        time = csd.time
        data = csd.data
        signals = csd.signal_names
        print(signals)

        # assert
        selectedFont = {'fontname': 'DejaVu Sans', 'size': 14}
        plt.figure(figsize=(6, 5))
        for s, signal in enumerate(selected_signals):
            print(s)
            print(signal)
            plt.plot(time, data[:,s], '-', linewidth=2.0, label=signals[s])
        plt.xlabel('Time [s]', **selectedFont)
        plt.ylabel('Current [A]', **selectedFont)
        plt.grid(True)
        plt.legend(loc='best')
        displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=2)

    def test_read_csd_frequencyDomain(self):
        # arrange
        file_name = os.path.join('input', 'test_csd_frequency.csd')

        # act
        csd = CSD_read(file_name)
        freq = csd.time
        data = csd.data
        signals = csd.signal_names

        assert len(data[0])==8, 'No Im and Re part for all signals present'
        assert (np.max(data)-3.4302132)<0.1, 'Max value of result does not fit anymore'
        selectedFont = {'fontname': 'DejaVu Sans', 'size': 14}
        plt.figure(figsize=(10, 10))
        plt.plot(freq, data, 'k-', linewidth=2.0, label=signals)
        displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)
