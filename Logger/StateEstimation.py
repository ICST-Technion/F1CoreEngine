from typing import List

import Perception
from enum import Enum
import random
from math import pi


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def get_random():
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        return Vector2D(x, y)


class CarState:
    def __init__(self, position: Vector2D, position_deviation: Vector2D,
                 velocity: Vector2D, velocity_deviation: Vector2D,
                 theta: float, theta_deviation: float,
                 theta_dot: float, theta_dot_deviation: float,
                 steering_angle: float, steering_angle_deviation: float,
                 acceleration: float, acceleration_deviation: float):
        self.position = position
        self.position_deviation = position_deviation

        self.velocity = velocity
        self.velocity_deviation = velocity_deviation

        self.theta = theta
        self.theta_deviation = theta_deviation

        self.theta_dot = theta_dot
        self.theta_dot_deviation = theta_dot_deviation

        self.steering_angle = steering_angle
        self.steering_angle_deviation = steering_angle_deviation

        self.acceleration = acceleration
        self.acceleration_deviation = acceleration_deviation

    @staticmethod
    def get_random():
        position = Vector2D.get_random()
        position_deviation = Vector2D.get_random()
        velocity = Vector2D.get_random()
        velocity_deviation = Vector2D.get_random()
        theta = random.uniform(0, 2 * pi)
        theta_deviation = random.uniform(0, 2 * pi)
        theta_dot = random.uniform(0, 2 * pi)
        theta_dot_deviation = random.uniform(0, 2 * pi)
        steering_angle = random.uniform(0, 2 * pi)
        steering_angle_deviation = random.uniform(0, 2 * pi)
        acceleration = random.uniform(-1, 1)
        acceleration_deviation = random.uniform(-1, 1)
        return CarState(position, position_deviation, velocity, velocity_deviation,
                        theta, theta_deviation, theta_dot, theta_dot_deviation,
                        steering_angle, steering_angle_deviation,
                        acceleration, acceleration_deviation)


class ClusterInfo:
    def __init__(self, age: int, num_of_cones: int, extra: float):
        self.age = age
        self.num_of_cones = num_of_cones
        self.extra = extra

    @staticmethod
    def get_random():
        age = random.randint(0, 100)  # this is just a guess
        num_of_cones = random.randint(1, 5)  # this is just a guess
        extra = random.uniform(-1, 1)  # this is just a guess
        return ClusterInfo(age, num_of_cones, extra)


class FormulaStateMessageType(Enum):
    only_prediction = 0
    prediction_and_correction = 1
    still_calibrating = 2
    finished_lap = 3

    @staticmethod
    def get_random():
        return random.choice(list(FormulaStateMessageType))


class StateCone:
    def __init__(self, cone_id: int, r: float, alpha: float, position: Vector2D,
                 type: Perception.ConeType, position_deviation: float, cluster_info: ClusterInfo):
        self.cone_id = cone_id
        self.r = r
        self.alpha = alpha
        self.position = position
        self.type = type
        self.position_deviation = position_deviation
        self.cluster_info = cluster_info

    @staticmethod
    def get_random():
        cone_id = random.randint(0, 100)  # this is just a guess
        r = random.uniform(0, 100)  # this is just a guess
        alpha = random.uniform(0, 2 * pi)
        position = Vector2D.get_random()
        type = Perception.ConeType.get_random()
        position_deviation = random.uniform(-1, 1)  # this is just a guess
        cluster_info = ClusterInfo.get_random()
        return StateCone(cone_id, r, alpha, position, type, position_deviation, cluster_info)


class FormulaState:
    def __init__(self, right_bound_cones: List[StateCone], left_bound_cones: List[StateCone],
                 current_state: CarState, distance_to_finish: float, message_type: FormulaStateMessageType,
                 distance_from_left: float, distance_from_right: float, road_angle: float):
        self.right_bound_cones = right_bound_cones
        self.left_bound_cones = left_bound_cones
        self.current_state = current_state
        self.distance_to_finish = distance_to_finish
        self.message_type = message_type

        self.distance_from_left = distance_from_left
        self.distance_from_right = distance_from_right
        self.road_angle = road_angle

    @staticmethod
    def get_random():
        right_bound_cones = []
        for i in range(0, random.randint(1, 10)):
            right_bound_cones.append(StateCone.get_random())

        left_bound_cones = []
        for i in range(0, random.randint(1, 10)):
            left_bound_cones.append(StateCone.get_random())

        current_state = CarState.get_random()
        distance_to_finish = random.uniform(0, 100)  # this is just a guess
        message_type = FormulaStateMessageType.get_random()

        distance_from_left = random.uniform(0, 100)  # this is just a guess
        distance_from_right = random.uniform(0, 100)  # this is just a guess
        road_angle = random.uniform(0, 2 * pi)
        return FormulaState(right_bound_cones, left_bound_cones, current_state, distance_to_finish,
                            message_type, distance_from_left, distance_from_right, road_angle)


class StateEstimation:
    def __init__(self, formula_state: FormulaState):
        self.formula_state = formula_state

    @staticmethod
    def get_random():
        formula_state = FormulaState.get_random()
        return StateEstimation(formula_state)
