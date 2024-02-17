import os
import sys
import subprocess


class DriverFiQuS:
    """
        Class to drive FiQuS models
    """
    def __init__(self, FiQuS_path: str = '', path_folder_FiQuS_input: str = None, path_folder_FiQuS_output: str = None, GetDP_path: str = None, verbose: bool = False) -> object:
        """

        :param FiQuS_path: full path to fiqus module
        :type FiQuS_path: str
        :param path_folder_FiQuS_input: full path to FiQuS input folder, i.e. where the input file .yaml is
        :type path_folder_FiQuS_input: str
        :param path_folder_FiQuS_output: full path to FiQuS output folder. This is typically where the same as the path_folder_FiQuS_input
        :type path_folder_FiQuS_output: str
        :param GetDP_path: full path to GetDP executable, with the executable name and extension
        :type GetDP_path: str
        :param verbose: if set to True more logs are printed to the console
        :type verbose: bool
        """
        self.FiQuS_path = FiQuS_path
        self.path_folder_FiQuS_input = path_folder_FiQuS_input
        self.path_folder_FiQuS_output = path_folder_FiQuS_output
        self.GetDP_path = GetDP_path
        self.verbose = verbose

        if self.FiQuS_path == 'pypi':
            import fiqus
            self.FiQuS_path = os.path.dirname(os.path.dirname(fiqus.__file__))

        if self.verbose:
            print('FiQuS path =               {}'.format(self.FiQuS_path))
            print('path_folder_FiQuS_input =  {}'.format(self.path_folder_FiQuS_input))
            print('path_folder_FiQuS_output = {}'.format(self.path_folder_FiQuS_output))
            print('GetDP_path =               {}'.format(self.GetDP_path))


    def run_FiQuS(self, sim_file_name: str):
        """
        Method to run FiQuS with a given input file name. The run type is specified in the input file.
        :rtype: object
        :param sim_file_name: name of the input file (without .yaml) that must be inside the path_folder_FiQuS_input specified in the initialization
        :type sim_file_name: str
        """
        call_commands_list = [
            sys.executable,
            os.path.join(self.FiQuS_path, 'fiqus', 'MainFiQuS.py'),
            '--in', os.path.join(self.path_folder_FiQuS_input, sim_file_name + '.yaml'),
            '--out', self.path_folder_FiQuS_output,
            '--getdp', self.GetDP_path,
        ]
        if self.verbose:
            print(f'Calling MainFiQuS via Python Subprocess.call() with: {" ".join(call_commands_list)}')
        subprocess.call(call_commands_list)
