import Perception
import StateEstimation
import Control


def to_gRPC(state):
    return state


class Logger:

    @staticmethod
    def log(message):
        to_gRPC(message)



