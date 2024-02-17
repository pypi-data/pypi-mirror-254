import os

from steam_sdk.data.DataCosim import NSTI
from steam_sdk.data.DataModelCosim import DataModelCosim
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.parsers.utils_ParserCosims import write_model_input_files


class CosimPyCosim:
    """
        Class to run a co-operative simulation
    """

    def __init__(self,
                 file_model_data: str = None,
                 flag_run: bool = False,
                 verbose: bool = False
                 ):
        """
            Builder object to generate models from STEAM simulation tools specified by user

            file_model_data: path to folder with input data (roxie files, geometry, modelData.yaml = config from userinput)
            verbose: to display internal processes (output of status & error messages) for troubleshooting

            Notes:
            The PyCOSIM folder structure will be as follows:
            - local_PyCOSIM is the main folder
              - COSIM_NAME
                - SOFTWARE_FOLDER
                  - SIMULATION_NAME
                    - {COSIM_NUMBER}_{SIMULATION_NUMBER}_{TIME_WINDOW_NUMBER}_{ITERATION_NUMBER}

            Example 1:
            - C:\local_PyCOSIM
              - RQX
                - LEDET
                  - MQXA
                    - Field Maps
                    - 55_1_1_1\LEDET\Input
                  - MQXA
                    - 55_2_1_1
                  - MQXB
                    - 55_1_1_1
                  - MQXB
                    - 55_2_1_1

            Example 1:
            - C:\local_PyCOSIM
              - RQX
                - FiQuS
                  - MQXA
                    - G1
                      - M1
                        - 55_1_1_1
                - LEDET
                  - MQXB
                    - Field Maps
                    - 55
                     - 1_1_1\LEDET\Input
                - PSPICE
                  - RQX_cosim
                    - 55_1_1_1

            D:\library_mesh

        """

        # Load data from input file
        if file_model_data:
            self.cosim_data = yaml_to_data(file_model_data, DataModelCosim)
            # BC = BuilderCosim(file_model_data=file_model_data, flag_build=False, verbose=verbose)
            # self.BC = BC
            # self.cosim_data = BC.cosim_data
        else:
            raise Exception('No file_model_data .yaml input file provided.')

        # # Unpack arguments
        # if file_model_data:
        #     self.file_model_data: str = file_model_data
        # else:
        #     raise Exception('No file_model_data .yaml input file provided.')

        # self.dict_sims # info about the simulations to run from "Simulations" key of DataCosim
        # self.local_COSIM_folder


        if flag_run:
            # Initialize co-simulation
            self.initialize_cosim(verbose=verbose)

            # Run co-simulation
            # While loop...






    def run_cosim(self):
        # Read initial
        # A1 Make the folder structure
        # A2 Make the input files for the pre-run simulation
        # A3 Run the pre-run input files
        # B Start a while loop with some convergence criteria
        #   B0 If present, check output to see if convergence is met
        #   B1 Make new folders
        #   B2 Make new input files using output of previous simulation
        #   B3 Run the new input files
        # C1 Make the folder structure for the final run
        # C2 Make the input files for the final-run simulation
        # C3 Run the final-run input files
        pass

    def initialize_cosim(self, verbose: bool = False):
        '''
        Initialize the co-simulation
        :param verbose:
        :return:
        '''
        for model_name, model in self.cosim_data.Simulations.items():
            nsti = NSTI(model.simulationNumber, model.modelSet, 0, 0)  # Initial time window and iteration  # cosim_nsti --> N=Simulation number. S=Simulation set. T=Time window. I=Iteration.
            write_model_input_files(cosim_data=self.cosim_data, model_name=model_name, model=model, cosim_software='PyCOSIM', nsti=nsti, verbose=verbose)
    #
    # def make_folder_structure(self, software: str, cosim_name: str, sim_number: int, time_window_number: int, iteration_number: int):
    #     # Make folders
    #     # Save folder name to a dict of current_folder?
    #     if software == 'FiQuS':
    #         pass
    #     elif software == 'LEDET':
    #         path_submodel_folder = os.path.join(self.local_COSIM_folder, cosim_name, sim_number, 'Input', model_name)
    #         make_folder_if_not_existing(path_submodel_folder, verbose=verbose)
    #         make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input'), verbose=verbose)
    #         make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'Control current input'), verbose=verbose)
    #         make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'Initialize variables'), verbose=verbose)
    #         make_folder_if_not_existing(os.path.join(path_submodel_folder, 'LEDET', magnet_name, 'Input', 'InitializationFiles'), verbose=verbose)
    #         make_folder_if_not_existing(os.path.join(path_submodel_folder, 'Field maps', magnet_name), verbose=verbose)
    #     elif software == 'PSPICE':
    #         pass
    #     elif software == 'XYCE':
    #         pass
    #
    #
    # def make_model(self):
    #     # Make the input files for the models and write them to the dict of current_folder
    #     pass
    # # write_model_input_files(cosim_data=self.cosim_data, model_name=model_name, model=model, cosim_software='COSIM', verbose=verbose)
    #
    # def run_model(self):
    #     # Run the input files for the models and write them to the dict of current_folder
    #     pass

    def check_convergence(self):
        # check whether converge criteria are met
        flag_converged = False
        return flag_converged
