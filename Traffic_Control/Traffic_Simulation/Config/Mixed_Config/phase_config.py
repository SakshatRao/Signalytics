from .simulation_config import *

#########################################################################################
# Direction Status
#########################################################################################

NS = 0;     NE = 1;     NW = 2
EW = 3;     EN = 4;     ES = 5
SN = 6;     SE = 7;     SW = 8
WE = 9;     WN = 10;    WS = 11
num_directions = 12

# direction   --direction_street_mapping-->   street
direction_street_mapping = [
   0, 0, 0,
   1, 1, 1,
   2, 2, 2,
   3, 3, 3
]
num_streets = 4
# Car id for each direction
direction_specific_ids = [[] for _ in range(num_directions)]
direction_specific_noncrossed_ids = [[] for _ in range(num_directions)]

# Config Format: (coord index, thresh, coord>thresh?)

# For cars to turn directions at junction
direction_turn_config = [
   # NS
   [(3, CANVAS_HEIGHT // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET, 1)],
   # NE
   [(3, CANVAS_HEIGHT // 2 - 2 * LANE_WIDTH - CAR_INITIAL_OFFSET, 1)],
   # NW
   [(1, CANVAS_HEIGHT // 2 + CAR_INITIAL_OFFSET, 1)],
   # EW
   [(0, CANVAS_WIDTH // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET, 0)],
   # EN
   [(2, CANVAS_WIDTH // 2 - CAR_INITIAL_OFFSET, 0)],
   # ES
   [(0, CANVAS_WIDTH // 2 + 2 * LANE_WIDTH + CAR_INITIAL_OFFSET, 0)],
   # SN
   [(1, CANVAS_HEIGHT // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET, 0)],
   # SE
   [(3, CANVAS_HEIGHT // 2 - CAR_INITIAL_OFFSET, 0)],
   # SW
   [(1, CANVAS_HEIGHT // 2 + 2 * LANE_WIDTH + CAR_INITIAL_OFFSET, 0)],
   # WE
   [(2, CANVAS_WIDTH // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET, 1)],
   # WN
   [(2, CANVAS_WIDTH // 2 - 2 * LANE_WIDTH - CAR_INITIAL_OFFSET, 1)],
   # WS
   [(0, CANVAS_WIDTH // 2 + CAR_INITIAL_OFFSET, 1)]
]

# For whether car has crossed street and entered into junction
street_crossed_config = [
   # N
   [(3, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, 1)],
   # E
   [(0, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, 0)],
   # S
   [(1, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, 0)],
   # W
   [(2, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, 1)],
]

# For whether car has exited screen
direction_out_config = [
   # NS
   [(3, CANVAS_HEIGHT, 1)],
   # NE
   [(2, CANVAS_WIDTH, 1)],
   # NW
   [(0, 0, 0)],
   # EW
   [(0, 0, 0)],
   # EN
   [(1, 0, 0)],
   # ES
   [(3, CANVAS_HEIGHT, 1)],
   # SN
   [(1, 0, 0)],
   # SE
   [(2, CANVAS_WIDTH, 1)],
   # SW
   [(0, 0, 0)],
   # WE
   [(2, CANVAS_WIDTH, 1)],
   # WN
   [(1, 0, 0)],
   # WS
   [(3, CANVAS_HEIGHT, 1)]
]

# Threshold for stopping the car
street_stop_config = [
   # N
   [[3, CANVAS_HEIGHT // 2 - CAR_STOP_GAP, 1]],
   # E
   [[0, CANVAS_WIDTH // 2 + CAR_STOP_GAP, 0]],
   # S
   [[1, CANVAS_HEIGHT // 2 + CAR_STOP_GAP, 0]],
   # W
   [[2, CANVAS_WIDTH // 2 - CAR_STOP_GAP, 1]],
]

# Direction for the car to move in
# Config Format: [[(coord indices to be changed), +change?]]
direction_move_config = [
   # NS
   [[(1, 3), 1], [(1, 3), 1]],
   # NE
   [[(1, 3), 1], [(0, 2), 1]],
   # NW
   [[(1, 3), 1], [(0, 2), 0]],
   # EW
   [[(0, 2), 0], [(0, 2), 0]],
   # EN
   [[(0, 2), 0], [(1, 3), 0]],
   # ES
   [[(0, 2), 0], [(1, 3), 1]],
   # SN
   [[(1, 3), 0], [(1, 3), 0]],
   # SE
   [[(1, 3), 0], [(0, 2), 1]],
   # SW
   [[(1, 3), 0], [(0, 2), 0]],
   # WE
   [[(0, 2), 1], [(0, 2), 1]],
   # WN
   [[(0, 2), 1], [(1, 3), 0]],
   # WS
   [[(0, 2), 1], [(1, 3), 1]]
]
#########################################################################################









#########################################################################################
# Phase Status
#########################################################################################

phases = [
   [WS, NS, NE],
   [NW, ES, EW],
   [EN, SN, SW],
   [SE, WE, WN]
]
num_phases = len(phases)

direction_phase_mapping = {}
for direction in range(num_directions):
   direction_phase_mapping[direction] = []
   for phase_idx, phase in enumerate(phases):
      if(direction in phase):
         direction_phase_mapping[direction].append(phase_idx)

#########################################################################################