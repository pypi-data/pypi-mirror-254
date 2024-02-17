from typing import List

from pydantic import BaseModel


class TimeVectorSolutionSIGMA(BaseModel):
    time_step: List[List[float]] = None


class Simulation(BaseModel):
    generate_study: bool = None
    study_type: str = None
    make_batch_mode_executable: bool = None
    nbr_elements_mesh_width: int = None
    nbr_elements_mesh_height: int = None


class Physics(BaseModel):
    FLAG_M_pers: int = None
    FLAG_ifcc: int = None
    FLAG_iscc_crossover: int = None
    FLAG_iscc_adjw: int = None
    FLAG_iscc_adjn: int = None
    tauCC_PE: int = None


class QuenchInitialization(BaseModel):
    PARAM_time_quench: float = None
    FLAG_quench_all: int = None
    FLAG_quench_off: int = None
    num_qh_div: List[int] = None
    quench_init_heat: float = None
    quench_init_HT: List[str] = None
    quench_stop_temp: float = None


class Out2DAtPoints(BaseModel):
    coordinate_source: str = None
    variables: List[str] = None
    time: List[List[float]] = None
    map2d: str = None


class Out1DVsTimes(BaseModel):
    variables: List[str] = None
    time: List[List[float]] = None


class Out1DVsAllTimes(BaseModel):
    variables: List[str] = None


class Postprocessing(BaseModel):
    out_2D_at_points: Out2DAtPoints = Out2DAtPoints()
    out_1D_vs_times: Out1DVsTimes = Out1DVsTimes()
    out_1D_vs_all_times: Out1DVsAllTimes = Out1DVsAllTimes()


class QuenchHeatersSIGMA(BaseModel):
    quench_heater_positions: List[List[int]] = None
    th_coils: List[float] = None


class PySIGMAOptions(BaseModel):
    time_vector_solution: TimeVectorSolutionSIGMA = TimeVectorSolutionSIGMA()
    simulation: Simulation = Simulation()
    physics: Physics = Physics()
    quench_initialization: QuenchInitialization = QuenchInitialization()
    postprocessing: Postprocessing = Postprocessing()
    quench_heaters: QuenchHeatersSIGMA = QuenchHeatersSIGMA()
