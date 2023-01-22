from typing import List

import random

import perception_pb2 as perception
import Common as common
from SmartRandomizer import SmartRandomizer
from Logger import Logger


class ConeTypeRandomizer():
    @staticmethod
    def get_random():
        return random.choice(list(perception.ConeType.values()))


class ConeRandomizer:
    proximityRandomizer = SmartRandomizer([(random.uniform, -1, 1), (random.uniform, -1, 1), (random.uniform, -1, 1)])

    @staticmethod
    def get_random():
        randomList = ConeRandomizer.proximityRandomizer.getRandom()
        cone = perception.Cone()
        cone.cone_id = random.randint(0, 100)  # this is just a guess
        cone.x = randomList[0]
        cone.y = randomList[1]
        cone.z = randomList[2]
        cone.type = ConeTypeRandomizer.get_random()
        cone.confidence = random.random()
        return cone


class ConeMapRandomizer:
    @staticmethod
    def get_random():
        cone_map = perception.ConeMap()
        for i in range(0, random.randint(1, 10)):
            cone_map.cones.append(ConeRandomizer.get_random())
        return cone_map


class FramePositionRandomizer:
    @staticmethod
    def get_random():
        frame_position = perception.FramePosition()
        frame_position.u = random.randint(0, 100)  # this is just a guess
        frame_position.v = random.randint(0, 100)  # this is just a guess
        frame_position.depth = random.randint(0, 100)  # this is just a guess
        return frame_position


class BoundingBoxRandomizer:

    positionRandomizer = common.Vector3DRandomizer(proximity=True)
    @staticmethod
    def get_random():
        boundingBox = perception.BoundingBox()
        boundingBox.cone_id = random.randint(0, 100)
        boundingBox.type = ConeTypeRandomizer.get_random()
        boundingBox.height = random.random()
        boundingBox.width = random.random()
        boundingBox.length = random.random()
        boundingBox.frame_position.CopyFrom(FramePositionRandomizer.get_random())
        boundingBox.position.CopyFrom(BoundingBoxRandomizer.positionRandomizer.get_random())
        return boundingBox


class PerceptionGroundTruthRandomizer:
    @staticmethod
    def get_random():
        bounding_boxes = perception.PerceptionGroundTruth()
        bounding_boxes.has_bounding_boxes_truth = True
        for i in range(0, random.randint(1, 10)):
            bounding_boxes.bbs.append(BoundingBoxRandomizer.get_random())
        return bounding_boxes


class Perception:

    @staticmethod
    def send_message(debug=False):
        cone_map = ConeMapRandomizer.get_random()

        if debug:
            box_map = PerceptionGroundTruthRandomizer.get_random()
            Logger.log(common.MessageWrapper(cone_map, common.Module.PERCEPTION_MODULE, "cones"))
            Logger.log(common.MessageWrapper(box_map, common.Module.PERCEPTION_MODULE, "boxes"))
        else:
            Logger.log(common.MessageWrapper(cone_map, common.Module.PERCEPTION_MODULE, "cones").message)


