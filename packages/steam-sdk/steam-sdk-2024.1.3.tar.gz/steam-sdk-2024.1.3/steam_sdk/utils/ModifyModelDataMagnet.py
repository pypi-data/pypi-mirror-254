import os
from pathlib import Path
import yaml
from steam_sdk.data.DataModelMagnet import DataModelMagnet
from steam_sdk.parsers.ParserYAML import model_data_to_yaml

if __name__ == "__main__":  # pragma: no cover
    # path_to_models = Path.joinpath(
    #     Path(__file__).parent.parent.parent,
    #     "C:\\Users\emm\cernbox\SWAN_projects\steam_models\magnets",
    # )
    path_to_models = Path.joinpath(
        Path(__file__).parent.parent.parent, r"E:\Python\steam_models\magnets")

    # path_to_models = Path.joinpath(
    #     Path(__file__).parent.parent.parent, "tests/builders/model_library/magnets"
    # )
    model_names = [x.parts[-1] for x in Path(path_to_models).iterdir() if x.is_dir()]
    #model_names = ['MCBRD']

    for model_name in model_names:
        # Read the file:
        yaml_file = Path.joinpath(
            path_to_models, model_name, "input", "modelData_" + model_name + ".yaml"
        )
        if os.path.isfile(yaml_file):
            # Read the yaml file and store the date inside ruamel_yaml_object:
            with open(yaml_file, "r") as stream:
                ruamel_yaml_object = yaml.safe_load(stream)

            print(f"The file has been read: {yaml_file}")

            # Create a DataModelMagnet object from the yaml file's data:
            # Note: Obsolete keys (the keys that are not in DataModelMagnet) will
            # automatically be deleted. Moreover, if new keys are added to
            # DataModelMagnet, they will be added to the YAML file. The new key's values
            # will be DataModelMagnet's default values.
            # del ruamel_yaml_object["Options_FiQuS"]["Pancake3D"]
            model_data = DataModelMagnet(**ruamel_yaml_object)

            # Some values of the new and old keys can be changed like this:
            # model_data.Options_LEDET.magnet_inductance.flag_calculate_inductance = True

            # Old values of obsolete keys can be moved to new keys like this:
            # model_data.Options_LEDET.conductor_geometry_used_for_ISCL.mirrorY_ht = (
            #     ruamel_yaml_object["CoilWindings"]["multipole"]["mirrorY_ht"]
            # )

            # Set to True if you wish to test the results of this script, and False if
            # you wish to really update all yaml input files
            test = False
            if test:
                yaml_file_output = Path.joinpath(
                    path_to_models,
                    model_name,
                    "input",
                    "modelData_" + model_name + "_MODIFIED.yaml",
                )
            else:
                yaml_file_output = yaml_file

            addDescriptionAsComments = True
            keysAsPydanticAliases = True
            model_data_to_yaml(
                model_data,
                yaml_file_output,
                list_exceptions=["Conductors"],
                with_comments=addDescriptionAsComments,
                by_alias=keysAsPydanticAliases,
            )
            print(f"The file has been written: {yaml_file_output}")
        else:
            print(f"WARNING: {yaml_file} is not found.")
