# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66service.proto\x12\x1aTechnionFormulaAV.Messages\x1a\x0c\x63ommon.proto\".\n\x16SimulationStartRequest\x12\x14\n\x0csimulationid\x18\x01 \x01(\x05\"+\n\x13NotifySimulationEnd\x12\x14\n\x0csimulationid\x18\x01 \x01(\x05\" \n\nMessageAck\x12\x12\n\nackmessage\x18\x01 \x01(\t2\xca\x02\n\x0eMessagePassing\x12o\n\x0fSimulationStart\x12\x32.TechnionFormulaAV.Messages.SimulationStartRequest\x1a&.TechnionFormulaAV.Messages.MessageAck\"\x00\x12j\n\rSimulationEnd\x12/.TechnionFormulaAV.Messages.NotifySimulationEnd\x1a&.TechnionFormulaAV.Messages.MessageAck\"\x00\x12[\n\nGetMessage\x12#.TechnionFormulaAV.Messages.Message\x1a&.TechnionFormulaAV.Messages.MessageAck\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIMULATIONSTARTREQUEST._serialized_start=60
  _SIMULATIONSTARTREQUEST._serialized_end=106
  _NOTIFYSIMULATIONEND._serialized_start=108
  _NOTIFYSIMULATIONEND._serialized_end=151
  _MESSAGEACK._serialized_start=153
  _MESSAGEACK._serialized_end=185
  _MESSAGEPASSING._serialized_start=188
  _MESSAGEPASSING._serialized_end=518
# @@protoc_insertion_point(module_scope)
