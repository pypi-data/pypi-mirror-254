from pydantic import BaseModel, Field
from typing import (List, Union)

from steam_sdk.data.DataConductor import Conductor
from steam_sdk.data.DataModelCommon import Circuit_Class
from steam_sdk.data.DataModelCommon import PowerSupply
from steam_sdk.data.DataModelCommon import QuenchProtection
from steam_sdk.data.DataFiQuSOptions import FiQuSOptions
from steam_sdk.data.DataPySIGMAOptions import PySIGMAOptions
from steam_sdk.data.DataLEDETOptions import LEDETOptions
from steam_sdk.data.DataProteCCTOptions import PROTECCTOptions


############################
# Source files
class SourceFiles(BaseModel):
    """
        Level 1: Class for the source files
    """
    coil_fromROXIE: str = Field(
        default = None,
        title = 'Name of the file',
        description= '.data file',
    )
    conductor_fromROXIE: str = None  # ROXIE .cadata file
    iron_fromROXIE: str = None    # ROXIE .iron file
    BH_fromROXIE: str = None      # ROXIE .bhdata file (BH-curves)
    magnetic_field_fromROXIE: str = None # ROXIE .map2d file
    sm_inductance: str = None


############################
# General parameters
class Model(BaseModel):
    """
        Level 2: Class for information on the model
    """
    name: str = None  # magnetIdentifier (ProteCCT)
    version: str = None
    case: str = None
    state: str = None


class General(BaseModel):
    """
        Level 1: Class for general information on the case study
    """
    magnet_name: str = None
    circuit_name: str = None
    model: Model = Model()
    magnet_type: str = None
    T_initial: float = None               # T00 (LEDET), Top (SIGMA)
    magnetic_length: float = None   # l_magnet (LEDET), magLength (SIGMA), magneticLength (ProteCCT)


############################
# Coil Windings
class CoilWindingsElectricalOrder(BaseModel):
    """
        Level 2: Class for the order of the electrical pairs
    """
    group_together: List[List[int]] = []   # elPairs_GroupTogether
    reversed: List[int] = []         # elPairs_RevElOrder
    overwrite_electrical_order: List[int] = []


class MultipoleWedge(BaseModel):
    """
        Level 3: Class for multi-pole coil data
    """
    material: str = None
    RRR: float = None
    T_ref_RRR_high: float = None


class CoilWindingsMultipole(BaseModel):
    """
        Level 2: Class for multi-pole coil data
    """
    wedges: MultipoleWedge = MultipoleWedge()


class SolenoidCoil(BaseModel):
    """
        Level 3: Class for Solenoid windings
    """
    name: str = None            # -             solenoid name
    a1: float = None            # m             smaller radial dimension of solenoid
    a2: float = None            # m             larger radial dimension of solenoid
    b1: float = None            # m             smaller axial dimension of solenoid
    b2: float = None            # m             larger axial dimension of solenoid
    conductor_name: str = None  # -             wire name - name must correspond to existing conductor name in the same yaml file
    ntpl: int = None            # -             number of turns per layer
    nl: int = None              # -             number of layers
    pre_preg: float = None     # m              Pre-preg thicknes (radial) i.e. in LEDET in width direction
    section: int = None         # Section in ledet for the block

class CoilWindingsSolenoid(BaseModel):
    """
        Level 2: Class for Solenoid windings
    """
    coils: List[SolenoidCoil] = [SolenoidCoil()]

class CoilWindingsPancake(BaseModel):
    """
        Level 2: Class for Pancake windings
    """
    tbc: str = None

class CoilWindingsCCT_straight(BaseModel):
    """
        Level 2: Class for straight CCT windings
    """
    winding_order: List[int] = None
    winding_numberTurnsFormers: List[int] = None            # total number of channel turns, ProteCCT: numTurnsPerStrandTotal, FiQuS: n_turnss
    winding_numRowStrands: List[int] = None                 # number of rows of strands in channel, ProteCCT: numRowStrands, FiQuS: windings_wwns
    winding_numColumnStrands: List[int] = None              # number of columns of strands in channel, ProteCCT: numColumnStrands, FiQuS: windings_whns
    winding_chws: List[float] = None                          # width of winding slots, ProteCTT: used to calc. wStrandSlot=winding_chws/numRowStrands, FiQuS: wwws
    winding_chhs: List[float] = None                          # width of winding slots, ProteCTT: used to calc. wStrandSlot=winding_chhs/numColumnStrands, FiQuS: wwhs
    former_inner_radiuses: List[float] = []                  # innerRadiusFormers (ProteCCT)
    former_outer_radiuses: List[float] = []                  # innerRadiusFormers (ProteCCT)
    former_RRRs: List[float] = []                   # RRRFormer (ProteCCT)
    #former_thickness_underneath_coil: float = None          # formerThicknessUnderneathCoil. Thickness of the former underneath the slot holding the strands in [m] (ProteCCT)
    cylinder_inner_radiuses: List[float] = []              # innerRadiusOuterCylinder (ProteCCT)
    cylinder_outer_radiuses: List[float] = []                  # ProteCCT: thicknessOuterCylinder = cylinder_outer_radiuses - cylinder_inner_radiuses
    cylinder_RRRs: List[float] = []                         # ProteCCT: RRROuterCylinder


class CoilWindingsCCT_curved(BaseModel):
    """
        Level 2: Class for curved CCT windings
    """
    tbc: str = None


class Coil_Windings(BaseModel):
    """
        Level 1: Class for winding information
    """
    conductor_to_group: List[int] = []  # This key assigns to each group a conductor of one of the types defined with Conductor.name
    group_to_coil_section: List[int] = []  # This key assigns groups of half-turns to coil sections
    polarities_in_group: List[int] = []  # This key assigns the polarity of the current in each group # TODO: Consider if it is convenient to remove this (and check DictionaryLEDET when you do)
    n_half_turn_in_group: List[int] = []
    half_turn_length: List[float] = []
    electrical_pairs: CoilWindingsElectricalOrder = CoilWindingsElectricalOrder()  # Variables used to calculate half-turn electrical order
    multipole: CoilWindingsMultipole = CoilWindingsMultipole()
    pancake: CoilWindingsPancake = CoilWindingsPancake()
    solenoid: CoilWindingsSolenoid = CoilWindingsSolenoid()
    CCT_straight: CoilWindingsCCT_straight = CoilWindingsCCT_straight()
    CCT_curved: CoilWindingsCCT_curved = CoilWindingsCCT_curved()


############################
# Highest level
class DataModelMagnet(BaseModel):
    """
        **Class for the STEAM inputs**

        This class contains the data structure of STEAM model inputs.

        :return: DataModelMagnet object
    """

    Sources: SourceFiles = SourceFiles()
    GeneralParameters: General = General()
    CoilWindings: Coil_Windings = Coil_Windings()
    Conductors: List[Conductor] = [Conductor(cable={'type': 'Rutherford'}, strand={'type': 'Round'}, Jc_fit={'type': 'CUDI1'})]
    Circuit: Circuit_Class = Circuit_Class()
    Power_Supply: PowerSupply = PowerSupply()
    Quench_Protection: QuenchProtection = QuenchProtection()
    Options_FiQuS: FiQuSOptions = FiQuSOptions()
    Options_LEDET: LEDETOptions = LEDETOptions()
    Options_ProteCCT: PROTECCTOptions = PROTECCTOptions()
    Options_SIGMA: PySIGMAOptions = PySIGMAOptions()
