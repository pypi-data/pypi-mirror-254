import datetime
import os
from pathlib import Path

from steam_sdk.data.DataModelCosim import DataModelCosim
from steam_sdk.parsers.ParserCOSIM import ParserCOSIM
from steam_sdk.parsers.ParserYAML import yaml_to_data


class BuilderCosim:
    """
        Class to generate co-operative simulation models, which can be later on run with various co-simulation tools
    """

    def __init__(self,
                 file_model_data: str = None,
                 software: [str] = None,
                 relative_path_settings: str = '',  # TODO needed?
                 flag_build: bool = True,
                 output_path: str = '',
                 verbose: bool = False
                 ):
        """
            Builder object to generate models from STEAM simulation tools specified by user

            file_model_data: path to folder with input data (roxie files, geometry, modelData.yaml = config from userinput)
            software: list of simulation software to be used
            relative_path_settings: path to user specific settings.SYSTEM.yaml file
            flag_build: defines whether the model has to be build (so whether output folder should be created) - but why ???
            output_path: path to the output models
            verbose: to display internal processes (output of status & error messages) for troubleshooting
        """

        # Unpack arguments
        if file_model_data:
            self.file_model_data: str = file_model_data
        else:
            raise Exception('No file_model_data .yaml input file provided.')
        if software is None:
            self.software = []
        else:
            self.software = software
        self.relative_path_settings = relative_path_settings
        self.flag_build = flag_build
        self.output_path: str = output_path
        self.verbose: bool = verbose

        # If a model needs to be built, the output folder is not an empty string, and the folder does not exist, make it
        if flag_build and self.output_path != '' and not os.path.isdir(self.output_path):
            print("Output folder {} does not exist. Making it now".format(self.output_path))
            Path(self.output_path).mkdir(parents=True)

        # Initialize
        self.cosim_data: DataModelCosim = DataModelCosim()
        self.path_settings = None

        # Load model data from the input .yaml file
        self.loadModelCosim()

        # Set paths of input files and settings
        self.set_input_paths()

        # If flag_build set true, the model will be generated during the initialization
        if flag_build:
            if self.verbose:
                print('output_path: {}'.format(self.output_path))

            # Build model
            for s in self.software:
                if s == 'COSIM':
                    self.buildCOSIM()
                elif s == 'PyCOSIM':
                    self.buildPyCOSIM()
                else:
                    raise Exception(f'Selected software {s} is not supported. Supported co-simulation software: COSIM, PyCOSIM.')

        # Display time stamp
        if self.verbose:
            print(f'BuilderModel ended. Time stamp: {datetime.datetime.now()}')

    def set_input_paths(self):
        """
            Sets input paths from created DataModelCosim, set path to usersettings and displays related information
        """
        # TODO: Add test for this method

        # Find folder where the input file is located, which will be used as the "anchor" for all input files
        self.path_input_file = Path(self.file_model_data).parent

        # Set settings path
        user_name = os.getlogin()
        if self.verbose:
            print('user_name:   {}'.format(user_name))

        # TODO: Change this logic with a tree structure depending on the current location, not the file location
        if self.relative_path_settings == '':
            self.path_settings = Path(os.getcwd())
        else:
            self.path_settings = Path(os.getcwd() / self.relative_path_settings).resolve()

        settings_file = Path.joinpath(self.path_settings, f"settings.{user_name}.yaml")
        if not Path.exists(settings_file):
            settings_file = Path.joinpath(Path(os.getcwd()).parent, "settings.SYSTEM.yaml")
        self.settings_dict = yaml_to_data(settings_file)

        # Display defined paths
        if self.verbose:
            print('These paths were set:')
            print('path_input_file:   {}'.format(self.path_input_file))
            print('path_settings: {}'.format(self.path_settings))
            print(f'path to settings file: {settings_file}')

    def loadModelCosim(self):
        """
            Loads model data from yaml file to model data object
        """
        if self.verbose:
            print('Loading .yaml file to cosim model data object.')

        # Load yaml keys into DataModelCosim dataclass
        self.cosim_data = yaml_to_data(self.file_model_data, DataModelCosim)

    def buildCOSIM(self):
        """
            Build a COSIM model
        """
        # Make COSIM model
        pCOSIM = ParserCOSIM(cosim_data=self.cosim_data, temp_output_path='temp')
        pCOSIM.write_cosim_model(verbose=self.verbose)
