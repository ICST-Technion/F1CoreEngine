from typing import List

import random

import perception_pb2 as perception
import Common as common


class ConeTypeRandomizer():
    @staticmethod
    def get_random():
        return random.choice(list(perception.ConeType.values()))


class ConeRandomizer:
    @staticmethod
    def get_random():
        cone = perception.Cone()
        cone.cone_id = random.randint(0, 100)  # this is just a guess
        cone.x = random.uniform(-1, 1)
        cone.y = random.uniform(-1, 1)
        cone.z = random.uniform(-1, 1)
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
    @staticmethod
    def get_random():
        boundingBox = perception.BoundingBox()
        boundingBox.cone_id = random.randint(0, 100)
        boundingBox.type = ConeTypeRandomizer.get_random()
        boundingBox.height = random.random()
        boundingBox.width = random.random()
        boundingBox.length = random.random()
        boundingBox.frame_position.CopyFrom(FramePositionRandomizer.get_random())
        boundingBox.position.CopyFrom(common.Vector3DRandomizer.get_random())
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
    def __init__(self, cone_map, box_map=None):
        self.cone_map = cone_map
        self.box_map = box_map  # this member might be inaccurate

    @staticmethod
    def get_random(debug=False):
        cone_map = ConeMapRandomizer.get_random()

        if debug:
            box_map = PerceptionGroundTruthRandomizer.get_random()
            return Perception(cone_map, box_map)
        else:
            return Perception(cone_map)
