#########################################################################################
# Variable-Duration Cyclic-Phase Scheduler
#
# Description:  Cyclic phases, variable phase durations,
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
        self.past_traffic = [(100.0 / (len(phases) - 1))]
        self.PAST_TRAFFIC_LEN = 10
    
    def schedule(self, traffic_density, emer_traffic_density, pedestrian_call):
        
        # Phase Selection
        new_phase_idx = (self.prev_phase_idx + 1) % len(self.phases)
        self.prev_phase_idx = new_phase_idx

        # Phase Duration Calculation
        phase_scores = []
        for phase_directions in self.phases:
            traffic_score = np.mean([traffic_density[self.direction_street_mapping[x]] for x in phase_directions])
            phase_scores.append(traffic_score)
        if(np.sum(phase_scores) == 0):
            sel_phase_score = 100 / len(traffic_density)
        else:
            sel_phase_score = phase_scores[new_phase_idx] / np.sum(phase_scores) * 100

        min_traff_density_allowed = 0
        avg_traff_density_allowed = np.mean(self.past_traffic)
        max_traff_density_allowed = 100
        min_period = self.min_period
        avg_period = self.static_period
        max_period = self.max_period
        
        if(sel_phase_score < avg_traff_density_allowed):
            phase_duration = (sel_phase_score - min_traff_density_allowed) / (avg_traff_density_allowed - min_traff_density_allowed) * (avg_period - min_period) + min_period
        else:
            phase_duration = (sel_phase_score - avg_traff_density_allowed) / (max_traff_density_allowed - avg_traff_density_allowed) * (max_period - avg_period) + avg_period
        phase_duration = int(phase_duration)

        if(len(self.past_traffic) == self.PAST_TRAFFIC_LEN):
            self.past_traffic = self.past_traffic[1:]
        self.past_traffic.append(sel_phase_score)
        
        return new_phase_idx, phase_duration