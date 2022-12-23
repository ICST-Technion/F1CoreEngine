from enum import Enum

from typing import List

import random


class ConeType(Enum):
    UnkownType = 0
    Yellow = 1
    Blue = 2
    Orange = 3
    OrangeBig = 4

    @staticmethod
    def get_random():
        return random.choice(list(ConeType))


class Cone:
    def __init__(self, cone_id: int, x: float, y: float, z: float,
                 type: ConeType, confidence: float):
        self.cone_id = cone_id
        self.x = x  # Ease/West
        self.y = y  # North/South
        self.z = z  # Up/Down
        self.type = type
        self.confidence = confidence

    @staticmethod
    def get_random():
        cone_id = random.randint(0, 100)  # this is just a guess
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        type = ConeType.get_random()
        confidence = random.random()
        return Cone(cone_id, x, y, z, type, confidence)


class ConeMap:
    def __init__(self, cones: List[Cone]):
        self.cones = cones

    @staticmethod
    def get_random():
        cones = []
        for i in range(0, random.randint(1, 10)):
            cones.append(Cone.get_random())
        return ConeMap(cones)


class FramePosition:
    def __init__(self, u: int, v: int, depth: int):
        self.u = u
        self.v = v
        self.depth = depth

    @staticmethod
    def get_random():
        u = random.randint(0, 100)  # this is just a guess
        v = random.randint(0, 100)  # this is just a guess
        depth = random.randint(0, 100)  # this is just a guess
        return FramePosition(u, v, depth)


class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def get_random():
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        return Vector3D(x, y, z)


class BoundingBox:
    def __init__(self, cone_id: int, type: ConeType, height: float,
                 width: float, length: float, frame_position: FramePosition,
                 position: Vector3D):
        self.cone_id = cone_id
        self.type = type
        self.height = height
        self.width = width
        self.length = length
        self.frame_position = frame_position
        self.position = position

    @staticmethod
    def get_random():
        cone_id = random.randint(0, 100)
        type = ConeType.get_random()
        height = random.random()
        width = random.random()
        length = random.random()
        frame_position = FramePosition.get_random()
        position = Vector3D.get_random()
        return BoundingBox(cone_id, type, height, width, length,
                           frame_position, position)


class PerceptionGroundTruth:
    def __init__(self, debug: bool, bbs: List[BoundingBox]):
        self.has_bounding_boxes = debug
        self.bbs = bbs

    @staticmethod
    def get_random():
        bbs = []
        for i in range(0, random.randint(1, 10)):
            bbs.append(BoundingBox.get_random())
        return PerceptionGroundTruth(True, bbs)


class Perception:
    def __init__(self, cone_map: ConeMap, box_map: PerceptionGroundTruth = None):
        self.cone_map = cone_map
        self.box_map = box_map  # this member might be inaccurate

    @staticmethod
    def get_random(debug=False):
        cone_map = ConeMap.get_random()

        if debug:
            box_map = PerceptionGroundTruth.get_random()
            return Perception(cone_map, box_map)
        else:
            return Perception(cone_map)
