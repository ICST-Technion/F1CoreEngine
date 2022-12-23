import random

import common_pb2 as common


class Vector2DRandomizer:
    @staticmethod
    def get_random():
        vector2D = common.Vector2D()
        vector2D.x = random.uniform(-1, 1)
        vector2D.y = random.uniform(-1, 1)
        return vector2D


class Vector3DRandomizer:
    @staticmethod
    def get_random():
        vector3D = common.Vector3D()
        vector3D.x = random.uniform(-1, 1)
        vector3D.y = random.uniform(-1, 1)
        vector3D.z = random.uniform(-1, 1)
        return vector3D
