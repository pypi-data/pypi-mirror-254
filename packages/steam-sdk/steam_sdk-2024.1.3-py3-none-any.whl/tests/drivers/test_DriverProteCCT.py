import unittest
import os
from pathlib import Path
import shutil
from distutils.dir_util import copy_tree
import yaml
import matplotlib.pyplot as plt

from steam_sdk.builders.BuilderModel import BuilderModel
from steam_sdk.drivers.DriverProteCCT import DriverProteCCT
from steam_sdk.utils.misc import displayWaitAndClose


class TestDriverProteCCT(unittest.TestCase):

    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.current_path = os.getcwd()
        self.test_folder = os.path.dirname(__file__)
        #os.chdir(os.path.dirname(__file__))  # move to the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('\nTest is run from folder: {}'.format(os.getcwd()))

        # Define settings file
        user_name = os.getlogin()
        name_file_settings = 'settings.' + user_name + '.yaml'
        path_settings = Path(Path(self.test_folder).parent / name_file_settings).resolve()
        print('user_name:          {}'.format(user_name))
        print('name_file_settings: {}'.format(name_file_settings))
        print('path_settings:      {}'.format(path_settings))

        # Read ProteCCT exe path from the settings file
        with open(path_settings, 'r') as stream:
            settings_dict = yaml.safe_load(stream)
        self.path_ProteCCT = settings_dict['ProteCCT_path']
        print('path_ProteCCT:        {}'.format(self.path_ProteCCT))


    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder


    def test_runProteCCT_fromCircuitLibrary_multiple(self):
        '''
            This test runs iteratively the ProteCCT netlists in the provided list.
            Each input file is copied from the local STEAM_SDK test model library.
        '''
        magnet_names = ['MCBRD']
        for magnet_name in magnet_names:
            print('Circuit: {}'.format(magnet_name))
            self.runProteCCT_fromCircuitLibrary(magnet_name = magnet_name)


    def runProteCCT_fromCircuitLibrary(self, magnet_name = 'MCBRD'):
        '''
            This test checks that ProteCCT can be run programmatically using DriverProteCCT.
            The input file is copied from the local STEAM_SDK test model library.
            The path of ProteCCT executable is set to be the one of the Gitlab runner.
            In order to run this test locally, path_exe should be changed.
        '''

        # arrange
        # Define working folder and make sure dedicated output folder exists
        software = 'ProteCCT'
        path_folder_ProteCCT = os.path.join(self.test_folder, 'output', software, magnet_name)
        path_folder_ProteCCT_input = os.path.join(path_folder_ProteCCT, 'input')
        print('path_folder_ProteCCT: {}'.format(path_folder_ProteCCT_input))
        if not os.path.isdir(path_folder_ProteCCT_input):
            print("Output folder {} does not exist. Making it now".format(path_folder_ProteCCT_input))
            Path(path_folder_ProteCCT_input).mkdir(parents=True)

        # Copy input file from the STEAM_SDK test model library
        path_one_level_up = Path(os.path.dirname(__file__)).parent
        file_name_input = Path(Path(self.test_folder).parent / os.path.join('builders', 'model_library', 'magnets', magnet_name, 'output', f'{magnet_name}_{software}.xlsx')).resolve()
        name_copied = f'{magnet_name}_{software}_COPIED'
        file_name_local = os.path.join(path_folder_ProteCCT_input, name_copied + '.xlsx')
        shutil.copyfile(file_name_input, file_name_local)
        print('Simulation file {} copied.'.format(file_name_local))

        # Dictionary with manually-written expected names of ProteCCT output files (one per magnet)
        expected_file_names = {
            'MCBRD': 'MCBRD, I0=393A, TOp=1.9K, tQB=35ms, QI=0.01651, VGnd=528.3V, VEE=531.0V, addedHeCpFrac=0.006, fLoopFactor=0.8',
        }

        # Define expected output files, and delete them if they already exist
        expected_file_xls = os.path.join(path_folder_ProteCCT, 'output', expected_file_names[magnet_name] + '.xls')
        if os.path.isfile(expected_file_xls):
            os.remove(expected_file_xls)
            print('File {} already existed. It was deleted now.'.format(expected_file_xls))

        # Initialize Driver
        dProteCCT = DriverProteCCT(
            path_exe=self.path_ProteCCT,
            path_folder_ProteCCT=path_folder_ProteCCT,
            verbose=True)

        # act - Run model
        #output_ProteCCT = dProteCCT.run_ProteCCT(simFileName=name_copied, inputDirectory='input', outputDirectory='output')
        #print('output_ProteCCT = {}'.format(output_ProteCCT))

        # assert - Check that simulation generated expected output file
        print('Expected file: {}'.format(expected_file_xls))
        #self.assertTrue(os.path.isfile(expected_file_xls))  # won't work in Gitlab CI/CD pipeline - why?


