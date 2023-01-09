import random

import control_pb2 as control
from SmartRandomizer import SmartRandomizer
from Logger import Logger

class DriveInstructionsRandomizer:
    proximityRandomizer = SmartRandomizer([(random.uniform, 0, 1), (random.uniform, 0, 1), (random.uniform, -1, 1),
                                           (random.randint, 0, 80)])

    @staticmethod
    def get_random():
        randomList = DriveInstructionsRandomizer.proximityRandomizer.getRandom()
        drive_instructions = control.DriveInstructions()
        drive_instructions.gas = randomList[0]
        drive_instructions.brakes = randomList[1]
        drive_instructions.steering = randomList[2]
        drive_instructions.optimal_speed = randomList[3]
        return drive_instructions


class ControlRandomizer:
    def __init__(self, drive_instructions):
        self.drive_instructions = drive_instructions

    @staticmethod
    def send_message():
        drive_instructions = DriveInstructionsRandomizer.get_random()
        control = ControlRandomizer(drive_instructions)
        Logger.log(control)
