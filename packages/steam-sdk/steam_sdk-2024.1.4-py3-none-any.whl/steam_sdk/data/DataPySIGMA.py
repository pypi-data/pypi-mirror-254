from typing import List, Literal, Union, Dict

from pydantic import BaseModel

from steam_sdk.data.DataPySIGMAOptions import PySIGMAOptions
from steam_pysigma.data.DataRoxieParser import RoxieData


class Sources(BaseModel):
    bh_curve_source: str = None


class GeneralParameters(BaseModel):
    magnet_name: str = None
    T_initial: float = None
    magnetic_length: float = None


class MultipoleRoxieGeometry(BaseModel):
    """
        Class for FiQuS multipole Roxie data (.geom)
    """
    Roxie_Data: RoxieData = RoxieData()


class Jc_FitSIGMA(BaseModel):
    type: str = None
    C1_CUDI1: float = None
    C2_CUDI1: float = None


class StrandSIGMA(BaseModel):
    filament_diameter: float = None
    diameter: float = None
    f_Rho_effective: float = None
    fil_twist_pitch: float = None
    RRR: float = None
    T_ref_RRR_high: float = None
    Cu_noCu_in_strand: float = None


class MultipoleGeneralSetting(BaseModel):
    """
        Class for general information on the case study
    """
    I_ref: List[float] = None


class MultipoleMono(BaseModel):
    """
        Rutherford cable type
    """
    type: Literal['Mono']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None
    th_insulation_along_height: float = None
    th_insulation_along_width: float = None
    Rc: float = None
    Ra: float = None
    bare_cable_height_low: float = None
    bare_cable_height_high: float = None
    n_strands: int = None
    n_strands_per_layers: int = None
    n_strand_layers: int = None
    strand_twist_pitch: float = None
    width_core: float = None
    height_core: float = None
    strand_twist_pitch_angle: float = None
    f_inner_voids: float = None
    f_outer_voids: float = None


class MultipoleRibbon(BaseModel):
    """
        Rutherford cable type
    """
    type: Literal['Ribbon']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None
    th_insulation_along_height: float = None
    th_insulation_along_width: float = None
    Rc: float = None
    Ra: float = None
    bare_cable_height_low: float = None
    bare_cable_height_high: float = None
    n_strands: int = None
    n_strands_per_layers: int = None
    n_strand_layers: int = None
    strand_twist_pitch: float = None
    width_core: float = None
    height_core: float = None
    strand_twist_pitch_angle: float = None
    f_inner_voids: float = None
    f_outer_voids: float = None


class MultipoleRutherford(BaseModel):
    """
        Rutherford cable type
    """
    type: Literal['Rutherford']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None
    th_insulation_along_height: float = None
    th_insulation_along_width: float = None
    Rc: float = None
    Ra: float = None
    bare_cable_height_low: float = None
    bare_cable_height_high: float = None
    n_strands: int = None
    n_strands_per_layers: int = None
    n_strand_layers: int = None
    strand_twist_pitch: float = None
    width_core: float = None
    height_core: float = None
    strand_twist_pitch_angle: float = None
    f_inner_voids: float = None
    f_outer_voids: float = None


class MultipoleConductor(BaseModel):
    """
        Class for conductor type
    """
    cable: Union[MultipoleRutherford, MultipoleRibbon, MultipoleMono] = {'type': 'Rutherford'}
    strand: StrandSIGMA = StrandSIGMA()
    Jc_fit: Jc_FitSIGMA = Jc_FitSIGMA()


class MultipoleModelDataSetting(BaseModel):
    """
        Class for model data
    """
    general_parameters: MultipoleGeneralSetting = MultipoleGeneralSetting()
    conductors: Dict[str, MultipoleConductor] = {}


class MultipoleSettings(BaseModel):
    """
        Class for FiQuS multipole settings (.set)
    """
    Model_Data_GS: MultipoleModelDataSetting = MultipoleModelDataSetting()


class MultipoleConductor(BaseModel):
    """
        Class for conductor type
    """
    cable: Union[MultipoleRutherford, MultipoleRibbon, MultipoleMono] = {'type': 'Rutherford'}
    strand: StrandSIGMA = StrandSIGMA()
    Jc_fit: Jc_FitSIGMA = Jc_FitSIGMA()


class PowerSupply(BaseModel):
    I_initial: float = None


class QuenchHeaters(BaseModel):
    N_strips: int = None
    t_trigger: List[float] = None
    U0: List[float] = None
    C: List[float] = None
    R_warm: List[float] = None
    w: List[float] = None
    h: List[float] = None
    s_ins: List[float] = None
    type_ins: List[float] = None
    s_ins_He: List[float] = None
    type_ins_He: List[float] = None
    l: List[float] = None
    l_copper: List[float] = None
    l_stainless_steel: List[float] = None
    f_cover: List[float] = None


class CLIQ(BaseModel):
    t_trigger: float = None
    sym_factor: int = None
    U0: float = None
    I0: float = None
    C: float = None
    R: float = None
    L: float = None


class Circuit(BaseModel):
    R_circuit: float = None
    L_circuit: float = None
    R_parallel: float = None


class QuenchProtection(BaseModel):
    Quench_Heaters: QuenchHeaters = QuenchHeaters()
    CLIQ: CLIQ = CLIQ()


class DataPySIGMA(BaseModel):
    Sources: Sources = Sources()
    GeneralParameters: GeneralParameters = GeneralParameters()
    Power_Supply: PowerSupply = PowerSupply()
    Circuit: Circuit = Circuit()
    Quench_Protection: QuenchProtection = QuenchProtection()
    Options_SIGMA: PySIGMAOptions = PySIGMAOptions()

