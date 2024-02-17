from pydantic import BaseModel, Field, PositiveFloat, PositiveInt, NonNegativeFloat
from typing import (Union, Dict, List, Literal, Optional)

from steam_sdk.data.DataConductor import ConstantJc, Bottura, CUDI3, Bordini, BSCCO_2212_LBNL, CUDI1, Summers, Round, \
    Rectangular, Rutherford, Mono, Ribbon
from steam_sdk.data.DataRoxieParser import RoxieData


from steam_sdk.data.DataModelCommon import Circuit_Class
from steam_sdk.data.DataModelCommon import PowerSupply


class CCTGeometryCWSInputs(BaseModel):
    """
        Level 3: Class for controlling if and where the conductor files and brep files are written for the CWS (conductor with step) workflow
    """
    write: bool = False             # if true only conductor and brep files are written, everything else is skipped.
    output_folder: str = None       # this is relative path to the input file location


class CCTGeometryWinding(BaseModel):  # Geometry related windings _inputs
    """
        Level 2: Class for FiQuS CCT
    """
    names: List[str] = None  # name to use in gmsh and getdp
    r_wms: List[float] = None  # radius of the middle of the winding
    n_turnss: List[float] = None  # number of turns
    ndpts: List[int] = None  # number of divisions of turn, i.e. number of hexagonal elements for each turn
    ndpt_ins: List[int] = None  # number of divisions of terminals ins
    ndpt_outs: List[int] = None  # number of divisions of terminals outs
    lps: List[float] = None  # layer pitch
    alphas: List[float] = None  # tilt angle
    wwws: List[float] = None  # winding wire widths (assuming rectangular)
    wwhs: List[float] = None  # winding wire heights (assuming rectangular)


class CCTGeometryFQPCs(BaseModel):
    """
        Level 2: Class for FiQuS CCT
    """
    names: List[str] = []  # name to use in gmsh and getdp
    fndpls: List[int] = None  # fqpl number of divisions per length
    fwws: List[float] = None  # fqpl wire widths (assuming rectangular) for theta = 0 this is x dimension
    fwhs: List[float] = None  # fqpl wire heights (assuming rectangular) for theta = 0 this is y dimension
    r_ins: List[float] = None  # radiuses for inner diameter for fqpl (radial (or x direction for theta=0) for placing the fqpl
    r_bs: List[float] = None  # radiuses for bending the fqpl by 180 degrees
    n_sbs: List[int] = None  # number of 'bending segmetns' for the 180 degrees turn
    thetas: List[float] = None  # rotation in deg from x+ axis towards y+ axis about z axis.
    z_starts: List[str] = None  # which air boundary to start at. These is string with either: z_min or z_max key from the Air region.
    z_ends: List[float] = None  # z coordinate of loop end


class CCTGeometryFormer(BaseModel):  # Geometry related formers _inputs
    """
        Level 2: Class for FiQuS CCT
    """
    names: List[str] = None  # name to use in gmsh and getdp
    r_ins: List[float] = None  # inner radius
    r_outs: List[float] = None  # outer radius
    z_mins: List[float] = None  # extend of former  in negative z direction
    z_maxs: List[float] = None  # extend of former in positive z direction
    rotates: List[float] = None  # rotation of the former around its axis in degrees


class CCTGeometryAir(BaseModel):  # Geometry related air_region _inputs
    """
        Level 2: Class for FiQuS CCT
    """
    name: str = None  # name to use in gmsh and getdp
    sh_type: str = None  # cylinder or cuboid are possible
    ar: float = None  # if box type is cuboid a is taken as a dimension, if cylinder then r is taken
    z_min: float = None  # extend of air region in negative z direction
    z_max: float = None  # extend of air region in positive z direction


class CCTGeometry(BaseModel):
    """
        Level 2: Class for FiQuS CCT
    """
    CWS_inputs: CCTGeometryCWSInputs = CCTGeometryCWSInputs()
    windings: CCTGeometryWinding = CCTGeometryWinding()
    fqpcs: CCTGeometryFQPCs = CCTGeometryFQPCs()
    formers: CCTGeometryFormer = CCTGeometryFormer()
    air: CCTGeometryAir = CCTGeometryAir()


class CCTMesh(BaseModel):
    """
        Level 2: Class for FiQuS CCT
    """
    MaxAspectWindings: float = None  # used in transfinite mesh_generators settings to define mesh_generators size along two longer lines of hex elements of windings
    ThresholdSizeMin: float = None  # sets field control of Threshold SizeMin
    ThresholdSizeMax: float = None  # sets field control of Threshold SizeMax
    ThresholdDistMin: float = None  # sets field control of Threshold DistMin
    ThresholdDistMax: float = None  # sets field control of Threshold DistMax


class CCTSolveWinding(BaseModel):  # Solution time used windings _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CCT
    """
    currents: List[float] = None  # current in the wire
    sigmas: List[float] = None  # electrical conductivity
    mu_rs: List[float] = None  # relative permeability


class CCTSolveFormer(BaseModel):  # Solution time used formers _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CCT
    """
    sigmas: List[float] = None  # electrical conductivity
    mu_rs: List[float] = None  # relative permeability


class CCTSolveFQPCs(BaseModel):  # Solution time used windings _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CCT
    """
    currents: List[float] = []  # current in the wire
    sigmas: List[float] = []  # electrical conductivity
    mu_rs: List[float] = []  # relative permeability


class CCTSolveAir(BaseModel):  # Solution time used air _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CCT
    """
    sigma: float = None  # electrical conductivity
    mu_r: float = None  # relative permeability


class CCTSolve(BaseModel):
    """
        Level 2: Class for FiQuS CCT
    """
    windings: CCTSolveWinding = CCTSolveWinding()  # windings solution time _inputs
    formers: CCTSolveFormer = CCTSolveFormer()  # former solution time _inputs
    fqpcs: CCTSolveFQPCs = CCTSolveFQPCs()  # fqpls solution time _inputs
    air: CCTSolveAir = CCTSolveAir()  # air solution time _inputs
    pro_template: str = None  # file name of .pro template file
    variables: List[str] = None  # Name of variable to post-process by GetDP, like B for magnetic flux density
    volumes: List[str] = None  # Name of volume to post-process by GetDP, line Winding_1
    file_exts: List[str] = None  # Name of file extensions to post-process by GetDP, like .pos


class CCTPostproc(BaseModel):
    """
        Level 2: Class for  FiQuS CCT
    """
    windings_wwns: List[int] = None  # wires in width direction numbers
    windings_whns: List[int] = None  # wires in height direction numbers
    additional_outputs: List[str] = None  # Name of software specific input files to prepare, like :LEDET3D
    winding_order: List[int] = None
    fqpcs_export_trim_tol: List[
        float] = None  # this multiplier times winding extend gives 'z' coordinate above(below) which hexes are exported for LEDET, length of this list must match number of fqpls
    variables: List[str] = None  # Name of variable to post-process by python Gmsh API, like B for magnetic flux density
    volumes: List[str] = None  # Name of volume to post-process by python Gmsh API, line Winding_1
    file_exts: List[str] = None  # Name of file extensions o post-process by python Gmsh API, like .pos


class CCT(BaseModel):
    """
        Level 2: Class for FiQuS CCT
    """
    type: Literal['CCT_straight']
    geometry: CCTGeometry = CCTGeometry()
    mesh: CCTMesh = CCTMesh()
    solve: CCTSolve = CCTSolve()
    postproc: CCTPostproc = CCTPostproc()


class CWSGeometryConductors(BaseModel):  # Conductor file data for geometry building
    """
        Level 2: Class for FiQuS CWS
    """
    resample: List[int] = None
    skip_middle_from: List[int] = None  # decides which bricks are skipped in fuse operation, basically only a few bricks should overlap with the former.
    skip_middle_to: List[int] = None  # decides which bricks are skipped in fuse operation, basically only a few bricks should overlap with the former.
    file_names_large: List[str] = None
    file_names: List[str] = None  # Inner_17.1mm #[inner_FL, outer_FL] #
    ends_need_trimming: bool = False    # If there are windings "sticking out" of the air region this needs to set to True. It removes 2 volumes per winding after the fragment operation


class CWSGeometryFormers(BaseModel):  # STEP file data for geometry building
    """
        Level 2: Class for FiQuS CWS
    """
    file_names: List[str] = None    # STEP file names to use
    air_pockets: List[int] = None   # number of air pockets (for e.g. for heater or temperature sensor pads) on the formers


class CWSGeometryShells(BaseModel):  # STEP file data for geometry building
    """
        Level 2: Class for FiQuS CWS
    """
    file_names: List[str] = None    # STEP file names to use


class CWSGeometryAir(BaseModel):  # Geometry related air_region _inputs
    """
        Level 2: Class for FiQuS CWS
    """
    name: str = None  # name to use in gmsh and getdp
    sh_type: str = None  # cylinder, cuboid, cylinder_offset, cylinder_cov or cylinder_link are possible
    ar: float = None  # if box type is cuboid 'a' is taken as a dimension, if cylinder then 'r' is taken
    z_min: float = None  # extend of air region in negative z direction, for cylinder_cov this is ignored
    z_max: float = None  # extend of air region in positive z direction, for cylinder_cov this is ignored
    rotate: float = None    # rotation around z axis in degrees
    xy_offset: List[float] = None  # list with x and y offset of the cylinder, only works if sh_type is set to cylinder_offset, e.g. [0, 0.3]
    extension_distance: List[float] = None # list with distances in meter to take along the line going through bricks of end terminals. For example to extend the air region by 0.5 m each way the entry could be [0.5, -0.5]


class CWSGeometry(BaseModel):
    """
        Level 2: Class for FiQuS CWS for FiQuS input
    """
    conductors: CWSGeometryConductors = CWSGeometryConductors()
    formers: CWSGeometryFormers = CWSGeometryFormers()
    shells: CWSGeometryShells = CWSGeometryShells()
    air: CWSGeometryAir = CWSGeometryAir()

class CWSSolveMaterialPropertyListConductors(BaseModel):
    constant: List[float] = None  # list of values if constant is used


class CWSSolveMaterialPropertyList(BaseModel):
    constant: List[float] = None  # list of values if constant is used
    function: List[str] = None  # list of material property function names if function is used


class CWSSolveMaterialPropertySingle(BaseModel):
    constant: float = None  # value if constant is used
    function: str = None  # material property function name if function is used


class CWSSolveConductorsExcitationFunction(BaseModel):  # Solution time used Conductor _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    initials: List[float] = Field(default=None, description="Initial current or voltage in the conductor")
    names: List[str] = Field(default=None, description="Currently, these function names are supported: exp_decrease, exp_increase, linear_decrease, linear_increase ")
    taus: List[float] = Field(default=None, description="Time constant for exponential: Amplitude*Exp(-time/tau), for linear: Amplitude*(time-time_initial)/tau ")


class CWSSolveConductorsExcitationFromFile(BaseModel):  # Solution time used Conductor _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    file_name: str = None  # full file name (i.e. with extension) in the input folder or complete path
    time_header: str = None  # string defining the time signal header in the txt file
    value_headers: List[str] = Field(default=None, description="string defining the value (typically current) signal header in the txt file")


class CWSSolveConductorsExcitation(BaseModel):  # Solution time used Conductor _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    conductors_nw: List[int] = Field(default=None, description="Number of conductors in channel in the height direction (pointing out of the channel direction)")
    conductors_nh: List[int] = Field(default=None, description="Number of conductors in channel in the width direction")
    multips: List[float] = Field(default=None, description="This is decide on polarity of powering the magnet, most often value of 1 or -1 is used. However, arbitrary multiplication is also supported")
    function: CWSSolveConductorsExcitationFunction = CWSSolveConductorsExcitationFunction()
    from_file: CWSSolveConductorsExcitationFromFile = CWSSolveConductorsExcitationFromFile()
    transient_use: str = None  # function or from_file allowed


class CWSSolveConductors(BaseModel):  # Solution time used Conductor _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    excitation: CWSSolveConductorsExcitation = CWSSolveConductorsExcitation()
    conductivity_el: CWSSolveMaterialPropertyListConductors = CWSSolveMaterialPropertyListConductors()
    permeability: List[float] = None  # relative permeability


class CWSSolveInduced(BaseModel):  # Solution time used fqpls _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    RRR_functions: List[float] = None  # RRR to use in material functions
    conductivity_el: CWSSolveMaterialPropertyList = CWSSolveMaterialPropertyList()
    permeability: List[float] = []  # relative permeability
    conductivity_th: CWSSolveMaterialPropertyList = Field(default=CWSSolveMaterialPropertyList(), alias="conductivity_th", description="W/mK")
    heat_capacity: CWSSolveMaterialPropertyList = Field(default=CWSSolveMaterialPropertyList(), alias="heat_capacity", description="J/m^3 K")


class CWSSolveInsulation(BaseModel):
    """
        Level 2: Class for FiQuS CWS
    """
    thickness: float = Field(default=None, description="Thickness of insulation former to former or former to shell")     #
    conductivity_th: CWSSolveMaterialPropertySingle = CWSSolveMaterialPropertySingle()
    heat_capacity: CWSSolveMaterialPropertySingle = Field(default=CWSSolveMaterialPropertySingle(), alias="heat_capacity", description="J/m^3 K")


class CWSSolveAir(BaseModel):  # Solution time used air _inputs (materials and BC)
    """
        Level 2: Class for FiQuS CWS
    """
    conductivity_el: float = Field(default=None, description="Electrical conductivity")
    permeability: float = Field(default=None, description="Relative permeability")


class CWSSolveOutputResample(BaseModel):  # Solution outputs definition
    enabled: bool = Field(default=None, description="Flag to decide if the output is resampled or not")
    delta_t: float = Field(default=None, description="Delta time for resampling")


class CWSSolveOutput(BaseModel):  # Solution outputs definition
    saved: bool = Field(default=None, description="Flat to decide if the output is saved")
    resample: CWSSolveOutputResample = CWSSolveOutputResample()
    variables: List[str] = Field(default=None, description="Name of variable to post-process by GetDP")
    volumes: List[str] = Field(default=None, description="Name of volume to post-process by GetDP")
    file_exts: List[str] = Field(default=None, description="Name of file extensions to output by GetDP")


class CWSSolveStaticSettings(BaseModel):
    solved: bool = Field(default=None, description="Chooses if static solution is solved. Note the transient solution starts with a static solution, so if this and the transient are set to true, the static is solved twice")
    output: CWSSolveOutput = CWSSolveOutput()


class CWSSolveTime(BaseModel):
    initial: float = Field(default=None, description="Initial time")
    end: float = Field(default=None, description="End time")


class CWSSolveTimeFixed(BaseModel):
    step: float = Field(default=None, description="Time step")
    theta: float = Field(default=None, description="Time stepping scheme")


class CWSSolveTimeAdaptiveLTEInputs(BaseModel):
    names: List[str] = Field(default=None, description="string: name of post operation to use")
    relatives: List[float] = Field(default=None, description="relative tolerance")
    absolutes: List[float] = Field(default=None, description="absolute tolerance")
    normTypes: List[str] = Field(default=None, description="string with norm type, allowed: L1Norm, MeanL1Norm, L2Norm, MeanL2Norm, LinfNorm")


class CWSSolveTimeAdaptiveLTE(BaseModel):
    System: CWSSolveTimeAdaptiveLTEInputs = CWSSolveTimeAdaptiveLTEInputs()         # Quantities of interest specified at system level
    PostOperation: CWSSolveTimeAdaptiveLTEInputs = CWSSolveTimeAdaptiveLTEInputs()  # Quantities of interest specified at PostOperation level


class CWSSolveTimeAdaptive(BaseModel):
    initial_step: float = Field(default=None, description="Initial time step. Note this is only used when not starting from previous result")
    min_step: float = Field(default=None, description="Minimum time step")
    max_step: float = Field(default=None, description="Maximum time step")
    integration_method: str = Field(default=None, description="string: Euler, Trapezoidal, Gear_2, Gear_3, Gear_4, Gear_5, Gear_6")
    breakpoints_every: float = Field(default=None, description="this creates a list from initial to end time with this step")
    additional_breakpoints: List[float] = Field(default=None, description="Additional break points to request, typically when the solution is expected to change steeply, like t_PC_off of LEDET")
    LTE: CWSSolveTimeAdaptiveLTE = CWSSolveTimeAdaptiveLTE()  # local_truncation_errors


class CWSSolveNonLinearThermalSettingsTolerance(BaseModel):
    name: str = Field(default=None, description="string: name of post operation to use")
    relative: float = Field(default=None, description="relative tolerance")
    absolute: float = Field(default=None, description="absolute tolerance")
    normType: str = Field(default=None, description="string with norm type, allowed: L1Norm, MeanL1Norm, L2Norm, MeanL2Norm, LinfNorm")


class CWSSolveNonLinearThermalSettings(BaseModel):
    enabled: bool = Field(default=None, description="Flag to decide if constant material properties or nonlinear material functions should be used")
    maximumNumberOfIterations: int = Field(default=None, description="Number of iterations to use")
    relaxationFactor: float = Field(default=None, description="Relaxation factor to use")
    tolerance: CWSSolveNonLinearThermalSettingsTolerance = CWSSolveNonLinearThermalSettingsTolerance()


class CWSSolveTransientSettings(BaseModel):
    solved: bool = Field(default=None, description="Flag to decide if a transient solution is solved (when true), when false the transient is skipped")
    with_thermal: bool = Field(default=None, description="Flag to decide if thermal transient is is solved and weakly coupled to the electromagnetic (when true), when false only electromagnetic is considered (depending on the flag 'solved' above)")
    thermal_TSA_N_elements: int = Field(default=None, description="When set to 0 the thermal TSA is disabled so the is no heat flow between induced parts. Otherwise, this is number of elements across the thin shell")
    nonlinear_thermal_iterations: CWSSolveNonLinearThermalSettings = CWSSolveNonLinearThermalSettings()
    time_stepping: str = Field(default=None, description="either 'fixed' or 'adaptive'")
    start_from_previous: bool = Field(default=None, description="flag to decide if the previous solution (time window of transient should be used as a starting point for this time window)")
    time: CWSSolveTime = CWSSolveTime()
    fixed: CWSSolveTimeFixed = CWSSolveTimeFixed()
    adaptive: CWSSolveTimeAdaptive = CWSSolveTimeAdaptive()
    em_output: CWSSolveOutput = CWSSolveOutput()
    th_output: CWSSolveOutput = CWSSolveOutput()


class CWSSolve(BaseModel):
    """
        Level 2: Class for FiQuS CWS
    """
    verbose_level: int = None # Verbosity level for GetDP
    temperature: float = None  # Initial temperature for the thermal solve
    link: bool= Field(default=None, description="Decides if powering volumes in a 'linked' way is used")
    conductors: CWSSolveConductors = CWSSolveConductors()  # windings solution time _inputs
    formers: CWSSolveInduced = CWSSolveInduced()  # formers solution time _inputs
    shells: CWSSolveInduced = CWSSolveInduced()   # shells solution time _inputs
    insulation_th: CWSSolveInsulation = CWSSolveInsulation()  # insulation former to former or former to shell, thermal properties only.
    insulation_el: bool= Field(default=None, description="Flag to decide if windings are insulated from formers and formers from each other")
    air: CWSSolveAir = CWSSolveAir()  # air solution time _inputs
    pro_template: str = None  # file name of .pro template file
    static: CWSSolveStaticSettings = CWSSolveStaticSettings()  # transient solution settings
    transient: CWSSolveTransientSettings = CWSSolveTransientSettings() # transient solution settings


class CWSMesh(BaseModel):
    """
        Level 2: Class for FiQuS CWS
    """
    MaxAspectWindings: float = None  # used in transfinite mesh_generators settings to define mesh_generators size along two longer lines of hex elements of windings
    Min_length_windings: float = None  # sets how small the edge length for the winding geometry volumes could be used. Overwrites the calculated value if it is smaller than this number.
    ThresholdSizeMinWindings: float = None  # sets field control of Threshold SizeMin
    ThresholdSizeMaxWindings: float = None  # sets field control of Threshold SizeMax
    ThresholdDistMinWindings: float = None  # sets field control of Threshold DistMin
    ThresholdDistMaxWindings: float = None  # sets field control of Threshold DistMax
    ThresholdSizeMinFormers: float = None  # sets field control of Threshold SizeMin
    ThresholdSizeMaxFormers: float = None  # sets field control of Threshold SizeMax
    ThresholdDistMinFormers: float = None  # sets field control of Threshold DistMin
    ThresholdDistMaxFormers: float = None  # sets field control of Threshold DistMax
    link_terminal: List[List[int]] = Field(default=None, description="Specify which windings are connected by giving indexes of winding to connect in the file_names. This is 0 based indexing. To connect first with second winding this is the entry [[0, 1]]")


class CWSPostproc_FieldMap(BaseModel):
    process_static: bool = None # flag to switch on and off processing of static solution for field map
    process_transient: bool = None # flag to switch on and off processing of transient solution for field map
    channel_ws: List[float] = None # wire width
    channel_hs: List[float] = None # wire height
    winding_order: List[int] = Field(default=None, description="[1, 2, 3, 4, 5, 6, 7, 8]")
    trim_from: List[int] = None
    trim_to: List[int] = None
    n_points_for_B_avg: List[int] = None    # number of points to extract for calculating average for B in the center of each wire turn
    variable: str = Field(default=None, description="Name of variable to post-process by gmsh for LEDET") # Name of variable to post-process by python Gmsh API, like B for magnetic flux density
    volume: str = Field(default=None, description="Name of volume to post-process by gmsh for LEDET") # Name of volume to post-process by python Gmsh API, line Winding_1
    file_ext: str = Field(default=None, description="Name of file extensions to output to by gmsh for LEDET") # Name of file extensions o post-process by python Gmsh API, like .pos


class CWSPostproc_Inductance(BaseModel):
    process_static: bool = None # flag to switch on and off processing of static solution for inductance
    process_transient: bool = None # flag to switch on and off processing of transient solution for inductance


class CWSPostproc_TemperatureMap(BaseModel):
    process_transient: bool = None # flag to switch on and off processing of transient solution of temperature


class CWSPostproc_CircuitValues(BaseModel):
    process_static_and_transient: bool = None # flag to switch on and off processing of static and transient solutions for circuit values


class CWSPostproc(BaseModel):
    """
        Class for FiQuS CWS input file
    """
    field_map: CWSPostproc_FieldMap = CWSPostproc_FieldMap()
    inductance: CWSPostproc_Inductance = CWSPostproc_Inductance()
    temperature_map: CWSPostproc_TemperatureMap = CWSPostproc_TemperatureMap()
    circuit_values: CWSPostproc_CircuitValues = CWSPostproc_CircuitValues()


class CWS(BaseModel):
    """
        Level 1: Class for FiQuS CWS
    """
    type: Literal['CWS']
    geometry: CWSGeometry = CWSGeometry()
    mesh: CWSMesh = CWSMesh()
    solve: CWSSolve = CWSSolve()
    postproc: CWSPostproc = CWSPostproc()


# Multipole


class MultipoleSolveTimeParametersAdaptive(BaseModel):
    """
        Level 6: Class for FiQuS Multipole
    """
    initial_time_step: float = None
    min_time_step: float = None
    max_time_step: float = None
    integration_method: str = None
    rel_tol_time: float = None
    abs_tol_time: float = None
    norm_type: str = None


class MultipoleSolveTimeParametersFixed(BaseModel):
    """
        Level 6: Class for FiQuS Multipole
    """
    time_step: float = None
    theta: int = None


class MultipoleSolveConvectionBoundaryCondition(BaseModel):
    """
        Level 5: Class for FiQuS Multipole
    """
    boundaries: List[str] = []
    const_heat_transfer_coefficient: float = None
    function_heat_transfer_coefficient: str = None


class MultipoleSolveHeatFluxBoundaryCondition(BaseModel):
    """
        Level 5: Class for FiQuS Multipole
    """
    boundaries: List[str] = None
    const_heat_flux: float = None
    # function_heat_flux: str = None


class MultipoleSolveTemperatureBoundaryCondition(BaseModel):
    """
        Level 5: Class for FiQuS Multipole
    """
    boundaries: List[str] = []
    const_temperature: float = None
    # function_temperature: str = None


class MultipoleSolveTimeParameters(BaseModel):
    """
        Level 5: Class for FiQuS Multipole
    """
    time_stepping: str = None
    initial_time: float = None
    final_time: float = None
    fixed: MultipoleSolveTimeParametersFixed = MultipoleSolveTimeParametersFixed()
    adaptive: MultipoleSolveTimeParametersAdaptive = MultipoleSolveTimeParametersAdaptive()


class MultipoleSolveQuenchInitiation(BaseModel):
    """
        Level 5: Class for FiQuS Multipole
    """
    turns: List[int] = []
    temperatures: List[float] = []


class MultipoleSolveBoundaryConditionsElectromagnetics(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    currents: List[float] = []


class MultipoleSolveBoundaryConditionsThermal(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    temperature: Dict[str, MultipoleSolveTemperatureBoundaryCondition] = {}
    heat_flux: Dict[str, MultipoleSolveHeatFluxBoundaryCondition] = {}
    cooling: Dict[str, MultipoleSolveConvectionBoundaryCondition] = {}


class MultipoleSolveTransientElectromagnetics(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    time_pars: MultipoleSolveTimeParameters = MultipoleSolveTimeParameters()
    initial_current: float = None


class MultipoleSolveHeCooling(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    sides: str = None
    const_heat_transfer_coefficient: float = None
    function_heat_transfer_coefficient: str = None


class MultipoleSolveNonLinearSolver(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    rel_tolerance: float = None
    abs_tolerance: float = None
    relaxation_factor: float = None
    max_iterations: int = None
    norm_type: str = None


class MultipoleSolveTransientThermal(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    time_pars: MultipoleSolveTimeParameters = MultipoleSolveTimeParameters()
    stop_temperature: float = None
    quench_initiation: MultipoleSolveQuenchInitiation = MultipoleSolveQuenchInitiation()


class MultipoleSolveBasisOrder(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    coil_and_wedges: int = 1
    insulation: int = 1


class MultipoleSolveThinShellApproximationParameters(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    integration_points: int = None  # needs to be reasonably large to properly integrate non-linearity (>= 2)
    global_size: float = None
    minimum_discretizations: int = 1


class MultipoleSolveInsulationBlockToBlock(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    material: str = None
    blocks_connection_overwrite: List[List[str]] = []  # the order of blocks should be: [inner, outer] for mid-layer couples or [lower, higher] for mid-pole and mid-winding couples
    materials_overwrite: List[List[str]] = None
    thicknesses_overwrite: List[List[Union[float, None]]] = None


class MultipoleSolveInsulationExterior(BaseModel):
    """
        Level 4: Class for FiQuS Multipole
    """
    blocks: List[str] = []
    materials_append: List[List[str]] = None  # from block
    thicknesses_append: List[List[float]] = None


class MultipoleSolveWedge(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    material: str = None
    RRR: float = None
    T_ref_RRR_high: float = None


class MultipoleSolveInsulationTSA(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    block_to_block: MultipoleSolveInsulationBlockToBlock = MultipoleSolveInsulationBlockToBlock()
    exterior: MultipoleSolveInsulationExterior = MultipoleSolveInsulationExterior()


class MultipoleSolveElectromagnetics(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    solved: str = None
    boundary_conditions: MultipoleSolveBoundaryConditionsElectromagnetics = MultipoleSolveBoundaryConditionsElectromagnetics()
    non_linear_solver: MultipoleSolveNonLinearSolver = MultipoleSolveNonLinearSolver()
    transient: MultipoleSolveTransientElectromagnetics = MultipoleSolveTransientElectromagnetics()


class MultipoleSolveThermal(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    solved: str = None
    TSA: MultipoleSolveThinShellApproximationParameters = MultipoleSolveThinShellApproximationParameters()
    basis_order: MultipoleSolveBasisOrder = MultipoleSolveBasisOrder()
    isothermal_conductors: bool = False
    isothermal_wedges: bool = False
    initial_temperature: float = None
    enforce_initial_temperature_as_minimum: bool = False
    He_cooling: MultipoleSolveHeCooling = MultipoleSolveHeCooling()
    boundary_conditions: MultipoleSolveBoundaryConditionsThermal = MultipoleSolveBoundaryConditionsThermal()
    non_linear_solver: MultipoleSolveNonLinearSolver = MultipoleSolveNonLinearSolver()
    transient: MultipoleSolveTransientThermal = MultipoleSolveTransientThermal()


class MultipoleMeshThreshold(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    SizeMin: float = None
    SizeMax: float = None
    DistMin: float = None
    DistMax: float = None


class MultipoleMeshTargetSize(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    height: float = None
    width: float = None


class MultipoleMeshTransfiniteSurfaces(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    conductors: bool = True
    wedges: bool = False


class MultipoleGeometry(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    with_iron_yoke: bool = None
    with_wedges: bool = None
    symmetry: str = None


class MultipoleMesh(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    transfinite_surfaces: MultipoleMeshTransfiniteSurfaces = MultipoleMeshTransfiniteSurfaces()
    conductor_target_sizes: MultipoleMeshTargetSize = MultipoleMeshTargetSize()
    wedge_target_sizes: MultipoleMeshTargetSize = MultipoleMeshTargetSize()
    coil_and_wedges: MultipoleMeshThreshold = MultipoleMeshThreshold()
    iron: MultipoleMeshThreshold = MultipoleMeshThreshold()
    bore: MultipoleMeshThreshold = MultipoleMeshThreshold()
    Algorithm: int = None  # sets gmsh Mesh.Algorithm
    ElementOrder: int = None  # sets gmsh Mesh.ElementOrder
    Optimize: int = None  # sets gmsh Mesh.Optimize


class MultipoleSolve(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    insulation_TSA: MultipoleSolveInsulationTSA = MultipoleSolveInsulationTSA()
    wedges: MultipoleSolveWedge = MultipoleSolveWedge()
    electromagnetics: MultipoleSolveElectromagnetics = MultipoleSolveElectromagnetics()
    thermal: MultipoleSolveThermal = MultipoleSolveThermal()
    pro_template: str = None  # file name of .pro template file


class MultipolePostProc(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    output_time_steps: int = None
    compare_to_ROXIE: str = None
    plot_all: str = None
    variables: List[str] = None  # Name of variables to post-process, like "b" for magnetic flux density
    volumes: List[str] = None  # Name of domains to post-process, like "powered"
    file_exts: List[str] = None  # Name of file extensions to output to, like "pos"
    additional_outputs: List[str] = None  # Name of software specific input files to prepare, like "LEDET3D"


class Multipole(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    type: Literal['multipole']
    geometry: MultipoleGeometry = MultipoleGeometry()
    mesh: MultipoleMesh = MultipoleMesh()
    solve: MultipoleSolve = MultipoleSolve()
    postproc: MultipolePostProc = MultipolePostProc()


# Pancake3D
class Pancake3DPosition(BaseModel):
    x: Optional[float] = Field(default=None, title='x coordinate', description='x coordinate of the position.')
    y: Optional[float] = Field(default=None, title='y coordinate', description='y coordinate of the position.')
    z: Optional[float] = Field(default=None, title='z coordinate', description='z coordinate of the position.')
    turnNumber: Optional[PositiveFloat] = Field(default=None, title='Turn Number', description='Winding turn number as a position input.')
    whichPancakeCoil: Optional[PositiveInt] = Field(default=None, title='Pancake Coil Number', description='The first pancake coil is 1, the second is 2, etc.')

class Pancake3DGeometryWinding(BaseModel):
    r_i: Optional[PositiveFloat] = Field(alias='innerRadius', title='Inner Radius', description='Inner radius of the winding.')
    t: Optional[PositiveFloat] = Field(alias='thickness', title='Winding Thickness', description='Thickness of the winding.')
    N: Optional[float] = Field(alias='numberOfTurns', ge=3, title='Number of Turns', description='Number of turns of the winding.')
    h: Optional[PositiveFloat] = Field(alias='height', title='Winding Height', description='Height/width of the winding.')
    name: Optional[str] = Field(default='winding', title='Winding Name', description='The The name to be used in the mesh..', examples=['winding', 'myWinding'])
    NofVolPerTurn: Optional[int] = Field(default=2, alias='numberOfVolumesPerTurn', ge=2, title='Number of Volumes Per Turn (Advanced Input)', description='The number of volumes per turn (CAD related, not physical).')
    theta_i: Optional[float] = Field(default=0.0, alias='startAngle', title='Start Angle', description='The start angle of the first pancake coil in radians.')

class Pancake3DGeometryContactLayer(BaseModel):
    tsa: Optional[bool] = Field(alias='thinShellApproximation', title='Use Thin Shell Approximation', description='If True, the contact layer will be modeled with 2D shell elements (thin shell approximation), and if False, the contact layer will be modeled with 3D elements.')
    t: Optional[PositiveFloat] = Field(alias='thickness', title='Contact Layer Thickness', description='Thickness of the contact layer.')
    name: Optional[str] = Field(default='contactLayer', title='Contact Layer Name', description='The name to be used in the mesh.', examples=['myContactLayer'])

class Pancake3DGeometryTerminal(BaseModel):
    name: Optional[str] = Field(title='Terminal Name', description='The name to be used in the mesh.', examples=['innerTerminal', 'outerTeminal'])
    t: Optional[PositiveFloat] = Field(alias='thickness', title='Terminal Thickness', description="Thickness of the terminal's tube.")

class Pancake3DGeometryTerminals(BaseModel):
    i: Optional[Pancake3DGeometryTerminal] = Field(alias='inner')
    o: Optional[Pancake3DGeometryTerminal] = Field(alias='outer')
    firstName: Optional[str] = Field(default='firstTerminal', description='name of the first terminal')
    lastName: Optional[str] = Field(default='lastTerminal', description='name of the last terminal')

class Pancake3DGeometryAir(BaseModel):
    r: Optional[PositiveFloat] = Field(default=None, alias='radius', title='Air Radius', description='Radius of the air (for cylinder type air).')
    a: Optional[PositiveFloat] = Field(default=None, alias='sideLength', title='Air Side Length', description='Side length of the air (for cuboid type air).')
    margin: Optional[PositiveFloat] = Field(alias='axialMargin', title='Axial Margin of the Air', description='Axial margin between the ends of the air and first/last pancake coils.')
    name: Optional[str] = Field(default='air', title='Air Name', description='The name to be used in the mesh.', examples=['air', 'myAir'])
    type: Optional[Literal['cylinder', 'cuboid']] = Field(default='cylinder', title='Air Type', description='Air can be a cylinder or cuboid.')
    shellTransformation: Optional[bool] = Field(default=False, alias='shellTransformation', title='Use Shell Transformation', description='Generate outer shell air to apply shell transformation if True (GetDP related, not physical)')
    shellTransformationMultiplier: Optional[float] = Field(default=1.2, gt=1, alias='shellTransformationMultiplier', title='Shell Transformation Multiplier (Advanced Input)', description="multiply the air's outer dimension by this value to get the shell's outer dimension")
    cutName: Optional[str] = Field(default='Air-Cut', title='Air Cut Name', description='name of the cut (cochain) to be used in the mesh', examples=['Air-Cut', 'myAirCut'])
    shellVolumeName: Optional[str] = Field(default='air-Shell', title='Air Shell Volume Name', description='name of the shell volume to be used in the mesh', examples=['air-Shell', 'myAirShell'])
    fragment: Optional[bool] = Field(default=False, alias='generateGapAirWithFragment', title='Generate Gap Air with Fragment (Advanced Input)', description='generate the gap air with gmsh/model/occ/fragment if true (CAD related, not physical)')

class Pancake3DMeshWinding(BaseModel):
    axne: Optional[Union[List[PositiveInt], PositiveInt]] = Field(alias='axialNumberOfElements', title='Axial Number of Elements', description='The number of axial elements for the whole height of the coil. It can be either a list of integers to specify the value for each pancake coil separately or an integer to use the same setting for each pancake coil.')
    ane: Optional[Union[List[PositiveInt], PositiveInt]] = Field(alias='azimuthalNumberOfElementsPerTurn', title='Azimuthal Number of Elements Per Turn', description='The number of azimuthal elements per turn of the coil. It can be either a list of integers to specify the value for each pancake coil separately or an integer to use the same setting for each pancake coil.')
    rne: Optional[Union[List[PositiveInt], PositiveInt]] = Field(alias='radialNumberOfElementsPerTurn', title='Winding Radial Number of Elements Per Turn', description='The number of radial elements per tape of the winding. It can be either a list of integers to specify the value for each pancake coil separately or an integer to use the same setting for each pancake coil.')
    axbc: Optional[Union[List[PositiveFloat], PositiveFloat]] = Field(default=[1], alias='axialDistributionCoefficient', title='Axial Bump Coefficients', description="If 1, it won't affect anything. If smaller than 1, elements will get finer in the axial direction at the ends of the coil. If greater than 1, elements will get coarser in the axial direction at the ends of the coil. It can be either a list of floats to specify the value for each pancake coil separately or a float to use the same setting for each pancake coil.")
    elementType: Optional[Union[List[Literal['tetrahedron', 'hexahedron', 'prism']], Literal['tetrahedron', 'hexahedron', 'prism']]] = Field(default=['tetrahedron'], title='Element Type', description='The element type of windings and contact layers. It can be either a tetrahedron, hexahedron, or a prism. It can be either a list of strings to specify the value for each pancake coil separately or a string to use the same setting for each pancake coil.')

class Pancake3DMeshContactLayer(BaseModel):
    rne: Optional[List[PositiveInt]] = Field(alias='radialNumberOfElementsPerTurn', title='Contact Layer Radial Number of Elements Per Turn', description='The number of radial elements per tape of the contact layer. It can be either a list of integers to specify the value for each pancake coil separately or an integer to use the same setting for each pancake coil.')

class Pancake3DMeshAirAndTerminals(BaseModel):
    structured: Optional[bool] = Field(default=False, title='Structure Mesh', description='If True, the mesh will be structured. If False, the mesh will be unstructured.')
    radialElementSize: Optional[PositiveFloat] = Field(default=1, title='Radial Element Size', description="If structured mesh is used, the radial element size can be set. It is the radial element size in terms of the winding's radial element size.")

class Pancake3DSolveAir(BaseModel):
    permeability: Optional[PositiveFloat] = Field(title='Permeability of Air', description='Permeability of air.')

class Pancake3DSolveIcVsLength(BaseModel):
    lengthValues: Optional[List[float]] = Field(title='Tape Length Values', description='Tape length values that corresponds to criticalCurrentValues.')
    criticalCurrentValues: Optional[List[float]] = Field(title='Critical Current Values', description='Critical current values that corresponds to lengthValues.')

class Pancake3DSolveCERNSuperConductorMaterial(BaseModel):
    name: Optional[Literal['HTSSuperPower']] = Field(title='Superconductor Material Name', description='Name of the superconductor material.')
    IcAtTinit: Optional[Union[PositiveFloat, str, Pancake3DSolveIcVsLength]] = Field(alias='criticalCurrentAtInitialTemperature', title='Critical Current at Initial Temperature', description='Critical current at initial temperature. The critical current value will change with temperature depending on the superconductor material.\nEither the same critical current for the whole tape or the critical current with respect to the tape length can be specified. To specify the same critical current for the entire tape, just use a scalar. To specify critical current with respect to the tape length: a CSV file can be used, or lengthValues and criticalCurrentValues can be given as lists. The data will be linearly interpolated.\nIf a CSV file is to be used, the input should be the name of a CSV file (which is in the same folder as the input file) instead of a scalar. The first column of the CSV file will be the tape length, and the second column will be the critical current.', examples=[230, 'IcVSlength.csv'])
    nValue: Optional[PositiveFloat] = Field(default=30, alias='N-Value for E-J Power Law', description='N-value for E–J power law.')
    relativeThickness: Optional[float] = Field(default=None, le=1, title='Relative Thickness (only for winding)', description='Winding tapes generally consist of more than one material. Therefore, when materials are given as a list in winding, their relative thickness, (thickness of the material) / (thickness of the winding), should be specified.')
    jCriticalScalingNormalToWinding: Optional[PositiveFloat] = Field(default=1, title='Critical Current Scaling Normal to Winding', description='Critical current scaling normal to winding, i.e., along the c_axis.  We have Jc_cAxis = scalingFactor * Jc_abPlane. A factor of 1 means no scaling such that the HTS layer is isotropic.')
    electricFieldCriterion: Optional[PositiveFloat] = Field(default=0.0001, title='Electric Field Criterion', description='The electric field that defines the critical current density, i.e., the electric field at which the current density reaches the critical current density.')

class Pancake3DSolveCERNPlating(BaseModel):
    name: Optional[Literal['Copper']] = Field(title='Material Name', description='choices: Copper')
    relativeWidth: Optional[float] = Field(default=0, title='Relative width of plating', le=1, description='HTS 2G coated conductor are typically plated, usually  using copper. The relative width of the plating is the  width of the plating divided by the width of the tape.  0 means no plating.')

class Pancake3DSolveCERNNormalMaterial(BaseModel):
    name: Optional[Literal['Copper', 'Hastelloy', 'Silver', 'Indium', 'Stainless Steel']] = Field(title='Material Name', description='choices: Copper, Hastelloy, Silver, Indium, Stainless Steel')
    relativeThickness: Optional[float] = Field(default=None, le=1, title='Relative Thickness (only for winding)', description='Winding tapes generally consist of more than one material. Therefore, when materials are given as a list in winding, their relative thickness, (thickness of the material) / (thickness of the winding), should be specified.')
    rrr: Optional[PositiveFloat] = Field(default=100, alias='residualResistanceRatio', title='Residual Resistance Ratio', description='Residual-resistivity ratio (also known as Residual-resistance ratio or just RRR) is the ratio of the resistivity of a material at reference temperature and at 0 K.')
    rrrRefT: Optional[PositiveFloat] = Field(default=295, alias='residualResistanceRatioReferenceTemperature', title='Residual Resistance Ratio Reference Temperature', description='Reference temperature for residual resistance ratio')

class Pancake3DSolveMaterial(BaseModel):
    numberOfThinShellElements: Optional[PositiveInt] = Field(default=1, title='Number of Thin Shell Elements (Advanced Input)', description='Number of thin shell elements in the FE formulation (GetDP related, not physical and only used when TSA is set to True)')
    resistivity: Optional[PositiveFloat] = Field(default=None, title='Resistivity', description="A scalar value. If this is given, material properties won't be used for resistivity.")
    thermalConductivity: Optional[PositiveFloat] = Field(default=None, title='Thermal Conductivity', description="A scalar value. If this is given, material properties won't be used for thermal conductivity.")
    specificHeatCapacity: Optional[PositiveFloat] = Field(default=None, title='Specific Heat Capacity', description="A scalar value. If this is given, material properties won't be used for specific heat capacity.")
    material: Optional[Pancake3DSolveCERNNormalMaterial] = Field(default=None, title='Material', description='Material from CERN material library.')

class Pancake3DSolveContactLayerMaterial(Pancake3DSolveMaterial):
    resistivity: Optional[Union[PositiveFloat, Literal['perfectlyInsulating']]] = Field(default=None, title='Resistivity', description='A scalar value or "perfectlyInsulating". If "perfectlyInsulating" is given, the contact layer will be perfectly insulating. If this value is given, material properties won\'t be used for resistivity.')

class Pancake3DSolveTerminalMaterialAndBoundaryCondition(Pancake3DSolveMaterial):
    cooling: Optional[Literal['adiabatic', 'fixedTemperature', 'cryocooler']] = Field(default='fixedTemperature', title='Cooling condition', description='Cooling condition of the terminal. It can be either adiabatic, fixed temperature, or cryocooler.')

class Pancake3DSolveWindingMaterial(BaseModel):
    resistivity: Optional[PositiveFloat] = Field(default=None, title='Resistivity', description="A scalar value. If this is given, material properties won't be used for resistivity.")
    thermalConductivity: Optional[PositiveFloat] = Field(default=None, title='Thermal Conductivity', description="A scalar value. If this is given, material properties won't be used for thermal conductivity.")
    specificHeatCapacity: Optional[PositiveFloat] = Field(default=None, title='Specific Heat Capacity', description="A scalar value. If this is given, material properties won't be used for specific heat capacity.")
    minimumPossibleResistivity: Optional[NonNegativeFloat] = Field(default=0, title='Minimum Possible Resistivity', description="The resistivity of the winding won't be lower than this value, no matter what.")
    maximumPossibleResistivity: Optional[PositiveFloat] = Field(default=1, title='Maximum Possible Resistivity', description="The resistivity of the winding won't be higher than this value, no matter what.")
    material: Optional[List[Union[Pancake3DSolveCERNNormalMaterial, Pancake3DSolveCERNSuperConductorMaterial]]] = Field(default=None, title='Winding Material', description='Because generally winding tapes consist of more than one material, materials should be given as a list of Material dictionaries.')
    plating: Optional[Pancake3DSolveCERNPlating] = Field(default=Pancake3DSolveCERNPlating(name='Copper', relativeWidth=0), title='Tape plating', description='The plating of the winding tape. Only copper is supported for now.By default, the tape is not plated.')

class Pancake3DSolveTolerance(BaseModel):
    quantity: Optional[Literal['solutionVector', 'totalResistiveHeating', 'voltageBetweenTerminals', 'resistiveHeating', 'temperature', 'magnitudeOfCurrentDensity', 'magnitudeOfMagneticField', 'axialComponentOfTheMagneticField', 'currentThroughCoil', 'magnitudeOfHeatFlux', 'magneticEnergy']] = Field(title='Quantity', description='Name of the quantity for tolerance.')
    relative: Optional[NonNegativeFloat] = Field(title='Relative Tolerance', description='Relative tolerance for the quantity.')
    absolute: Optional[NonNegativeFloat] = Field(title='Absolute Tolerance', description='Absolute tolerance for the quantity')
    position: Optional[Pancake3DPosition] = Field(default=None, title='Probing Position of the Quantity', description='Probing position of the quantity for tolerance.')
    normType: Optional[Literal['L1Norm', 'MeanL1Norm', 'L2Norm', 'MeanL2Norm', 'LinfNorm']] = Field(default='L2Norm', alias='normType', title='Norm Type', description='Sometimes, tolerances return a vector instead of a scalar (ex, solutionVector). Then, the magnitude of the tolerance should be calculated with a method. Norm type selects this method.')

class Pancake3DSolveAdaptiveTimeLoopSettings(BaseModel):
    initialStep: Optional[PositiveFloat] = Field(default=None, alias='initialStep', title='Initial Step for Adaptive Time Stepping', description='Initial step for adaptive time stepping')
    minimumStep: Optional[PositiveFloat] = Field(default=None, alias='minimumStep', title='Minimum Step for Adaptive Time Stepping', description='The simulation will be aborted if a finer time step is required than this minimum step value.')
    maximumStep: Optional[PositiveFloat] = Field(default=None, alias='maximumStep', description="Bigger steps than this won't be allowed")
    tolerances: Optional[List[Pancake3DSolveTolerance]] = Field(default=None, title='Tolerances for Adaptive Time Stepping', description='Time steps will be adjusted so the predicted error of quantities below will stay in the tolerance range. Tolerances will decide how fine the time stepping will be.')
    integrationMethod: Optional[Literal['Euler', 'Gear_2', 'Gear_3', 'Gear_4', 'Gear_5', 'Gear_6']] = Field(default='Euler', alias='integrationMethod', title='Integration Method', description='Integration method for transient analysis')
    breakPoints: Optional[List[float]] = Field(default=[0], alias='breakPoints', title='Break Points for Adaptive Time Stepping', description='Make sure to solve the system for these times.')

class Pancake3DSolveFixedTimeLoopSettings(BaseModel):
    step: Optional[PositiveFloat] = Field(default=None, title='Step for Fixed Time Stepping', description='Time step for fixed time stepping.')

class Pancake3DSolveFixedLoopInterval(BaseModel):
    startTime: Optional[NonNegativeFloat] = Field(title='Start Time of the Interval', description='Start time of the interval.')
    endTime: Optional[NonNegativeFloat] = Field(title='End Time of the Interval', description='End time of the interval.')
    step: Optional[PositiveFloat] = Field(title='Step for the Interval', description='Time step for the interval')

class Pancake3DSolveTime(BaseModel):
    adaptive: Optional[Pancake3DSolveAdaptiveTimeLoopSettings] = Field(default=None, alias='adaptiveSteppingSettings', title='Adaptive Time Loop Settings', description='Adaptive time loop settings (only used if stepping type is adaptive).')
    fixed: Optional[Union[List[Pancake3DSolveFixedLoopInterval], Pancake3DSolveFixedTimeLoopSettings]] = Field(default=None, alias='fixedSteppingSettings', title='Fixed Time Loop Settings', description='Fixed time loop settings (only used if stepping type is fixed).')
    start: Optional[float] = Field(title='Start Time', description='Start time of the simulation.')
    end: Optional[float] = Field(title='End Time', description='End time of the simulation.')
    timeSteppingType: Optional[Literal['fixed', 'adaptive']] = Field(title='Time Stepping Type', description='Time stepping type.')
    extrapolationOrder: Optional[Literal[0, 1, 2, 3]] = Field(default=1, alias='extrapolationOrder', title='Extrapolation Order', description='Before solving for the next time steps, the previous solutions can be extrapolated for better convergence.')

class Pancake3DSolveNonlinearSolverSettings(BaseModel):
    tolerances: Optional[List[Pancake3DSolveTolerance]] = Field(default=None, title='Tolerances for Nonlinear Solver', description='The nonlinear solver will check the tolerance quantities to make sure it converged or not. If the quantities stay in the tolerance region after an iteration, it will conclude that the nonlinear solver converged.')
    maxIter: Optional[PositiveInt] = Field(default=100, alias='maximumNumberOfIterations', title='Maximum Number of Iterations', description='Maximum number of iterations allowed for the nonlinear solver.')
    relaxationFactor: Optional[float] = Field(default=0.7, gt=0, alias='relaxationFactor', title='Relaxation Factor', description='Calculated step changes of the solution vector will be multiplied with this value for better convergence.')

class Pancake3DSolveInitialConditions(BaseModel):
    T: Optional[PositiveFloat] = Field(alias='temperature', title='Initial Temperature', description='Initial temperature of the pancake coils.')

class Pancake3DSolveLocalDefect(BaseModel):
    value: Optional[NonNegativeFloat] = Field(default=None, alias='value', title='Value', description='Value of the local defect.')
    transitionDuration: Optional[PositiveFloat] = Field(default=None, title='Transition Duration', description='Transition duration of the local defect. If not given, the transition will be instantly.')
    whichPancakeCoil: Optional[PositiveInt] = Field(default=None, title='Pancake Coil Number', description='The first pancake coil is 1, the second is 2, etc.')
    startTurn: Optional[NonNegativeFloat] = Field(default=None, alias='startTurn', title='Start Turn', description='Start turn of the local defect.')
    endTurn: Optional[PositiveFloat] = Field(default=None, alias='endTurn', title='End Turn', description='End turn of the local defect.')
    startTime: Optional[NonNegativeFloat] = Field(default=None, alias='startTime', title='Start Time', description='Start time of the local defect.')

class Pancake3DSolveLocalDefects(BaseModel):
    jCritical: Optional[Pancake3DSolveLocalDefect] = Field(default=Pancake3DSolveLocalDefect(), alias='criticalCurrentDensity', title='Local Defect for Critical Current Density', description='Set critical current density locally.')

class Pancake3DSolveSaveQuantity(BaseModel):
    quantity: Optional[Literal['magneticField', 'magnitudeOfMagneticField', 'currentDensity', 'magnitudeOfCurrentDensity', 'resistiveHeating', 'temperature', 'voltageBetweenTerminals', 'currentThroughCoil', 'criticalCurrentDensity', 'heatFlux', 'resistivity', 'thermalConductivity', 'specificHeatCapacity', 'jHTSOverjCritical', 'criticalCurrent', 'magneticEnergy']] = Field(title='Quantity', description='Name of the quantity to be saved.')
    timesToBeSaved: Optional[List[float]] = Field(default=None, title='Times to be Saved', description='List of times that wanted to be saved. If not given, all the time steps will be saved.')

class Pancake3DPostprocessTimeSeriesPlot(BaseModel):
    position: Optional[Pancake3DPosition] = Field(default=Pancake3DPosition(), title='Probing Position', description='Probing position of the quantity for time series plot.')
    quantity: Optional[Literal['magnitudeOfMagneticField', 'temperature', 'magnitudeOfCurrentDensity', 'resistiveHeating', 'axialComponentOfTheMagneticField', 'totalResistiveHeating', 'voltageBetweenTerminals', 'currentThroughCoil', 'magnitudeOfHeatFlux', 'resistivity', 'derivativeOfRhoWithRespectToJ', 'magneticEnergy']] = Field(default=None, title='Quantity', description='Name of the quantity to be plotted.')

class Pancake3DPostprocessMagneticFieldOnPlane(BaseModel):
    colormap: Optional[str] = Field(default='viridis', title='Colormap', description='Colormap for the plot.')
    streamLines: Optional[bool] = Field(default=True, title='Stream Lines', description="If True, streamlines will be plotted. Note that magnetic field vectors may have components perpendicular to the plane, and streamlines will be drawn depending on the vectors' projection onto the plane.")
    interpolationMethod: Optional[Literal['nearest', 'linear', 'cubic']] = Field(default='linear', title='Interpolation Method', description='Interpolation type for the plot.\n#Because of the FEM basis function selections of FiQuS, each mesh element has a constant magnetic field vector. Therefore, for smooth 2D plots, interpolation can be used.\n#Types:\n#nearest: it will plot the nearest magnetic field value to the plotting point.\n#linear: it will do linear interpolation to the magnetic field values.\n#cubic: it will do cubic interpolation to the magnetic field values.')
    timesToBePlotted: Optional[List[float]] = Field(default=None, title='Times to be Plotted', description='List of times that wanted to be plotted. If not given, all the time steps will be plotted.')
    planeNormal: Optional[List[float]] = Field(default=[1, 0, 0], title='Plane Normal', description='Normal vector of the plane. The default is YZ-plane (1, 0, 0).')
    planeXAxisUnitVector: Optional[List[float]] = Field(default=[0, 1, 0], title='Plane X Axis', description="If an arbitrary plane is wanted to be plotted, the arbitrary plane's X axis unit vector must be specified. The dot product of the plane's X axis and the plane's normal vector must be zero.")

class Pancake3DGeometry(BaseModel):
    wi: Optional[Pancake3DGeometryWinding] = Field(alias='winding', title='Winding Geometry', description='This dictionary contains the winding geometry information.')
    ii: Optional[Pancake3DGeometryContactLayer] = Field(alias='contactLayer', title='Contact Layer Geometry', description='This dictionary contains the contact layer geometry information.')
    ti: Optional[Pancake3DGeometryTerminals] = Field(alias='terminals', title='Terminals Geometry', description='This dictionary contains the terminals geometry information.')
    ai: Optional[Pancake3DGeometryAir] = Field(alias='air', title='Air Geometry', description='This dictionary contains the air geometry information.')
    N: Optional[PositiveInt] = Field(alias='numberOfPancakes', title='Number of Pancakes', description='Number of pancake coils stacked on top of each other.')
    gap: Optional[PositiveFloat] = Field(alias='gapBetweenPancakes', title='Gap Between Pancakes', description='Gap distance between the pancake coils.')
    dimTol: Optional[PositiveFloat] = Field(default=1e-08, alias='dimensionTolerance', description='dimension tolerance (CAD related, not physical)')
    pancakeBoundaryName: Optional[str] = Field(default='PancakeBoundary', description="name of the pancake's curves that touches the air to be used in the mesh")
    contactLayerBoundaryName: Optional[str] = Field(default='contactLayerBoundary', description="name of the contact layers's curves that touches the air to be used in the mesh (only for TSA)")

class Pancake3DMesh(BaseModel):
    wi: Optional[Pancake3DMeshWinding] = Field(alias='winding', title='Winding Mesh', description='This dictionary contains the winding mesh information.')
    ii: Optional[Pancake3DMeshContactLayer] = Field(alias='contactLayer', title='Contact Layer Mesh', description='This dictionary contains the contact layer mesh information.')
    ti: Optional[Pancake3DMeshAirAndTerminals] = Field(default=Pancake3DMeshAirAndTerminals(), alias='terminals', title='Terminal Mesh', description='This dictionary contains the terminal mesh information.')
    ai: Optional[Pancake3DMeshAirAndTerminals] = Field(default=Pancake3DMeshAirAndTerminals(), alias='air', title='Air Mesh', description='This dictionary contains the air mesh information.')
    relSizeMin: Optional[PositiveFloat] = Field(alias='minimumElementSize', title='Minimum Element Size', description='The minimum mesh element size in terms of the largest mesh size in the winding. This mesh size will be used in the regions close the the winding, and then the mesh size will increate to maximum mesh element size as it gets away from the winding.')
    relSizeMax: Optional[PositiveFloat] = Field(alias='maximumElementSize', title='Maximum Element Size', description='The maximum mesh element size in terms of the largest mesh size in the winding. This mesh size will be used in the regions close the the winding, and then the mesh size will increate to maximum mesh element size as it gets away from the winding.')

class Pancake3DSolve(BaseModel):
    t: Optional[Pancake3DSolveTime] = Field(alias='time', title='Time Settings', description='All the time related settings for transient analysis.')
    nls: Optional[Pancake3DSolveNonlinearSolverSettings] = Field(alias='nonlinearSolver', title='Nonlinear Solver Settings', description='All the nonlinear solver related settings.')
    wi: Optional[Pancake3DSolveWindingMaterial] = Field(alias='winding', title='Winding Properties', description='This dictionary contains the winding material properties.')
    ii: Optional[Pancake3DSolveContactLayerMaterial] = Field(alias='contactLayer', title='Contact Layer Properties', description='This dictionary contains the contact layer material properties.')
    ti: Optional[Pancake3DSolveTerminalMaterialAndBoundaryCondition] = Field(alias='terminals', title='Terminals Properties', description='This dictionary contains the terminals material properties and cooling condition.')
    ai: Optional[Pancake3DSolveAir] = Field(alias='air', title='Air Properties', description='This dictionary contains the air material properties.')
    ic: Optional[Pancake3DSolveInitialConditions] = Field(alias='initialConditions', title='Initial Conditions', description='Initial conditions of the problem.')
    save: Optional[List[Pancake3DSolveSaveQuantity]] = Field(alias='quantitiesToBeSaved', default=None, title='Quantities to be Saved', description='List of quantities to be saved.')
    type: Optional[Literal['electromagnetic', 'thermal', 'weaklyCoupled', 'stronglyCoupled']] = Field(title='Simulation Type', description='FiQuS/Pancake3D can solve only electromagnetics and thermal or electromagnetic and thermal coupled. In the weaklyCoupled setting, thermal and electromagnetics systems will be put into different matrices, whereas in the stronglyCoupled setting, they all will be combined into the same matrix. The solution should remain the same.')
    proTemplate: Optional[str] = Field(default='Pancake3D_template.pro', description='file name of the .pro template file')
    localDefects: Optional[Pancake3DSolveLocalDefects] = Field(default=Pancake3DSolveLocalDefects(), alias='localDefects', title='Local Defects', description='Local defects (like making a small part of the winding normal conductor at some time) can be introduced.')
    initFromPrevious: Optional[str] = Field(default='', title='Full path to res file to continue from', description='The simulation is continued from an existing .res file.  The .res file is from a previous computation on the same geometry and mesh. The .res file is taken from the folder Solution_<<initFromPrevious>>')
    isothermalInAxialDirection: Optional[bool] = Field(default=False, title='Equate DoF along axial direction', description='If True, the DoF along the axial direction will be equated. This means that the temperature will be the same along the axial direction reducing the number of DoF. This is only valid for the thermal analysis.')

class Pancake3DPostprocess(BaseModel):
    timeSeriesPlots: Optional[List[Pancake3DPostprocessTimeSeriesPlot]] = Field(default=None, title='Time Series Plots', description='Values can be plotted with respect to time.')
    magneticFieldOnCutPlane: Optional[Pancake3DPostprocessMagneticFieldOnPlane] = Field(default=None, title='Magnetic Field on a Cut Plane', description='Color map of the magnetic field on the YZ plane can be plotted with streamlines.')

class Pancake3D(BaseModel):
    type: Optional[Literal['Pancake3D']]
    geometry: Optional[Pancake3DGeometry] = Field(default=None, title='Geometry', description='This dictionary contains the geometry information.')
    mesh: Optional[Pancake3DMesh] = Field(default=None, title='Mesh', description='This dictionary contains the mesh information.')
    solve: Optional[Pancake3DSolve] = Field(default=None, title='Solve', description='This dictionary contains the solve information.')
    postproc: Optional[Pancake3DPostprocess] = Field(default=None, title='Postprocess', description='This dictionary contains the postprocess information.')


class MultipoleMonoSet(BaseModel):
    """
        Rutherford cable type for settings (.set)
    """
    type: Literal['Mono']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None


class MultipoleRibbonSet(BaseModel):
    """
        Rutherford cable type for settings (.set)
    """
    type: Literal['Ribbon']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None


class MultipoleRutherfordSet(BaseModel):
    """
        Rutherford cable type for settings (.set)
    """
    type: Literal['Rutherford']
    bare_cable_width: float = None
    bare_cable_height_mean: float = None


class MultipoleConductorSet(BaseModel):
    """
        Class for conductor type for settings (.set)
    """
    cable: Union[MultipoleRutherfordSet, MultipoleRibbonSet, MultipoleMonoSet] = {'type': 'Rutherford'}


class MultipoleConductor(BaseModel):
    """
        Class for conductor type for FiQuS input (.yaml)
    """
    version: str = None
    case: str = None
    state: str = None
    cable: Union[Rutherford, Ribbon, Mono] = {'type': 'Rutherford'}
    strand: Union[Round, Rectangular] = {'type': 'Round'}  # TODO: Tape, WIC
    Jc_fit: Union[ConstantJc, Bottura, CUDI1, CUDI3, Summers, Bordini, BSCCO_2212_LBNL] = {
        'type': 'CUDI1'}  # TODO: CUDI other numbers? , Roxie?


class MultipoleRoxieGeometry(BaseModel):
    """
        Class for FiQuS multipole Roxie data (.geom)
    """
    Roxie_Data: RoxieData = RoxieData()


class MultipoleGeneralSetting(BaseModel):
    """
        Class for general information on the case study
    """
    I_ref: List[float] = None


class MultipoleModelDataSetting(BaseModel):
    """
        Class for model data for settings (.set)
    """
    general_parameters: MultipoleGeneralSetting = MultipoleGeneralSetting()
    conductors: Dict[str, MultipoleConductorSet] = {}


class MultipoleSettings(BaseModel):
    """
        Class for FiQuS multipole settings (.set)
    """
    Model_Data_GS: MultipoleModelDataSetting = MultipoleModelDataSetting()


class RunFiQuS(BaseModel):
    """
        Class for FiQuS run
    """
    type: str = None
    geometry: str = None
    mesh: str = None
    solution: str = None
    launch_gui: bool = None
    overwrite: bool = None


class General(BaseModel):
    """
        Class for FiQuS general
    """
    magnet_name: str = None


class EnergyExtraction(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    t_trigger: float = None
    R_EE: float = None
    power_R_EE: float = None
    L: float = None
    C: float = None


class QuenchHeaters(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    N_strips: int = None
    t_trigger: List[float] = None
    U0: List[float] = None
    C: List[float] = None
    R_warm: List[float] = None
    w: List[float] = None
    h: List[float] = None
    h_ins: List[List[float]] = []
    type_ins: List[List[str]] = []
    h_ground_ins: List[List[float]] = []
    type_ground_ins: List[List[str]] = []
    l: List[float] = None
    l_copper: List[float] = None
    l_stainless_steel: List[float] = None
    ids: List[int] = None
    turns: List[int] = None
    turns_sides: List[str] = None


class Cliq(BaseModel):
    """
        Level 3: Class for FiQuS Multipole
    """
    t_trigger: float = None
    current_direction: List[int] = None
    sym_factor: int = None
    N_units: int = None
    U0: float = None
    C: float = None
    R: float = None
    L: float = None
    I0: float = None


class QuenchProtection(BaseModel):
    """
        Level 2: Class for FiQuS Multipole
    """
    energy_extraction:  EnergyExtraction = EnergyExtraction()
    quench_heaters: QuenchHeaters = QuenchHeaters()
    cliq: Cliq = Cliq()


class DataFiQuS(BaseModel):
    """
        This is data structure of FiQuS Input file
    """
    general: General = General()
    run: RunFiQuS = RunFiQuS()
    magnet: Union[CCT, CWS, Multipole, Pancake3D] = {'type': 'multipole'}
    circuit: Circuit_Class = Circuit_Class()
    power_supply: PowerSupply = PowerSupply()
    quench_protection: QuenchProtection = QuenchProtection()
    conductors: Dict[str, MultipoleConductor] = {}
