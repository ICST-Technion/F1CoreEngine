from Control import Control
import common_pb2 as common
import control_pb2 as control
from StateEstimation import StateEstimation
from Perception import Perception


import random


def main():
    for _ in range(3):
        Control.send_message()

    # Perception.send_message()
    # Perception.send_message()
    
    # StateEstimation.send_message()
    # StateEstimation.send_message()
    

    return


if __name__ == '__main__':
    main()
