import unittest
import os

from pathlib import Path

from tests.TestHelpers import assert_equal_readable_files
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.parsers.ParserDakota import ParserDakota
from steam_sdk.data.DataDakota import DataDakota
from steam_sdk.utils.make_folder_if_not_existing import make_folder_if_not_existing


class TestParserDakota(unittest.TestCase):

    def setUp(self) -> None:
        """
            This function is executed before each test in this class
        """
        self.test_folder = os.path.dirname(__file__)
        self.current_path = Path(__file__).parent  # os.getcwd()
        os.chdir(os.path.dirname(__file__))  # move to the directory where this file is located
        print('\nCurrent folder:          {}'.format(self.current_path))
        print('\nTest is run from folder: {}'.format(os.getcwd()))

    def tearDown(self) -> None:
        """
            This function is executed after each test in this class
        """
        os.chdir(self.current_path)  # go back to initial folder

    def test_write_Dakota_in_from_yaml(self):
        """
        Test function to test basic input conversion .yaml -> .in
        """
        output_folder = os.path.join(self.test_folder, 'output', 'Dakota')
        make_folder_if_not_existing(output_folder)
        dakota_in = os.path.join(output_folder, 'DAKOTA_input')
        Parser_DAKOTA = ParserDakota(dakota_in)


        dakota_yaml = os.path.join(self.test_folder, 'input', 'Dakota', 'DAKOTA_input.yaml')

        file_DAKOTA_yaml = yaml_to_data(dakota_yaml, DataDakota)
        Parser_DAKOTA.assemble_in_file(template='template_Dakota.in', dakota_data=file_DAKOTA_yaml)

        dakota_in_ref = os.path.join(self.test_folder, 'references', 'Dakota', 'DAKOTA_input.in')
        assert_equal_readable_files(dakota_in + '.in', dakota_in_ref)
