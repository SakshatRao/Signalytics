from tkinter import Tk, Canvas, Button, Label
import tkinter
import random

from Traffic_Simulation.Base import *
from .simulation_config import *
from .phase_config import *

class CustomTraffic(Traffic):

    def draw_roads(self):
        self.road_NS = self.canvas.create_rectangle((CANVAS_WIDTH - ROAD_WIDTH) // 2, 0, (CANVAS_WIDTH + ROAD_WIDTH) // 2, CANVAS_HEIGHT, outline = '#595959', fill = '#595959')
        self.road_WE = self.canvas.create_rectangle(0, (CANVAS_HEIGHT - ROAD_WIDTH) // 2, CANVAS_WIDTH, (CANVAS_HEIGHT + ROAD_WIDTH) // 2, outline = '#595959', fill = '#595959')
    
    def draw_dividers(self):
        self.road_N_divider = self.canvas.create_line(CANVAS_WIDTH // 2, 0, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, fill = '#cc9900', width = DIVIDER_WIDTH)
        self.road_S_divider = self.canvas.create_line(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2, CANVAS_HEIGHT, fill = '#cc9900', width = DIVIDER_WIDTH)
        self.road_W_divider = self.canvas.create_line(0, CANVAS_HEIGHT // 2, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2, fill = '#cc9900', width = DIVIDER_WIDTH)
        self.road_E_divider = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2, CANVAS_WIDTH, CANVAS_HEIGHT // 2, fill = '#cc9900', width = DIVIDER_WIDTH)
    
    def draw_footpath(self):
        self.footpath_N_r = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, 0, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_N_l = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH, 0, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_S_r = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH, CANVAS_HEIGHT, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_S_l = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_W_t = self.canvas.create_rectangle(0, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_W_b = self.canvas.create_rectangle(0, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_E_t = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
        self.footpath_E_b = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, outline = '#b3b3b3', fill = '#b3b3b3')
    
    def draw_road_lines(self):
        self.road_N_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, 0, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_N_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 + 1 * LANE_WIDTH, 0, CANVAS_WIDTH // 2 + 1 * LANE_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_S_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, CANVAS_HEIGHT, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_S_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 - 1 * LANE_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 - 1 * LANE_WIDTH, CANVAS_HEIGHT, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_W_L_line = self.canvas.create_line(0, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_W_R_line = self.canvas.create_line(0, CANVAS_HEIGHT // 2 - 1 * LANE_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - 1 * LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_E_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.road_E_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + 1 * LANE_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 + 1 * LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)

        self.outroad_N_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, 0, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_N_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 - 1 * LANE_WIDTH, 0, CANVAS_WIDTH // 2 - 1 * LANE_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_S_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, CANVAS_HEIGHT, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_S_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 + 1 * LANE_WIDTH, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2, CANVAS_WIDTH // 2 + 1 * LANE_WIDTH, CANVAS_HEIGHT, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_W_L_line = self.canvas.create_line(0, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_W_R_line = self.canvas.create_line(0, CANVAS_HEIGHT // 2 + 1 * LANE_WIDTH, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 + 1 * LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_E_L_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
        self.outroad_E_R_line = self.canvas.create_line(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, CANVAS_HEIGHT // 2 - 1 * LANE_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT // 2 - 1 * LANE_WIDTH, dash = (ROAD_LINE_DASH, ROAD_LINE_DASH), fill = 'white', width = ROAD_LINE_WIDTH)
    
    def draw_traffic_lights(self):
        
        self.traffic_lights = [
            # NS
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + 3 *LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + 3 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # NE
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + 5 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + 5 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + 5 * LANE_WIDTH // 2 + ARROW_EXTENSION,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # NW
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + LANE_WIDTH // 2 - ARROW_EXTENSION,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            
            # EW
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - 3 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - 3 * LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # EN
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - 5 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - 5 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - 5 * LANE_WIDTH // 2 - ARROW_EXTENSION,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # ES
            self.canvas.create_line(
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2 + ARROW_EXTENSION,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            
            # SN
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - 3 *LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - 3 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # SE
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - LANE_WIDTH // 2 + ARROW_EXTENSION,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # SW
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - 5 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - 5 * LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - 5 * LANE_WIDTH // 2 - ARROW_EXTENSION,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            
            # WE
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + 3 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + 3 * LANE_WIDTH // 2,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # WN
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2 - ARROW_EXTENSION,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
            # WS
            self.canvas.create_line(
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + 5 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + 5 * LANE_WIDTH // 2,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + 5 * LANE_WIDTH // 2 + ARROW_EXTENSION,
                arrow = tkinter.LAST, fill = 'green', width = 3, smooth = True),
        ]
    
    def draw_user_buttons(self):
        self.button = Button(self.root, text = "Spawn NS Car", command = self.NS_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, y = 0 * USER_BUTTON_GAP)
        self.button = Button(self.root, text = "Spawn NE Car", command = self.NE_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, y = 1 * USER_BUTTON_GAP)
        self.button = Button(self.root, text = "Spawn NW Car", command = self.NW_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 + ROAD_WIDTH // 2, y = 2 * USER_BUTTON_GAP)

        self.button = Button(self.root, text = "Spawn EW Car", command = self.EW_button_command)
        self.button.place(x = CANVAS_WIDTH, y = CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + 0 * USER_BUTTON_GAP, anchor = tkinter.NE)
        self.button = Button(self.root, text = "Spawn EN Car", command = self.EN_button_command)
        self.button.place(x = CANVAS_WIDTH, y = CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + 1 * USER_BUTTON_GAP, anchor = tkinter.NE)
        self.button = Button(self.root, text = "Spawn ES Car", command = self.ES_button_command)
        self.button.place(x = CANVAS_WIDTH, y = CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + 2 * USER_BUTTON_GAP, anchor = tkinter.NE)
        
        self.button = Button(self.root, text = "Spawn SN Car", command = self.SN_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, y = CANVAS_HEIGHT - 0 * USER_BUTTON_GAP, anchor = tkinter.SE)
        self.button = Button(self.root, text = "Spawn SE Car", command = self.SE_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, y = CANVAS_HEIGHT - 1 * USER_BUTTON_GAP, anchor = tkinter.SE)
        self.button = Button(self.root, text = "Spawn SW Car", command = self.SW_button_command)
        self.button.place(x = CANVAS_WIDTH // 2 - ROAD_WIDTH // 2, y = CANVAS_HEIGHT - 2 * USER_BUTTON_GAP, anchor = tkinter.SE)
        
        self.button = Button(self.root, text = "Spawn WE Car", command = self.WE_button_command)        
        self.button.place(x = 0, y = CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - 0 * USER_BUTTON_GAP, anchor = tkinter.SW)
        self.button = Button(self.root, text = "Spawn WN Car", command = self.WN_button_command)
        self.button.place(x = 0, y = CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - 1 * USER_BUTTON_GAP, anchor = tkinter.SW)
        self.button = Button(self.root, text = "Spawn WS Car", command = self.WS_button_command)
        self.button.place(x = 0, y = CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - 2 * USER_BUTTON_GAP, anchor = tkinter.SW)
    
    def draw_texts(self):
        self.counter_var = tkinter.StringVar()
        self.title_text = Label(self.root, textvariable = self.counter_var, height = 100, width = 100)
        self.title_text.pack()
    
    def draw_pedestrian_buttons(self):
        self.pedestrian_buttons = [
            # N
            self.canvas.create_oval(
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH // 2 + PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + PEDESTRIAN_BUTTON_SIDE,
                fill = 'black'
            ),
            # E
            self.canvas.create_oval(
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + FOOTPATH_WIDTH // 2 + PEDESTRIAN_BUTTON_SIDE,
                fill = 'black'
            ),
            # S
            self.canvas.create_oval(
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH // 2 + PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + PEDESTRIAN_BUTTON_SIDE,
                fill = 'black'
            ),
            # W
            self.canvas.create_oval(
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH // 2 - PEDESTRIAN_BUTTON_SIDE,
                CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + PEDESTRIAN_BUTTON_SIDE,
                CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - FOOTPATH_WIDTH // 2 + PEDESTRIAN_BUTTON_SIDE,
                fill = 'black'
            ),
        ]
    
    def draw_zebra_crossings(self):
        # N
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            fill = 'white', width = ZEBRA_CROSSING_WIDTH, dash = (10, 5)
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            fill = 'white', width = 2
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            fill = 'white', width = 2
        )

        # E
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            fill = 'white', width = ZEBRA_CROSSING_WIDTH, dash = (10, 5)
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            fill = 'white', width = 2
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            fill = 'white', width = 2
        )

        # S
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            fill = 'white', width = ZEBRA_CROSSING_WIDTH, dash = (10, 5)
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            fill = 'white', width = 2
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 + ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 + (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            fill = 'white', width = 2
        )

        # W
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            fill = 'white', width = ZEBRA_CROSSING_WIDTH, dash = (10, 5)
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 + ZEBRA_CROSSING_WIDTH // 2 + 5,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            fill = 'white', width = 2
        )
        self.canvas.create_line(
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2,
            CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 - (CAR_STOP_GAP - ROAD_WIDTH // 2) // 2 - ZEBRA_CROSSING_WIDTH // 2 - 5,
            CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2,
            fill = 'white', width = 2
        )
    
    def random_button_command(self):
        
        uniform_prob = 1 / (num_directions + BIASED_DIRECTIONS * BIAS_WEIGHT)
        biased_prob = [(1 + BIAS_WEIGHT) * uniform_prob] * BIASED_DIRECTIONS
        for direc in range(BIASED_DIRECTIONS, num_directions):
            biased_prob.append(uniform_prob)
        random.Random(self.random_seed).shuffle(biased_prob)
        direction = np.random.choice(np.arange(num_directions), p = biased_prob)
        
        is_emergency = False
        if(EMERGENCY_SPAWN_ENABLE == True):
            emergency_prob = RANDOM_SPAWN_PROB_TIME / EMERGENCY_SPAWN_PROB_TIME
            is_emergency = np.random.choice([False, True], p = [1 - emergency_prob, emergency_prob])

        if(direction == NS):
            car = self.NS_button_command(is_emergency)
        elif(direction == NE):
            car = self.NE_button_command(is_emergency)
        elif(direction == NW):
            car = self.NW_button_command(is_emergency)
        elif(direction == EW):
            car = self.EW_button_command(is_emergency)
        elif(direction == EN):
            car = self.EN_button_command(is_emergency)
        elif(direction == ES):
            car = self.ES_button_command(is_emergency)
        elif(direction == SN):
            car = self.SN_button_command(is_emergency)
        elif(direction == SE):
            car = self.SE_button_command(is_emergency)
        elif(direction == SW):
            car = self.SW_button_command(is_emergency)
        elif(direction == WE):
            car = self.WE_button_command(is_emergency)
        elif(direction == WN):
            car = self.WN_button_command(is_emergency)
        elif(direction == WS):
            car = self.WS_button_command(is_emergency)
        
    def car_new(self, car, is_emergency = False):
        direction_specific_ids[car.direction].append(car.car_id)
        direction_specific_noncrossed_ids[car.direction].append(car.car_id)

        self.traffic_densities[car.street] += 1
        if(is_emergency == True):
            self.emergency_traffic_densities[car.street] += 1
    
    def NS_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET, CAR_INITIAL_OFFSET, CANVAS_WIDTH // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET + CAR_SIDE, CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, NS, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def NE_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH + CAR_INITIAL_OFFSET, CAR_INITIAL_OFFSET, CANVAS_WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH + CAR_INITIAL_OFFSET + CAR_SIDE, CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, NE, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj

    def NW_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 + CAR_INITIAL_OFFSET, CAR_INITIAL_OFFSET, CANVAS_WIDTH // 2 + CAR_INITIAL_OFFSET + CAR_SIDE, CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, NW, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj

    def EW_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET, CANVAS_WIDTH - CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 + LANE_WIDTH + CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, EW, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def EN_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT // 2 + CAR_INITIAL_OFFSET, CANVAS_WIDTH - CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 + CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, EN, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def ES_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH + CAR_INITIAL_OFFSET, CANVAS_WIDTH - CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 + ROAD_WIDTH // 2 - LANE_WIDTH + CAR_INITIAL_OFFSET + CAR_SIDE, outline = 'black', fill = car_color)
        car_obj = Car(car_id, ES, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def SN_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_WIDTH // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET, CANVAS_HEIGHT - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, SN, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def SE_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_WIDTH // 2 - CAR_INITIAL_OFFSET, CANVAS_HEIGHT - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, SE, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def SW_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_HEIGHT - CAR_INITIAL_OFFSET - CAR_SIDE, CANVAS_WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH - CAR_INITIAL_OFFSET, CANVAS_HEIGHT - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, SW, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj

    def WE_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CAR_SIDE + CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - LANE_WIDTH - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, WE, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def WN_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH - CAR_INITIAL_OFFSET - CAR_SIDE, CAR_SIDE + CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - ROAD_WIDTH // 2 + LANE_WIDTH - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, WN, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj
    
    def WS_button_command(self, is_emergency = False):
        if(is_emergency == True):
            car_color = 'white'
        else:
            car_color = choose_color()
        car_id = self.canvas.create_rectangle(CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - CAR_INITIAL_OFFSET - CAR_SIDE, CAR_SIDE + CAR_INITIAL_OFFSET, CANVAS_HEIGHT // 2 - CAR_INITIAL_OFFSET, outline = 'black', fill = car_color)
        car_obj = Car(car_id, WS, is_emergency = is_emergency)
        self.cars[car_id] = car_obj
        self.car_new(car_obj, is_emergency = is_emergency)
        return car_obj