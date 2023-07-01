from tkinter import Tk, Canvas, Button, Label
import tkinter
import time
import numpy as np
import copy
import importlib
import argparse

from Traffic_Simulation.Config.Default_Config.graph_config import *
from Traffic_Simulation.Config.Default_Config.phase_config import *
from Traffic_Simulation.Config.Default_Config.simulation_config import *
from Traffic_Simulation.Base import *

from Algorithms.Static_Algo import Scheduler

parser = argparse.ArgumentParser(description = 'Simulation Options')
parser.add_argument('--to_log', action = 'store_true')
parser.add_argument('--disable_graphics', action = 'store_true')
args = parser.parse_args()

TO_LOG = args.to_log
DISABLE_GRAPHICS = args.disable_graphics

class FinalTraffic(CustomTraffic):
    def __init__(self, to_log = False, disable_graphics = False):
        self.scheduler = Scheduler(phases, STATIC_PERIOD, MIN_PERIOD, MAX_PERIOD, direction_street_mapping, direction_phase_mapping)
        self.random_seed = np.random.randint(100)
        super().__init__(to_log = to_log, disable_graphics = disable_graphics)

    def schedule(self, traffic_density_ratio, emer_traffic_ratio, pedestrian_call):
        int_pedestrian_call = np.asarray(pedestrian_call, dtype = np.uint8)
        new_phase_idx, phase_time = self.scheduler.schedule(traffic_density_ratio, emer_traffic_ratio, int_pedestrian_call)
        return new_phase_idx, phase_time

# Starting Simulation
FinalTraffic(to_log = TO_LOG, disable_graphics = DISABLE_GRAPHICS)