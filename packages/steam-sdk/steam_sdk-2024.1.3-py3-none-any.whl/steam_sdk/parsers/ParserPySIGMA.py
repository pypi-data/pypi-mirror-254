import os
import shutil
import pandas as pd
from pathlib import Path

from steam_sdk.parsers.ParserYAML import dict_to_yaml
from steam_sdk.utils.make_folder_if_not_existing import make_folder_if_not_existing


class ParserPySIGMA:
    """
        Class with methods to write SIGMA input files from sdk model data file
    """

    def __init__(self, builder_SIGMA, output_path=None):
        """
        Initialization using a BuilderFiQuS object containing FiQuS parameter structure
        :param builder_SIGMA: BuilderFiQuS object
        :param output_path: full path to the output folder
        """

        self.builder_SIGMA = builder_SIGMA
        self.output_path = output_path
        make_folder_if_not_existing(output_path)
        self.attributes = ['data_SIGMA', 'data_SIGMA_geo', 'data_SIGMA_set']
        self.file_exts = ['yaml', 'geom', 'set']

    def writeSIGMA2yaml(self, simulation_name=None):
        """
        ** Writes SIGMA input files **

        :param simulation_name: This is used in analysis steam to change yaml name from magnet name to simulation name
        :return:  Nothing, writes files to output folder.
        """

          # If the output folder is not an empty string, and it does not exist, make it
        for attribute, file_ext in zip(self.attributes, self.file_exts):
            yaml_file_name = f'{simulation_name}.{file_ext}'
            dict_to_yaml(getattr(self.builder_SIGMA, attribute).dict(), os.path.join(self.output_path, yaml_file_name), list_exceptions=[])

        if self.builder_SIGMA.make_bh_copy:
            source_path = Path(os.path.join(self.builder_SIGMA.path_model_folder, self.builder_SIGMA.model_data.Sources.BH_fromROXIE)).resolve()
            destination_path = os.path.join(self.output_path, self.builder_SIGMA.data_SIGMA.Sources.bh_curve_source)
            shutil.copy2(source_path, destination_path)


    def coordinate_file_preprocess(self, model_data=None):
        """
        Function to copy map2d file and create coordinates.csv file.
        """
        magnet_name = model_data.GeneralParameters.magnet_name
        if model_data.Options_SIGMA.postprocessing.out_2D_at_points.coordinate_source is None:
            if model_data.Options_SIGMA.postprocessing.out_2D_at_points.map2d is not None:
                source_map2d_path = Path(os.path.join(self.builder_SIGMA.path_model_folder, model_data.Options_SIGMA.postprocessing.out_2D_at_points.map2d)).resolve()
                destination_map2d_path = os.path.join(self.output_path, magnet_name + "_ROXIE_REFERENCE.map2d")
                shutil.copyfile(source_map2d_path, destination_map2d_path)
                coordinate_file_path = os.path.join(self.output_path, magnet_name + "_ROXIE_COORD.csv")
                self.create_coordinate_file(destination_map2d_path, coordinate_file_path)
                return coordinate_file_path

    def create_coordinate_file(self, path_map2d, coordinate_file_path):
        """
        Creates a csv file with same coordinates as the map2d.

        :param path_map2d: Map2d file to read coordinates from
        :param coordinate_file_path: Path to csv filw to be created
        :return:
        """
        df = pd.read_csv(path_map2d, delim_whitespace=True)
        df_new = pd.DataFrame()
        df_new["X-POS/MM"] = df["X-POS/MM"].apply(lambda x: x / 1000)
        df_new["Y-POS/MM"] = df["Y-POS/MM"].apply(lambda x: x / 1000)
        df_new.to_csv(coordinate_file_path, header=None, index=False)

