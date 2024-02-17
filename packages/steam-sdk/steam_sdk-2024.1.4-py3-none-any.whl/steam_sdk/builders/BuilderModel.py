import datetime
import os
import shutil
from pathlib import Path

import numpy as np
from steam_pysigma.MainPySIGMA import MainPySIGMA

from steam_sdk.builders.BuilderFiQuS import BuilderFiQuS
from steam_sdk.builders.BuilderLEDET import BuilderLEDET
from steam_sdk.builders.BuilderProteCCT import BuilderProteCCT
from steam_sdk.builders.BuilderPyBBQ import BuilderPyBBQ
from steam_sdk.builders.BuilderPySIGMA import BuilderPySIGMA
from steam_sdk.data.DataModelCircuit import DataModelCircuit
from steam_sdk.data.DataModelConductor import DataModelConductor
from steam_sdk.data.DataModelMagnet import DataModelMagnet
from steam_sdk.data.DataRoxieParser import RoxieData
from steam_sdk.data.DataSettings import DataSettings
from steam_sdk.parsers.ParserCsv import find_by_position, find_column_list
from steam_sdk.parsers.ParserFiQuS import ParserFiQuS
from steam_sdk.parsers.ParserLEDET import ParserLEDET, copy_modified_map2d_ribbon_cable, copy_map2d
from steam_sdk.parsers.ParserMap2d import getParametersFromMap2d
from steam_sdk.parsers.ParserPSPICE import ParserPSPICE
from steam_sdk.parsers.ParserProteCCT import ParserProteCCT
from steam_sdk.parsers.ParserPyBBQ import ParserPyBBQ
from steam_sdk.parsers.ParserPySIGMA import ParserPySIGMA
from steam_sdk.parsers.ParserRoxie import ParserRoxie, RoxieList
from steam_sdk.parsers.ParserXYCE import ParserXYCE
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.plotters import PlotterRoxie
from steam_sdk.plotters.PlotterModel import PlotterModel


class BuilderModel:
    """
        Class to generate STEAM models, which can be later on written to input files of supported programs
    """

    def __init__(self,
                 file_model_data: str = None, software: [str] = None, case_model: str = 'magnet',
                 relative_path_settings: str = '', results_folder_name: str = None,
                 flag_build: bool = True, flag_json: bool = False,
                 output_path: str = '',
                 verbose: bool = False, flag_plot_all: bool = False, sim_number: int = None):
        """
            Builder object to generate models from STEAM simulation tools specified by user

            file_model_data: path to folder with input data (roxie files, geometry, modelData.yaml = config from userinput)
            software: list of simulation software to be used
            case_model: defines whether it is a magnet, a conductor or a circuit
            relative_path_settings: path to user specific settings.SYSTEM.yaml file
            flag_build: defines whether the model has to be build (so whether output folder should be created) - but why ???
            flag_json: ????
            output_path: path to the output models
            verbose: to display internal processes (output of status & error messages) for troubleshooting
            flag_plot_all: defines whether the tools in steam framework should show the figrues
            :param local_folder_output: if set to true the path from settings file is used for each tool. If false the output_path is used.
        """

        # Unpack arguments
        self.file_model_data: str = file_model_data
        if software is None:
            self.software = []
        else:
            self.software = software
        self.case_model = case_model
        self.relative_path_settings: str = relative_path_settings
        self.results_folder_name = results_folder_name
        self.flag_build = flag_build
        self.flag_plot_all: bool = flag_plot_all
        self.flag_json: bool = flag_json
        self.output_path: str = output_path
        self.verbose: bool = verbose

        if self.verbose:
            print('case_model: {}'.format(self.case_model))

        # If a model needs to be built, the output folder is not an empty string, and the folder does not exist, make it
        if flag_build and self.output_path != '' and not os.path.isdir(self.output_path):
            print("Output folder {} does not exist. Making it now".format(self.output_path))
            Path(self.output_path).mkdir(parents=True)

        ### Case of a magnet model
        if self.case_model == 'magnet':
            # Initialized
            self.model_data: DataModelMagnet = DataModelMagnet()
            self.roxie_data: RoxieData = RoxieData()
            self.path_magnet = None
            self.path_data = None
            self.path_cadata = None
            self.path_iron = None
            self.path_map2d = None
            self.path_settings = None
            self.roxie_param = {}

            # If flag_build set true, the model will be generated during the initialization
            if flag_build:
                if self.verbose:
                    print('output_path: {}'.format(self.output_path))

                # Load model data from the input .yaml file
                self.loadModelData()

                # Set paths of input files and settings
                self.set_input_paths()

                # Load model data from the input ROXIE files
                self.loadRoxieData()

                # Read these variables from ParserRoxie and assign them to model_data
                # TODO polarities_inGroup
                RL = RoxieList(self.roxie_data)
                self.roxie_param['x_strands'] = RL.x_strand
                self.roxie_param['y_strands'] = RL.y_strand
                self.roxie_param['I_strands'] = RL.i_strand
                self.roxie_param['strandToHalfTurn'] = RL.strand_to_halfTurn
                self.roxie_param['strandToGroup'] = RL.strand_to_group

                # nT (has as many elements as groups. Each element defines the number of half-turns in that group)
                counter_nT = 1
                nT = []
                for i in range(1, len(RL.strand_to_group)):
                    if RL.strand_to_halfTurn[i] != RL.strand_to_halfTurn[i - 1] and RL.strand_to_group[i] == RL.strand_to_group[
                        i - 1]:  # counts the number of half-turns in the group by counting non-equal strandsToHalfTurn
                        counter_nT += 1
                    if RL.strand_to_group[i] != RL.strand_to_group[i - 1] or i == len(
                            RL.strand_to_group) - 1:  # the counted number is stored in the array and the counter restarts
                        nT.append(counter_nT)
                        counter_nT = 1
                self.roxie_param['nT'] = nT

                indexTstop = np.cumsum(nT).tolist()
                indexTstart = [1]
                for i in range(len(nT) - 1):
                    indexTstart.extend([indexTstart[i] + nT[i]])
                self.roxie_param['indexTstart'] = indexTstart
                self.roxie_param['indexTstop'] = indexTstop

                # nStrands_inGroup (has as many elements as groups. Each element defines the number of strands in the conductor of that group)
                counter_nStrands_inGroup = 1
                nStrands_inGroup = []
                for i in range(1, len(RL.strand_to_group)):
                    if RL.strand_to_group[i] == RL.strand_to_group[i-1] and RL.strand_to_halfTurn[i] != RL.strand_to_halfTurn[i-1]:  #the number of equal strandsToHalfTurn are only counted once per group and otherwise resetted
                        counter_nStrands_inGroup = 1
                    elif RL.strand_to_halfTurn[i] == RL.strand_to_halfTurn[i - 1]:  #counts the number of strands in the group by counting equal strandsToHalfTurn
                        counter_nStrands_inGroup += 1
                    if RL.strand_to_group[i] != RL.strand_to_group[i - 1] or i == len(RL.strand_to_group) - 1:  #the counted number is stored in the array and the counter restarts
                        nStrands_inGroup.append(counter_nStrands_inGroup)
                        counter_nStrands_inGroup = 1
                self.roxie_param['nStrands_inGroup'] = nStrands_inGroup

                # sign_i = lambda x: math.copysign(1, x)
                polarities_inGroup = []
                for i in range(1, len(RL.strand_to_group)):
                    if RL.strand_to_group[i] != RL.strand_to_group[i-1] or i == len(RL.strand_to_group) - 1:  #for each group the polarities is stored in the array
                        polarities_inGroup.append(float(np.sign(RL.i_strand[i-1])))
                self.roxie_param['polarities_inGroup'] = polarities_inGroup
                
                # Calculate half-turn electrical order
                self.calc_electrical_order(flag_plot=self.flag_plot_all)

                # Build model
                for s in self.software:
                    if s == 'FiQuS':    self.buildFiQuS()
                    if s == 'LEDET':    self.buildLEDET()
                    if s == 'ProteCCT': self.buildProteCCT()
                    if s == 'SIGMA':
                        settings = DataSettings(**self.settings_dict)
                        self.buildPySIGMA(sim_number, use_model_builder_path=True, make_bh_copy=False, settings=settings)
                    if s not in ['FiQuS', 'LEDET', 'ProteCCT', 'SIGMA']:
                        raise Exception(f'Software: {s} is not supported by STEAM SDK!')

                if flag_plot_all:
                    PlotterRoxie.plot_all(self.roxie_data)
                    PM = PlotterModel(self.roxie_data)
                    PM.plot_all(self.model_data)

        ### Case of a circuit model
        elif self.case_model == 'circuit':
            # Initialize
            self.circuit_data: DataModelCircuit = DataModelCircuit()
            self.path_settings = None

            # If flag_build set true, the model will be generated during the initialization
            if flag_build:
                if self.verbose:
                    print('output_path: {}'.format(self.output_path))

                # Load model data from the input .yaml file
                self.loadModelData()

                # Set paths of input files and settings
                self.set_input_paths()

                # Build circuit model
                for s in self.software:
                    if s == 'PSPICE':
                        self.buildPSPICE()
                    elif s == 'XYCE':
                        self.buildXYCE()
                    else:
                        raise Exception('Please specify software (PSPICE/XYCE).')

        ### Case of a conductor model
        elif self.case_model == 'conductor':
            # Initialize
            self.conductor_data: DataModelConductor = DataModelConductor()
            self.path_settings = None

            # If flag_build set true, the model will be generated during the initialization
            if flag_build:
                if self.verbose:
                    print('output_path: {}'.format(self.output_path))

                # Load model data from the input .yaml file
                self.loadModelData()

                # Set paths of input files and settings
                self.set_input_paths()

                # Build model
                for s in self.software:
                    if s == 'LEDET':    self.buildLEDET()
                    if s == 'PyBBQ':    self.buildPyBBQ()  # TODO: raise error when wrong software selected?

        else:
            raise Exception(f'Selected case {self.case_model} is not supported. Supported cases: circuit, magnet, conductor.')

        # Display time stamp
        if self.verbose:
            print(f'BuilderModel ended. Time stamp: {datetime.datetime.now()}')

    def set_input_paths(self):
        """
            Sets input paths from created DataModel, set path to usersettings and displays related information
        """
        # TODO: Add test for this method

        # Find folder where the input file is located, which will be used as the "anchor" for all input files
        self.path_magnet = Path(self.file_model_data).parent
        self.path_data = None
        self.path_map2d = None
        self.path_cadata = None
        self.path_iron = None

        if self.case_model == 'magnet':
            # Set a few paths relative to the "anchor" path
            # If input paths are not defined, their value remains to their default None
            # The construct Path(x / y).resolve() allows defining relative paths in the .yaml input file
            if self.model_data.Sources.coil_fromROXIE:
                self.path_data = Path(self.path_magnet / self.model_data.Sources.coil_fromROXIE).resolve()
            if self.model_data.Sources.magnetic_field_fromROXIE:
                self.path_map2d = Path(self.path_magnet / self.model_data.Sources.magnetic_field_fromROXIE).resolve()
            if self.model_data.Sources.conductor_fromROXIE:
                self.path_cadata = Path(self.path_magnet / self.model_data.Sources.conductor_fromROXIE).resolve()
            if self.model_data.Sources.iron_fromROXIE:
                self.path_iron = Path(self.path_magnet / self.model_data.Sources.iron_fromROXIE).resolve()
            if self.model_data.Sources.BH_fromROXIE:
                self.path_bh = str(Path(self.path_magnet / self.model_data.Sources.BH_fromROXIE).resolve())
        elif self.case_model in 'circuit':
            pass  # no paths to assign
        elif self.case_model == 'conductor':
            if self.conductor_data.Sources.magnetic_field_fromROXIE:
                self.path_map2d = Path(
                    self.path_magnet / self.conductor_data.Sources.magnetic_field_fromROXIE).resolve()
        else:
            raise Exception('case_model ({}) no supported'.format(self.case_model))

        # Set settings path
        # Find user name
        # user_name = 'user'  # till GitLab path problem is solved
        # for environ_var in ['HOMEPATH', 'SWAN_HOME']:  # TODO: why not use os.getlogin() as in AnalysisSTEAM.py
        #     if environ_var in os.environ:
        #         user_name = os.path.basename(os.path.normpath(os.environ[environ_var]))
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
            print('path_magnet:   {}'.format(self.path_magnet))
            print('path_cadata:   {}'.format(self.path_cadata))
            print('path_iron:     {}'.format(self.path_iron))
            print('path_map2d:    {}'.format(self.path_map2d))
            print('path_settings: {}'.format(self.path_settings))
            print(f'path to settings file: {settings_file}')

    def loadModelData(self):
        """
            Loads model data from yaml file to model data object
        """
        if self.verbose:
            print('Loading .yaml file to model data object.')

        if not self.file_model_data:
            raise Exception('No .yaml path provided.')

        if self.case_model == 'magnet':
            # Load yaml keys into DataModelMagnet dataclass
            self.model_data = yaml_to_data(self.file_model_data, DataModelMagnet)
        elif self.case_model == 'circuit':
            for s in self.software:
                if s == 'PSPICE':
                    Parser = ParserPSPICE(self.circuit_data)
                    Parser.readFromYaml(self.file_model_data)
                    self.circuit_data = Parser.circuit_data
                elif s == 'XYCE':
                    Parser = ParserXYCE(self.circuit_data)
                    Parser.readFromYaml(self.file_model_data)
                    self.circuit_data = Parser.circuit_data
                else:
                    raise Exception(f'Software {s} not supported. Supported software: PSPICE, XYCE.')
        elif self.case_model == 'conductor':
            # Load yaml keys into DataModelConductor dataclass
            self.conductor_data = yaml_to_data(self.file_model_data, DataModelConductor)
        else:
            raise ValueError('results: case_model must be one of {}.'.format(['magnet', 'circuit', 'conductor']))

    def loadRoxieData(self):
        """
            Apply roxie parser to fetch magnet information for the given magnet and stores in member variable
        """
        if not self.model_data:
            raise Exception('Model data not loaded to object.')

        # TODO: add option to set a default path if no path is provided
        #######################################
        # Alternative if provided path is wrong
        if self.path_iron is not None and not os.path.isfile(self.path_iron):
            print('Cannot find {}, will attempt to proceed without file'.format(self.path_iron))
            self.path_iron = None
        if self.path_data is not None and not os.path.isfile(self.path_data):
            print('Cannot find {}, will attempt to proceed without file'.format(self.path_data))
            self.path_data = None
        if self.path_cadata is not None and not os.path.isfile(self.path_cadata):
            print('Cannot find {}, will attempt to proceed without file'.format(self.path_cadata))
            self.path_cadata = None

        ############################################################
        # Load information from ROXIE input files using ROXIE parser
        roxie_parser = ParserRoxie()
        self.roxie_data = roxie_parser.getData(dir_data=self.path_data, dir_cadata=self.path_cadata,
                                               dir_iron=self.path_iron, path_to_yaml_model_data=self.file_model_data)

    def calc_electrical_order(self, flag_plot: bool = False):
        """
            **Calculates electrical order of each half turn (for multipole magnets) or of each turn (for solenoid and CCT magnets) **

            :param elPairs_GroupTogether: list of 2-element tuples that includes the electrical order of groups
                (e.g. [[1,17], [2,18]] means group 1 and 17 are electrically connected)
            :param elPairs_RevElOrder: list defining whether the (half-)turns present in the groups need to be electrically ordered following their order in the group (=0), or reversed (=1)
        """
        # Unpack variables
        elPairs_GroupTogether      = self.model_data.CoilWindings.electrical_pairs.group_together
        elPairs_RevElOrder         = self.model_data.CoilWindings.electrical_pairs.reversed
        typeWindings               = self.model_data.GeneralParameters.magnet_type
        nT                         = self.roxie_param['nT']
        indexTstart                = self.roxie_param['indexTstart']
        indexTstop                 = self.roxie_param['indexTstop']
        strandToGroup              = self.roxie_param['strandToGroup']
        strandToHalfTurn           = self.roxie_param['strandToHalfTurn']

        if self.verbose:
            print('Setting the electrical order')

        # If the key overwrite_electrical_order is defined, the electrical order is
        if self.model_data and len(self.model_data.CoilWindings.electrical_pairs.overwrite_electrical_order) > 0:
            if self.verbose: print('Electrical order is defined manually based on the input key CoilWindings.electrical_pairs.overwrite_electrical_order')

            el_order_half_turns = self.model_data.CoilWindings.electrical_pairs.overwrite_electrical_order
            # Assign values to the attribute in the model_data dataclass
            self.el_order_half_turns = el_order_half_turns  # TODO assign it to a better structure
            return el_order_half_turns  # stop here the function without calculating the electrical order

        el_order_half_turns = []
        if typeWindings in ['multipole', 'busbar']:
            if len(elPairs_RevElOrder) != len(elPairs_GroupTogether):
                raise Exception('Length of the vector elPairs_RevElOrder ({}) must be equal to nElPairs={}.'.format(
                    len(elPairs_RevElOrder), len(elPairs_GroupTogether)))
            for p in range(len(elPairs_GroupTogether)):
                if nT[elPairs_GroupTogether[p][0] - 1] != nT[elPairs_GroupTogether[p][1] - 1]:
                    raise Exception('Pair of groups defined by the variable elPairs_GroupTogether must have the same number of half-turns.')
                for k in range(nT[elPairs_GroupTogether[p][0] - 1]):
                    if elPairs_RevElOrder[p] == 0:
                        el_order_half_turns.append(indexTstart[elPairs_GroupTogether[p][0] - 1] + k)
                        el_order_half_turns.append(indexTstart[elPairs_GroupTogether[p][1] - 1] + k)
                    if elPairs_RevElOrder[p] == 1:
                        el_order_half_turns.append(indexTstop[elPairs_GroupTogether[p][0] - 1] - k)
                        el_order_half_turns.append(indexTstop[elPairs_GroupTogether[p][1] - 1] - k)
        elif typeWindings in ['solenoid']:
            # nGroupsDefined = len(nT)
            # winding_order_groups = (nGroupsDefined * [0, 1])[:nGroupsDefined]
            # for p in range(nGroupsDefined, 0, -1):
            #     for k in range(nT[p - 1]):
            #         if winding_order_groups[p - 1] == 0:
            #             el_order_half_turns.append(indexTstart[p - 1] + k)
            #         if winding_order_groups[p - 1] == 1:
            #             el_order_half_turns.append(indexTstop[p - 1] - k)
            pass        # electricall order calculated in assignSolenoidValuesWindings method of this class
        elif typeWindings in ['CCT_straight']:

            wwns = self.model_data.CoilWindings.CCT_straight.winding_numRowStrands  # number of wires in width direction
            whns = self.model_data.CoilWindings.CCT_straight.winding_numColumnStrands  # number of wires in height direction
            n_turns_formers = self.model_data.CoilWindings.CCT_straight.winding_numberTurnsFormers  # number of turns [-]
            winding_order = self.model_data.CoilWindings.CCT_straight.winding_order
            fqpl_names = [val for val, flag in zip(self.model_data.Quench_Protection.FQPCs.names, self.model_data.Quench_Protection.FQPCs.enabled) if flag]

            # ----- formers' turns -----
            all_turns_magnet = []  # list for all turns of the former
            for former_i in range(len(n_turns_formers)):  # for each former of cct
                all_turns_former = []  # list of lists of lists for actual turns positions
                former_start_offset = former_i * wwns[former_i] * whns[former_i] * n_turns_formers[former_i]  # offset for the first turn on the next former
                for channel_turn in range(n_turns_formers[former_i]):  # for number of turns in each former
                    actual_turns = []  # list to collect turn numbers
                    current_turn = channel_turn + former_start_offset + 1  # start first turn of the fist channel with the former offset
                    for i_w in range(1, wwns[former_i] + 1):  # for each turn in the width direction of the channel
                        for i_h in range(1, whns[former_i] + 1):  # for each turn in the height direction of the channel
                            actual_turns.append(current_turn)
                            current_turn = current_turn + n_turns_formers[former_i]  # next turn is 'above' i.e. in the height direction so add number of turns in the width direction
                    all_turns_former.append(actual_turns)  # collect all turns for the former
                all_turns_magnet.append(all_turns_former)  # collect all turns for the magnet windings
            all_actual_pos = []  # list for regrouped turns, so directly an electrical position index could be used
            for i in range(len(all_turns_magnet[0])):  # get the former index to extract only turns for that former
                positional_turns = []  # list to collect turn numbers in a sequence of positional turns (of length of winding order)
                for all_turns_former in all_turns_magnet:
                    positional_turns.extend(all_turns_former[i])  # put turns in groove number from inner former number and outer former number
                all_actual_pos.append(positional_turns)  # put lists together
            electrical_order = []  # list to put electrical order into
            for el_pos in winding_order:  # for each winding order positional turn
                for actual_pos in all_actual_pos:  # for each positional turn (a list of length of max integer in the winding order)
                    electrical_order.append(actual_pos[el_pos - 1])  # get turn number corresponding to position specified in the winding order (-1 due to 0 based list)

            # ----- fqpls' turns -----
            max_turn = int(np.max(electrical_order))
            for _ in range(len(fqpl_names)):  # for each fqpl
                for _ in range(2):  # for 'go' and 'return' part of fqpl
                    max_turn += 1   # increment by one, this matches fiqus postprocessing
                    electrical_order.append(max_turn)

            el_order_half_turns = electrical_order
        elif typeWindings in ['CWS']:
            el_order_half_turns = self.model_data.Options_FiQuS.cws.postproc.field_map.winding_order
        # Assign values to the attribute in the model_data dataclass
        self.el_order_half_turns = el_order_half_turns  #TODO assign it to a better structure

        if self.verbose:
            print('Setting electrical order was successful.')

        if flag_plot:
            PM = PlotterModel(self.roxie_data)
            if typeWindings not in ['CCT_straight', 'CWS']:
                PM.plot_electrical_order(el_order_half_turns, elPairs_GroupTogether, strandToGroup, self.roxie_param['x_strands'], self.roxie_param['y_strands'], strandToHalfTurn, self.model_data)
        return np.array(el_order_half_turns)

    def buildFiQuS(self, simulation_name=None, library_path=None, output_path=None):
        """
            Building a FiQuS model
            :param simulation_name: This is used in analysis steam to change yaml name from magnet name to simulation name
        """

        if library_path != None:
            if self.model_data.GeneralParameters.magnet_type =='mulipole':
                bh_data_file_path = os.path.join(library_path, "magnets", "roxie.bhdata")
                shutil.copyfile(bh_data_file_path, os.path.join(self.output_path, 'roxie.bhdata'))
                path_map2d = os.path.join(library_path, 'magnets', self.model_data.GeneralParameters.magnet_name, 'input', self.model_data.Sources.magnetic_field_fromROXIE)
                destination_map2d = os.path.join(self.output_path, simulation_name + "_ROXIE_REFERENCE.map2d")
                # Copy map2d file
                shutil.copyfile(path_map2d, destination_map2d)
            else:
                pass # for CCT and Pancake3D no bhdata is needed
        builder_FiQuS = BuilderFiQuS(model_data=self.model_data, roxie_data=self.roxie_data,
                                     flag_build=self.flag_build, flag_plot_all=self.flag_plot_all, verbose=self.verbose)

        # Write output files
        self.parser_FiQuS = ParserFiQuS(builder_FiQuS, verbose=self.verbose)
        if not output_path:
            output_path = self.output_path

        self.parser_FiQuS.writeFiQuS2yaml(output_path=output_path, simulation_name=simulation_name,
                                          append_str_to_magnet_name='_FiQuS')

    def buildLEDET(self, verbose: bool = None):
        """
            Building a LEDET model
            case_model is a string defining the type of model to build (magnet or conductor)
        """
        if verbose is None:
            verbose = self.verbose

        if self.case_model == 'magnet':
            magnet_name = self.model_data.GeneralParameters.magnet_name
            nameFileSMIC = os.path.join(self.output_path, magnet_name + '_selfMutualInductanceMatrix.csv')  # full path of the .csv file with self-mutual inductances to write

            # Copy/edit the ROXIE map2d file
            if self.path_map2d:
                suffix = "_All"
                if self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == 1:
                    #     # [[...half_turn_length, Ribbon...n_strands],.....]
                    # TODO: geometry when conductor has a combination of ribbon and non-ribbon cables

                    # List of flags that are True is the cable type is "Ribbon"
                    list_flag_ribbon = []
                    for i, cond in enumerate(self.model_data.CoilWindings.conductor_to_group):
                        list_flag_ribbon.append(self.model_data.Conductors[cond - 1].cable.type == 'Ribbon')

                    nT_from_original_map2d, nStrands_inGroup_original_map2d, _, _, _, _, _, _ = getParametersFromMap2d(
                        map2dFile=self.path_map2d,
                        headerLines=self.model_data.Options_LEDET.field_map_files.headerLines,
                        verbose=verbose)

                    n_groups_original_file = len(nT_from_original_map2d)
                    geometry_ribbon_cable = []

                    for i in range(n_groups_original_file):
                        list = [None, None]
                        list[0] = int(nStrands_inGroup_original_map2d[i])  # layers
                        list[1] = nT_from_original_map2d[
                            i]  # number of half-turns; in case it is not a ribbon cable, it is going to be ignored in the modify-ribbon-cable function
                        geometry_ribbon_cable.append(list)

                    if verbose:
                        print('geometry_ribbon_cable: {}'.format(geometry_ribbon_cable))

                    file_name_output = copy_modified_map2d_ribbon_cable(magnet_name,
                                                                        self.path_map2d,
                                                                        self.output_path, geometry_ribbon_cable,
                                                                        self.model_data.Options_LEDET.field_map_files.flagIron,
                                                                        self.model_data.Options_LEDET.field_map_files.flagSelfField,
                                                                        list_flag_ribbon,
                                                                        suffix=suffix, verbose=verbose)

                elif self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == 0 or self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == None:
                    file_name_output = copy_map2d(magnet_name, self.path_map2d, self.output_path,
                                                  self.model_data.Options_LEDET.field_map_files.flagIron,
                                                  self.model_data.Options_LEDET.field_map_files.flagSelfField,
                                                  suffix=suffix, verbose=verbose)

                self.map2d_file_modified = os.path.join(self.output_path, file_name_output)
            else:
                self.map2d_file_modified = None

            # Copy the additional geometry and magnetic field csv file, if defined in the input file
            if self.model_data.Options_LEDET.simulation_3D.sim3D_flag_Import3DGeometry == 1:
                name_geometry_csv_file = magnet_name + '_' + str(
                    self.model_data.Options_LEDET.simulation_3D.sim3D_import3DGeometry_modelNumber) + '.csv'
                input_path_full = os.path.join(self.path_magnet, name_geometry_csv_file)
                output_path_full = os.path.join(self.output_path, name_geometry_csv_file)
                shutil.copy2(input_path_full, output_path_full)
                if verbose:
                    print('File {} copied to {}.'.format(input_path_full, output_path_full))

            builder_ledet = BuilderLEDET(path_magnet=self.path_magnet, input_model_data=self.model_data,
                                         input_roxie_data=self.roxie_data, input_map2d=self.map2d_file_modified,
                                         smic_write_path=nameFileSMIC, flag_build=self.flag_build,
                                         flag_plot_all=self.flag_plot_all, verbose=verbose,
                                         case_model=self.case_model,
                                         el_order_half_turns=self.el_order_half_turns, roxie_param=self.roxie_param)

            # Copy or modify+copy magnet-name_E....map2d files
            number_input_files = len([entry for entry in os.listdir(self.path_magnet) if
                                      os.path.isfile(os.path.join(self.path_magnet, entry))])
            for file in range(number_input_files + 1):
                suffix = '_E{}'.format(file)
                path_map2d_E = os.path.join(self.path_magnet, magnet_name + suffix + '.map2d')
                if os.path.isfile(path_map2d_E):
                    if self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == 1:
                        copy_modified_map2d_ribbon_cable(magnet_name,
                                                         path_map2d_E,
                                                         self.output_path, geometry_ribbon_cable,
                                                         self.model_data.Options_LEDET.field_map_files.flagIron,
                                                         self.model_data.Options_LEDET.field_map_files.flagSelfField,
                                                         list_flag_ribbon,
                                                         suffix=suffix, verbose=verbose)
                    elif self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == 0 or self.model_data.Options_LEDET.field_map_files.flag_modify_map2d_ribbon_cable == None:
                        copy_map2d(magnet_name, path_map2d_E, self.output_path,
                                   self.model_data.Options_LEDET.field_map_files.flagIron,
                                   self.model_data.Options_LEDET.field_map_files.flagSelfField, suffix=suffix,
                                   verbose=verbose)

            # Write output excel file
            parser_ledet = ParserLEDET(builder_ledet)
            nameFileLEDET = os.path.join(self.output_path, magnet_name + '.xlsx')  # full path of the LEDET input file to write
            parser_ledet.writeLedet2Excel(full_path_file_name=nameFileLEDET, verbose=verbose,
                                          SkipConsistencyCheck=True)

            # Write output yaml file
            nameFileLedetYaml = os.path.join(self.output_path, magnet_name + '.yaml')  # full path of the LEDET input file to write
            parser_ledet.write2yaml(full_path_file_name=nameFileLedetYaml, verbose=verbose,
                                    SkipConsistencyCheck=True)

            # Write output json file
            if self.flag_json:
                nameFileLedetJson = os.path.join(self.output_path, magnet_name + '.json')  # full path of the LEDET input file to write
                parser_ledet.write2json(full_path_file_name=nameFileLedetJson, verbose=verbose,
                                        SkipConsistencyCheck=True)

        elif self.case_model == 'conductor':
            conductor_name = self.conductor_data.GeneralParameters.conductor_name

            # Copy the ROXIE map2d file, if defined in the input file
            if self.path_map2d:
                suffix = "_All"
                file_name_output = copy_map2d(conductor_name,
                                              self.path_map2d,
                                              self.output_path,
                                              self.conductor_data.Options_LEDET.field_map_files.flagIron,
                                              self.conductor_data.Options_LEDET.field_map_files.flagSelfField,
                                              suffix=suffix,
                                              verbose=verbose)
                self.map2d_file_modified = os.path.join(self.output_path, file_name_output)
            else:
                self.map2d_file_modified = None
                if verbose:
                    print('Map2d file {} not present, hence it will not be copied.'.format(self.path_map2d))

            # Copy the additional geometry and magnetic field csv file, if defined in the input file
            if self.conductor_data.Options_LEDET.simulation_3D.sim3D_flag_Import3DGeometry == 1:
                name_geometry_csv_file = conductor_name + '_' + str(self.conductor_data.Options_LEDET.simulation_3D.sim3D_import3DGeometry_modelNumber) + '.csv'
                input_path_full = os.path.join(self.path_magnet, name_geometry_csv_file)
                output_path_full = os.path.join(self.output_path, name_geometry_csv_file)
                shutil.copy2(input_path_full, output_path_full)
                if verbose:
                    print('File {} copied to {}.'.format(input_path_full, output_path_full))

            builder_ledet = BuilderLEDET(path_magnet=self.path_magnet, input_model_data=self.conductor_data,
                                         input_map2d=self.map2d_file_modified,
                                         flag_build=self.flag_build, flag_plot_all=self.flag_plot_all,
                                         verbose=verbose,
                                         case_model=self.case_model)

            # Write output excel file
            parser_ledet = ParserLEDET(builder_ledet)
            nameFileLEDET = os.path.join(self.output_path, conductor_name + '.xlsx')  # full path of the LEDET input file to write
            parser_ledet.writeLedet2Excel(full_path_file_name=nameFileLEDET, verbose=verbose, SkipConsistencyCheck=True)

            # Write output yaml file
            nameFileLedetYaml = os.path.join(self.output_path, conductor_name + '.yaml')  # full path of the LEDET input file to write
            parser_ledet.write2yaml(full_path_file_name=nameFileLedetYaml, verbose=verbose, SkipConsistencyCheck=True)

            # Write output json file
            if self.flag_json:
                nameFileLedetJson = os.path.join(self.output_path, conductor_name + '.json')  # full path of the LEDET input file to write
                parser_ledet.write2json(full_path_file_name=nameFileLedetJson, verbose=verbose, SkipConsistencyCheck=True)

        else:
            raise Exception('Case model {} is not supported when building a LEDET model.'.format(self.case_model))

    def buildProteCCT(self):
        """
            Building a ProteCCT model
        """

        magnet_name = self.model_data.GeneralParameters.magnet_name
        builder_protecct = BuilderProteCCT(input_model_data=self.model_data, flag_build=self.flag_build, verbose=self.verbose)

        # Write output excel file
        parser_protecct = ParserProteCCT(builder_protecct)
        nameFileProteCCT = os.path.join(self.output_path, f'{magnet_name}_ProteCCT.xlsx')  # full path of the ProteCCT input file to write
        parser_protecct.writeProtecct2Excel(full_path_file_name=nameFileProteCCT, verbose=self.verbose, SkipConsistencyCheck=True)

    def buildPSPICE(self):
        """
            Build a PSPICE circuit netlist model
        """
        # Write output .cir file
        parser_pspice = ParserPSPICE(circuit_data=self.circuit_data, path_input=self.path_magnet, output_path=self.output_path)
        nameFilePSPICE = os.path.join(self.output_path, self.circuit_data.GeneralParameters.circuit_name + '.cir')  # full path of the PSPICE netlist to write
        parser_pspice.write2pspice(full_path_file_name=nameFilePSPICE, verbose=self.verbose)

        # Copy additional files
        parser_pspice.copy_additional_files()

    def buildXYCE(self):
        """
            Build a XYCE circuit netlist model
        """
        # Write output .cir file
        parser_xyce = ParserXYCE(circuit_data=self.circuit_data, path_input=self.path_magnet, output_path=self.output_path)
        nameFileXYCE = os.path.join(self.output_path, self.circuit_data.GeneralParameters.circuit_name + '.cir')  # full path of the PSPICE netlist to write
        parser_xyce.write2XYCE(nameFileXYCE, verbose=self.verbose)
        parser_xyce.copy_additional_files(flag_translate=True, verbose=self.verbose)
        parser_xyce.resolve_paths_netlist(nameFileXYCE)

    def buildPyBBQ(self):
        """
            Build a PyBBQ model
        """

        conductor_name = self.conductor_data.GeneralParameters.conductor_name
        builder_PyBBQ = BuilderPyBBQ(input_model_data=self.conductor_data, flag_build=self.flag_build, verbose=self.verbose)

        # Write output yaml file
        parser_PyBBQ = ParserPyBBQ(builder_PyBBQ)
        nameFilePyBBQ = os.path.join(self.output_path, conductor_name + '.yaml')  # full path of the PyBBQ input file to write
        parser_PyBBQ.writePyBBQ2yaml(full_path_file_name=nameFilePyBBQ, verbose=self.verbose)

    def buildPySIGMA(self, sim_number=None, use_model_builder_path=True, make_bh_copy=True, settings=None):
        """
            Build a pySIGMA input files
        """
        magnet_name = self.model_data.GeneralParameters.magnet_name
        if use_model_builder_path:
            output_path = self.output_path
        else:
            output_path = os.path.join(self.settings_dict['local_SIGMA_folder'], f'{magnet_name}_{sim_number}')
        if sim_number:
            builder_SIGMA = BuilderPySIGMA(model_data=self.model_data, roxie_data=self.roxie_data, path_model_folder=self.path_magnet, make_bh_copy=make_bh_copy)
            self.parser_SIGMA = ParserPySIGMA(builder_SIGMA, output_path=output_path)
            self.parser_SIGMA.writeSIGMA2yaml(simulation_name=magnet_name)
            coordinate_file_path = self.parser_SIGMA.coordinate_file_preprocess(model_data=self.model_data)
            # Call mainPySIGMA which generates the Java files.
            input_yaml_file_path = os.path.join(output_path, f'{magnet_name}.yaml')
            mps = MainPySIGMA(model_folder=output_path)
            mps.build(input_yaml_file_path=input_yaml_file_path, input_coordinates_path=coordinate_file_path, results_folder_name=self.results_folder_name, settings=settings)


    def load_circuit_parameters_from_csv(self, input_file_name: str, selected_circuit_name: str = None):
        '''
            Load circuit parameters from a csv file into a case=circuit object
            :param input_file_name: full path to the csv file
            :param selected_circuit_name: name of the circuit name whose parameters will be loaded
        '''

        # Unpack input
        verbose = self.verbose

        # Check that the model case is circuit
        if self.case_model != 'circuit':
            raise Exception(f'This method can only be used for circuit models, but case_model={self.case_model}')

        # TODO: Think on whether this is good to add as a default option
        # if selected_circuit_name is None:
        #     selected_circuit_name = self.circuit_data.GeneralParameters.circuit_name

        circuit_param = find_by_position(input_file_name, 0,
                                         selected_circuit_name)  # TODO make it more robust by referring to a key rather than the first column
        # del circuit_param[0]
        param_names = find_column_list(input_file_name)
        # del param_names[0]
        dict_circuit = {k: v for k, v in zip(param_names, circuit_param)}

        for key, value in dict_circuit.items():
            if key in self.circuit_data.GlobalParameters.global_parameters:
                if self.circuit_data.GlobalParameters.global_parameters[key] != value:
                    if verbose:
                        print(
                            f'Circuit {self.circuit_data.GeneralParameters.circuit_name}: Value of parameter {key} was changed from {self.circuit_data.GlobalParameters.global_parameters[key]} to {value}')
                    self.circuit_data.GlobalParameters.global_parameters[key] = value


