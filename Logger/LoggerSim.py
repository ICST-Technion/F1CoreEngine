import Perception
import StateEstimation
import Control


def to_gRPC(state):
    return state


class Logger:

    @staticmethod
    def get_random_perception():
        return to_gRPC(Perception.Perception.get_random(debug=True))

    @staticmethod
    def get_random_state_estimation():
        return to_gRPC(StateEstimation.StateEstimation.get_random())

    @staticmethod
    def get_random_contol():
        return to_gRPC(Control.Control.get_random())




