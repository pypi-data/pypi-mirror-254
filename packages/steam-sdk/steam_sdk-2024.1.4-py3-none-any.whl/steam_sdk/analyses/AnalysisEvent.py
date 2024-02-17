import csv
import os
import re
import warnings
import ruamel.yaml
import pandas as pd
from steam_sdk.parsers.ParserPSPICE import ParserPSPICE

'''
This file contains helper functions for certain analyses of steam-models-dev that:
 - do not need an instance but are static
 - do not fit in the AnalysisSTEAM.py because their use-case is not as general usable as the functions in the AnalysisSTEAM.py
'''

#TODO: Include further functions from AnalysisSteam.py here and maybe try to summarize some of them as the functionality is concruent for some of them
def find_n_magnets_in_circuit(filename: str, circuit_name: str):
    '''
    ** Find the number of magnets present in the current circuit by reading the value from a csv file **
    :param filename: path to the input csv file
    :param circuit_name: string that defines the name of the circuit (the code will look into the row that bears this name)
    :return string defining the number of magnets in the circuit
    '''
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['circuit'] == circuit_name:
                return row['NumberOfMagnets']
        return None


def find_IPQ_circuit_type_from_IPQ_parameters_table(filename: str , circuit_name: str):
    '''
    ** This function returns the circuit type e.g. IPQ_RQ4_4_2xRPHH_4xMQY for a specific circuitname e.g. RQ4.L8 from a table
    :param filename: path to the IPQ_circuit_parameters.csv file
    :param circuit_name: string that defines the name of the circuit (the code will look into the row that bears this name)
    '''
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['circuit'] == circuit_name:
                return row['circuit_type']
        return None


def get_circuit_name_from_eventfile(event_file: str):
    '''
    ** This function returns the circuit name for a given event file by opening it and reading the entry "Circuit Name"
    :param event_file: eventfile from the LHC postmortem database e.g. ROD.A23B1_FPA-2022-04-14-10h39-2022-04-14-11h04.csv
    '''
    with open(event_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_entry = row.get("Circuit Name")
            if first_entry:
                # TODO: for some reason, the circuit names in the RQ event files have wrong names..
                #  one has to be carefull since IPQ circuit names can also start with RQ., however those never contain
                #  an "A" in der name..--> this is just a quick solution for now, one could also replace with "RQF_"
                if first_entry.startswith("RQ.") and "A" in first_entry: first_entry = first_entry.replace("RQ.","RQD_")
                return first_entry


# def get_circuit_family_from_circuit_name(circuit_name: str):
#     '''
#     ** This function returns the the circuit family for a given circuit name by a simple logic without any additional files necessary
#     :param circuit_name: name of the circuit e.g. RQ.A12
#     '''
#     if circuit_name.startswith("RCBH") or circuit_name.startswith("RCBV"):
#         return "60A"
#     elif circuit_name.startswith("RD"):
#         return "IPD"
#     elif circuit_name.startswith("RQX"):
#         return "RQX"
#     elif circuit_name.startswith(("RQ4", "RQ5", "RQ7", "RQ8", "RQ9", "RQ10")) or (circuit_name.startswith("RQ6.") and len(circuit_name) == 6):
#         return "IPQ"
#     elif circuit_name.startswith(("RQT12", "RQT13", "RQS", "RSS", "RQTL7", "RQTL8", "RQTL10", "RQTL11", "RCBX", "RQSX3", "RCS", "ROD", "ROF", "RSD", "RSF", "RQTL9", "RQTD", "RQTF", "RCD", "RCO", "RC.","RU")) or (circuit_name.startswith("RQ6.") and len(circuit_name) == 8):
#         return "600A"
#     elif circuit_name.startswith("RQ"):
#         return "RQ"
#     elif circuit_name.startswith(("RCBY", "RCBC", "RCTX")):
#         return "80-120A"
#     elif circuit_name.startswith("RB"):
#         return "RB"

def get_circuit_family_from_circuit_name(circuit_name, library_path):
    # Load the file from library_path into a DataFrame
    df = pd.read_csv(os.path.join(library_path,'circuits','circuit_parameters', 'Table_CircuitName_CircuitFamily_CircuitType.csv'))

    # Find the row where 'circuit_name' matches the 'circuit_name' column
    row = df.loc[df['circuit_name'] == circuit_name]
    # If the row is found, get the corresponding 'circuit_types' entry
    if not row.empty:
        circuit_family_entry = row['circuit_family'].values[0]
        return circuit_family_entry
    else:
        return None  # Circuit name not found in the file

def create_two_csvs_from_odd_and_even_rows(input_file_name, output_odd_file_name: str = 'output_odd.csv', output_even_file_name:str = 'output_even.csv'):
    '''
    ** This function creates two csv files from the odd and the even rows of a given csv file and returns the filenames of the respective files created
    :param imput_file_name: path of the input csv file
    '''
    # Create empty lists to hold the odd and even rows
    odd_rows = []
    even_rows = []

    # Open the input CSV file and read in the rows
    with open(input_file_name, 'r') as input_file:
        reader = csv.reader(input_file)

        # Save the header row
        header = next(reader)

        # Loop over the remaining rows and append them to the odd or even list
        for i, row in enumerate(reader):
            if i % 2 == 0:
                even_rows.append(row)
            else:
                odd_rows.append(row)

    # Write the odd and even rows to separate output files'
    with open(output_odd_file_name, 'w', newline='') as output_odd_file:
        writer_odd = csv.writer(output_odd_file)
        writer_odd.writerow(header)
        writer_odd.writerows(odd_rows)

    with open(output_even_file_name, 'w', newline='') as output_even_file:
        writer_even = csv.writer(output_even_file)
        writer_even.writerow(header)
        writer_even.writerows(even_rows)

    # Return a list of the output file names
    return [output_even_file_name, output_odd_file_name]

def get_number_of_apertures_from_circuit_family_name(circuit_family_name: str):
    '''
    **This function returns the number of apertures for a given circuit name by a simple logic
    :param circuit_family_name: This parameter defines the circuit family name which determines the number apertures
    '''
    #circuit_family_name = get_circuit_family_from_circuit_name(circuit_name)
    if circuit_family_name in ["IPQ", "RB"]:
        return 2
    else:
        return 1

def get_number_of_quenching_magnets_from_layoutdetails(position: str, circuit_family_name: str,library_path):
    '''
    **This function returns the #Electric_circuit value of a magnet based on its position argument which is the text
    **after the dot in the entries of the 'Magnet' column of  the LayoutDetails.csv
    :param position: position of the magnet
    :param circuit_family_name: family name of the circuit
    :library_path: absolute path of steam_models
    '''
    df = pd.read_csv(
        os.path.join(library_path, 'circuits', 'circuit_parameters', f"{circuit_family_name}_LayoutDetails.csv"))
    mask = df['Magnet'].str.split('.').str[1] == position
    result = df.loc[mask, '#Electric_circuit'].iloc[0]
    return result

def get_magnet_types_list(number_of_magnets: int, simulation_name: str):
    """
    **Generates a list representing types of magnets based on simulation parameters.
    :param number_of_magnets: The total number of magnets in the simulation.
    :param simulation_name: The name of the simulation.

    Explanation:
        - If the simulation involves 4 magnets and starts with "RQX", the list
          will be [1, 2, 2, 1]. This pattern is specific to this simulation case.
        - If the simulation starts with "IPQ" and involves 2 magnets, the list
          will be [1, 2].
        - If the simulation starts with "RB", all magnets will be of type 1.
        - If the simulation name is not "RQX", "IPQ" or "RB", For specific numbers of magnets (154, 13, 8, 77, 6, 12, 11, 10, 9, 4, 2),
          the list will consist of one type 1 magnet followed by (number_of_magnets - 1)
          type 2 magnets.
        - For all other cases, the default magnet type is 1 for all magnets.
    Returns:
            List[int]: A list representing types of magnets, where each element indicates the type of the corresponding magnet in the simulation.
    """
    if number_of_magnets == 4 and simulation_name.startswith("RQX"): #to be improved
        return [1, 2, 2, 1]
    elif simulation_name.startswith("IPQ") and number_of_magnets == 2:
        return [1, 2]
    elif simulation_name.startswith("RB"):
        return [1] * number_of_magnets
    elif number_of_magnets in [154, 13, 8, 77, 6, 12, 11, 10, 9, 4, 2]:
        return [1] + [2] * (number_of_magnets - 1)
    else:
        return [1] * number_of_magnets

def get_number_of_magnets(circuit_name: str, simulation_name: str, circuit_type: str, circuit_family_name: str):
    """
    **Determines the number of magnets in a specific circuit based on circuit name and type, and simulation name.
    :param circuit_name: The name of the circuit.
    :param simulation_name: The name of the simulation.
    :param circuit_type: The type of the circuit.

    Returns:
        int: The number of magnets in the specified circuit.

    Algorithm:
        - If the circuit type is "RCS" or "RB", returns 154.
        - If the circuit type is "RCD" or "RCO", returns 77.
        - If the circuit name starts with "RQ6." and has a length of 8, returns 6.
        - If the circuit name starts with "RQS.R", "RQS.L", or "RQTL9", returns 2.
        - If the circuit name starts with "RQS.A", "RSS", or "RQX", returns 4.
        - If the circuit name starts with "RQTD" or "RQTF", returns 8.
        - If the circuit family name is "60A", "IPD", "80-120A", or "600A", returns 1.
        - If the circuit type is "RQ_47magnets", returns 47.
        - If the circuit type is "RQ_51magnets", returns 51.
        - If the circuit family name is "IPQ", calculates the number of magnets based on the simulation name.

    Note:
        - For "IPQ" circuits, the function extracts a numeric value from the simulation name and divides it by 2 to determine the number of magnets.
    """
    #circuit_family_name = get_circuit_family_from_circuit_name(circuit_name)
    #circuit_type = self.__get_circuit_type(circuit_name, self.library_path)
    if circuit_type in ["RCS", "RB"]:
        return 154
    elif circuit_type in ["RCD", "RCO"]:
        return 77
    elif circuit_name.startswith("RQ6.") and len(circuit_name) == 8:
        return 6
    elif circuit_name.startswith(("RQS.R", "RQS.L", "RQTL9")):
        return 2
    elif circuit_name.startswith(("RQS.A", "RSS", "RQX")):
        return 4
    elif circuit_name.startswith(("RQTD", "RQTF")):
        return 8
    elif circuit_family_name in ["60A", "IPD", "80-120A", "600A"]:
        return 1
    elif circuit_type == "RQ_47magnets":
        return 47
    elif circuit_type == "RQ_51magnets":
        return 51
    elif circuit_family_name == "IPQ":
        return int(int(re.search(r'_(\d+)_', simulation_name).group(1))/2)

def get_magnet_name(circuit_name: str, simulation_name: str, circuit_type: str):
    '''
    **Function that determines the magnet name(s) based on the provided circuit name, simulation name, and circuit type.
    :param circuit_name: The name of the circuit.
    :param simulation_name: The name of the simulation.
    :param circuit_type: The type of the circuit.

    Returns:
        str or list: The name of the magnet(s) corresponding to the given circuit and simulation.
        If multiple magnet names are possible, a list is returned.
    '''
    #assert (simulation_name == self.data_analysis.AnalysisStepDefinition['runParsimEvent'].simulation_name)
    #assert (circuit_type == self.__get_circuit_type(circuit_name, self.library_path))
    #assert (True == False)

    if circuit_name.startswith("RCBH") or circuit_name.startswith("RCBV"):
        return "MCBH"
    elif circuit_name.startswith("RD"):
        #circuit_type = self.__get_circuit_type(circuit_name, self.library_path)
        magnet_dict = {"RD1": "MBX", "RD2": "MBRC", "RD3": "MBRS", "RD4": "MBRB"}
        return magnet_dict.get(circuit_type, "")
    elif circuit_name.startswith("RQX"):
        return ["MQXA", "MQXB"]
    elif circuit_name.startswith(("RQ4", "RQ5", "RQ7", "RQ8", "RQ9", "RQ10")) or (circuit_name.startswith("RQ6.") and len(circuit_name) == 6):
        magnet_dict = {"IPQ_RQ4_2_2xRPHH_2xMQY": "MQY", "IPQ_RQ4_4_2xRPHH_4xMQY": ["MQY", "MQY"], "IPQ_RQ5_2_2xRPHGB_2xMQML": "MQML", "IPQ_RQ5_2_2xRPHH_2xMQY": "MQY", "IPQ_RQ5_4_2xRPHGB_4xMQM": ["MQM", "MQM"], "IPQ_RQ5_4_2xRPHH_4xMQY": ["MQY", "MQY"], "IPQ_RQ6_2_2xRPHGB_2xMQML": "MQML", "IPQ_RQ6_2_2xRPHGB_2xMQY": "MQY", "IPQ_RQ6_4_2xRPHGB_2xMQM_2xMQML": ["MQM", "MQML"], "IPQ_RQ7_2_2xRPHGA_2xMQM": "MQM", "IPQ_RQ7_4_2xRPHGA_4xMQM": ["MQM", "MQM"], "IPQ_RQ8_2_2xRPHGA_2xMQML": "MQML", "IPQ_RQ9_4_2xRPHGA_2xMQM_2xMQMC": ["MQM", "MQMC"], "IPQ_RQ10_2_2xRPHGA_2xMQML": "MQML"}
        return magnet_dict.get(simulation_name, "")
    elif circuit_name.startswith("RQ6.") and len(circuit_name) == 8:
        return ["MQTLH", "MQTLH_quenchback"]
    elif circuit_name.startswith(("RQTL7", "RQTL8", "RQTL10", "RQTL11")):
        return "MQTLI"
    elif circuit_name.startswith("RQTL9"):
        return ["MQTLI", "MQTLI_quenchback"]
    elif circuit_name.startswith("RQSX3"):
        return "MQSX"
    elif circuit_name.startswith("RQS"):
        return ["MQS", "MQS_quenchback"]
    elif circuit_name.startswith(("RQT12", "RQT13")):
        return "MQT"
    elif circuit_name.startswith(("RQTD", "RQTF")):
        return ["MQT", "MQT_quenchback"]
    elif circuit_name.startswith("RQ"):
        return "MQ"
    elif circuit_name.startswith("RCBY"):
        return "MCBYH"
    elif circuit_name.startswith("RCBC"):
        return "MCBCH"
    elif circuit_name.startswith("RCS"):
        return ["MCS", "MCS_quenchback"]
    elif circuit_name.startswith("RB"):
        return "MB"
    elif circuit_name.startswith("RCBX"):
        return ["MCBXH", "MCBXV"]
    elif circuit_name.startswith("RSS"):
        return ["MSS", "MSS_quenchback"]
    elif circuit_name.startswith(("ROD", "ROF")):
        return ["MO", "MO_quenchback"]
    elif circuit_name.startswith(("RSD", "RSF")):
        return ["MS", "MS_quenchback"]
    elif simulation_name == "RCD":
        return ["MCD", "MCD_quenchback"]
    elif simulation_name == "RCO":
        return ["MCO", "MCO_quenchback"]


#this is an old method which is to be deleted
# def get_circuit_type(circuit_name: str, library_path, simulation_name: str = None):
#     """
#     Determines the circuit type based on the provided circuit name, library path, and optional simulation name.
#     The simulation name is only needed in case of RCD and RCO magnets
#
#     :param circuit_name: The name of the circuit.
#     :param library_path: The path to the steam models.
#     :param simulation_name: The name of the simulation (optional).
#     :return: The determined circuit type as a string.
#     """
#     # if simulation_name:
#     #     assert(self.data_analysis.AnalysisStepDefinition['runParsimEvent'].simulation_name == simulation_name)
#     #     #assert(True == False)
#     if circuit_name.startswith("RCBH") or circuit_name.startswith("RCBV"):
#         return "RCB"
#     elif circuit_name.startswith(("RD1", "RD2", "RD3", "RD4")):
#         return {"RD1": "RD1", "RD2": "RD2", "RD3": "RD3", "RD4": "RD4"}.get(circuit_name[:3], "No match found")
#     elif circuit_name.startswith("RQX"):
#         return "RQX"
#     elif circuit_name.startswith(("RQ4", "RQ5", "RQ6", "RQ7", "RQ8", "RQ9", "RQ10")):
#         #assert(True==False)
#         return circuit_name.split(".")[0]
#     elif circuit_name.startswith(("RQT12", "RQT13")):
#         return "RQT_12_13"
#     elif circuit_name.startswith(("RQTL7", "RQTL8", "RQTL10", "RQTL11")):
#         return "RQTL_7_8_10_11"
#     elif circuit_name.startswith("RQTL9"):
#         return "RQTL9"
#     elif circuit_name.startswith(("RQTD", "RQTF")):
#         return "RQT"
#     elif circuit_name.startswith("RQSX3"):
#         return "RQSX3"
#     elif circuit_name.startswith("RQS"):
#         return "RQS"
#     elif circuit_name.startswith("RQ."):
#         circuit_name_temp = circuit_name.replace(".", "D_")
#         magnet_number = find_n_magnets_in_circuit(os.path.join(library_path, "circuits","circuit_parameters","RQ_circuit_parameters.csv"), circuit_name_temp)
#         return f"RQ_{magnet_number}magnets"
#     elif circuit_name.startswith("RCS"):
#         return "RCS"
#     elif circuit_name.startswith("RB"):
#         return "RB"
#     elif circuit_name.startswith("RCBX"):
#         return "RCBX"
#     elif circuit_name.startswith("RCBC"):
#         return "RCBC"
#     elif circuit_name.startswith("RCBY"):
#         return "RCBY"
#     elif circuit_name.startswith("RSS"):
#         return "RSS"
#     elif circuit_name.startswith(("RSD")):
#         magnet_number = find_n_magnets_in_circuit(os.path.join(library_path, "circuits","circuit_parameters","600A_circuit_parameters.csv"), circuit_name)
#         return f"RSD_{magnet_number}magnets"
#     elif circuit_name.startswith(("RSF")):
#         magnet_number = find_n_magnets_in_circuit(os.path.join(library_path, "circuits","circuit_parameters","600A_circuit_parameters.csv"), circuit_name)
#         return f"RSF_{magnet_number}magnets"
#     elif circuit_name.startswith(("RO")):
#         magnet_number = find_n_magnets_in_circuit(os.path.join(library_path, "circuits","circuit_parameters","600A_circuit_parameters.csv"), circuit_name)
#         return f"RO_{magnet_number}magnets"
#     elif simulation_name == "RCD": #improvement pending
#         return "RCD"
#     elif simulation_name == "RCO": #improvement pending
#         return "RCO"

def get_t_PC_off_from_PSPICE_netlist_data(path_to_circuit_file: str, verbose: bool = False):
    """
    ** Extracts t_PC_off values from a PSPICE netlist file and returns them in a dictionary. **

    Returns:
        dict: A dictionary containing component names with 't_PC_off' values extracted from the netlist file.

    :param path_to_circuit_file: The file path to the PSPICE netlist file.
    :param verbose: (bool, optional) If True, prints information about the extraction process. Default is False.
    """
    pp = ParserPSPICE(None)
    if verbose:
        print(f"Getting t_PC_off from netlist data at {path_to_circuit_file}")
    netlist_data = pp.read_netlist(path_to_circuit_file, flag_acquire_auxiliary_files=False, verbose=False)
    dictionary_global_parameters = netlist_data.GlobalParameters.global_parameters
    t_PC_off_dict = {}
    for key, value in dictionary_global_parameters.items():
        if "t_PC_off" in key:
            t_PC_off_dict[key] = value
    if verbose:
        print(f"The following values of t_PC_off were extracted from the netlist file: {t_PC_off_dict}")
    if not len(set(t_PC_off_dict.values())) == 1:
        warnings.warn('t_PC_off values are not identical in netlist!')
    else:
        return float(t_PC_off_dict[next(iter(t_PC_off_dict))])


def generate_unique_event_identifier_from_eventfile(file_name, verbose: bool = False):
    """"
    *** Method that returns a unique identifier for an event by cutting the filename after the first date entry found ***
    :param file_name: name of the event file with ending
    :param verbose:
    """
    pattern = r'(.*?)(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}-\d{4}-\d{2}-\d{2}-\d{2}h\d{2})(?:_(\w+))?\..*'

    match = re.search(pattern, file_name)

    if verbose:
        print("-" * 50)
        print("File Name:", file_name)

    if match:
        output = match.group(1) + match.group(2)
        if verbose:
            print("Unique identifier is:", output)
    else:
        output = None
        if verbose:
            warnings.warn("Unique identifier is None")

    return output

def get_signal_keys_from_configurations_file(full_config_file_path, configuration):
    """
        Extracts unique simulation signal labels from a YAML configurations file.
        This function is used to include all signals specified in a config
        file in the CSDF signals of a simulation

        Parameters:
        - yaml_file_path (str): The path to the YAML file containing configurations.

        Returns:
        - List[str]: A list of unique simulation signal labels extracted from the YAML file.

        This function reads the specified YAML file using ruamel.yaml, iterates through
        the 'ConfigurationList' and 'SignalList' sections, and extracts the 'sim_label'
        field for each signal. It ignores signals ending with '_zoom' and returns a list
        of unique simulation signal labels.

        """
    with open(full_config_file_path, 'r') as file:
        yaml_data = ruamel.yaml.load(file, ruamel.yaml.RoundTripLoader)

    signal_keys = []

    for config_key, config_value in yaml_data['ConfigurationList'].items():
        if config_key == configuration:
            for signal_key, signal_value in config_value['SignalList'].items():
                if signal_key.endswith('_zoom'):
                   continue
                signal_keys.append(signal_value['sim_signals_to_add_y'][0])
    return list(set(signal_keys))

def determine_config_path_and_configuration(directory_config_files, steam_circuit_type):
    """
    Function to determine the full path to the config file. If for directory config files, a file instead of a directory\
    is given, the file will be used. If a directory is provided, the usual config file in accordance to the circuit type
    will be used. Beside this the configuration is returned. In case of a directory beeing passed for directory_config_files,
    the standart configurations may be returned. In case of an absolute path, different cases for the according scenarios may
    be defined, depending on the steam_circuit type.
    """
    if os.path.isdir(directory_config_files):
        config_filepath = os.path.join(directory_config_files,f"config_{steam_circuit_type}.yaml")
        configuration =  f"{steam_circuit_type}_1"
    elif os.path.isfile(directory_config_files): # Full path to SIGMON specific config file was defined
        config_filepath = directory_config_files
        #Here cases for different configurations may be included
        if os.path.basename(config_filepath).startswith("config_SIGMON"):

            IPQ_list = ["IPQ_RQ4_2_2xRPHH_2xMQY", "IPQ_RQ4_4_2xRPHH_4xMQY","IPQ_RQ5_2_2xRPHGB_2xMQML"
            "IPQ_RQ5_2_2xRPHGB_2xMQML",
            "IPQ_RQ5_4_2xRPHH_4xMQY",
            "IPQ_RQ5_2_2xRPHH_2xMQY",
            "IPQ_RQ5_4_2xRPHGB_4xMQM",
            "IPQ_RQ5_2_2xRPHGB_2xMQML",
            "IPQ_RQ6_2_2xRPHGB_2xMQML",
            "IPQ_RQ6_4_2xRPHGB_2xMQM_2xMQML",
            "IPQ_RQ6_2_2xRPHGB_2xMQY",
            "IPQ_RQ7_4_2xRPHGA_4xMQM",
            "IPQ_RQ7_2_2xRPHGA_2xMQM",
            "IPQ_RQ8_2_2xRPHGA_2xMQML",
            "IPQ_RQ9_4_2xRPHGA_2xMQM_2xMQMC",
            "IPQ_RQ10_2_2xRPHGA_2xMQML"]

            default_circuits_with_EE = ["RCS", "RQ6","RQS","RQT","RQTL9","RSD_11magnets","RSF_10magnets","RSS","RU",
                                        "RO_13magnets","RO_8magnets", "RCD", "RQ_47magnets","RQ_51magnets", "RQS_AxxBx",
                                        "RSD_12magnets", "RSF_9magnets"]
            default_circuits_without_EE = ["RCB", "RCBC", "RCBY", "RQT_12_13", "RQTL_7_8_10_11", "RQT", "RCBX",
                                           "RCO", "RQSX3", "IPD", "RQX", "RCD_RCO"]

            circuits_80_120A = ["RCBC", "RCBY"]
            if steam_circuit_type in circuits_80_120A:
                configuration = "SIGMON_80-120A"
            elif steam_circuit_type in IPQ_list:
                configuration = "SIGMON_IPQ"
            elif steam_circuit_type.startswith("RB"):
                configuration = "SIGMON_RB"
            elif steam_circuit_type in default_circuits_with_EE:
                configuration = "SIGMON_default_with_EE"
            elif steam_circuit_type in default_circuits_without_EE:
                configuration = "SIGMON_default_without_EE"
    else:
        print(f"{directory_config_files} does not exist or is not a valid path.")
        warnings.warn("!Invalid config file path!")
        config_filepath = None
    return config_filepath , configuration


def get_circuit_type_from_circuit_name(circuit_name, library_path, simulation_name = None):
    """"
    *** Reads the file Table_CircuitName_CircuitFamily_CircuitTypes.csv in steam-models/circuits/circuit_parameters and
    returns a string array containing the name of the model needed to be run in this simulation aka the
    circuit type.
    :param  circuit_name: The name of the circuit for which circuit types are to be determined.
    :param library_path: The path to the library where the 'Table_CircuitName_CircuitFamily_CircuitTypes.csv' file is located.
    """

    #This line is needed for RCD_RCO events
    if simulation_name == "RCD":  # improvement pending
        return "RCD"
    elif simulation_name == "RCO":  # improvement pending
        return "RCO"
    else:
            #If not a RCD_RCO event, we
            # Load the file from library_path into a DataFrame
            df = pd.read_csv(os.path.join(library_path,'circuits','circuit_parameters', 'Table_CircuitName_CircuitFamily_CircuitType.csv'))

            # Find the row where 'circuit_name' matches the 'circuit_name' column
            row = df.loc[df['circuit_name'] == circuit_name]
            # If the row is found, get the corresponding 'circuit_types' entry
            if not row.empty:
                circuit_type_entry = row['circuit_type'].values[0]
                return circuit_type_entry
            else:
                return None  # Circuit name not found in the file
