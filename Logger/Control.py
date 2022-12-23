import random

import control_pb2 as control


class DriveInstructionsRandomizer:
    @staticmethod
    def get_random():
        drive_instructions = control.DriveInstructions()
        drive_instructions.gas = random.random()
        drive_instructions.brakes = random.random()
        drive_instructions.steering = random.uniform(-1, 1)
        drive_instructions.optimal_speed = random.uniform(0, 80)
        return drive_instructions

class ControlRandomizer:
    def __init__(self, drive_instructions):
        self.drive_instructions = drive_instructions

    @staticmethod
    def get_random():
        drive_instructions = DriveInstructionsRandomizer.get_random()
        return ControlRandomizer(drive_instructions)

