from typing import List

import Perception as perception
import Common as common
from enum import Enum
import random
from math import pi

import state_est_pb2 as state_estimation


class CarStateRandomizer:
    @staticmethod
    def get_random():
        car_state = state_estimation.CarState()
        car_state.position.CopyFrom(common.Vector2DRandomizer.get_random())
        car_state.position_deviation.CopyFrom(common.Vector2DRandomizer.get_random())
        car_state.velocity.CopyFrom(common.Vector2DRandomizer.get_random())
        car_state.velocity_deviation.CopyFrom(common.Vector2DRandomizer.get_random())
        car_state.theta = random.uniform(0, 2 * pi)
        car_state.theta_deviation = random.uniform(0, 2 * pi)
        car_state.theta_dot = random.uniform(0, 2 * pi)
        car_state.theta_dot_deviation = random.uniform(0, 2 * pi)
        car_state.steering_angle = random.uniform(0, 2 * pi)
        car_state.steering_angle_deviation = random.uniform(0, 2 * pi)
        car_state.acceleration = random.uniform(-1, 1)
        car_state.acceleration_deviation = random.uniform(-1, 1)
        return car_state


class ClusterInfoRandomizer:
    @staticmethod
    def get_random():
        cluster_info = state_estimation.ClusterInfo()
        cluster_info.age = random.randint(0, 100)  # this is just a guess
        cluster_info.num_of_cones = random.randint(1, 5)  # this is just a guess
        cluster_info.extra = random.uniform(-1, 1)  # this is just a guess
        return cluster_info


class FormulaStateMessageTypeRandomizer(Enum):
    @staticmethod
    def get_random():
        return random.choice(list(state_estimation.FormulaStateMessageType.values()))


class StateConeRandomizer:
    @staticmethod
    def get_random():
        state_cone = state_estimation.StateCone()
        state_cone.cone_id = random.randint(0, 100)  # this is just a guess
        state_cone.r = random.uniform(0, 100)  # this is just a guess
        state_cone.alpha = random.uniform(0, 2 * pi)
        state_cone.position.CopyFrom(common.Vector2DRandomizer.get_random())
        state_cone.type = perception.ConeTypeRandomizer.get_random()
        state_cone.position_deviation = random.uniform(-1, 1)  # this is just a guess
        state_cone.cluster_info.CopyFrom(ClusterInfoRandomizer.get_random())
        return state_cone


class FormulaStateRandomizer:
    @staticmethod
    def get_random():
        formula_state = state_estimation.FormulaState()
        for i in range(0, random.randint(1, 10)):
            formula_state.right_bound_cones.append(StateConeRandomizer.get_random())

        for i in range(0, random.randint(1, 10)):
            formula_state.left_bound_cones.append(StateConeRandomizer.get_random())

        formula_state.current_state.CopyFrom(CarStateRandomizer.get_random())
        formula_state.distance_to_finish = random.uniform(0, 100)  # this is just a guess
        formula_state.message_type = FormulaStateMessageTypeRandomizer.get_random()

        formula_state.distance_from_left = random.uniform(0, 100)  # this is just a guess
        formula_state.distance_from_right = random.uniform(0, 100)  # this is just a guess
        formula_state.road_angle = random.uniform(0, 2 * pi)
        return formula_state


class StateEstimationRandomizer:
    def __init__(self, formula_state):
        self.formula_state = formula_state

    @staticmethod
    def get_random():
        formula_state = FormulaStateRandomizer.get_random()
        return StateEstimationRandomizer(formula_state)
