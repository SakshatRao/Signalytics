from tkinter import Tk, Canvas, Button, Label
import tkinter
import numpy as np
import time
import copy
import sys
import os
from pathlib import Path
from datetime import datetime

from Traffic_Simulation.Config.Default_Config.simulation_config import *
from Traffic_Simulation.Config.Default_Config.phase_config import *

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
def choose_color():
    return np.random.choice(colors)

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

class Car:
    def __init__(self, car_id, direction, is_emergency = False):
        self.car_id = car_id
        self.direction = direction
        self.street = direction_street_mapping[self.direction]
        self.phase = direction_phase_mapping[self.direction]
        self.is_emergency = is_emergency
        self.crossed = False
        self.to_turn = False
        self.waiting_time = 0
        self.traffic_waiting_time = 0
        self.speed = CAR_SPEED
    
    def direction_position(self):
        return direction_specific_ids[self.direction].index(self.car_id)
    
    def waiting_position(self):
        return direction_specific_noncrossed_ids[self.direction].index(self.car_id)
    
    def car_move(self, canvas):
        coords = canvas.coords(self.car_id)
        move_config = direction_move_config[self.direction]
        if(self.to_turn == False):
            move_config = move_config[0]
        else:
            move_config = move_config[1]
        
        car_position = self.direction_position()
        if(car_position > 0):
            next_car_coords = canvas.coords(direction_specific_ids[self.direction][car_position - 1])
            mid_coords = [coords[0] + CAR_SIDE / 2, coords[1] + CAR_SIDE / 2]
            mid_next_car_coords = [next_car_coords[0] + CAR_SIDE / 2, next_car_coords[1] + CAR_SIDE / 2]
            dist = np.sqrt(np.sum(np.square(np.subtract(mid_coords, mid_next_car_coords))))
            if(dist < 1 * (CAR_SIDE + CAR_GAP)):
                self.speed = -TIME_STEP
            elif(dist < 1.5 * (CAR_SIDE + CAR_GAP)):
                self.speed /= 2
                if(self.speed <= 0.1):
                    self.speed = -TIME_STEP
        
        for idx in move_config[0]:
            if(self.speed > 0):
                if(move_config[1] == 1):
                    coords[idx] += self.speed
                else:
                    coords[idx] -= self.speed
        
        if(self.speed < CAR_SPEED):
            self.speed += TIME_STEP
        canvas.coords(self.car_id, coords)
    
    def check_pos(self, canvas, config, use_direction = True):
        coords = canvas.coords(self.car_id)
        if(use_direction == True):
            config = config[self.direction]
        else:
            config = config[self.street]
        for cfg in config:
            if(cfg[2] == 1):
                if(coords[cfg[0]] >= cfg[1]):
                    return True
            else:
                if(coords[cfg[0]] <= cfg[1]):
                    return True
        return False
    
    def stop_car_config(self):
        config = copy.deepcopy(street_stop_config)
        for config_idx in range(len(config[self.street])):
            if(config[self.street][config_idx][2] == 1):
                config[self.street][config_idx][1] -= (CAR_SIDE + CAR_GAP)
            else:
                config[self.street][config_idx][1] += (CAR_SIDE + CAR_GAP)
        return config

class Traffic:
    def __init__(self, to_log = False, disable_graphics = False):
        self.TO_LOG = to_log
        self.DISABLE_GRAPHICS = disable_graphics

        
        self.cars = {}
        self.counter = 0
        self.pedestrian_calls = [[False, -1] for _ in range(num_streets)]
        
        self.latest_waiting_times = []
        self.total_waiting_time = 0
        self.total_traffic_waiting_time = 0
        self.total_sq_waiting_time = 0
        self.total_traffic_len = 0
        self.car_cnt = 0
        self.emergency_total_waiting_time = 0
        self.emergency_car_cnt = 0
        self.traffic_densities = {}
        self.emergency_traffic_densities = {}
        self.pedestrian_total_waiting_time = 0
        self.pedestrian_call_cnt = 0
        for street in range(num_streets):
            self.traffic_densities[street] = 0
            self.emergency_traffic_densities[street] = 0

        self.root = Tk()
        self.canvas = Canvas(self.root, height =  CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = 'green')
        
        if(self.DISABLE_GRAPHICS == False):
            self.draw_roads()
            self.draw_zebra_crossings()
            self.draw_dividers()
            self.draw_footpath()
            self.draw_road_lines()
            self.draw_traffic_lights()
            self.draw_pedestrian_buttons()
            self.canvas.pack()
            if(RANDOM_SPAWN_ENABLE == False):
                self.draw_user_buttons()
        else:
            print("\nSimulation Progress:")
        
        self.draw_texts()

        self.root.after(0, self.animation)
        self.root.mainloop()
    
    def animation(self):
        
        sel_phase_idx = INITIAL_PHASE
        log_path = 'Traffic_Control/Traffic_Simulation/Logs/'
        log_file_path = os.path.join(log_path, 'Default_Config_Static_Algo.csv')
        log_waitingTimes_file_path = os.path.join(log_path, 'WaitingTimes_Default_Config_Static_Algo.csv')
        
        if(self.TO_LOG == True):
            Path(log_path).mkdir(parents=True, exist_ok=True)
            log_file = open(log_file_path, 'w+')
            log_file.write("TimeStamp,SimulationTime,AvgWaitingTime,StdWaitingTime,AvgTrafficWaitingTime,AvgEmergencyWaitingTime,AvgTrafficLen,AvgPedestrianWaitingTime\n")
            log_file.close()
            log_waitingTimes_file = open(log_waitingTimes_file_path, 'w+')
            log_waitingTimes_file.write("WaitingTimes\n")
            log_waitingTimes_file.close()
        
        sim_start_time = time.time()
        
        iteration = 1
        while(True):

            # Preparing relative traffic densities
            traffic_density_ratio = list(self.traffic_densities.values())
            emergency_traffic_density_ratio = list(self.emergency_traffic_densities.values())
            pedestrian_call = [x[0] for x in self.pedestrian_calls]

            # Applying custom algorithm
            sel_phase_idx, phase_time = self.schedule(traffic_density_ratio, emergency_traffic_density_ratio, pedestrian_call)
            assert(phase_time >= MIN_PERIOD)
            assert(phase_time <= MAX_PERIOD)
            sel_phase = phases[sel_phase_idx]
            green_light_streets = np.unique([direction_street_mapping[x] for x in sel_phase])
            red_light_streets = [x for x in range(num_streets) if x not in green_light_streets]
            
            # Calculating traffic length
            self.total_traffic_len += np.sum([len(x) for x in direction_specific_noncrossed_ids])
            
            # Updating traffic lights
            if(self.DISABLE_GRAPHICS == False):
                for traffic_light_idx, traffic_light in enumerate(self.traffic_lights):
                    if(traffic_light_idx in sel_phase):
                        self.canvas.itemconfigure(traffic_light, fill = '#39e600')
                    else:
                        self.canvas.itemconfigure(traffic_light, fill = '#ff3300')
            
            # Checking clearing for pedestrians
            for street_idx in red_light_streets:
                if(self.pedestrian_calls[street_idx][0] == True):
                    self.pedestrian_total_waiting_time += (self.counter - self.pedestrian_calls[street_idx][1])
                    self.pedestrian_calls[street_idx][0] = False
                    self.pedestrian_calls[street_idx][1] = -1
                    if(self.DISABLE_GRAPHICS == False):
                        self.canvas.itemconfigure(self.pedestrian_buttons[street_idx], fill = 'black')
            
            for timestep in range(int(phase_time / TIME_STEP)):
                
                if(self.DISABLE_GRAPHICS == False):
                    time.sleep(TIME_STEP / TIME_SCALE)
                else:
                    if(int(self.counter / TIME_STEP) % int(UPDATE_STEP / TIME_STEP) == 0):
                        progress(self.counter, STOP_SIM_TIME)
                
                # Updating yellow traffic lights
                if(self.DISABLE_GRAPHICS == False):
                    for traffic_light_idx, traffic_light in enumerate(self.traffic_lights):
                        if(traffic_light_idx in sel_phase):
                            if(phase_time - timestep * TIME_STEP == 5):
                                self.canvas.itemconfigure(traffic_light, fill = '#ffff00')
                
                # Updating traffic metrics display
                if(int(self.counter / TIME_STEP) % int(UPDATE_STEP / TIME_STEP) == 0):

                    counter_val = self.counter
                    remaining_val = phase_time - timestep * TIME_STEP
                    if(self.car_cnt != 0):
                        avg_waiting_val = self.total_waiting_time / self.car_cnt
                        std_waiting_val = np.sqrt((self.total_sq_waiting_time / self.car_cnt) - (avg_waiting_val) ** 2)
                        traffic_waiting_val = self.total_traffic_waiting_time / self.car_cnt
                    else:
                        avg_waiting_val = 0
                        std_waiting_val = 0
                        traffic_waiting_val = 0
                    if(self.emergency_car_cnt != 0):
                        avg_emergency_waiting_val = self.emergency_total_waiting_time / self.emergency_car_cnt
                    else:
                        avg_emergency_waiting_val = 0
                    avg_traffic_len = self.total_traffic_len / (num_directions * iteration)
                    car_cnt_val = self.car_cnt
                    emergency_car_cnt_val = self.emergency_car_cnt
                    if(self.pedestrian_call_cnt == 0):
                        pedestrian_waiting = 0
                    else:
                        pedestrian_waiting = self.pedestrian_total_waiting_time / self.pedestrian_call_cnt
                    pedestrian_call_cnt = self.pedestrian_call_cnt

                    if(self.DISABLE_GRAPHICS == False):
                        self.counter_var.set(
                            f"Traffic Metrics:\n" +
                            f"Time:                                 {counter_val:.0f}\n" +
                            f"Remaining Time:                       {remaining_val:.0f}\n\n" +
                            f"Avg Waiting Time:                     {avg_waiting_val:.1f}\n" +
                            f"Avg Emergency Waiting Time:           {avg_emergency_waiting_val:.1f}\n" +
                            f"Avg Traffic-weighted Waiting Time:    {traffic_waiting_val:.1f}\n" +
                            f"Pedestrian Waiting Time:              {pedestrian_waiting:.1f}"
                        )
                    else:
                        self.counter_var.set("Simulation Stopping!")

                    if(self.TO_LOG == True):
                        if(int(self.counter / TIME_STEP) % int(LOG_STEP / TIME_STEP) == 0):
                            log_file = open(log_file_path, 'a')
                            date_format = "%d/%m/%Y %H:%M:%S"
                            log_file.write(f"{datetime.strftime(datetime.now(), date_format)},{counter_val:.0f},{avg_waiting_val:.1f},{std_waiting_val:.2f},{traffic_waiting_val:.2f},{avg_emergency_waiting_val:.1f},{avg_traffic_len:.2f},{pedestrian_waiting:.2f}\n")
                            log_file.close()
                            log_waitingTimes_file = open(log_waitingTimes_file_path, 'a')
                            for waitingTime in self.latest_waiting_times:
                                log_waitingTimes_file.write(f"{waitingTime:.1f}\n")
                            log_waitingTimes_file.close()
                            self.latest_waiting_times = []
                
                # Spawning vehicles
                if(RANDOM_SPAWN_ENABLE == True):
                    spawn_prob = (TIME_STEP / RANDOM_SPAWN_PROB_TIME) + (TIME_STEP / EMERGENCY_SPAWN_PROB_TIME)
                    if(np.random.choice([False, True], p = [1 - spawn_prob, spawn_prob]) == True):
                        self.random_button_command()
                
                # Spawning pedestrian calls
                if(PEDESTRIAN_CALL_SPAWN_ENABLE == True):
                    spawn_prob = (TIME_STEP / PEDESTRIAN_CALL_SPAWN_PROB_TIME)
                    if(np.random.choice([False, True], p = [1 - spawn_prob, spawn_prob]) == True):
                        which_street = np.random.choice(green_light_streets)
                        if(self.pedestrian_calls[which_street][0] == False):
                            self.pedestrian_calls[which_street][0] = True
                            self.pedestrian_calls[which_street][1] = self.counter
                            self.pedestrian_call_cnt += 1
                            if(self.DISABLE_GRAPHICS == False):
                                self.canvas.itemconfigure(self.pedestrian_buttons[which_street], fill = 'red')
                
                deleted_car_id = []
                for car_id in self.cars:
                    car = self.cars[car_id]

                    # If car is stopped, add to waiting time
                    if(car.speed <= 0):
                        car.waiting_time += TIME_STEP
                        car.traffic_waiting_time += TIME_STEP * (car.waiting_position() + 1)

                    # Checking whether car should stop
                    if(car.crossed == False):
                        if(sel_phase_idx not in car.phase):
                            #stop_config = car.stop_car_config()
                            if(car.check_pos(self.canvas, street_stop_config, use_direction = False) == True):
                                car.speed = CAR_SPEED - ACCELERATION * (car.waiting_position() + 1)
                                continue

                    # Moving the car
                    car.car_move(self.canvas)

                    # Checking whether car should turn
                    if(car.check_pos(self.canvas, direction_turn_config) == True):
                        car.to_turn = True
                    
                    # Checking whether car has crossed the traffic signal
                    if(car.crossed == False):
                        if(car.check_pos(self.canvas, street_crossed_config, use_direction = False) == True):
                            car.crossed = True
                            direction_specific_noncrossed_ids[car.direction].remove(car.car_id)
                            self.traffic_densities[car.street] -= 1
                            self.latest_waiting_times.append(car.waiting_time)
                            self.total_waiting_time += car.waiting_time
                            self.total_sq_waiting_time += (car.waiting_time) ** 2
                            self.total_traffic_waiting_time += car.traffic_waiting_time
                            self.car_cnt += 1
                            if(car.is_emergency == True):
                                self.emergency_traffic_densities[car.street] -= 1
                                self.emergency_total_waiting_time += car.waiting_time
                                self.emergency_car_cnt += 1
                    
                    # Checking whether car has exited the screen
                    if(car.check_pos(self.canvas, direction_out_config) == True):
                        direction_specific_ids[car.direction].remove(car.car_id)
                        self.canvas.delete(car_id)
                        deleted_car_id.append(car_id)
                
                for car_id in deleted_car_id:
                    self.cars.pop(car_id)

                self.counter += TIME_STEP
                
                if(self.DISABLE_GRAPHICS == False):
                    self.canvas.update()
                if(self.counter > STOP_SIM_TIME):
                    sim_stop_time = time.time()
                    print(f"\nTotal Time Elapsed: {sim_stop_time - sim_start_time:.1f} seconds!")
                    sys.exit()
            
            iteration += 1