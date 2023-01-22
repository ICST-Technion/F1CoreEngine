from time import sleep

from Control import Control
from StateEstimation import StateEstimation
from Perception import Perception
from Logger import Logger
from random import randint

def main():
    
    Logger.connect()
    
    id = randint(0, 10000)
    Logger.newExperiment(id)
    print(f"createing experiment {id=}")
    # while(True):
    #     Control.send_message()
    #     sleep(2)

    for _ in range(3):
        StateEstimation.send_message()
        
    # for _ in range(3):
        # Perception.send_message()
    
    # for _ in range(3):
        # Perception.send_message(debug=True)
    Logger.endExperiment()

    return


if __name__ == '__main__':
    main()
