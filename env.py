import math
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
    The agent is started at the random position on the observable space. For any given
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
    Reward is decrease based on the distance from the beacon. Minimum reward equals 0 
        
    Starting State:
    The position of the agent is assigned a uniform random value in
    [-1 , 1].  
    
    ATTRIBUTES:
    
    min_position: Minimum value for the observation space
    max_position: Maximum value for the observation space
    step_size: Predetermined amount of movement along the x-axis
    action_space:
    observation_space: Continious, one dimenional observation space or x-axis between the min_position and the max_position
    SIC!!! reward_range:
    reward: Variable to hold a calculated during step value of reward
    movement: Variable to hold a calculated during step value of movement with respect to the direction of movement and movement size 
    '''
    
    def __init__(self):
        self.min_position = -1
        self.max_position = 1
        self.step_size = 0.25
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=self.min_position, high=self.max_position, shape=(1,), dtype=np.float32
        )
        self.reward_min_value = 0
        self.reward_max_value = 1
        self.reward = None
        self.movement = None
        self.seed()
        
    def step(self, action):
        '''
        Calculates a step defined by the action input and returns two values.
        The first value is a position on the x-axis after the step.
        The second value is the reward value after the step.
        
        If the position of the agent is out of observation space borders after the movement, the position is
        set as maximum or minimum position avaliable in observation space.   
        '''
        position = self.state[0]  
        movement = np.multiply(action,self.step_size)
        position += movement
        # Return the max and min position if the position is above or below the border
        if position > self.max_position:
            position = self.max_position
        if position < self.min_position:
            position = self.min_position
        self.state = np.array([position], dtype=np.float32)
        #Calculating reward
        self.reward = (1-math.fabs(self.state[0]))
        
        return self.state.item(), self.reward

    
    def seed(self, seed=None):
        '''
        Define seed for random starting point generation for the test repeatability.
        '''
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        '''
        Randomise a starting point between minimum and maximum values for the observation space.
        Set reward to None.
        '''
        self.state = np.array([self.np_random.uniform(low=self.min_position, high=self.max_position)])
        self.reward = None

#Simple Test
if False:
    game_instance = MoveToBeacon1D()
    game_instance.seed(seed=42)
    game_instance.reset()
    print(f'Initial position:{game_instance.state}')
    action_sequence = [-1,-1,-1,-1,1,1,1,-1,1,1]
    step = 1
    state = None
    reward = None
    expected_state_list=[-0.5017132,-0.7517132,-1,-1,-0.5,-0.25,-0.5,-0.25,0]
    expected_reward_list=[0.49828678369522095,0.24828678369522095,0,0,0.25,0.5,0.75,0.5,0.75,1]
    test_state_list=[]
    test_reward_list=[]
    for element in action_sequence:
        print(f'Step: {step}')
        state, reward = game_instance.step(element)
        print (f'Game step = {step}, action = {element}, State = {state}, Reward = {reward}')
        step +=1
        test_state_list.append(state)
        test_reward_list.append(reward)