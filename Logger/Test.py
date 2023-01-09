from Control import Control
from StateEstimation import StateEstimation
from Perception import Perception


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
