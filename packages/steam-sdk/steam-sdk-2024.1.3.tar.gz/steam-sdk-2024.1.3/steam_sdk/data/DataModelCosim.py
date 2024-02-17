from typing import (List, Union, Dict, Literal, Optional)

from pydantic import BaseModel, Field, Extra


############################
# General parameters
class Model(BaseModel):
    """
        Level 2: Class for information on the model
    """
    name: str = None
    version: str = None
    case: str = None
    state: str = None

class General(BaseModel):
    """
        Level 1: Class for general information on the case study
    """
    cosim_name: str = None
    model: Model = Model()
    simulation_number: int = None  # TODO consider whether str should be allowed as well


############################
# Co-simulation folders
class CosimulationFolders(BaseModel):
    """
        Level 1: Class for co-simulation folders
    """
    local_COSIM_folder: str = None
    path_model_folder: str = None  # TODO: maybe this key should be deleted, since each model could be read from different libraries for different models, see key "modelFolder"


############################
# Simulation configurations - one for simulation tool

class ParametersToModify(BaseModel):
    """
        Level 2: Class to define parameters to modify
    """
    variables_to_change: List[str] = []
    variables_values: List[List[float]] = []

class sim_FiQuS(BaseModel): # TODO add/edit keys
    """
        Level 1: Class of FiQuS simulation configuration
    """
    type: Literal['FiQuS']
    solverPath: str = None
    modelFolder: str = None  # TODO: is this needed?
    modelName: str = None
    modelCase: str = None
    modelSet: int = None
    simulationNumber: int = None  # TODO consider whether str should be allowed as well
    variables_to_modify: ParametersToModify = ParametersToModify()

class sim_LEDET(BaseModel):
    """
        Level 1: Class of LEDET simulation configuration
    """
    type: Literal['LEDET']
    solverPath: str = None
    modelFolder: str = None  # TODO: is this needed?
    modelName: str = None
    modelCase: str = None
    modelSet: int = None
    simulationNumber: int = None  # TODO consider whether str should be allowed as well
    variables_to_modify: ParametersToModify = ParametersToModify()

class sim_PSPICE(BaseModel):
    """
        Level 1: Class of PSPICE simulation configuration
    """
    type: Literal['PSPICE']
    solverPath: str = None
    modelFolder: str = None  # TODO: is this needed?
    modelCase: str = None
    modelName: str = None
    modelSet: int = None
    configurationFileName: str = None
    externalStimulusFileName: str = None
    initialConditions: Dict[str, Union[float, int]] = {}
    skipBiasPointCalculation: bool = None
    variables_to_modify: ParametersToModify = ParametersToModify()

class sim_XYCE(BaseModel):
    """
        Level 1: Class of XYCE simulation configuration
    """
    type: Literal['XYCE']
    solverPath: str = None
    modelFolder: str = None  # TODO: is this needed?
    modelCase: str = None
    modelName: str = None
    modelSet: int = None
    configurationFileName: str = None
    externalStimulusFileName: str = None
    initialConditions: Dict[str, Union[float, int]] = {}
    skipBiasPointCalculation: bool = None
    variables_to_modify: ParametersToModify = ParametersToModify()

############################
# Co-simulation port
# class CosimPortModel(BaseModel):
#     input_model: str = None
#     input_variable_component: str = None
#     input_variable_name: str = None
#     input_variable_coupling_parameter: str = None
#     input_variable_type: str = None
#     output_model: str = None
#     output_variable_component: str = None
#     output_variable_name: str = None
#     output_variable_coupling_parameter: str = None
#     output_variable_type: str = None

class CosimPortVariable(BaseModel):
    variable_names: List[str] = []
    variable_coupling_parameter: str = None
    variable_types: List[str] = []

class CosimPortModel(BaseModel):
    components: List[str] = []
    inputs: Dict[str, CosimPortVariable] = {}
    outputs: Dict[str, CosimPortVariable] = {}

class CosimPort(BaseModel):
    """
    Class for co-simulation port to be used within PortDefinition
    """
    Models: Dict[str, CosimPortModel] = {}


############################
# Co-simulation settings
class Convergence(BaseModel):
    """
        Level 2: Class for convergence options
    """
    convergenceVariables: Dict[str, Union[str, None]] = {}
    relTolerance: Dict[str, Union[float, int, None]] = {}
    absTolerance: Dict[str, Union[float, int, None]] = {}

class Time_Windows(BaseModel):
    """
        Level 2: Class for time window options
    """
    t_0: List[Union[float, int]] = []
    t_end: List[Union[float, int]] = []
    t_step_max: Dict[str, List[Union[float, int]]] = {}

class Options_run(BaseModel):
    """
        Level 2: Class for co-simulation run options
    """
    executionOrder: List[int] = []
    executeCleanRun: List[bool] = []

class CosimulationSettings(BaseModel):
    """
        Level 1: Class for co-simulation settings
    """
    Convergence: Convergence = Convergence()
    Time_Windows: Time_Windows = Time_Windows()
    Options_run: Options_run = Options_run()

class CosimulationSettings(BaseModel):
    """
        Level 1: Class for co-simulation settings
    """
    Convergence: Convergence = Convergence()
    Time_Windows: Time_Windows = Time_Windows()
    Options_run: Options_run = Options_run()


############################
# COSIM options
class Options_COSIM(BaseModel):
    """
        Level 1: Class for co-simulation settings
    """
    pass


############################
# pyCOSIM options
class Options_PyCOSIM(BaseModel):
    """
        Level 1: Class for co-simulation settings
    """
    pass




############################
# Highest level
class DataModelCosim(BaseModel):
    """
        **Class for the STEAM inputs**

        This class contains the data structure of STEAM model inputs for cooperative simulations (co-simulations).

        :return: DataCosim object
    """

    GeneralParameters: General = General()
    Folders: CosimulationFolders = CosimulationFolders()
    Simulations: Dict[str, Union[sim_FiQuS, sim_LEDET, sim_PSPICE, sim_XYCE]] = {}
    # ModifyParameters: Dict[str, ?]: {}  #TODO
    PortDefinition: Dict[str, CosimPort] = {}
    Settings: CosimulationSettings = CosimulationSettings()
    Options_COSIM: Options_COSIM = Options_COSIM()
    Options_PyCOSIM: Options_PyCOSIM = Options_PyCOSIM()