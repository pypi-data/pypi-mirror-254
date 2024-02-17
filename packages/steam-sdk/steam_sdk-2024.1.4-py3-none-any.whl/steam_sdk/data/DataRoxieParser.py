from pydantic import BaseModel, PrivateAttr, Field
from typing import (Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union, Type)


class Coord(BaseModel):
    """
        Class for coordinates
    """
    x: float = None
    y: float = None
    z: float = None


class Roll(BaseModel):
    """
        Class for roll2 transformation
    """
    coor: Coord = Coord()
    alph: float = None


class HyperHole(BaseModel):
    """
        Class for hyper holes
    """
    areas: List[str] = []


class HyperArea(BaseModel):
    """
        Class for hyper areas
    """
    material: str = None
    lines: List[str] = []


class HyperLine(BaseModel):
    """
        Class for hyper lines: lines, arcs, elliptic arcs, circles
    """
    type: str = None
    kp1: str = None
    kp2: str = None
    kp3: str = None
    arg1: float = None
    arg2: float = None
    elements: int = None


class CondPar(BaseModel):
    """
        Class for conductor parameters
    """
    wInsulNarrow: float = None
    wInsulWide: float = None
    dFilament: float = None
    dstrand: float = None
    fracCu: float = None
    fracSc: float = None
    RRR: float = None
    TupRRR: float = None
    Top: float = None
    Rc: float = None
    Ra: float = None
    fRhoEff: float = None
    lTp: float = None
    wBare: float = None
    hInBare: float = None
    hOutBare: float = None
    noOfStrands: int = None
    noOfStrandsPerLayer: int = None
    noOfLayers: int = None
    lTpStrand: float = None
    wCore: float = None
    hCore: float = None
    thetaTpStrand: float = None
    degradation: float = None
    C1: float = None
    C2: float = None
    fracHe: float = None
    fracFillInnerVoids: float = None
    fracFillOuterVoids: float = None


class Conductor(BaseModel):
    """
        Class for conductor type
    """
    conductorType: int = None
    cableGeom: str = None
    strand: str = None
    filament: str = None
    insul: str = None
    trans: str = None
    quenchMat: str = None
    T_0: float = None
    comment: str = None
    parameters: CondPar = CondPar()


class Cable(BaseModel):
    """
        Class for cable parameters
    """
    height: float = None
    width_i: float = None
    width_o: float = None
    ns: int = None
    transp: float = None
    degrd: float = None
    comment: str = None


class Quench(BaseModel):
    """
        Class for quench parameters
    """
    SCHeatCapa: int = None
    CuHeatCapa: int = None
    CuThermCond: int = None
    CuElecRes: int = None
    InsHeatCapa: int = None
    InsThermCond: int = None
    FillHeatCapa: int = None
    He: int = None
    comment: str = None


class Transient(BaseModel):
    """
        Class for transient parameters
    """
    Rc: float = None
    Ra: float = None
    filTwistp: float = None
    filR0: float = None
    fil_dRdB: float = None
    strandfillFac: float = None
    comment: str = None


class Strand(BaseModel):
    """
        Class for strand parameters
    """
    diam: float = None
    cu_sc: float = None
    RRR: float = None
    Tref: float = None
    Bref: float = None
    Jc_BrTr: float = None
    dJc_dB: float = None
    comment: str = None


class Filament(BaseModel):
    """
        Class for filament parameters
    """
    fildiao: float = None
    fildiai: float = None
    Jc_fit: str = None
    fit: str = None
    comment: str = None


class Insulation(BaseModel):
    """
        Class for insulation parameters
    """
    radial: float = None
    azimut: float = None
    comment: str = None

class RemFit(BaseModel):
    """
        Class for REMFIT parameters (not used in STEAM, but still parsed)
    """
    type: int = None
    C1: float = None
    C2: float = None
    C3: float = None
    C4: float = None
    C5: float = None
    C6: float = None
    C7: float = None
    C8: float = None
    C9: float = None
    C10: float = None
    C11: float = None
    comment: str = None


class Block(BaseModel):
    """
        Class for block list
    """
    type: int = None
    nco: int = None
    radius: float = None
    phi: float = None
    alpha: float = None
    current: float = None
    condname: str = None
    n1: int = None
    n2: int = None
    imag: int = None
    turn: float = None
    coil: int = None
    pole: int = None
    layer: int = None
    winding: int = None
    shift2: Coord = Coord()
    roll2: Roll = Roll()


class Group(BaseModel):
    """
        Class for group list
    """
    symm: int = None
    typexy: int = None
    blocks: List[int] = []  # map


class Trans(BaseModel):
    """
        Class for transformation list
    """
    x: float = None
    y: float = None
    alph: float = None
    bet: float = None
    string: str = None
    act: int = None
    bcs: List[int] = []  # map


class Iron(BaseModel):
    """
        Class for the iron yoke data
    """
    key_points: Dict[str, Coord] = {}
    hyper_lines: Dict[str, HyperLine] = {}
    hyper_areas: Dict[str, HyperArea] = {}
    hyper_holes: Dict[int, HyperHole] = {}


class Cadata(BaseModel):
    """
        Class for the conductor data
    """
    insul: Dict[str, Insulation] = {}
    remfit: Dict[str, RemFit] = {}
    filament: Dict[str, Filament] = {}
    strand: Dict[str, Strand] = {}
    transient: Dict[str, Transient] = {}
    quench: Dict[str, Quench] = {}
    cable: Dict[str, Cable] = {}
    conductor: Dict[str, Conductor] = {}


class Coil(BaseModel):
    """
        Class for the coil data
    """
    blocks: Dict[str, Block] = {}
    groups: Dict[str, Group] = {}
    transs: Dict[str, Trans] = {}


class StrandGroup(BaseModel):
    """
        Class for strand group
    """
    strand_positions: Dict[int, Coord] = {}


class Corner(BaseModel):
    """
        Class for corner positions
    """
    iH: Coord = Coord()  # inner left
    iL: Coord = Coord()  # inner right
    oH: Coord = Coord()  # outer left
    oL: Coord = Coord()  # outer right


class HalfTurnCorner(BaseModel):
    """
        Class for corner type
    """
    insulated: Corner = Corner()
    bare: Corner = Corner()


class HalfTurn(BaseModel):
    """
        Class for half-turn data
    """
    corners: HalfTurnCorner = HalfTurnCorner()
    strand_groups: Dict[int, StrandGroup] = {}


class Order(BaseModel):
    """
        Class for electrical order (block location)
    """
    coil: int = None
    pole: int = None
    layer: int = None
    winding: int = None
    block: int = None


class CenterShift(BaseModel):
    """
        Class for bore center shift
    """
    inner: Coord = Coord()
    outer: Coord = Coord()


class Wedge(BaseModel):
    """
        Class for wedge positions
    """
    corners: Corner = Corner()
    corners_ins: Corner = Corner()
    corrected_center: CenterShift = CenterShift()
    corrected_center_ins: CenterShift = CenterShift()
    order_l: Order = Order()
    order_h: Order = Order()


class BlockData(BaseModel):
    """
        Class for block data
    """
    block_corners: Corner = Corner()
    block_corners_ins: Corner = Corner()
    current_sign: int = None
    half_turns: Dict[int, HalfTurn] = {}


class WindingData(BaseModel):
    """
        Class for winding data
    """
    blocks: Dict[int, BlockData] = {}
    conductor_name: str = None
    conductors_number: int = None


class Winding(BaseModel):
    """
        Class for windings
    """
    windings: Dict[int, WindingData] = {}


class Layer(BaseModel):
    """
        Class for winding layers
    """
    layers: Dict[int, Winding] = {}


class Pole(BaseModel):
    """
        Class for poles
    """
    type: str = None
    poles: Dict[int, Layer] = {}
    bore_center: Coord = Coord()


class CoilData(BaseModel):
    """
        Class for coils
    """
    coils: Dict[int, Pole] = {}
    physical_order: List[Order] = []


class RoxieRawData(BaseModel):
    """
        Class for the raw data
    """
    cadata: Cadata = Cadata()
    coil: Coil = Coil()


class RoxieData(BaseModel):
    """
        Class for the roxie parser
    """
    iron: Iron = Iron()
    coil: CoilData = CoilData()
    wedges: Dict[int, Wedge] = {}
