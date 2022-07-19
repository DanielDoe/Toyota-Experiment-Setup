import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np

MAX_ACCEPTABLE_LATENCY = 120
MAX_NUM_PAIRINGS = 120
MAX_OPEN_PAIRINGS = 5
MAX_STEPS = 2000

INITIAL_LATENCY_VALUE = 0


class VehicleServerEnv(gym.Env):
    """A vehicle server selection environment with OpenAI gym"""
    metadata = {'render.modes': ['human']}

    def __init__(self, df):
        super(VehicleServerEnv, self).__init__()

        self.df = df
        self.reward_range = (0, MAX_ACCEPTABLE_LATENCY)

        # Actions of the format pair x%, unpair x%, Nothing, etc.
        self.action_space = spaces.Box(
            low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)

        # Prices contains the OHCL values for the last actions
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(6, 6), dtype=np.float16)

    def _next_observation(self):
        # Get the next action
        frame = np.array([
            self.df.loc[self.current_step: self.current_step +
                        5, 'server_idx'].values,
            self.df.loc[self.current_step: self.current_step +
                        5, 'vehicle_idx'].values,
            self.df.loc[self.current_step: self.current_step +
                        5, 'vehicle_location'].values,
            self.df.loc[self.current_step: self.current_step +
                        5, 'server_location'].values,
            self.df.loc[self.current_step: self.current_step +
                        5, 'image_size'].values,
            self.df.loc[self.current_step: self.current_step +
                        5, 'detected_objects'].values,
        ])

        # Append additional data and scale each value to between 0-1
        obs = np.append(frame, [[
            self.latency,
            self.max_latency,
            self.total_number_servers,
            self.total_vehicles_paired,
            self.total_number_vehicles,
        ]], axis=0)

        return obs

    def _take_action(self, action):
        # Set the current request to a random request within the time step
        current_request = random.uniform(
            self.df.loc[self.current_step, "vehicle_location"], self.df.loc[self.current_step, "server_location"])

        action_type = action[0]
        selection = action[1]

        if action_type < 1:
            # pair vehicle to servers
            if (self.df.vehicle_location < self.current_step.server_location) and (self.df.image_size < self.current_step.image_size) and (self.df.detected_objects < self.current_step.detected_objects):
                server_idx = self.df.server_idx,
                vehicle_idx = self.df.vehicle_idx

                return [server_idx, vehicle_idx]

        elif action_type < 2:
            # unpair vehicle from servers
            if (self.df.vehicle_location < self.current_step.server_location) and (self.df.image_size < self.current_step.image_size) and (self.df.detected_objects < self.current_step.detected_objects):
                server_idx = self.df.server_idx,
                vehicle_idx = self.df.vehicle_idx

                return [server_idx, vehicle_idx]

        # Do nothing for invalid selections    
        else:
            print("No vehicle-server pair can be generated for entry.")

    def step(self, action):
        # Execute one time step within the environment
        self._take_action(action)

        self.current_step += 1

        if self.current_step > len(self.df.loc[:, 'Open'].values) - 6:
            self.current_step = 0

        delay_modifier = (self.current_step / MAX_STEPS)

        # Reward = minus the time taken to make decision on vehicle-server selection
        reward = -self.latency
        done = self.max_latency <= 0

        obs = self._next_observation()

        return obs, reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.balance = INITIAL_ACCOUNT_BALANCE
        self.net_worth = INITIAL_ACCOUNT_BALANCE
        self.max_net_worth = INITIAL_ACCOUNT_BALANCE
        self.shares_held = 0
        self.cost_basis = 0
        self.total_shares_sold = 0
        self.total_sales_value = 0

        # Set the current step to a random point within the data frame
        self.current_step = random.randint(
            0, len(self.df.loc[:, 'Open'].values) - 6)

        return self._next_observation()

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        profit = self.net_worth - INITIAL_ACCOUNT_BALANCE
