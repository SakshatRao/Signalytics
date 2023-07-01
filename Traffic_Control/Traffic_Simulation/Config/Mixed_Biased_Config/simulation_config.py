#########################################################################################
# Simulation Configuration
#########################################################################################

# Graphical Configs
CANVAS_WIDTH                            =           1400                                        # Width of canvas
CANVAS_HEIGHT                           =           850                                         # Height of canvas
ROAD_WIDTH                              =           150                                         # Width of entire road
NUM_LANES                               =           3                                           # Number of lanes on either side of the divider
LANE_WIDTH                              =           ROAD_WIDTH // 2 / NUM_LANES                 # Width of each lane
DIVIDER_WIDTH                           =           4                                           # Width of the divider
ROAD_LINE_WIDTH                         =           2                                           # Width of markers separating lanes
ROAD_LINE_DASH                          =           20                                          # Separation between dashed markers
CAR_SIDE                                =           15                                          # Length of a car (given car is of square shape)
CAR_INITIAL_OFFSET                      =           5                                           # Distance between car and road markers
FOOTPATH_WIDTH                          =           30                                          # Width of the footpath
ARROW_EXTENSION                         =           25                                          # Amount by which traffic arrows extends
CAR_GAP                                 =           10                                          # Minimum Gap between waiting cars
USER_BUTTON_GAP                         =           25                                          # Distance between user buttons and the roads
CAR_STOP_GAP                            =           200                                         # Distance between center of junction and the waiting line for cars
TEXT_GAP                                =           25                                          # Gap between user buttons
TEXT_WIDTH                              =           50                                          # Width of each user button
ZEBRA_CROSSING_WIDTH                    =           30                                          # Width of zebra crossing
PEDESTRIAN_BUTTON_SIDE                  =           5                                           # Diameter of pedestrian call buttons

# Performance Configs
TIME_STEP                               =           0.1                                         # Smallest unit of time to run simulation
STOP_SIM_TIME                           =           86400                                       # Time (in simulation seconds) after which to stop simulation
TIME_SCALE                              =           10                                          # Scale factor to speed up simulation
STATIC_PERIOD                           =           30                                          # Static period of the traffic signal
CAR_SPEED                               =           5                                           # Maximum peed of the car (pixels/timestep)
ACCELERATION                            =           5                                           # Timesteps from rest to maximum speed
INITIAL_PHASE                           =           0                                           # Initial phase index
RANDOM_SPAWN_ENABLE                     =           True                                        # Enable random spawning of cars?
RANDOM_SPAWN_PROB_TIME                  =           3                                           # Average probabilistic spawning time (seconds / car spawn)
MIN_PERIOD                              =           20                                          # Minimum phase duration
MAX_PERIOD                              =           40                                          # Maximum phase duration
UPDATE_STEP                             =           1                                           # Traffic metrics update period (/second)
EMERGENCY_SPAWN_ENABLE                  =           True                                        # Enable random spawning of emergency vehicles?
EMERGENCY_SPAWN_PROB_TIME               =           60                                          # Average probabilistic spawning time for emergency vehicles (seconds / vehicle)
LOG_STEP                                =           5                                           # Logging period (second)
BIASED_DIRECTIONS                       =           5                                           # Number of directions to have biased traffic
BIAS_WEIGHT                             =           10                                          # Bias factor (0 implies non-biased traffic)
PEDESTRIAN_CALL_SPAWN_ENABLE            =           True                                        # Enable random spawning of Pedestrian Calls
PEDESTRIAN_CALL_SPAWN_PROB_TIME         =           60                                          # Average probabilistic spawning time of Pedestrian Calls (seconds / call spawn)

assert(STATIC_PERIOD > MIN_PERIOD)
assert(TIME_STEP < RANDOM_SPAWN_PROB_TIME)
assert(CAR_SIDE + 2 * CAR_INITIAL_OFFSET == LANE_WIDTH)
assert(CAR_STOP_GAP > ROAD_WIDTH // 2)

#########################################################################################