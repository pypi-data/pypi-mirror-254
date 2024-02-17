import unittest
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from steam_sdk.builders.BuilderLEDET import BuilderLEDET
from steam_sdk.builders.BuilderModel import BuilderModel
from steam_sdk.parsers.ParserLEDET import CompareLEDETParameters, ParserLEDET, check_for_differences
from steam_sdk.parsers.ParserProteCCT import CompareProteCCTParameters
from steam_sdk.parsers.ParserMap2d import parseRoxieMap2d
from tests.TestHelpers import assert_equal_yaml


class TestBuilderModel(unittest.TestCase):

    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.current_path = os.path.dirname(__file__)
        os.chdir(os.path.dirname(__file__))  # move the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('Test is run from folder: {}'.format(os.getcwd()))

    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder

        # Close all figures
        plt.close('all')


    def test_BuilderModel_COSIM_multiple(self):
        """
            Check that BuilderModel object can be initialized, read a real model input yaml file, and generate the correct COSIM model

            :param cosim_name: can be any co-simulation model name in the library
        """
        # arrange
        cosim_names = ['IPQ_2magnets']

        # act+assert
        for cosim_name in cosim_names:
            print('Co-simulation: {}'.format(cosim_name))
            self._compare_to_reference_COSIM(cosim_name, verbose=True)  # TODO write this test method


    ###############################################################################################
    # Helper methods
    def _compare_to_reference_COSIM(self, cosim_name, verbose=False, flag_plot_all=False, magnet_type='multipole'):
        """
            Helper method called by other methods
            Check that BuilderModel object can be initialized, read a model input yaml file, and generate a COSIM model
            This test checks:
             - TODO
             - TODO
             - TODO

            cosim_name: can be any co-simulation model name in the library
        """

        # arrange
        max_relative_error = 1e-6  # Maximum accepted relative error for excel, csv and map2d file comparison

        file_model_data = os.path.join('model_library', 'cosims', cosim_name, 'input', 'modelData_' + cosim_name + '.yaml')
        output_path = os.path.join('model_library', 'cosims', cosim_name, 'output')
        # input_file_REFERENCE = os.path.join('references', 'cosims', cosim_name, cosim_name + '_REFERENCE.xlsx')
        # input_file_GENERATED = os.path.join('model_library', 'cosims', cosim_name, 'output', cosim_name + '.xlsx')

        # act
        BM = BuilderModel(file_model_data=file_model_data, software=['COSIM'], case_model='cosim', flag_build=True,
                          output_path=output_path, verbose=verbose, flag_plot_all=flag_plot_all)

        # assert
        # TODO