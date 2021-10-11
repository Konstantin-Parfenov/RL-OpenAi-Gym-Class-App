from env import MoveToBeacon1D

def main():
    print ('New game:')
    game_instance = MoveToBeacon1D()
    game_instance.reset()
    action_sequence = [1,1,0,0,1,1,1,0,1,1,2,-1,2,3,1,1,1]
    step = 1
    for element in action_sequence:   
        print (f'Game step = {step}, action = {element}, State = {game_instance.step(element)[0]}, Reward = {game_instance.step(element)[1]} ')
        step +=1


if __name__ == '__main__':
    print('Start program')
    main()
    
    
    