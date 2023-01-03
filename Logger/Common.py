import random

import common_pb2 as common
from SmartRandomizer import SmartRandomizer


class Vector2DRandomizer:

    def __init__(self, proximity=False):
        self.proximity = proximity
        if proximity:
            self.proximityRandomizer = SmartRandomizer([(random.uniform, -1, 1), (random.uniform, -1, 1)])

    def get_random(self):
        vector2D = common.Vector2D()
        if self.proximity:
            randomList = self.proximityRandomizer.getRandom()
            vector2D.x = randomList[0]
            vector2D.y = randomList[1]
        else:
            vector2D.x = random.uniform(-1, 1)
            vector2D.y = random.uniform(-1, 1)

        return vector2D


class Vector3DRandomizer:

    def __init__(self, proximity=False):
        self.proximity = proximity
        if proximity:
            self.proximityRandomizer = SmartRandomizer([(random.uniform, -1, 1), (random.uniform, -1, 1), (random.uniform, -1, 1)])

    def get_random(self):
        vector3D = common.Vector3D()
        if self.proximity:
            randomList = self.proximityRandomizer.getRandom()
            vector3D.x = randomList[0]
            vector3D.y = randomList[1]
            vector3D.z = randomList[2]
        else:
            vector3D.x = random.uniform(-1, 1)
            vector3D.y = random.uniform(-1, 1)
            vector3D.z = random.uniform(-1, 1)
        return vector3D
