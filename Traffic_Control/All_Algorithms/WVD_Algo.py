#########################################################################################
# Window-based Variable-Duration Cyclic-Phase Scheduler
#
# Description:  Cyclic phases, Window-based variable phase durations,
#               No emergency prioritization
# 
# Inputs:
#   * traffic_density                       Street-wise number of vehicles
#     (street-indexed array)                Eg. - [5, 9, 10, 0]
#   * emer_traffic_density                  Street-wise number of emergency vehicles
#     (street-indexed array)                Eg. - [1, 0, 0, 0]
#   * pedestrian_call                       Street-wise pedestrian call status
#     (street-indexed array)                Eg. - [False, False, True, False]
#
# Outputs:
#   * new_phase_idx                         Index of new phase
#     (int)                                 Eg. - 1
#   * phase_duration                        Duration for new phase
#     (int)                                 Eg. - 25
#########################################################################################

import numpy as np

class Scheduler:
    def __init__(self, phases, static_period, min_period, max_period, direction_street_mapping, direction_phase_mapping):
        self.prev_phase_idx = 0
        self.phases = phases
        self.static_period = static_period
        self.min_period = min_period
        self.max_period = max_period
        self.direction_street_mapping = direction_street_mapping
        self.direction_phase_mapping = direction_phase_mapping
        self.past_traffic = [(100.0 / len(phases))]
        self.past_cars = [0]
        self.PAST_TRAFFIC_LEN = 10
        self.PAST_CARS_LEN = 10
    
    def schedule(self, traffic_density, emer_traffic_density, pedestrian_call):
        
        # Phase Selection
        new_phase_idx = (self.prev_phase_idx + 1) % len(self.phases)
        self.prev_phase_idx = new_phase_idx

        #######################################
        # Phase Duration Calculation
        #######################################

        # Choosing phase which can affect maximum no. of cars
        phase_scores = []
        for phase_directions in self.phases:
            traffic_score = np.mean([traffic_density[self.direction_street_mapping[x]] for x in phase_directions])
            phase_scores.append(traffic_score)
        
        # Calculating relative traffic percentages
        if(np.sum(phase_scores) == 0):
            sel_phase_score = 100 / len(traffic_density)
        else:
            sel_phase_score = phase_scores[new_phase_idx] / np.sum(phase_scores) * 100
        
        window = self.abs_traffic_duration_map(phase_scores[new_phase_idx])
        phase_duration = self.rel_traffic_duration_map(sel_phase_score, window)

        # Updating list used for Relative Traffic Moving Average
        if(len(self.past_traffic) == self.PAST_TRAFFIC_LEN):
            self.past_traffic = self.past_traffic[1:]
        self.past_traffic.append(sel_phase_score)

        # Updating list used for Absolute Traffic Moving Average
        if(len(self.past_cars) == self.PAST_CARS_LEN):
            self.past_cars = self.past_cars[1:]
        self.past_cars.append(phase_scores[new_phase_idx])
        
        return new_phase_idx, phase_duration

    ####################################################################################
    #   Function to shift duration window based on absolute traffic
    #
    #               Low Traffic: Window shifts to left
    #               20s             30s            40s
    #                   <----------->
    #                      Window
    #
    #               High Traffic:
    #               20s             30s            40s
    #                              <----------->
    #                                  Window
    #
    #   * Relative Traffic can only select a duration within this window
    ####################################################################################
    def abs_traffic_duration_map(self, car_num):
        
        # If no cars present on street
        if(np.sum(self.past_cars) == 0):
            return self.min_period, self.min_period, self.min_period
        
        # Setting minimum, average & maximum traffic and duration limits
        v0 = 0                                                                      # Minimum no. of cars = 0
        v50 = np.mean(self.past_cars)                                               # Moving average of number of cars
        v100 = 2 * np.mean(self.past_cars)                                          # Maximum no. of cars considered to be twice the average
        t0 = (2 * self.min_period + self.static_period) / 3                         # Minimum value of window's center
        t50 = self.static_period                                                    # Window's center assumed to be on static period
        t100 = (2 * self.max_period + self.static_period) / 3                       # Maximum value of window's center

        # Linear interpolation
        if(car_num <= v50):
            tentative_duration = (car_num - v0) / (v50 - v0) * (t50 - t0) + t0
        else:
            tentative_duration = (car_num - v50) / (v100 - v50) * (t100 - t50) + t50
        
        # Window limit check
        tentative_duration = min(tentative_duration, self.max_period)
        tentative_duration = max(tentative_duration, self.min_period)
        
        # Extension on either side
        t_ext = ((t0 - self.min_period) + (self.max_period - t100)) / 2

        return tentative_duration - t_ext, tentative_duration, tentative_duration + t_ext
    
    def rel_traffic_duration_map(self, rel_car_perc, window):
        
        # Setting minimum, average & maximum traffic and duration limits
        min_traff_density_allowed = 0                                               # Minimum traffic percentage = 0%
        avg_traff_density_allowed = np.mean(self.past_traffic)                      # Moving average of relative traffic percentage
        max_traff_density_allowed = 100                                             # Maximum traffic percentage = 100%
        min_period, avg_period, max_period = window                                 # Extracting window min, center & max values
        
        # Linear interpolation
        if(rel_car_perc < avg_traff_density_allowed):
            phase_duration = (rel_car_perc - min_traff_density_allowed) / (avg_traff_density_allowed - min_traff_density_allowed) * (avg_period - min_period) + min_period
        else:
            phase_duration = (rel_car_perc - avg_traff_density_allowed) / (max_traff_density_allowed - avg_traff_density_allowed) * (max_period - avg_period) + avg_period
        
        # Phase duration limit check
        phase_duration = min(phase_duration, self.max_period)
        phase_duration = max(phase_duration, self.min_period)
        phase_duration = int(phase_duration)
        
        return phase_duration