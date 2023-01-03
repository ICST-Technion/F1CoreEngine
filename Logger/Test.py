from LoggerSim import Logger


import random



def main():
    perception = Logger.get_random_perception()
    perception1 = Logger.get_random_perception()
    state_estimation = Logger.get_random_state_estimation()
    state_estimation2 = Logger.get_random_state_estimation()
    control = Logger.get_random_contol()
    control2 = Logger.get_random_contol()
    return


if __name__ == '__main__':
    main()
