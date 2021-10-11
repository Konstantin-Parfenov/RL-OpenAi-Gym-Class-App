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
        self.step_size = 0.25
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=self.min_position, high=self.max_position, shape=(1,), dtype=np.float32
        )
        self.reward_range = (0,1)
        self.reward = None
        self.movement = None
        self.seed()
        
    def step(self, action):
        print('DEBUG action value',action)
        position = self.state[0]  
        #print(f'Start Movement step. Current position is {position}')
        #print(f'Start Movement step. Current self.state is {self.state}')
        #print(f'Start Movement step. Current reward is {self.reward}')
        
        #1
        movement = np.multiply((action-0.5)*2,self.step_size)
        #print(f'Calculated movement is {movement}')
        #print(f'Performing movement')
        position += movement
        # Return the max and min position if the position is above or below the border
        if position > self.max_position:
            #print(f'NOTE: Movement exceeds borders. Returned to max position')
            position = self.max_position
        if position < self.min_position:
            #print(f'NOTE: Movement exceeds borders. Returned to min position')
            position = self.min_position
        #print(f'End of Movement step. Current position is {position}')
        #print(f'Update self.state from calculated position')
        self.state = np.array([position], dtype=np.float32)
        #print(f'End of Movement step. Current self.state is {self.state}')
        #print(f'Calculate reward')
        self.reward = (1-math.fabs(self.state[0]))
        #print(f'calc for self reward_1,{position}')
        #print(f'calc for self reward {math.fabs(position)}')
        #print(f'End of Movement step. Current reward is {self.reward}')
        return self.state.item(), self.reward
    
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.state = np.array([self.np_random.uniform(low=-1, high=1)])
        self.reward = None
        print('Reset Done')
        return np.array(self.state[0], dtype=np.float32)


#Simple Test
if False:
    game_instance = MoveToBeacon1D()
    game_instance.seed(seed=42)
    game_instance.reset()
    print(f'Initial position:{game_instance.state}')
    action_sequence = [0,0,0,0,1,1,1,0,1,1]
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