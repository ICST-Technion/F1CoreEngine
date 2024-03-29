# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensors.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsensors.proto\x12\x1aTechnionFormulaAV.Messages\x1a\x0c\x63ommon.proto\"]\n\tIMUConfig\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12=\n\x0fsensor_position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\"]\n\tGPSConfig\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12=\n\x0fsensor_position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\"|\n\x0c\x43\x61meraConfig\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12=\n\x0fsensor_position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\x0c\n\x04hfov\x18\x03 \x01(\x02\x12\x0c\n\x04vfov\x18\x04 \x01(\x02\"\xc5\x01\n\x11\x44\x65pthCameraConfig\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12=\n\x0fsensor_position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\x0c\n\x04hfov\x18\x03 \x01(\x02\x12\x0c\n\x04vfov\x18\x04 \x01(\x02\x12\x42\n\tdata_type\x18\x05 \x01(\x0e\x32/.TechnionFormulaAV.Messages.DepthCameraDataType\"\xe8\x01\n\x0e\x43\x61rMeasurments\x12 \n\x18wheel_velocity_rear_left\x18\x01 \x01(\x01\x12!\n\x19wheel_velocity_rear_right\x18\x02 \x01(\x01\x12!\n\x19wheel_velocity_front_left\x18\x03 \x01(\x01\x12\"\n\x1awheel_velocity_front_right\x18\x04 \x01(\x01\x12\x19\n\x11throttle_position\x18\x05 \x01(\x01\x12\x16\n\x0esteering_angle\x18\x06 \x01(\x01\x12\x17\n\x0f\x62rakes_position\x18\x07 \x01(\x01\"\xd2\x02\n\x0eIMUMeasurments\x12:\n\x0c\x61\x63\x63\x65leration\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\x42\n\x14\x61ngular_acceleration\x18\x03 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\x36\n\x08velocity\x18\x04 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12>\n\x10\x61ngular_velocity\x18\x05 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\x39\n\x0borientation\x18\x06 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\x12\r\n\x05speed\x18\x07 \x01(\x02\"\x87\x01\n\tIMUSensor\x12\x35\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.TechnionFormulaAV.Messages.IMUConfig\x12\x43\n\x0fimu_measurments\x18\x02 \x01(\x0b\x32*.TechnionFormulaAV.Messages.IMUMeasurments\"\x89\x01\n\x07\x43\x61rData\x12\x39\n\nimu_sensor\x18\x01 \x01(\x0b\x32%.TechnionFormulaAV.Messages.IMUSensor\x12\x43\n\x0f\x63\x61r_measurments\x18\x02 \x01(\x0b\x32*.TechnionFormulaAV.Messages.CarMeasurments\"z\n\tGPSSensor\x12\x35\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.TechnionFormulaAV.Messages.GPSConfig\x12\x36\n\x08position\x18\x02 \x01(\x0b\x32$.TechnionFormulaAV.Messages.Vector3D\"\x8d\x01\n\x0c\x43\x61meraSensor\x12\x38\n\x06\x63onfig\x18\x01 \x01(\x0b\x32(.TechnionFormulaAV.Messages.CameraConfig\x12\x14\n\x0c\x66rame_number\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\x0e\n\x06pixels\x18\x05 \x01(\x0c\"\x97\x01\n\x11\x44\x65pthCameraSensor\x12=\n\x06\x63onfig\x18\x01 \x01(\x0b\x32-.TechnionFormulaAV.Messages.DepthCameraConfig\x12\x14\n\x0c\x66rame_number\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\x0e\n\x06pixels\x18\x05 \x01(\x0c*6\n\x13\x44\x65pthCameraDataType\x12\x0f\n\x0b\x44\x43H_Float32\x10\x00\x12\x0e\n\nDCS_UInt16\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensors_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEPTHCAMERADATATYPE._serialized_start=1851
  _DEPTHCAMERADATATYPE._serialized_end=1905
  _IMUCONFIG._serialized_start=59
  _IMUCONFIG._serialized_end=152
  _GPSCONFIG._serialized_start=154
  _GPSCONFIG._serialized_end=247
  _CAMERACONFIG._serialized_start=249
  _CAMERACONFIG._serialized_end=373
  _DEPTHCAMERACONFIG._serialized_start=376
  _DEPTHCAMERACONFIG._serialized_end=573
  _CARMEASURMENTS._serialized_start=576
  _CARMEASURMENTS._serialized_end=808
  _IMUMEASURMENTS._serialized_start=811
  _IMUMEASURMENTS._serialized_end=1149
  _IMUSENSOR._serialized_start=1152
  _IMUSENSOR._serialized_end=1287
  _CARDATA._serialized_start=1290
  _CARDATA._serialized_end=1427
  _GPSSENSOR._serialized_start=1429
  _GPSSENSOR._serialized_end=1551
  _CAMERASENSOR._serialized_start=1554
  _CAMERASENSOR._serialized_end=1695
  _DEPTHCAMERASENSOR._serialized_start=1698
  _DEPTHCAMERASENSOR._serialized_end=1849
# @@protoc_insertion_point(module_scope)
