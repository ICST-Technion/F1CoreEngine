import random

import common_pb2 as common
from SmartRandomizer import SmartRandomizer


class Vector2DRandomizer:
    proximityRandomizer = SmartRandomizer([(random.uniform, -1, 1), (random.uniform, -1, 1)])

    @staticmethod
    def get_random():
        randomList = Vector2DRandomizer.proximityRandomizer.getRandom()
        vector2D = common.Vector2D()
        vector2D.x = randomList[0]
        vector2D.y = randomList[1]
        return vector2D


class Vector3DRandomizer:
    proximityRandomizer = SmartRandomizer([(random.uniform, -1, 1), (random.uniform, -1, 1), (random.uniform, -1, 1)])

    @staticmethod
    def get_random():
        randomList = Vector3DRandomizer.proximityRandomizer.getRandom()
        vector3D = common.Vector3D()
        vector3D.x = randomList[0]
        vector3D.y = randomList[1]
        vector3D.z = randomList[2]
        return vector3D
