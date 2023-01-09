from Control import ControlRandomizer as Control
from StateEstimation import StateEstimationRandomizer as StateEstimation
from Perception import PerceptionRandomizer as Perception


import random



def main():
    Perception.send_message()
    Perception.send_message()
    
    StateEstimation.send_message()
    StateEstimation.send_message()
    
    Control.send_message()
    Control.send_message()
    return


if __name__ == '__main__':
    main()
