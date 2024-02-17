from pydantic import BaseModel
from typing import (List, Union)

############################
# ProteCCT options
class TimeVectorProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT time vector options
    """
    tMaxStopCondition: float = None
    minTimeStep: float = None


class GeometryGenerationOptionsProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT geometry generation options
    """
    totalConductorLength: float = None
    #numTurnsPerStrandTotal: int = None
    thFormerInsul: float = None
    #wStrandSlot: float = None
    #numRowStrands: int = None
    #numColumnStrands: int = None
    IcFactor: float = None
    polyimideToEpoxyRatio: float = None



class PhysicsProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT physics options
    """
    M: List[List[float]] = [[]]
    BMaxAtNominal: float = None
    BMinAtNominal: float = None
    INominal: float = None
    fieldPeriodicity: float = None
    #RRRFormer: float = None
    #RRROuterCylinder: float = None
    coolingToHeliumBath: int = None
    fLoopLength: float = None
    addedHeCpFrac: float = None
    addedHeCoolingFrac: float = None


class SimulationProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT physics options
    """
    tempMaxStopCondition: float = None
    IOpFractionStopCondition: float = None
    fracCurrentChangeMax: float = None
    resultsAtTimeStep: float = None
    deltaTMaxAllowed: float = None
    turnLengthElements: int = None
    externalWaveform: int = None
    saveStateAtEnd: int = None
    restoreStateAtStart: int = None
    silentRun: int = None


class PlotsProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT plots options
    """
    withPlots: int = None
    plotPauseTime: float = None


class PostProcessingProteCCT(BaseModel):
    """
        Level 2: Class for ProteCCT post-processing options
    """
    withVoltageEvaluation: int = None
    voltageToGroundOutputSelection: str = None  # Note: it will be written in a single cell in the ProteCCT file


class PROTECCTOptions(BaseModel):
    """
        Level 1: Class for ProteCCT options
    """
    time_vector: TimeVectorProteCCT = TimeVectorProteCCT()
    geometry_generation_options: GeometryGenerationOptionsProteCCT = GeometryGenerationOptionsProteCCT()
    simulation: SimulationProteCCT = SimulationProteCCT()
    physics: PhysicsProteCCT = PhysicsProteCCT()
    post_processing: PostProcessingProteCCT = PostProcessingProteCCT()
    plots: PlotsProteCCT = PlotsProteCCT()
