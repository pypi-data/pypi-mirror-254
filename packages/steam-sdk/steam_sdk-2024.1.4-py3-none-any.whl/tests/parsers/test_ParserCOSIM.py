import os
import unittest

import numpy as np

from steam_sdk.builders.BuilderCosim import BuilderCosim
from steam_sdk.cosims.CosimPyCosim import CosimPyCosim
from steam_sdk.data.DataCosim import NSTI
from steam_sdk.data.DataModelCosim import DataModelCosim
from steam_sdk.parsers.ParserCOSIM import ParserCOSIM
from steam_sdk.parsers.ParserLEDET import CompareLEDETParameters
from steam_sdk.parsers.ParserMap2d import parseRoxieMap2d
from steam_sdk.parsers.ParserPSPICE import ParserPSPICE
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.utils.delete_if_existing import delete_if_existing
from tests.TestHelpers import assert_equal_json, assert_equal_readable_files, assert_equal_yaml


class TestParserCOSIM(unittest.TestCase):

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


    def test_write_config_file_COSIM(self):
        '''
        Test that the method write_config_file() generates a correct .json file
        '''
        # arrange
        path_output = os.path.join('output', 'COSIM', 'RQX', '23')
        delete_if_existing(path_output)
        file_name_GENERATED = 'TestFile_write_config_file_COSIM.json'
        path_model_data = os.path.join('input', 'COSIM', 'TestFile_model_data_write_config_file.yaml')
        path_name_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_config_file_COSIM_REFERENCE.json')
        path_name_GENERATED = os.path.join(path_output, 'Input', file_name_GENERATED)
        verbose = True

        # act
        BC = BuilderCosim(file_model_data=path_model_data, software=['COSIM'], flag_build=False,
                          output_path=os.path.join('output', 'COSIM'), verbose=verbose)
        pCOSIM = ParserCOSIM(BC.cosim_data)
        pCOSIM.write_config_file(output_file_name=file_name_GENERATED, verbose=verbose)

        # assert
        assert_equal_json(path_name_REFERENCE, path_name_GENERATED)


    def test_setup_folders_COSIM(self):
        '''
        Test that the method setup_cosim_folders() generates a correct .json file
        '''
        # arrange
        path_output = os.path.join('output', 'COSIM', 'RQX', '24')
        delete_if_existing(path_output)
        path_model_data = os.path.join('input', 'COSIM', 'TestFile_model_data_setup_cosim_folders.yaml')
        list_path_folder_GENERATED = [
            os.path.join(path_output, 'Input'),
            os.path.join(path_output, 'Input', 'PSPICE_1'),
            os.path.join(path_output, 'Input', 'LEDET_1'),
            os.path.join(path_output, 'Input', 'LEDET_2'),
            os.path.join(path_output, 'Input', 'LEDET_3'),
            os.path.join(path_output, 'Input', 'LEDET_4'),
            ]
        verbose = True

        # act
        BC = BuilderCosim(file_model_data=path_model_data, software=['COSIM'], flag_build=False,
                          output_path=os.path.join('output', 'COSIM'), verbose=verbose)
        pCOSIM = ParserCOSIM(BC.cosim_data)
        pCOSIM.setup_cosim_folders(verbose=verbose)

        # assert
        for folder in list_path_folder_GENERATED:
            self.assertTrue(os.path.isdir(folder))
            print(f'Folder {folder} exists.')


    def test_write_model_COSIM_LEDET_PSPICE(self):
        '''
        Test that the method write_cosim_model() generates a correct .json file
        '''
        # arrange
        max_relative_error = 1e-6  # Maximum accepted relative error for excel, csv and map2d file comparison
        path_output = os.path.join('output', 'COSIM', 'RQX', '25')
        delete_if_existing(path_output)
        path_model_data = os.path.join('input', 'COSIM', 'TestFile_model_data_write_model_COSIM_LEDET_PSPICE.yaml')
        # Subfolders to generate
        list_path_folder_GENERATED = [
            os.path.join(path_output, 'Input'),
            os.path.join(path_output, 'Input', 'PSPICE_1'),
            os.path.join(path_output, 'Input', 'LEDET_1', 'LEDET', 'MQXA', 'Input', 'Control current input'),
            os.path.join(path_output, 'Input', 'LEDET_1', 'LEDET', 'MQXA', 'Input', 'Initialize variables'),
            os.path.join(path_output, 'Input', 'LEDET_1', 'Field Maps', 'MQXA'),
            os.path.join(path_output, 'Input', 'LEDET_2'),
            os.path.join(path_output, 'Input', 'LEDET_3'),
            os.path.join(path_output, 'Input', 'LEDET_4'),
            ]
        # Configuration files to generate (only 1 and 2 are checked, 3 and 4 are not)
        path_name_PSPICE_1_config_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_PSPICE_1_config_REFERENCE.json')
        path_name_PSPICE_1_config_GENERATED = os.path.join(path_output, 'Input', 'PSPICE_1', 'PSPICE_1_config.json')
        path_name_LEDET_1_config_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_1_config_REFERENCE.json')
        path_name_LEDET_1_config_GENERATED = os.path.join(path_output, 'Input', 'LEDET_1', 'LEDET_1_config.json')
        path_name_LEDET_2_config_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_2_config_REFERENCE.json')
        path_name_LEDET_2_config_GENERATED = os.path.join(path_output, 'Input', 'LEDET_2', 'LEDET_2_config.json')
        # Port definition files to generate (only 1 and 2 are checked, 3 and 4 are not)
        path_name_PSPICE_1_ports_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_PSPICE_1_InputOutputPortDefinition_REFERENCE.json')
        path_name_PSPICE_1_ports_GENERATED = os.path.join(path_output, 'Input', 'PSPICE_1', 'PSPICE_1_InputOutputPortDefinition.json')
        path_name_LEDET_1_ports_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_1_InputOutputPortDefinition_REFERENCE.json')
        path_name_LEDET_1_ports_GENERATED = os.path.join(path_output, 'Input', 'LEDET_1', 'LEDET_1_InputOutputPortDefinition.json')
        path_name_LEDET_2_ports_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_2_InputOutputPortDefinition_REFERENCE.json')
        path_name_LEDET_2_ports_GENERATED = os.path.join(path_output, 'Input', 'LEDET_2', 'LEDET_2_InputOutputPortDefinition.json')
        # LEDET input files to generate (only 1 and 2 are checked, 3 and 4 are not)
        path_name_LEDET_1_input_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_1_MQXA_11_REFERENCE.xlsx')
        path_name_LEDET_1_input_GENERATED = os.path.join(path_output, 'Input', 'LEDET_1', 'LEDET', 'MQXA', 'Input', 'MQXA_11.xlsx')
        path_name_LEDET_2_input_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_1_MQXB_10_REFERENCE.xlsx')
        path_name_LEDET_2_input_GENERATED = os.path.join(path_output, 'Input', 'LEDET_2', 'LEDET', 'MQXB', 'Input', 'MQXB_10.xlsx')
        path_name_LEDET_1_fieldmap_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_1_MQXA_fieldmap_REFERENCE.map2d')
        path_name_LEDET_1_fieldmap_GENERATED = os.path.join(path_output, 'Input', 'LEDET_1', 'Field Maps', 'MQXA', 'MQXA_All_WithIron_WithSelfField.map2d')
        path_name_LEDET_2_fieldmap_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_LEDET_2_MQXB_fieldmap_REFERENCE.map2d')
        path_name_LEDET_2_fieldmap_GENERATED = os.path.join(path_output, 'Input', 'LEDET_2', 'Field Maps', 'MQXB', 'MQXB_All_WithIron_WithSelfField.map2d')
        # PSPICE netlist file and auxiliary files
        path_name_PSPICE_1_netlist_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_PSPICE_1_netlist_REFERENCE.cir')
        path_name_PSPICE_1_netlist_GENERATED = os.path.join(path_output, 'Input', 'PSPICE_1', 'RQX_cosim.cir')
        path_name_PSPICE_1_additional_file_REFERENCE = os.path.join('references', 'COSIM', 'TestFile_write_cosim_model_PSPICE_1_additional_file_REFERENCE.stl')
        path_name_PSPICE_1_additional_file_GENERATED = os.path.join(path_output, 'Input', 'PSPICE_1', 'ExternalStimulus.stl')
        list_PSPICE_1_additional_files_GENERATED = ['RQX_Busbars.lib', 'RQX_Diodes.lib', 'generic_power_converters.lib', 'magnets_generic.lib', 'RQX_PCs.lib', 'RQX_Thyristors.lib', 'ExternalStimulus.stl']
        verbose = True

        # act
        BC = BuilderCosim(file_model_data=path_model_data, software=['COSIM'], flag_build=False,
                          output_path=os.path.join('output', 'COSIM'), verbose=verbose)
        pCOSIM = ParserCOSIM(BC.cosim_data)
        pCOSIM.setup_cosim_folders(verbose=verbose)
        pCOSIM.write_cosim_model(verbose=verbose)

        # assert 1 - Subfolders generated
        for folder in list_path_folder_GENERATED:
            self.assertTrue(os.path.isdir(folder))
            print(f'Folder {folder} exists.')
        # assert 2 - LEDET configuration files generated
        assert_equal_json(path_name_LEDET_1_config_REFERENCE, path_name_LEDET_1_config_GENERATED)
        assert_equal_json(path_name_LEDET_2_config_REFERENCE, path_name_LEDET_2_config_GENERATED)
        # assert 3 - LEDET port definition files generated
        assert_equal_json(path_name_LEDET_1_ports_REFERENCE, path_name_LEDET_1_ports_GENERATED)
        assert_equal_json(path_name_LEDET_2_ports_REFERENCE, path_name_LEDET_2_ports_GENERATED)
        # assert 4 - LEDET input files generated
        self.assertTrue(CompareLEDETParameters(path_name_LEDET_1_input_GENERATED, path_name_LEDET_1_input_REFERENCE, max_relative_error=max_relative_error, verbose=verbose))
        self.assertTrue(CompareLEDETParameters(path_name_LEDET_2_input_GENERATED, path_name_LEDET_2_input_REFERENCE, max_relative_error=max_relative_error, verbose=verbose))
        # assert 5 - Magnetic field map needed for LEDET generated
        values_REFERENCE = parseRoxieMap2d(path_name_LEDET_1_fieldmap_REFERENCE, headerLines=1)
        values_GENERATED = parseRoxieMap2d(path_name_LEDET_1_fieldmap_GENERATED, headerLines=1)
        np.testing.assert_allclose(values_GENERATED, values_REFERENCE, rtol=max_relative_error, atol=0)
        print("Files {} and {} differ by less than {}%.".format(path_name_LEDET_1_fieldmap_REFERENCE, path_name_LEDET_1_fieldmap_GENERATED, max_relative_error * 100))
        values_REFERENCE = parseRoxieMap2d(path_name_LEDET_2_fieldmap_REFERENCE, headerLines=1)
        values_GENERATED = parseRoxieMap2d(path_name_LEDET_2_fieldmap_GENERATED, headerLines=1)
        np.testing.assert_allclose(values_GENERATED, values_REFERENCE, rtol=max_relative_error, atol=0)
        print("Files {} and {} differ by less than {}%.".format(path_name_LEDET_2_fieldmap_REFERENCE, path_name_LEDET_2_fieldmap_GENERATED, max_relative_error * 100))
        # assert 6 - PSPICE configuration files generated
        assert_equal_json(path_name_PSPICE_1_config_REFERENCE, path_name_PSPICE_1_config_GENERATED)
        # assert 7 - PSPICE port definition files generated
        assert_equal_readable_files(path_name_PSPICE_1_ports_REFERENCE, path_name_PSPICE_1_ports_GENERATED)
        # assert 8 - PSPICE netlist
        pPSPICE_netlist_REFERENCE = ParserPSPICE(None)
        pPSPICE_netlist_REFERENCE.read_netlist(path_name_PSPICE_1_netlist_REFERENCE, verbose=True)
        pPSPICE_netlist_GENERATED = ParserPSPICE(None)
        pPSPICE_netlist_GENERATED.read_netlist(path_name_PSPICE_1_netlist_GENERATED, verbose=True)
        self.assertDictEqual(dict(pPSPICE_netlist_REFERENCE.circuit_data.Netlist), dict(pPSPICE_netlist_GENERATED.circuit_data.Netlist))
        # assert 9 - PSPICE additional files generated
        for file in list_PSPICE_1_additional_files_GENERATED:
            self.assertTrue(os.path.isfile(os.path.join(path_output, 'Input', 'PSPICE_1', file)))
            print(f'File {file} exists.')
        # assert 10 - One selected PSPICE additional file equal to reference
        assert_equal_readable_files(path_name_PSPICE_1_additional_file_REFERENCE, path_name_PSPICE_1_additional_file_GENERATED)


    def test_write_model_PyCOSIM_FiQuS_LEDET(self):
        '''
        Test that the method write_cosim_model() generates a correct .json file
        '''
        # arrange
        max_relative_error = 1e-6  # Maximum accepted relative error for excel, csv and map2d file comparison
        verbose = True

        path_cosim_data = os.path.join('input', 'COSIM', 'TestFile_model_data_write_model_PyCOSIM_FiQuS_LEDET.yaml')
        cosim_data = yaml_to_data(path_cosim_data, DataModelCosim)
        output_path_common = os.path.join('output', 'COSIM', cosim_data.GeneralParameters.cosim_name)
        #delete_if_existing(path_output) # TODO uncomment

        FiQuS_set_name = 'FiQuS_1'
        output_file_path_FiQuS =  os.path.join(output_path_common, 'FiQuS', FiQuS_set_name, f'{cosim_data.GeneralParameters.cosim_name}_FiQuS.yaml')

        LEDET_set_name = 'LEDET_1'
        nsti = NSTI(cosim_data.Simulations[LEDET_set_name].simulationNumber, 1, 0, 0)
        output_file_path_LEDET =  os.path.join(output_path_common, 'LEDET', LEDET_set_name, nsti.n_s_t_i, 'LEDET', cosim_data.GeneralParameters.cosim_name, 'Input', f'{cosim_data.GeneralParameters.cosim_name}_{cosim_data.GeneralParameters.simulation_number}.yaml')

        reference_file_paths = os.path.join('references', 'COSIM', cosim_data.GeneralParameters.cosim_name)
        reference_file_path_FiQuS = os.path.join(reference_file_paths, f'{cosim_data.GeneralParameters.cosim_name}_FiQuS_REFERENCE.yaml')
        reference_file_path_LEDET = os.path.join(reference_file_paths, f'{cosim_data.GeneralParameters.cosim_name}_LEDET_REFERENCE.yaml')

        # act
        pyCOSIM = CosimPyCosim(file_model_data=path_cosim_data, flag_run=False, verbose=verbose)
        pyCOSIM.initialize_cosim(verbose=verbose)

        # assert
        assert_equal_yaml(output_file_path_FiQuS, reference_file_path_FiQuS, max_relative_error=max_relative_error)
        assert_equal_yaml(output_file_path_LEDET, reference_file_path_LEDET, max_relative_error=max_relative_error)

