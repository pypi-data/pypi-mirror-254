import json
import os.path


from steam_sdk.data.DataModelCosim import DataModelCosim, sim_PSPICE
from steam_sdk.parsers.utils_ParserCosims import write_model_input_files
from steam_sdk.utils.make_folder_if_not_existing import make_folder_if_not_existing
from steam_sdk.data.DataCosim import NSTI

class ParserCOSIM:
    """
        Class with methods to read/write COSIM information from/to other programs
    """

    def __init__(self, cosim_data: DataModelCosim = None,
                 #TODO remove if not needed relative_path_settings: str = '',
                 temp_output_path: str = 'temp'):
        '''
        Initialization using a BuilderModel object containing COSIM parameter structure
        :param builder_model: BuilderModel object containing COSIM parameter structure
        :param relative_path_settings: Path to the file defining the STEAM settings
        '''

        # Load co-simulation data from the BuilderModel object
        self.cosim_data = cosim_data
        # Assign input
        # self.relative_path_settings = relative_path_settings
        self.temp_output_path = temp_output_path

    def write_cosim_model(self, verbose: bool = False):
        self.setup_cosim_folders(verbose=verbose)
        self.write_config_file(verbose=verbose)
        for model_name, model in self.cosim_data.Simulations.items():
            if verbose: (f'{model_name}, {model}')
            if model.type == 'FiQuS':
                self.write_model_FiQuS(model_name=model_name, model=model, verbose=verbose)
            elif model.type == 'LEDET':
                self.write_model_LEDET(model_name=model_name, model=model, verbose=verbose)
            elif model.type == 'PSPICE':
                self.write_model_PSPICE(model_name=model_name, model=model, verbose=verbose)
            elif model.type == 'XYCE':
                self.write_model_XYCE(model_name=model_name, model=model, verbose=verbose)


    def write_config_file(self, output_file_name: str = 'COSIMConfig.json', verbose: bool = False):
        '''
        ** Write COSIM configuration file **
        '''

        # Unpack input
        local_COSIM_folder = self.cosim_data.Folders.local_COSIM_folder
        cosim_name = self.cosim_data.GeneralParameters.cosim_name
        sim_number = str(self.cosim_data.GeneralParameters.simulation_number)

        # Calculate variables
        coSimulationDir = self.reformat_path(os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Output')) + '\\'
        t_0 = self.cosim_data.Settings.Time_Windows.t_0
        t_end = self.cosim_data.Settings.Time_Windows.t_end
        executionOrder = self.cosim_data.Settings.Options_run.executionOrder
        executeCleanRun = self.cosim_data.Settings.Options_run.executeCleanRun
        coSimulationModelSolvers, coSimulationModelDirs, coSimulationModelConfigs, coSimulationPortDefinitions = [], [], [], []
        convergenceVariables, relTolerance, absTolerance, t_step_max = [], [], [], []
        for model_name, model in self.cosim_data.Simulations.items():
            coSimulationModelSolvers.append(model.type)
            coSimulationModelDirs.append(self.reformat_path(os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Input', model_name)) + '\\')
            coSimulationModelConfigs.append(f'{model_name}_config.json')
            coSimulationPortDefinitions.append(f'{model_name}_InputOutputPortDefinition.json')
            convergenceVariables.append(self.cosim_data.Settings.Convergence.convergenceVariables[model_name])
            relTolerance.append(self.cosim_data.Settings.Convergence.relTolerance[model_name])
            absTolerance.append(self.cosim_data.Settings.Convergence.absTolerance[model_name])
            t_step_max.append(self.cosim_data.Settings.Time_Windows.t_step_max[model_name])

        # Dictionary to write
        dict_cosim_config = {
                "coSimulationDir": coSimulationDir,
                "coSimulationModelSolvers": coSimulationModelSolvers,
                "coSimulationModelDirs": coSimulationModelDirs,
                "coSimulationModelConfigs": coSimulationModelConfigs,
                "coSimulationPortDefinitions": coSimulationPortDefinitions,
                "convergenceVariables": convergenceVariables,
                "t_0": t_0,
                "t_end": t_end,
                "t_step_max": t_step_max,
                "relTolerance": relTolerance,
                "absTolerance": absTolerance,
                "executionOrder": executionOrder,
                "executeCleanRun": executeCleanRun
        }

        # Serializing json
        json_cosim_config = json.dumps(dict_cosim_config, indent=4)

        # Writing to .json file
        path_output_file = os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Input', output_file_name)
        make_folder_if_not_existing(os.path.dirname(path_output_file), verbose=verbose)
        with open(path_output_file, "w") as outfile:
            outfile.write(json_cosim_config)
        if verbose:
            print(f'File {path_output_file} written.')


    def setup_cosim_folders(self, verbose: bool = False):
        '''
        ** Setup COSIM folder and subfolders **
        '''
        # Unpack input
        local_COSIM_folder = self.cosim_data.Folders.local_COSIM_folder
        cosim_name = self.cosim_data.GeneralParameters.cosim_name
        sim_number = str(self.cosim_data.GeneralParameters.simulation_number)

        path_model_folder = os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Input')
        make_folder_if_not_existing(path_model_folder, verbose=verbose)
        for model_name, model in self.cosim_data.Simulations.items():
            path_submodel_folder = os.path.join(path_model_folder, model_name)
            make_folder_if_not_existing(path_submodel_folder, verbose=verbose)


    def write_model_FiQuS(self, model_name: str, model, verbose: bool = False):
        '''
        ** Write selected FiQuS model **
        '''
        write_model_input_files(cosim_data=self.cosim_data, model_name=model_name, model=model, cosim_software='PyCOSIM', verbose=verbose)
        pass

    def write_model_LEDET(self, model_name: str, model, verbose: bool = False):
        '''
        ** Write selected LEDET model **
        '''
        # Unpack input
        local_COSIM_folder = self.cosim_data.Folders.local_COSIM_folder
        cosim_name = self.cosim_data.GeneralParameters.cosim_name
        sim_number = str(self.cosim_data.GeneralParameters.simulation_number)
        magnet_name = model.modelName
        solverPath = self.reformat_path(model.solverPath)

        # Make subfolders
        path_submodel_folder = os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Input', model_name)
        make_folder_if_not_existing(path_submodel_folder, verbose=verbose)
        make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input'), verbose=verbose)
        make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'Control current input'), verbose=verbose)
        make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'Initialize variables'), verbose=verbose)
        make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'InitializationFiles'), verbose=verbose)
        make_folder_if_not_existing(os.path.join(path_submodel_folder, 'Field maps', magnet_name), verbose=verbose)
        # Make configuration file
        path_config_file = os.path.join(path_submodel_folder, f'{model_name}_config.json')
        self.write_config_file_ledet(output_file=path_config_file, LEDET_path=solverPath, magnet_name=magnet_name, sim_set_number=model.simulationNumber)
        # Make input/output port definition file
        path_ports_file = os.path.join(path_submodel_folder, f'{model_name}_InputOutputPortDefinition.json')
        self.write_ports_file(output_file=path_ports_file, model_name=model_name)
        # Make input files, self-mutual inductance files, magnetic field map files. Save them to the COSIM subfolder. Delete temporary files.
        write_model_input_files(cosim_data=self.cosim_data, model_name=model_name, model=model, cosim_software='COSIM', verbose=verbose)

    def write_model_PSPICE(self, model_name: str, model, verbose: bool = False):  #TODO consider merging write_model_... methods since they have many tasks in common
        '''
        ** Write selected PSPICE model **
        '''
        # Unpack input
        local_COSIM_folder = self.cosim_data.Folders.local_COSIM_folder
        cosim_name = self.cosim_data.GeneralParameters.cosim_name
        sim_number = str(self.cosim_data.GeneralParameters.simulation_number)
        model_library_folder = model.modelFolder
        circuit_name = model.modelName

        # Make subfolders
        path_submodel_folder = os.path.join(local_COSIM_folder, cosim_name, sim_number, 'Input', model_name)
        make_folder_if_not_existing(path_submodel_folder, verbose=verbose)
        # Make configuration file
        path_config_file = os.path.join(path_submodel_folder, f'{model_name}_config.json')
        self.write_config_file_pspice(output_file=path_config_file, model=model)
        # Make input/output port definition file
        path_ports_file = os.path.join(path_submodel_folder, f'{model_name}_InputOutputPortDefinition.json')
        self.write_ports_file(output_file=path_ports_file, model_name=model_name)
        # Make input netlist files, auxiliary files. Save them to the COSIM subfolder. Delete temporary files.
        write_model_input_files(cosim_data=self.cosim_data, model_name=model_name, model=model, cosim_software='COSIM', verbose=verbose)

    def write_model_XYCE(self, model_name: str, model, verbose: bool = False):
        '''
        ** Write selected XYCE model **
        '''
        # Make subfolders
        # Make configuration file
        # Make input/output port definition file
        # Make input netlist file
        # Copy input netlist file
        # Copy auxiliary files
        # Delete temporary files
        pass  # TODO


    @staticmethod
    def reformat_path(path: str):
        '''
        Reformat a string defining a path so that all delimiters are double slashes
        :param path: string defining the original path
        :return: str
        '''

        return os.path.normpath(path).replace(os.sep, '\\')

    @staticmethod
    def write_config_file_ledet(output_file: str, LEDET_path: str, magnet_name: str, sim_set_number: int):
        '''
        Write the LEDET configuration .json file
        :param output_file: Target file
        :param LEDET_path: Path to PSPICE executable
        :param sim_set_number: Number of the simulation set, i.e. number of the LEDET simulation used in the COSIM model
        :return: None
        '''

        # Dictionary to write
        dict_ledet_config = {
            "solverPath": f"{LEDET_path}",
            "modelFolder": "LEDET",
            "modelName": f"{magnet_name}",
            "simulationNumber": f"{sim_set_number}"
        }

        # Serializing json
        json_ledet_config = json.dumps(dict_ledet_config, indent=4)

        # Writing to .json file
        with open(output_file, "w") as outfile:
            outfile.write(json_ledet_config)

    @staticmethod
    def write_config_file_pspice(output_file: str, model: sim_PSPICE):
        '''
        Write the PSPICE configuration .json file
        :param output_file: Target file
        :param model: sim_PSPICE object containing the information about this model
        :return: None
        '''
        # Unpack inputs
        solverPath = ParserCOSIM.reformat_path(model.solverPath)
        modelName = model.modelName
        configurationFileName = model.configurationFileName
        externalStimulusFileName = model.externalStimulusFileName
        initial_conditions = model.initialConditions
        skipBiasPointCalculation = model.skipBiasPointCalculation

        # Write a list of initial conditions
        string_initial_conditions = [f'{ic_name}={ic}' for ic_name, ic in initial_conditions.items()]

        # Dictionary to write
        dict_pspice_config = {
            "solverPath": solverPath,
            "modelName": f'{modelName}.cir',
            "configurationFileName": configurationFileName,
            "externalStimulusFileName": externalStimulusFileName,
            "initialConditions": string_initial_conditions,
            "skipBiasPointCalculation": skipBiasPointCalculation,
        }

        # Serializing json
        json_pspice_config = json.dumps(dict_pspice_config, indent=4)

        # Writing to .json file
        with open(output_file, "w") as outfile:
            outfile.write(json_pspice_config)

    def write_ports_file(self, output_file: str, model_name: str):
        '''
            Write the input/output port configuration .json file
            This method does not depend on the software tool
            :param output_file: Target file
            :return: None
        '''

        list_of_dict_ports = []
        for port_name, port in self.cosim_data.PortDefinition.items():
            if model_name in port.Models:
                port_info = port.Models[model_name]

                # Dictionary to write
                dict_ports = {
                    "name": port_name,
                    "components": port_info.components,
                    "inputs": [],
                    "outputs": [],
                }
                for input_name, input in port_info.inputs.items():
                    dict_ports["inputs"].append({
                        "couplingParameter": input.variable_coupling_parameter,
                        "labels": input.variable_names,
                        "types": input.variable_types})
                for output_name, output in port_info.outputs.items():
                    dict_ports["outputs"].append({
                        "couplingParameter": output.variable_coupling_parameter,
                        "labels": output.variable_names,
                        "types": output.variable_types})
                list_of_dict_ports.append(dict_ports)

        # Writing to .json file
        with open(output_file, "w") as outfile:
            # Serializing json
            for dict_ports in list_of_dict_ports:
                json_ports = json.dumps(dict_ports, indent=4)
                outfile.write(json_ports)
                outfile.write('\n')


    # def write_model_input_files(self, model_name: str, model: Union[sim_FiQuS, sim_LEDET, sim_PSPICE, sim_XYCE], verbose: bool = False):
    #     '''
    #     Make all required input files for the selected model. Save them to the COSIM subfolder. Delete temporary files.
    #     This method does not depend on the software tool
    #     :param model_name: Name of the model
    #     :param model: Object defining the model information
    #     :param verbose: If True, display information while running
    #     :return:
    #     '''
    #     # Hard-coded variables
    #     dummy_model_name = 'MODEL_NAME'  # This name is not important
    #
    #     # Unpack input
    #     file_model_data = model.modelName
    #     case_model = model.modelCase
    #     software = model.type
    #     simulation_name = model.modelName
    #     simulation_number = model.simulationNumber if hasattr(model, 'simulationNumber') else None  # PSPICE netlists don't have number
    #     variables_to_change = model.variables_to_modify.variables_to_change
    #     variables_values = model.variables_to_modify.variables_values
    #     library_path = model.modelFolder  # TODO: maybe the following key should be deleted: self.cosim_data.Folders.path_model_folder
    #     output_path = self.temp_output_path
    #     local_COSIM_folder = self.cosim_data.Folders.local_COSIM_folder
    #     cosim_name = self.cosim_data.GeneralParameters.cosim_name
    #     cosim_number = str(self.cosim_data.GeneralParameters.simulation_number)
    #
    #     # Delete temporary output folder, if present
    #     delete_if_existing(output_path, verbose=verbose)
    #
    #     # Define folder paths
    #     if software == 'FiQuS':
    #         local_folder = None  #TODO
    #     elif software == 'LEDET':
    #         local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name, 'LEDET')
    #     elif software == 'PSPICE':
    #         local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name)
    #     if software == 'XYCE':
    #         local_folder = os.path.join(local_COSIM_folder, cosim_name, cosim_number, 'Input', model_name)
    #
    #     make_folder_if_not_existing(output_path, verbose=verbose)
    #     # Define file_model_data. The following definition of file_model_data comes from the AnalysisSTEAM class
    #     # Assuming the steam-models directory structure if 'steam-models' or model_library found at the end of library path.
    #     # Else assuming library path directs straight to the model
    #     if (str(library_path).endswith('steam_models')) or (str(library_path).endswith('steam-models')) or (str(library_path).endswith('model_library')):
    #         file_model_data = os.path.join(library_path, case_model + 's', file_model_data, 'input', 'modelData_' + file_model_data + '.yaml')
    #     elif isinstance(library_path, (str, Path)):
    #         if library_path == 'same_as_analysis_yaml_use_model_name':
    #             file_model_data = '.' + os.sep + file_model_data + os.sep + 'input' + os.sep + 'modelData_' + file_model_data + '.yaml'
    #             file_model_data = Path(file_model_data).resolve()
    #         else:
    #             file_model_data = os.path.join(library_path, 'modelData_' + file_model_data + '.yaml')
    #     # Make BuilderModel object
    #     BM = BuilderModel(file_model_data=file_model_data, case_model=case_model, software=[software], output_path=output_path, verbose=verbose, flag_build=True)
    #     # Edit BuilderModel object with the variable changes set in the input file
    #     if not len(variables_to_change) == len(variables_values):
    #         raise Exception(f'Variables variables_to_change and variables_values must have the same length.')
    #     for v, (variable_to_change, value) in enumerate(zip(variables_to_change, variables_values)):
    #         if verbose:
    #             print(f'Modify variable {variable_to_change} to value {value}.')
    #         if 'Conductors[' in variable_to_change:  # Special case when the variable to change is the Conductors key
    #             if verbose:
    #                 idx_conductor = int(variable_to_change.split('Conductors[')[1].split(']')[0])
    #                 conductor_variable_to_change = variable_to_change.split('].')[1]
    #                 print(f'Variable {variable_to_change} is treated as a Conductors key. Conductor index: #{idx_conductor}. Conductor variable to change: {conductor_variable_to_change}.')
    #
    #                 old_value = get_attribute_model(case_model, BM, conductor_variable_to_change, idx_conductor)
    #                 print(f'Variable {conductor_variable_to_change} changed from {old_value} to {value}.')
    #
    #                 if case_model == 'conductor':
    #                     rsetattr(BM.conductor_data.Conductors[idx_conductor], conductor_variable_to_change, value)
    #                 elif case_model == 'magnet':
    #                     rsetattr(BM.model_data.Conductors[idx_conductor], conductor_variable_to_change, value)
    #                 else:
    #                     raise Exception(f'The selected case {case_model} is incompatible with the variable to change {variable_to_change}.')
    #         else:  # Standard case when the variable to change is not the Conductors key
    #             if verbose:
    #                 old_value = get_attribute_model(case_model, BM, variable_to_change)
    #                 print(f'Variable {variable_to_change} changed from {old_value} to {value}.')
    #                 set_attribute_model(case_model, BM, variable_to_change, value)
    #     # Write output of the BuilderModel object
    #     if 'FiQuS' == software:
    #         raise Exception(f'Writing of {software} models not yet supported within ParserCOSIM.')
    #     elif 'LEDET' == software:
    #         # Write LEDET model to temporary output folder
    #         BM.buildLEDET(verbose=False)  # verbose=False hard-coded to avoid unwanted logging info
    #         # Copy simulation file
    #         list_suffix = ['.xlsx', '.yaml']  # Hard-coded. '.json' would also be available
    #         for suffix in list_suffix:
    #             file_name_temp = os.path.join(output_path, simulation_name + suffix)
    #             file_name_local = os.path.join(local_folder, simulation_name, 'Input', simulation_name + '_' + str(simulation_number) + suffix)
    #             shutil.copyfile(file_name_temp, file_name_local)
    #             if verbose: print(f'Simulation file {file_name_local} copied.')
    #         # Copy csv files from the output folder
    #         list_csv_files = [entry for entry in os.listdir(output_path) if (simulation_name in entry) and ('.csv' in entry)]
    #         for csv_file in list_csv_files:
    #             file_to_copy = os.path.join(output_path, csv_file)
    #             file_copied = os.path.join(local_folder, simulation_name, 'Input', csv_file)
    #             shutil.copyfile(file_to_copy, file_copied)
    #             if verbose: print(f'Csv file {file_to_copy} copied to {file_copied}.')
    #         # Copy field-map files from the output folder
    #         field_maps_folder = Path(Path(local_folder) / '..' / 'Field maps' / simulation_name).resolve()
    #         list_field_maps = [entry for entry in os.listdir(output_path) if (simulation_name in entry) and ('.map2d' in entry)]
    #         for field_map in list_field_maps:
    #             file_to_copy = os.path.join(output_path, field_map)
    #             file_copied = os.path.join(field_maps_folder, field_map)
    #             shutil.copyfile(file_to_copy, file_copied)
    #             if verbose: print(f'Field map file {file_to_copy} copied to {file_copied}.')
    #     elif 'PSPICE' == software:
    #         # Write PSPICE model
    #         BM.buildPSPICE()
    #         # Copy simulation file
    #         file_name_temp = os.path.join(output_path, simulation_name + '.cir')
    #         file_name_local = os.path.join(local_folder, simulation_name + '.cir')
    #         shutil.copyfile(file_name_temp, file_name_local)
    #         if verbose: print(f'Simulation file {file_name_local} copied.')
    #         # Copy additional files originally specified in the circuit model data file
    #         list_additional_files = BM.circuit_data.GeneralParameters.additional_files
    #         for file_to_copy in list_additional_files:
    #             try:
    #                 if not os.path.isabs(file_to_copy):
    #                     file_to_copy = os.path.join(output_path, file_to_copy)
    #                 file_copied = os.path.join(local_folder, os.path.basename(file_to_copy))
    #                 shutil.copyfile(file_to_copy, file_copied)
    #             except:
    #                 print(f'WARNING: Problem while copying file {file_to_copy} to {file_copied}.')
    #         # Copy lib files from the output folder
    #         list_lib_files = [entry for entry in os.listdir(output_path) if ('.lib' in entry)]
    #         for lib_file in list_lib_files:
    #             file_to_copy = os.path.join(output_path, lib_file)
    #             file_copied = os.path.join(local_folder, lib_file)
    #             shutil.copyfile(file_to_copy, file_copied)
    #             if verbose: print('Lib file {} copied to {}.'.format(file_to_copy, file_copied))
    #         # Copy stl files from the output folder
    #         list_stl_files = [entry for entry in os.listdir(output_path) if ('.stl' in entry)]
    #         for stl_file in list_stl_files:
    #             file_to_copy = os.path.join(output_path, stl_file)
    #             file_copied = os.path.join(local_folder, stl_file)
    #             shutil.copyfile(file_to_copy, file_copied)
    #             if verbose: print('Stl file {} copied to {}.'.format(file_to_copy, file_copied))
    #     elif 'XYCE' == software:
    #         raise Exception(f'Writing of {software} models not yet supported within ParserCOSIM.')
    #     else:
    #         raise Exception(f'Writing of {software} models not yet supported within ParserCOSIM.')
    #
    #     # Delete temporary output folder
    #     delete_if_existing(output_path, verbose=verbose)
