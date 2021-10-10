import math
from math import sqrt
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

class MoveToBeacon1D(gym.Env):
    '''
    input
    (int) direction of agent eg left (-1) or right (1)
    
    output
    x_pos (float) location of agent on the x axis
    reward (float) current reward experienced by the agent
    
    Description:
    The agent (a car) is started at the random position on the observable space. For any given
    state the agent may choose to move to the left or right.
    
    
    Actions:
    Type: Discrete(2)
    Num    Action               step_destination
    0      move_left            -(step_size)
    1      move_right           step_size
    Note: step_size is a parameterised predetermined amount along the x axis
    
    Observation:
    Type: Box(1)
    Num    Observation               Min            Max
    0      State                     -1             1
    
    Reward:
    Reward of 1 is awarded if the agent reached the beacon (position = 0).
    Reward is decrease based on the distance from the beacon.
        
    Starting State:
    The position of the agent is assigned a uniform random value in
    [-1 , 1].  
      
    '''
    
    def __init__(self):
        self.min_position = -1
        self.max_position = 1
        self.step_size = 0.025
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=self.min_position, high=self.max_position, shape=(1,), dtype=np.float32
        )
        self.reward_range = (0,1)
        self.movement = None
        self.seed()
        
    def step(self, action):
        position = self.state[0]
        err_msg = "%r (%s) invalid" % (action, type(action))
        assert self.action_space.contains(action), err_msg   
        #print(f'Movement step. Current position is {position}')
        movement = np.multiply(action,self.step_size)
        #print(f'Calculated movement is {movement}')
        #print(f'Performing movement')
        position += movement
        #print(f'End of Movement step. Current position is {position}')
        self.state = np.array([position], dtype=np.float32)
        reward = sqrt(1-self.state[0])
        return self.state, reward
    
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.state = np.array([self.np_random.uniform(low=-1, high=1)])
        return np.array(self.state, dtype=np.float32)

game_instance = MoveToBeacon1D()
game_instance.reset()
action_sequence = [1,1,0,0,1,1,1,0,1,1]
step = 1
for element in action_sequence:
    print (f'Game step = {step}, action = {element}, State = {game_instance.step(element)[0]}, Reward = {game_instance.step(element)[1]} ')
    step +=1