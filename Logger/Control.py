import random


class DriveInstructions:
    def __init__(self, gas: float, brakes: float, steering: float, optimal_speed: float):
        self.gas = gas
        self.brakes = brakes
        self.steering = steering
        self.optimal_speed = optimal_speed

    @staticmethod
    def get_random():
        gas = random.random()
        brakes = random.random()
        steering = random.uniform(-1, 1)
        optimal_speed = random.uniform(0, 80)
        return DriveInstructions(gas, brakes, steering, optimal_speed)


class Control:
    def __init__(self, driving_instructions: DriveInstructions):
        self.driving_instructions = driving_instructions

    @staticmethod
    def get_random():
        return Control(DriveInstructions.get_random())
