from typing import List, Union

from pydantic import BaseModel


############################
# Circuit
class Circuit_Class(BaseModel):
    """
        Level 1: Class for the circuit parameters
    """
    R_circuit: float = None             # R_circuit
    L_circuit: float = None             # Lcir (SIGMA)
    R_parallel: float = None


############################
# Power Supply (aka Power Converter)
class PowerSupply(BaseModel):
    """
        Level 1: Class for the power supply (aka power converter)
    """
    I_initial: float = None          # I00 (LEDET), I_0 (SIGMA), I0 (BBQ)
    t_off: float = None            # t_PC
    t_control_LUT: List[float] = []    # t_PC_LUT
    I_control_LUT: List[float] = []    # I_PC_LUT
    R_crowbar: float = None     # Rcrow (SIGMA), RCrowbar (ProteCCT)
    Ud_crowbar: float = None

############################
# Quench Protection
class EnergyExtraction(BaseModel):
    """
        Level 2: Class for the energy extraction parameters
    """
    t_trigger: float = None                 # tEE (LEDET), tSwitchDelay (ProteCCT)
    R_EE: float = None       # R_EE_triggered
    power_R_EE: float = None  # RDumpPower, variable used to simulate varistors used in an EE system, R_EE(t)=R_EE_triggered*abs(Ia_t)^R_EE_power
    L: float = None
    C: float = None


class QuenchHeater(BaseModel):
    """
        Level 2: Class for the quench heater parameters
    """
    N_strips: int = None                              # nHeaterStrips
    t_trigger: List[float] = []                        # tQH
    U0: List[float] = []
    C: List[float] = []
    R_warm: List[float] = []
    w: List[float] = []                             # In Sigma this
    h: List[float] = []
    s_ins: Union[List[float], List[List[float]]] = []
    type_ins: Union[List[str], List[List[str]]] = []
    s_ins_He: Union[List[float], List[List[float]]] = []
    type_ins_He: Union[List[str], List[List[str]]] = []
    l: List[float] = []
    l_copper: List[float] = []
    l_stainless_steel: List[float] = []
    f_cover: List[float] = []
    iQH_toHalfTurn_From: List[int] = []
    iQH_toHalfTurn_To: List[int] = []
    turns_sides: List[str] = []


class CLIQ_Class(BaseModel):
    """
        Level 2: Class for the CLIQ parameters
    """
    t_trigger: float = None                        # tCLIQ
    current_direction: List[int] = []    # directionCurrentCLIQ
    sym_factor: float = None               # symFactor
    N_units: int = None                          # nCLIQ
    U0: float = None                       # V_cliq_0 (SIGMA)
    C: float = None                        # C_cliq (SIGMA)
    R: float = None                        # Rcapa (LEDET), R_cliq (SIGMA)
    L: float = None                        # L_cliq
    I0: float = None                       # I_cliq_0


class ESC_Class(BaseModel):
    """
        Level 2: Class for the ESC parameters
    """
    t_trigger: List[float] = []
    U0: List[float] = []
    C: List[float] = []
    R_unit: List[float] = []
    R_leads: List[float] = []
    Ud_Diode: List[float] = []


class FQPCs_Class(BaseModel):  # Geometry related fqpls _inputs
    """
        Level 2: Class for the FQPLs parameters for protection
    """
    enabled: List[bool] = None  # list specifying which fqpl is enabled
    names: List[str] = None  # name to use in gmsh and getdp
    fndpls: List[int] = None  # fqpl number of divisions per length
    fwws: List[float] = None  # fqpl wire widths (assuming rectangular) for theta = 0 this is x dimension
    fwhs: List[float] = None  # fqpl wire heights (assuming rectangular) for theta = 0 this is y dimension
    r_ins: List[float] = None  # radiuses for inner diameter for fqpl (radial (or x direction for theta=0) for placing the fqpl
    r_bs: List[float] = None  # radiuses for bending the fqpl by 180 degrees
    n_sbs: List[int] = None  # number of 'bending segmetns' for the 180 degrees turn
    thetas: List[float] = None  # rotation in deg from x+ axis towards y+ axis about z axis.
    z_starts: List[str] = None  # which air boundary to start at. These are string with either: z_min or z_max key from the Air region.
    z_ends: List[float] = None  # z coordinate of loop end
    currents: List[float] = None  # current in the wire
    sigmas: List[float] = None  # electrical conductivity
    mu_rs: List[float] = None  # relative permeability
    th_conns_def: List[List] = None

class QuenchProtection(BaseModel):
    """
        Level 1: Class for quench protection
    """
    Energy_Extraction: EnergyExtraction = EnergyExtraction()
    Quench_Heaters: QuenchHeater = QuenchHeater()
    CLIQ: CLIQ_Class = CLIQ_Class()
    ESC: ESC_Class = ESC_Class()
    FQPCs: FQPCs_Class = FQPCs_Class()