import random
from enum import Enum

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

class Module(Enum):
    UNKNOWN_MODULE = 0
    CONTROL_MODULE = 1
    STATE_EST_MODULE = 2
    PERCEPTION_MODULE = 3
    REAL_TIME_DATA_MODULE = 4
    SERVER = 5

class MessageWrapper:
    id = 0

    def __init__(self, data, module, trigger=""):
        header = common.Header()
        header.id = MessageWrapper.id
        if module == Module.PERCEPTION_MODULE:
            header.source = common.Module.PERCEPTION_MODULE
        elif module == Module.STATE_EST_MODULE:
            header.source = common.Module.STATE_EST_MODULE
        elif module == Module.CONTROL_MODULE:
            header.source = common.Module.CONTROL_MODULE
        header.timestamp.GetCurrentTime()
        if trigger != "":
            header.triggers.append(common.TriggerMessage(type_url=trigger, id=MessageWrapper.id))

        self.message = common.Message()
        self.message.header.CopyFrom(header)
        self.message.data.Pack(data)
        MessageWrapper.id += 1


