import os.path
import unittest
from steam_sdk.drivers.DriverFiQuS import DriverFiQuS
from steam_sdk.data.DataSettings import DataSettings
from pathlib import Path
import getpass
from steam_sdk.data.DataFiQuS import DataFiQuS
from steam_sdk.parsers.ParserYAML import yaml_to_data
from tests.TestHelpers import assert_equal_yaml


class TestDriverFiQuS(unittest.TestCase):

    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.current_path = os.getcwd()
        self.test_folder = os.path.dirname(__file__)
        os.chdir(self.test_folder)  # move to the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('\nTest is run from folder: {}'.format(os.getcwd()))

        # Define settings file
        user_name = getpass.getuser()
        print(f'FiQuS is running on machine with user name: {user_name}')
        if user_name in ['root', 'MP-WIN-02$']:
            user_name = 'SYSTEM'
        name_file_settings = 'settings.' + user_name + '.yaml'
        path_settings = Path(Path('..') / name_file_settings).resolve()
        print('user_name:          {}'.format(user_name))
        print('name_file_settings: {}'.format(name_file_settings))
        print('path_settings:      {}'.format(path_settings))

        # Read FiQuS_GetDP_path executable from the settings file
        self.settings = yaml_to_data(path_settings, DataSettings)
        print('FiQuS_path:        {}'.format(self.settings.FiQuS_path))

    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder

    def test_runFiQuS(self):
        """
        Test if FiQuS can be run
        """
        #magnet_names = ['MCBRD_2d2a_2n2a_0i', 'MQXA']
        #magnet_names = ['MQXA']
        magnet_names = ['MCBRD_2d2a_2n2a_0i'] # see if it passes now
        #magnet_names = []   # disabling this test due to inability to connect to remote to update fiqus-dev version

        for magnet_name in magnet_names:
            input_folder_path = os.path.join(self.test_folder, 'input', 'FiQuS', magnet_name)
            print(f'test_runFiQuS input folder path: {input_folder_path}')
            output_folder_path = os.path.join(self.test_folder, 'output', 'FiQuS', magnet_name)
            print(f'test_runFiQuS output folder path: {output_folder_path}')
            df = DriverFiQuS(FiQuS_path=self.settings.FiQuS_path, path_folder_FiQuS_input=input_folder_path,
                             path_folder_FiQuS_output=output_folder_path, GetDP_path=self.settings.GetDP_path)
            reference_folder_path = os.path.join(self.test_folder, 'references', 'FiQuS', magnet_name)
            fdm = yaml_to_data(os.path.join(input_folder_path, f'{magnet_name}.yaml'), DataFiQuS)
            geometry_folder = f'Geometry_{fdm.run.geometry}'

            df.run_FiQuS(sim_file_name=magnet_name)

            for file_content in ['geometry', 'mesh', 'solve', 'postproc']:
                if file_content == 'geometry':
                    output_file = os.path.join(output_folder_path, geometry_folder, f'{file_content}.yaml')
                elif file_content == 'mesh':
                    output_file = os.path.join(output_folder_path, geometry_folder, f'Mesh_{fdm.run.mesh}', f'{file_content}.yaml')
                else:
                    output_file = os.path.join(output_folder_path, geometry_folder, f'Mesh_{fdm.run.mesh}', f'Solution_{fdm.run.solution}', f'{file_content}.yaml')
                reference_file = os.path.join(reference_folder_path, f'{file_content}_REFERENCE.yaml')
                print(f'Comparing file type: {file_content}\noutput file: {output_file} and \nreference file: {reference_file}')
                assert_equal_yaml(output_file, reference_file)

