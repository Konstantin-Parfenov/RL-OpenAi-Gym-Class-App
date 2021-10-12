from env import MoveToBeacon1D

#Simple Test happy path
if True:
    game_instance = MoveToBeacon1D()
    game_instance.seed(seed=42)
    game_instance.reset()
    print(f'Initial position:{game_instance.state}')
    action_sequence = [0,0,0,0,1,1,1,0,1,1]
    step = 1
    state = None
    reward = None
    expected_state_list=[-0.501713216304779,-0.751713216304779,-1.0,-1.0,-0.75,-0.5,-0.25,-0.5,-0.25,0.0]
    expected_reward_list=[0.49828678369522095,0.24828678369522095,0,0,0.25,0.5,0.75,0.5,0.75,1.0]
    test_state_list=[]
    test_reward_list=[]
    for element in action_sequence:
        print(f'Step: {step}')
        state, reward = game_instance.step(element)
        print (f'Game step = {step}, action = {element}, State = {state}, Reward = {reward}')
        step +=1
        test_state_list.append(state)
        test_reward_list.append(reward)
    print(test_state_list)
    print('State equal:',expected_state_list==test_state_list) 
    print('Reward equal:',expected_reward_list==test_reward_list) 