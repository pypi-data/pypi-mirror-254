from pydantic import BaseModel, create_model
from typing import Any, Dict, List, Optional


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
    circuit_name: str = None
    model: Model = Model()
    additional_files: List[str] = []  # These files will be physically copied to the output folder


############################
# Auxiliary files
class Auxiliary_Files(BaseModel):
    """
        Level 1: Class for general information on the case study
        Note: These entries will be written in the netlist, but no further action will be taken (see General.additional_files)
    """
    files_to_include: List[str] = []

############################
# Stimuli
class Stimuli(BaseModel):
    """
        Level 1: Stimulus files
    """
    stimulus_files: List[str] = []


############################
# Libraries
class Libraries(BaseModel):
    """
        Level 1: Component_OLD libraries
    """
    component_libraries: List[str] = []


############################
# Global parameters
class Global_Parameters(BaseModel):
    """
        Level 1: Global circuit parameters
    """
    global_parameters: dict = None

############################
# Initial conditions
class InitialConditions(BaseModel):
    """
        Level 1: Initial conditions parameters
    """
    initial_conditions: dict = None


############################
# Netlist, defined as a list of Component_OLD objects
class Netlist(BaseModel):
    """
        Level 1: Netlist
    """
    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)

class Component(BaseModel):
    """
        Level 2: Circuit component
    """
    type: str = None
    nodes: List[str] = []
    value: str = None
    parameters: Optional[dict] = dict()

############################
# Simulation options
class Options(BaseModel):
    """
        Level 1: Simulation options
    """
    options_simulation: dict = None
    options_autoconverge: dict = None
    flag_inCOSIM: bool = None


############################
# Analysis settings
class SimulationTime(BaseModel):
    """
        Level 2: Simulation time settings
    """
    time_start: float = None
    time_end:   float = None
    min_time_step: float = None
    time_schedule: dict = None

class SimulationFrequency(BaseModel):
    """
        Level 2: Simulation frequency settings
    """
    frequency_step: str = None
    frequency_points:   float = None
    frequency_start: str = None
    frequency_end: str = None

class Analysis(BaseModel):
    """
        Level 1: Analysis settings
    """
    analysis_type: str = None
    simulation_time: Optional[SimulationTime] = SimulationTime()
    simulation_frequency: Optional[SimulationFrequency] = SimulationFrequency()

############################
# Post-processing settings
class Settings_Probe(BaseModel):
    """
        Level 2: Probe settings
    """
    probe_type: str = None
    variables: List[str] = []

class PostProcess(BaseModel):
    """
        Level 1: Post-processing settings
    """
    probe: Settings_Probe = Settings_Probe()


############################
# Highest level
class DataModelCircuit(BaseModel):
    '''
        **Class for the circuit netlist inputs**

        This class contains the data structure of circuit netlist model inputs.

        :param N: test 1
        :type N: int
        :param n: test 2
        :type n: int

        :return: DataModelCircuit object
    '''

    GeneralParameters: General = General()
    AuxiliaryFiles: Auxiliary_Files = Auxiliary_Files()
    Stimuli: Stimuli = Stimuli()
    Libraries: Libraries = Libraries()
    GlobalParameters: Global_Parameters = Global_Parameters()
    InitialConditions: InitialConditions = InitialConditions()
    Netlist: Netlist = Netlist()
    Options: Options = Options()
    Analysis: Analysis = Analysis()
    PostProcess: PostProcess = PostProcess()
