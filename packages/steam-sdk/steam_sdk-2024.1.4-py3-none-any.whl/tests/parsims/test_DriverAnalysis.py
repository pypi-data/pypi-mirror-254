import unittest
import getpass

from steam_sdk.data.DataSettings import DataSettings
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.drivers.DriverDakota import DriverDakota
from steam_sdk.drivers.DriverAnalysis import DriverAnalysis
from steam_sdk.utils.make_folder_if_not_existing import *


class TestDriverAnalysis(unittest.TestCase):


    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.current_path = os.getcwd()
        self.test_folder = os.path.dirname(__file__)
        self.settings_path = Path(self.test_folder).parent
        # os.chdir(self.test_folder)  # move to the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('\nTest is run from folder: {}'.format(os.getcwd()))

        # Define settings file
        user_name = getpass.getuser()
        print(f'AnalysisSTEAM is running on machine with user name: {user_name}')
        if user_name in ['root', 'MP-WIN-02$']:
            user_name = 'SYSTEM'
        name_file_settings = 'settings.' + user_name + '.yaml'
        path_settings = Path(self.settings_path / name_file_settings).resolve()
        print('user_name:          {}'.format(user_name))
        print('name_file_settings: {}'.format(name_file_settings))
        print('path_settings:      {}'.format(path_settings))

        # Read DAKOTA executable from the settings file
        self.settings = yaml_to_data(path_settings, DataSettings)
        print('Dakota_path:        {}'.format(self.settings.Dakota_path))

        self.folder = {}
        for folder in ['input', 'output']:
            self.folder[folder] = Path(Path(f'../parsims/{folder}/Dakota')).resolve()
            print(f'{folder} folder: {self.folder[folder]}')
            make_folder_if_not_existing(self.folder[folder])

    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder

    def test_DriverAnalysis_Initialize(self):
        analysis_yaml_path = Path(r"../drivers/input/Analysis/TestFile_AnalysisSTEAM_Dakota_FiQuS.yaml").resolve()
        DriverAnalysis(analysis_yaml_path=analysis_yaml_path, settings_path=self.settings_path)

    # def test_DriverAnalysis_Run(self):
    #     analysis_yaml_path = Path(r"../drivers/input/Analysis/TestFile_AnalysisSTEAM_Dakota_FiQuS.yaml").resolve()
    #     iterable_steps_list = ['modifyModel_for_preparation', 'modifyModel_for_mesh_and_solution', 'RunSim_BM1']
    #
    #     dd = DriverDakota(dakota_path=self.settings.Dakota_path, analysis_yaml_path=analysis_yaml_path, settings_path=self.settings_path,
    #                       iterable_steps=iterable_steps_list, dakota_input_folder=self.folder['input'])
    #     dakota_input_file = os.path.join(self.folder['input'], 'Dakota_test_Iref.in')
    #     print(f'Running Dakota with {dakota_input_file}')
    #     dd.prepare()
    #     dd.run(dakota_input_file)
