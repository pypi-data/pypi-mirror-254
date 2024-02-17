from pydantic import BaseModel
from typing import (List, Union)

class TimeVectorLEDET(BaseModel):
    """
        Level 2: Class for simulation time vector in LEDET
    """
    time_vector_params: List[float] = []


class MagnetInductance(BaseModel):
    """
        Level 2: Class for magnet inductance assignment
    """
    flag_calculate_inductance: bool = None
    overwrite_inductance_coil_sections: List[List[float]] = [[]]
    overwrite_HalfTurnToInductanceBlock: List[int] = []
    LUT_DifferentialInductance_current: List[float] = []
    LUT_DifferentialInductance_inductance: List[float] = []


class HeatExchange(BaseModel):
    """
        Level 2: Class for heat exchange information
    """
    heat_exchange_max_distance: float = None  # heat exchange max_distance
    iContactAlongWidth_pairs_to_add: List[List[int]] = [[]]
    iContactAlongWidth_pairs_to_remove: List[List[int]] = [[]]
    iContactAlongHeight_pairs_to_add: List[List[int]] = [[]]
    iContactAlongHeight_pairs_to_remove: List[List[int]] = [[]]
    th_insulationBetweenLayers: float = None


class ConductorGeometry(BaseModel):
    """
        Level 2: Class for multipole geometry parameters - ONLY USED FOR ISCC/ISCL CALCULATION
    """
    alphaDEG_ht: List[float] = []  # Inclination angle of each half-turn, alphaDEG (LEDET)
    rotation_ht: List[float] = []  # Rotation of each half-turn, rotation_block (LEDET)
    mirror_ht: List[int]   = []  # Mirror around quadrant bisector line for half-turn, mirror_block (LEDET)
    mirrorY_ht: List[int]  = []  # Mirror around Y axis for half-turn, mirrorY_block (LEDET)


class FieldMapFilesLEDET(BaseModel):
    """
        Level 2: Class for field map file parameters in LEDET
    """
    Iref: float = None
    flagIron: int = None
    flagSelfField: int = None
    headerLines: int = None
    columnsXY: List[int] = []
    columnsBxBy: List[int] = []
    flagPlotMTF: int = None
    fieldMapNumber: int = None
    flag_modify_map2d_ribbon_cable: int = None
    flag_calculateMagneticField: int = None


class InputGenerationOptionsLEDET(BaseModel):
    """
        Level 2: Class for input generation options in LEDET
    """
    # flag_typeWindings: int = None
    flag_calculateInductanceMatrix: int = None
    flag_useExternalInitialization: int = None
    flag_initializeVar: int = None
    selfMutualInductanceFileNumber: int = None


class SimulationLEDET(BaseModel):
    """
        Level 2: Class for simulation options in LEDET
    """
    flag_fastMode: int = None
    flag_controlCurrent: int = None
    flag_controlInductiveVoltages: int = None
    flag_controlMagneticField: int = None
    flag_controlBoundaryTemperatures: int = None
    flag_automaticRefinedTimeStepping: int = None


class PhysicsLEDET(BaseModel):
    """
        Level 2: Class for physics options in LEDET
    """
    flag_IronSaturation: int = None
    flag_InvertCurrentsAndFields: int = None
    flag_ScaleDownSuperposedMagneticField: int = None
    flag_HeCooling: int = None
    fScaling_Pex: float = None
    fScaling_Pex_AlongHeight: float = None
    flag_disableHeatExchangeBetweenCoilSections: int = None
    fScaling_MR: float = None
    flag_scaleCoilResistance_StrandTwistPitch: int = None
    flag_separateInsulationHeatCapacity: int = None
    flag_persistentCurrents: int = None
    flag_ISCL: int = None
    fScaling_Mif: float = None
    fScaling_Mis: float = None
    flag_StopIFCCsAfterQuench: int = None
    flag_StopISCCsAfterQuench: int = None
    tau_increaseRif: float = None
    tau_increaseRis: float = None
    fScaling_RhoSS: float = None
    maxVoltagePC: float = None
    minCurrentDiode: float = None
    flag_symmetricGroundingEE: int = None
    flag_removeUc: int = None
    BtX_background: float = None
    BtY_background: float = None


class MatProLEDET(BaseModel):
    STEAM_material_properties_set: Union[int, str] = None


class QuenchInitializationLEDET(BaseModel):
    """
        Level 2: Class for quench initialization parameters in LEDET
    """
    iStartQuench: List[int] = []
    tStartQuench: List[float] = []
    lengthHotSpot_iStartQuench: List[float] = []
    fScaling_vQ_iStartQuench: List[float] = []


class PostProcessingLEDET(BaseModel):
    """
        Level 2: Class for post processing options in LEDET
    """
    flag_showFigures: int = None
    flag_saveFigures: int = None
    flag_saveMatFile: int = None
    flag_saveTxtFiles: int = None
    flag_generateReport: int = None
    flag_saveResultsToMesh: int = None
    tQuench: List[float] = []
    initialQuenchTemp: List[float] = []
    flag_hotSpotTemperatureInEachGroup: int = None
    flag_importFieldWhenCalculatingHotSpotT: int = None


class Simulation3DLEDET(BaseModel):
    """
        Level 2: Class for 3D simulation parameters and options in lEDET
    """
    # Variables in the "Options" sheet
    flag_3D: int = None
    flag_adaptiveTimeStepping: int = None
    sim3D_flag_Import3DGeometry: int = None
    sim3D_import3DGeometry_modelNumber: int = None

    # Variables in the "Inputs" sheet
    sim3D_uThreshold: float = None
    sim3D_f_cooling_down: Union[float, List[float]] = None
    sim3D_f_cooling_up: Union[float, List[float]] = None
    sim3D_f_cooling_left: Union[float, List[float]] = None
    sim3D_f_cooling_right: Union[float, List[float]] = None
    sim3D_f_cooling_LeadEnds: List[int] = []
    sim3D_fExToIns: float = None
    sim3D_fExUD: float = None
    sim3D_fExLR: float = None
    sim3D_min_ds_coarse: float = None
    sim3D_min_ds_fine: float = None
    sim3D_min_nodesPerStraightPart: int = None
    sim3D_min_nodesPerEndsPart: int = None
    sim3D_idxFinerMeshHalfTurn: List[int] = []
    sim3D_flag_checkNodeProximity: int = None
    sim3D_nodeProximityThreshold: float = None
    sim3D_Tpulse_sPosition: float = None
    sim3D_Tpulse_peakT: float = None
    sim3D_Tpulse_width: float = None
    sim3D_tShortCircuit: float = None
    sim3D_coilSectionsShortCircuit: List[int] = []
    sim3D_R_shortCircuit: float = None
    sim3D_shortCircuitPosition: Union[float, List[List[float]]] = None
    sim3D_durationGIF: float = None
    sim3D_flag_saveFigures: int = None
    sim3D_flag_saveGIF: int = None
    sim3D_flag_VisualizeGeometry3D: int = None
    sim3D_flag_SaveGeometry3D: int = None


class PlotsLEDET(BaseModel):
    """
        Level 2: Class for plotting parameters in lEDET
    """
    suffixPlot: List[str] = []
    typePlot: List[int] = []
    outputPlotSubfolderPlot: List[str] = []
    variableToPlotPlot: List[str] = []
    selectedStrandsPlot: List[str] = []
    selectedTimesPlot: List[str] = []
    labelColorBarPlot: List[str] = []
    minColorBarPlot: List[str] = []
    maxColorBarPlot: List[str] = []
    MinMaxXYPlot: List[int] = []
    flagSavePlot: List[int] = []
    flagColorPlot: List[int] = []
    flagInvisiblePlot: List[int] = []


class VariablesToSaveLEDET(BaseModel):
    """
        Level 2: Class for variables to save in lEDET
    """
    variableToSaveTxt: List[str] = []
    typeVariableToSaveTxt: List[int] = []
    variableToInitialize: List[str] = []
    writeToMesh_fileNameMeshPositions: List[str] = []
    writeToMesh_suffixFileNameOutput: List[str] = []
    writeToMesh_selectedVariables: List[str] = []
    writeToMesh_selectedTimeSteps: List[str] = []
    writeToMesh_selectedMethod: List[str] = []


class LEDETOptions(BaseModel):
    """
        Level 1: Class for LEDET options
    """
    time_vector: TimeVectorLEDET = TimeVectorLEDET()
    magnet_inductance: MagnetInductance = MagnetInductance()
    heat_exchange: HeatExchange = HeatExchange()
    conductor_geometry_used_for_ISCL: ConductorGeometry = ConductorGeometry()
    field_map_files: FieldMapFilesLEDET = FieldMapFilesLEDET()
    input_generation_options: InputGenerationOptionsLEDET = InputGenerationOptionsLEDET()
    simulation: SimulationLEDET = SimulationLEDET()
    STEAM_Material_Properties: MatProLEDET = MatProLEDET()
    physics: PhysicsLEDET = PhysicsLEDET()
    quench_initiation: QuenchInitializationLEDET = QuenchInitializationLEDET()
    post_processing: PostProcessingLEDET = PostProcessingLEDET()
    simulation_3D: Simulation3DLEDET = Simulation3DLEDET()
    plots: PlotsLEDET = PlotsLEDET()
    variables_to_save: VariablesToSaveLEDET = VariablesToSaveLEDET()