import os
import shutil
from pathlib import Path
from typing import Union

from steam_sdk.data.DataModelMagnet import DataModelMagnet
from steam_sdk.data.DataCosim import NSTI

from steam_sdk.builders.BuilderModel import BuilderModel
from steam_sdk.data.DataModelCosim import DataModelCosim
from steam_sdk.data.DataModelCosim import sim_FiQuS, sim_LEDET, sim_PSPICE, sim_XYCE
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.utils.attribute_model import get_attribute_model, set_attribute_model
from steam_sdk.utils.delete_if_existing import delete_if_existing
from steam_sdk.utils.make_folder_if_not_existing import make_folder_if_not_existing
from steam_sdk.utils.sgetattr import rsetattr


def write_model_input_files(cosim_data: DataModelCosim, model_name: str,
                            model: Union[sim_FiQuS, sim_LEDET, sim_PSPICE, sim_XYCE], cosim_software: str,
                            nsti: NSTI = None,
                            verbose: bool = False, temp_path: str = 'temp'):
    '''
    Make all required input files for the selected model. Save them to the COSIM subfolder. Delete temporary files.
    This method does not depend on the software tool
    :param cosim_data TODO
    :param model_name: Name of the model
    :param model: Object defining the model information
    :param verbose: If True, display information while running
    :param nsti:  N=Simulation number, S=Simulation set, T=Time window, I=Iteration
    :type nsti: NSTI
    :param temp_path: TODO
    :return:
    '''
    # Hard-coded variables
    dummy_model_name = 'MODEL_NAME'  # This name is not important

    # Unpack input

    file_model_data = model.modelName
    case_model = model.modelCase
    software = model.type
    simulation_name = model.modelName
    simulation_number = model.simulationNumber if hasattr(model, 'simulationNumber') else None  # PSPICE netlists don't have number
    # TODO variables_to_change, variables_values should be defined based on a new argmetn 1,2,3... defining whether it's pre-cosim, cosim, or post-cosim
    variables_to_change = model.variables_to_modify.variables_to_change
    variables_values = model.variables_to_modify.variables_values
    library_path = model.modelFolder  # TODO: maybe the following key should be deleted: cosim_data.Folders.path_model_folder
    local_COSIM_folder = cosim_data.Folders.local_COSIM_folder
    cosim_name = cosim_data.GeneralParameters.cosim_name
    cosim_number = str(cosim_data.GeneralParameters.simulation_number)

    # Delete temporary output folder, if present
    file_model_data_path = os.path.join(library_path, case_model + 's', file_model_data, 'input', 'modelData_' + file_model_data + '.yaml')
    data_model = yaml_to_data(file_model_data_path, DataModelMagnet)
    delete_if_existing(temp_path, verbose=verbose)

    # Define folder paths
    if cosim_software == 'COSIM':
        if software == 'FiQuS':
            raise ValueError(f'FiQuS does not support COSIM. Please use PyCOSIM instead')
        elif software == 'LEDET':
            local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name, 'LEDET')
        elif software == 'PSPICE':
            local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name)
        if software == 'XYCE':
            local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name)
    elif cosim_software == 'PyCOSIM':
        local_folder_prefix = os.path.join(local_COSIM_folder, cosim_name, software, model_name)
        if software == 'FiQuS':
            local_folder = os.path.join(local_folder_prefix, data_model.Options_FiQuS.run.geometry, data_model.Options_FiQuS.run.mesh, data_model.Options_FiQuS.run.solution)
        elif software == 'LEDET':
            local_folder = os.path.join(local_folder_prefix, nsti.n_s_t_i, software)
        elif software in ['PSPICE', 'XYCE']:
            local_folder = os.path.join(local_folder_prefix)
    else:
         raise Exception(f'Co-simulation software {cosim_software} not supported.')
    make_folder_if_not_existing(temp_path, verbose=verbose)

    # Define file_model_data. The following definition of file_model_data comes from the AnalysisSTEAM class
    # Assuming the steam-models directory structure if 'steam-models' or model_library found at the end of library path.
    # Else assuming library path directs straight to the model
    # TODO the part until Builder Model call could be deleted as it does not need to deal with this case and is already used above to get: file_model_data_path
    if (str(library_path).endswith('steam_models')) or (str(library_path).endswith('steam-models')) or ( str(library_path).endswith('model_library')):
        file_model_data = os.path.join(library_path, case_model + 's', file_model_data, 'input', 'modelData_' + file_model_data + '.yaml')
    elif isinstance(library_path, (str, Path)):
        if library_path == 'same_as_analysis_yaml_use_model_name':
            file_model_data = '.' + os.sep + file_model_data + os.sep + 'input' + os.sep + 'modelData_' + file_model_data + '.yaml'
            file_model_data = Path(file_model_data).resolve()
        else:
            file_model_data = os.path.join(library_path, 'modelData_' + file_model_data + '.yaml')
    # Make BuilderModel object
    BM = BuilderModel(file_model_data=file_model_data, case_model=case_model, software=[software],
                      output_path=temp_path, verbose=verbose, flag_build=True)
    # Edit BuilderModel object with the variable changes set in the input file
    if not len(variables_to_change) == len(variables_values):
        raise Exception(f'Variables variables_to_change and variables_values must have the same length.')
    for v, (variable_to_change, value) in enumerate(zip(variables_to_change, variables_values)):
        if verbose:
            print(f'Modify variable {variable_to_change} to value {value}.')
        if 'Conductors[' in variable_to_change:  # Special case when the variable to change is the Conductors key
            if verbose:
                idx_conductor = int(variable_to_change.split('Conductors[')[1].split(']')[0])
                conductor_variable_to_change = variable_to_change.split('].')[1]
                print(
                    f'Variable {variable_to_change} is treated as a Conductors key. Conductor index: #{idx_conductor}. Conductor variable to change: {conductor_variable_to_change}.')

                old_value = get_attribute_model(case_model, BM, conductor_variable_to_change, idx_conductor)
                print(f'Variable {conductor_variable_to_change} changed from {old_value} to {value}.')

                if case_model == 'conductor':
                    rsetattr(BM.conductor_data.Conductors[idx_conductor], conductor_variable_to_change, value)
                elif case_model == 'magnet':
                    rsetattr(BM.model_data.Conductors[idx_conductor], conductor_variable_to_change, value)
                else:
                    raise Exception(
                        f'The selected case {case_model} is incompatible with the variable to change {variable_to_change}.')
        else:  # Standard case when the variable to change is not the Conductors key
            if verbose:
                old_value = get_attribute_model(case_model, BM, variable_to_change)
                print(f'Variable {variable_to_change} changed from {old_value} to {value}.')
                set_attribute_model(case_model, BM, variable_to_change, value)
    # Write output of the BuilderModel object
    if 'FiQuS' == software:
        BM.buildFiQuS(simulation_name=cosim_name, library_path=library_path, output_path=local_folder_prefix)
    elif 'LEDET' == software:
        # Write LEDET model to temporary output folder
        BM.buildLEDET(verbose=False)  # verbose=False hard-coded to avoid unwanted logging info
        # Copy simulation file
        list_suffix = ['.xlsx', '.yaml']  # Hard-coded. '.json' would also be available
        for suffix in list_suffix:
            file_name_temp = os.path.join(temp_path, simulation_name + suffix)
            folder_name_local = os.path.join(local_folder, simulation_name, 'Input')
            file_name = simulation_name + '_' + str(simulation_number) + suffix
            make_folder_if_not_existing(folder_name_local)
            file_name_local = os.path.join(folder_name_local, file_name)
            shutil.copyfile(file_name_temp, file_name_local)
            if verbose: print(f'Simulation file {file_name_local} copied.')
        # Copy csv files from the output folder
        list_csv_files = [entry for entry in os.listdir(temp_path) if
                          (simulation_name in entry) and ('.csv' in entry)]
        for csv_file in list_csv_files:
            file_to_copy = os.path.join(temp_path, csv_file)
            file_copied = os.path.join(local_folder, simulation_name, 'Input', csv_file)
            shutil.copyfile(file_to_copy, file_copied)
            if verbose: print(f'Csv file {file_to_copy} copied to {file_copied}.')
        # Copy field-map files from the output folder
        field_maps_folder = Path(Path(local_folder) / '..' / 'Field maps' / simulation_name).resolve()
        list_field_maps = [entry for entry in os.listdir(temp_path) if
                           (simulation_name in entry) and ('.map2d' in entry)]
        for field_map in list_field_maps:
            file_to_copy = os.path.join(temp_path, field_map)
            file_copied = os.path.join(field_maps_folder, field_map)
            shutil.copyfile(file_to_copy, file_copied)
            if verbose: print(f'Field map file {file_to_copy} copied to {file_copied}.')
    elif 'PSPICE' == software:
        # Write PSPICE model
        BM.buildPSPICE()
        # Copy simulation file
        file_name_temp = os.path.join(temp_path, simulation_name + '.cir')
        file_name_local = os.path.join(local_folder, simulation_name + '.cir')
        shutil.copyfile(file_name_temp, file_name_local)
        if verbose: print(f'Simulation file {file_name_local} copied.')
        # Copy additional files originally specified in the circuit model data file
        list_additional_files = BM.circuit_data.GeneralParameters.additional_files
        for file_to_copy in list_additional_files:
            try:
                if not os.path.isabs(file_to_copy):
                    file_to_copy = os.path.join(temp_path, file_to_copy)
                file_copied = os.path.join(local_folder, os.path.basename(file_to_copy))
                shutil.copyfile(file_to_copy, file_copied)
            except:
                print(f'WARNING: Problem while copying file {file_to_copy} to {file_copied}.')
        # Copy lib files from the output folder
        list_lib_files = [entry for entry in os.listdir(temp_path) if ('.lib' in entry)]
        for lib_file in list_lib_files:
            file_to_copy = os.path.join(temp_path, lib_file)
            file_copied = os.path.join(local_folder, lib_file)
            shutil.copyfile(file_to_copy, file_copied)
            if verbose: print('Lib file {} copied to {}.'.format(file_to_copy, file_copied))
        # Copy stl files from the output folder
        list_stl_files = [entry for entry in os.listdir(temp_path) if ('.stl' in entry)]
        for stl_file in list_stl_files:
            file_to_copy = os.path.join(temp_path, stl_file)
            file_copied = os.path.join(local_folder, stl_file)
            shutil.copyfile(file_to_copy, file_copied)
            if verbose: print('Stl file {} copied to {}.'.format(file_to_copy, file_copied))
    elif 'XYCE' == software:
        raise Exception(f'Writing of {software} models not yet supported within ParserCOSIM.')
    else:
        raise Exception(f'Writing of {software} models not yet supported within ParserCOSIM.')

    # Delete temporary output folder
    delete_if_existing(temp_path, verbose=verbose)
