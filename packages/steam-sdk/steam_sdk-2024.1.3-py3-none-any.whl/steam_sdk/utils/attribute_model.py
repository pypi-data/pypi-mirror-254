from typing import Union

from steam_sdk.builders.BuilderModel import BuilderModel
from steam_sdk.utils.rgetattr import rgetattr
from steam_sdk.utils.sgetattr import rsetattr


def get_attribute_model(case_model: str, builder_model: BuilderModel, name_variable: str, idx_conductor: int = None):
    """
    Helper function used to get an attribute from a key of the model data.
    Depending on the model type (circuit, magnet, conductor), the data structure to access is different.
    Also, there is a special case when the variable to read is a sub-key of the Conductors key. In such a case, an additional parameter idx_conductor must be defined (see below).
    :param case_model: Model type
    :param builder_model: BuilderModel object to access
    :param name_variable: Name of the variable to read
    :param idx_conductor: When defined, a sub-key form the Conductors key is read. The index of the conductor to read is defined by idx_conductor
    :return: Value of the variable to get
    """

    if case_model == 'magnet':
        if idx_conductor is None:  # Standard case when the variable to change is not the Conductors key
            value = rgetattr(builder_model.model_data, name_variable)
        else:
            value = rgetattr(builder_model.model_data.Conductors[idx_conductor], name_variable)
    elif case_model == 'conductor':
        if idx_conductor is None:  # Standard case when the variable to change is not the Conductors key
            value = rgetattr(builder_model.conductor_data, name_variable)
        else:
            value = rgetattr(builder_model.conductor_data.Conductors[idx_conductor], name_variable)
    elif case_model == 'circuit':
        value = rgetattr(builder_model.circuit_data, name_variable)
    else:
        raise Exception(f'Model type not supported: case_model={case_model}')
    return value


def set_attribute_model(case_model: str, builder_model: BuilderModel, name_variable: str,
                        value_variable: Union[int, float, str], idx_conductor: int = None):
    """
    Helper function used to set a key of the model data to a certain value.
    Depending on the model type (circuit, magnet, conductor), the data structure to access is different.
    Also, there is a special case when the variable to change is a sub-key of the Conductors key. In such a case, an additional parameter idx_conductor must be defined (see below).
    :param case_model: Model type
    :param builder_model: BuilderModel object to access
    :param name_variable: Name of the variable to change
    :param value_variable: New value of the variable of the variable
    :param idx_conductor: When defined, a sub-key form the Conductors key is read. The index of the conductor to read is defined by idx_conductor
    :return: Value of the variable to get
    """

    if case_model == 'magnet':
        if idx_conductor is None:  # Standard case when the variable to change is not the Conductors key
            rsetattr(builder_model.model_data, name_variable, value_variable)
        else:
            rsetattr(builder_model.model_data.Conductors[idx_conductor], name_variable, value_variable)
    elif case_model == 'conductor':
        if idx_conductor is None:  # Standard case when the variable to change is not the Conductors key
            rsetattr(builder_model.conductor_data, name_variable, value_variable)
        else:
            rsetattr(builder_model.conductor_data.Conductors[idx_conductor], name_variable, value_variable)
    elif case_model == 'circuit':
        rsetattr(builder_model.circuit_data, name_variable, value_variable)
    else:
        raise Exception(f'Model type not supported: case_model={case_model}')