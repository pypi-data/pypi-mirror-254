import shutil
import unittest
import os
import math

from steam_sdk.builders.BuilderModel import BuilderModel
from steam_sdk.data.DataEventMagnet import DataEventMagnet
from steam_sdk.parsims.ParsimEventMagnet import ParsimEventMagnet
from tests.TestHelpers import assert_equal_readable_files


class TestParsimEventMagnet(unittest.TestCase):

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


    def test_ParsimSweep_Initialize(self):
        name_reference_file = 'example_input_par_sweep.yml'
        file_path = os.getcwd()
        reference_file = os.path.join(os.path.dirname(file_path), 'parsims', 'input', 'run_parsim_sweep', name_reference_file)
        ref_model = BuilderModel(file_model_data=reference_file)
        ps = ParsimSweep(ref_model=ref_model)


    def test_ParsimSweep_ReadFromInput(self):
        file_path = os.getcwd()
        # path to yaml:
        yaml_file_name = 'example_input_par_sweep.yml'
        yaml_path = os.path.join(os.path.dirname(file_path), 'parsims', 'input', 'run_parsim_sweep', yaml_file_name)
        ref_model = BuilderModel(file_model_data=yaml_path)
        # create instance of ParsimSweep
        ps = ParsimSweep(ref_model=ref_model)
        # path to csv
        csv_file_name = 'TEST_par_sweep.csv'
        csv_path = os.path.join(os.path.dirname(file_path), 'parsims', 'input', 'run_parsim_sweep', csv_file_name)

        # act
        ps.read_from_input(file_path=csv_path, verbose=True)

        # assert
        sim_nums = ps.simulation_numbers
        self.assertEqual('0.001', ps.dict_BuilderModels[sim_nums[0]].model_data.Circuit.R_circuit)
        self.assertEqual('0.01', ps.dict_BuilderModels[sim_nums[1]].model_data.Circuit.R_circuit)
        self.assertEqual('0.0654', ps.dict_BuilderModels[sim_nums[2]].model_data.Circuit.R_circuit)
        self.assertEqual('nope', ps.dict_BuilderModels[sim_nums[0]].comments)
        self.assertEqual('124', ps.dict_BuilderModels[sim_nums[1]].simulation_number)
        self.assertEqual('MBRB', ps.dict_BuilderModels[sim_nums[2]].simulation_name)

