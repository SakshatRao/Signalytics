#########################################################################################
# Static Scheduler
#
# Description:  Cyclic phases, fixed phase durations,
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

    def schedule(self, traffic_density, emer_traffic_density, pedestrian_call):
        # Phase Selection
        new_phase_idx = (self.prev_phase_idx + 1) % len(self.phases)
        self.prev_phase_idx = new_phase_idx

        # Phase Duration Calculation
        phase_duration = self.static_period

        return new_phase_idx, phase_duration