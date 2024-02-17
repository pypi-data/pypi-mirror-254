from pydantic import BaseModel

class GeometryBBQ(BaseModel):
    """
        Level 2: Class for geometry options in BBQ
    """
    thInsul: float = None
    lenBusbar: float = None


class SimulationBBQ(BaseModel):
    """
        Level 2: Class for simulation options in BBQ
    """
    meshSize: float = None


class PhysicsBBQ(BaseModel):
    """
        Level 2: Class for physics options in BBQ
    """
    adiabaticZoneLength: float = None
    aFilmBoilingHeliumII: float = None
    aKap: float = None
    BBackground: float = None
    BPerI: float = None
    IDesign: float = None
    jointLength: float = None
    jointResistancePerMeter: float = None
    muTInit: float = None
    nKap: float = None
    QKapLimit: float = None
    Rjoint: float = None
    symmetryFactor: float = None
    tauDecay: float = None
    TInitMax: float = None
    TInitOp: float = None
    TLimit: float = None
    tValidation: float = None
    TVQRef: float = None
    VThreshold: float = None
    withCoolingToBath: float = None


class QuenchInitializationBBQ(BaseModel):
    """
        Level 2: Class for quench initialization parameters in BBQ
    """
    sigmaTInit: float = None

