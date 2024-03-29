# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dash.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import control_pb2 as control__pb2
import state_est_pb2 as state__est__pb2
import perception_pb2 as perception__pb2
import ground_truth_pb2 as ground__truth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndash.proto\x12\x1aTechnionFormulaAV.Messages\x1a\x0c\x63ommon.proto\x1a\rcontrol.proto\x1a\x0fstate_est.proto\x1a\x10perception.proto\x1a\x12ground_truth.proto\"\x91\x03\n\x10\x43ontrolDashbaord\x12\x43\n\x0cinstructions\x18\x01 \x01(\x0b\x32-.TechnionFormulaAV.Messages.DriveInstructions\x12>\n\x10\x63urrent_position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector2D\x12\x1e\n\x16\x63urrent_steering_angle\x18\x03 \x01(\x02\x12\x15\n\rcurrent_speed\x18\x04 \x01(\x02\x12\x15\n\roptimal_route\x18\x05 \x03(\x02\x12\x13\n\x0bright_bound\x18\x06 \x03(\x02\x12\x12\n\nleft_bound\x18\x07 \x03(\x02\x12@\n\x11right_bound_cones\x18\x08 \x03(\x0b\x32%.TechnionFormulaAV.Messages.StateCone\x12?\n\x10left_bound_cones\x18\t \x03(\x0b\x32%.TechnionFormulaAV.Messages.StateCone\"\x9a\x02\n\x10\x46ormulaStateDash\x12G\n\x15\x66ormula_state_message\x18\x01 \x01(\x0b\x32(.TechnionFormulaAV.Messages.FormulaState\x12;\n\x0c\x63one_samples\x18\x02 \x03(\x0b\x32%.TechnionFormulaAV.Messages.StateCone\x12<\n\rcone_clusters\x18\x03 \x03(\x0b\x32%.TechnionFormulaAV.Messages.StateCone\x12\x42\n\x0cground_truth\x18\x04 \x01(\x0b\x32,.TechnionFormulaAV.Messages.StateGroundTruth\"}\n\x0ePerceptionDash\x12\x34\n\x03\x62\x62s\x18\x01 \x03(\x0b\x32\'.TechnionFormulaAV.Messages.BoundingBox\x12\x35\n\x08\x63one_map\x18\x02 \x01(\x0b\x32#.TechnionFormulaAV.Messages.ConeMapb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dash_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTROLDASHBAORD._serialized_start=127
  _CONTROLDASHBAORD._serialized_end=528
  _FORMULASTATEDASH._serialized_start=531
  _FORMULASTATEDASH._serialized_end=813
  _PERCEPTIONDASH._serialized_start=815
  _PERCEPTIONDASH._serialized_end=940
# @@protoc_insertion_point(module_scope)
