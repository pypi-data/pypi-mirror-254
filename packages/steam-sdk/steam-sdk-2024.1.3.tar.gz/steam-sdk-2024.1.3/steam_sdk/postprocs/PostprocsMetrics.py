import re
from typing import List
import numpy as np
from steam_sdk.viewers.Viewer import Viewer

class PostprocsMetrics:

    """
        Class to calculate metrics
    """

    metrics_result: List = []

    def __init__(self, metrics_to_do: List[str] = [], var_to_interpolate: list = [], var_to_interpolate_ref: list = [],
                 time_vector: list = [], time_vector_ref: list = [], flag_run: bool = True):
        #TODO change argument names

        """
            Object gets initialized with the metrics which should be done, the variables and time_vectors to
            do the metrics on and a flag if the metrics should be done can be set to false
        """
        
        # Define inputs
        self.metrics_to_do = metrics_to_do
        self.var_to_interpolate = var_to_interpolate
        self.var_to_interpolate_ref = var_to_interpolate_ref
        self.time_vector = time_vector
        self.time_vector_ref = time_vector_ref

        # Convert variables to np.array, if needed
        self.var_to_interpolate = [np.array(v) for v in self.var_to_interpolate]
        self.var_to_interpolate_ref = [np.array(v) for v in self.var_to_interpolate_ref]
        self.time_vector = [np.array(v) for v in self.time_vector]
        self.time_vector_ref = [np.array(v) for v in self.time_vector_ref]

        if flag_run:
            self.run_metrics()

    def run_metrics(self):

        """
            Function to initiate interpolation, start the different metrics and append the result to the output
        """
        # unpack inputs
        metrics_to_do = self.metrics_to_do
        var_of_interest = self.var_to_interpolate
        var_ref = self.var_to_interpolate_ref
        time_vector = self.time_vector
        time_vector_ref = self.time_vector_ref

        # variables which need to be interpolated
        list_metrics_that_need_interpolation = ['maximum_abs_error', 'RMSE', 'RELATIVE_RMSE', 'RMSE_ratio', 'MARE','MARE_1S_AROUND_T_PC_OFF']
        # list_metrics_that_need_interpolation_ref = ['maximum_abs_error', 'RMSE', 'RELATIVE_RMSE','RMSE_ratio','MARE']
        # --> Having two lists here doesnt make any sense because for comparative metrics we ALWAYS have to do both interpolations

         # For metrics that need interpolation of both simulation data and reference data:
        if any(n in metrics_to_do for n in set(list_metrics_that_need_interpolation)):
            # If in the touples of timestep and datapoint at least one value is NaN, then we remove the whole row from both lists
            var_of_interest, time_vector = zip(*[var_pair for var_pair in zip(var_of_interest, time_vector) if
                                                 not any(np.isnan(value) for value in var_pair)])
            var_ref, time_vector_ref = zip(*[(var, time) for var, time in zip(var_ref, time_vector_ref) if
                                             not any(np.isnan(value) for value in (var, time))])

            # Get the equaly spaced timestamps within the time interval of the reference data for possible interpolations
            time_stamps_ref = np.linspace(time_vector_ref[0], time_vector_ref[-1], num=len(time_vector_ref))

            # Interpolate the simulation data to the timestamps of the reference data
            var_of_interest = self._interpolation(time_stamps_ref, time_vector, var_of_interest)
            var_ref = self._interpolation(time_stamps_ref, time_vector_ref, var_ref)

            # We only want to consider those parts of the interpolated datasets, where the original data overlapped, because
            # outside this region, the interpolation might be very wrong:
            # Determine start and end of the reference dataset
            start_ref = min(time_vector_ref)
            end_ref = max(time_vector_ref)
            # Determine start and end of the simulated dataset
            start_interest = min(time_vector)
            end_interest = max(time_vector)

            # Determine their overlap
            end_overlap = min(end_ref, end_interest)
            start_overlap = max(start_ref, start_interest)

            # Create a subset of data that only contains the region of the interpolation, where the initial datasets overlapped
            var_of_interest_overlap, time_stamps_overlap, var_ref_overlap = [], [], []
            for index, timestep in enumerate(time_stamps_ref):
                if (start_overlap <= timestep and timestep <= end_overlap):
                    var_of_interest_overlap.append(var_of_interest[index])
                    time_stamps_overlap.append(time_stamps_ref[index])
                    var_ref_overlap.append(var_ref[index])

            # Use only this region of the overlap to calculate the metrics:
            var_of_interest = np.array(var_of_interest_overlap)
            var_ref = np.array(var_ref_overlap)
            time_stamps_overlap = np.array(time_stamps_overlap)

        # evaluating which metrics will be done and appending results to metrics_result
        self.metrics_result = []
        for metric in metrics_to_do:
            if metric == 'maximum_abs_error':
                result = self._maximum_abs_error(var_of_interest, var_ref)
            elif metric == 'RMSE':
                result = self._RMSE(var_of_interest, var_ref)
            elif metric == 'RELATIVE_RMSE':
                result = self._RELATIVE_RMSE(var_of_interest, var_ref)
            elif metric == 'RMSE_ratio':
                result = self._RMSE_ratio(var_of_interest, var_ref)
            elif metric == 'MARE':
                result = self._MARE(var_of_interest, var_ref) # Calculate Mean Absolute Relative Error (MARE)
            elif metric == 'MARE_1S_AROUND_T_PC_OFF':
                result = self._MARE_1S_AROUND_T_PC_OFF(var_of_interest,var_ref,time_stamps_overlap)
            elif metric == 'quench_load_error':
                result = self._quench_load_error(time_vector, var_of_interest, time_vector_ref, var_ref)
            elif metric == 'quench_load':
                result = self._quench_load(time_vector, var_of_interest)
            elif metric == 'max':
                result = self._peak_value(var_of_interest)
            else:
                raise Exception(f'Metric {metric} not understood!')
            self.metrics_result.append(result)

    # calculating metrics
    @staticmethod
    def _interpolation(linspace_time_stamps, time_vector, var_to_interpolate):

        """
            function to interpolate a variable
        """

        return np.interp(linspace_time_stamps, time_vector, var_to_interpolate) if len(
            var_to_interpolate) != 0 else []

    @staticmethod
    def _maximum_abs_error(y, y_ref):

        """
            function to calculate the absolute error between simulation and measurement
        """

        return max(abs(y - y_ref))

    @staticmethod
    def _RMSE(y, y_ref):

        """
            function to calculate the RMSE between simulation and measurement
        """

        return np.sqrt(((y - y_ref) ** 2).mean()) # np.sqrt(mean_squared_error(y, y_ref))

    @staticmethod
    def _RELATIVE_RMSE(y, y_ref):

        """
            function to calculate the RMSE between simulation and measurement
        """
        avoid_zero_division = 1e-10
        RELATIVE_RMSE = np.sqrt(((y - y_ref) ** 2).mean())/(y_ref.mean()+avoid_zero_division)

        return RELATIVE_RMSE # np.sqrt(mean_squared_error(y, y_ref))

    @staticmethod
    def _MARE(y,y_ref):
        "Calculate Mean Absolute Relative Error (MARE)"
        avoid_zero_division = 1e-10
        MARE = np.abs((y - y_ref)/(y_ref+avoid_zero_division)).mean()
        return MARE

    def _MARE_1S_AROUND_T_PC_OFF(self, y,y_ref,time_stamps_overlap):
        "Calculate Mean Absolute Relative Error (MARE) 1S arround the switchoff time t_PC_off"
        y_around_t_PC_off = []
        y_ref_around_t_PC_off = []

        for index, timestamp in enumerate(time_stamps_overlap):
            if(-1 <= timestamp <= 1):
                y_around_t_PC_off.append(y[index])
                y_ref_around_t_PC_off.append(y_ref[index])

        y_around_t_PC_off = np.array(y_around_t_PC_off)
        y_ref_around_t_PC_off = np.array(y_ref_around_t_PC_off)

        avoid_zero_division = 1e-10
        MARE_1S_AROUND_T_PC_OFF = np.abs((y_around_t_PC_off - y_ref_around_t_PC_off)/(y_ref_around_t_PC_off+avoid_zero_division)).mean()
        return MARE_1S_AROUND_T_PC_OFF

    def _RMSE_ratio(self, y, y_ref):

        """
            function to calculate the RMSE divided by the peak value of the measurement between simulation and measurement
        """

        return np.sqrt(((y - y_ref) ** 2).mean())/self._peak_value(y_ref)

    def _quench_load_error(self, time_vector, Ia, time_vector_ref, Ia_ref):

        """
            function to calculate the quench load error between simulation and measurement
        """

        return self._quench_load(time_vector, Ia) - self._quench_load(time_vector_ref, Ia_ref)

    @staticmethod
    def _quench_load(time_vector, Ia):

        """
            function to calculate the quench load of a current
        """

        dt = [*np.diff(time_vector), 0]
        quench_load_sum = np.cumsum((Ia ** 2) * dt)
        quench_load = quench_load_sum[-1]

        return quench_load

    @staticmethod
    def _peak_value(signal):

        """
            function to calculate the peak value of a signal
        """

        return max(signal)

