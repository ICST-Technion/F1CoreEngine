from concurrent import futures

import grpc
from google.protobuf import any_pb2

import fservice_pb2_grpc
from timescaleDBAdapter import timescaleDBAdapter
from control_pb2 import DriveInstructions
from common_pb2 import Module
from fservice_pb2 import MessageAck
from perception_pb2 import PerceptionGroundTruth, ConeMap
from state_est_pb2 import FormulaState


class MessagePassingServicer(fservice_pb2_grpc.MessagePassingServicer):

    def __init__(self):
        self.dbadapter = timescaleDBAdapter()
        self.currentSimulation = 0

    def SimulationStart(self, request, context):
        self.currentSimulation = request.simulationid
        return MessageAck(ackmessage=f'Simlation {self.currentSimulation} started')

    def SimulationEnd(self, request, context):
        if request.simulationid != self.currentSimulation:
            return MessageAck(ackmessage=f'Error, simulation {request.simulationid} is not running')
        else:
            self.currentSimulation = request.simulationid
            return MessageAck(ackmessage=f'Simulation {request.simulationid} ended')

    def GetCarState(self, request, context):
        dict = {
            "position vector": (request.position.x, request.position.y),
            "position deviation vector": (request.position_deviation.x, request.position_deviation.y),
            "velocity vector": (request.velocity.x, request.velocity.y),
            "velocity deviation vector": (request.velocity_deviation.x, request.velocity_deviation.y),
            "theta": request.theta,
            "theta deviation": request.theta_deviation,
            "theta dot": request.theta_dot,
            "theta dot deviation": request.theta_dot_deviation,
            "steering angle": request.steering_angle,
            "steering angle deviation": request.steering_angle_deviation,
            "acceleration": request.acceleration,
            "acceleration deviation": request.acceleration_deviation
        }
        self.dbadapter.insert_into_car_state(dict)
        return MessageAck(ackmessage="Got CarState")

    def GetTimedDriveInstructions(self, request, context):
        dict = {
            "exp_num": self.currentSimulation,
            "gas": request.gas,
            "brakes": request.brakes,
            "steering": request.steering,
            "optimal_speed": request.optimal_speed,
            "time_stamp": request.time_stamp
        }
        self.dbadapter.insert_into_drive_instructions(dict)
        return MessageAck(ackmessage="Got TimedDriveInstructions")

    def GetMessage(self, request, context):
        any_message = any_pb2.Any()
        any_message.CopyFrom(request.data)
        my_message = None
        if request.header.source == Module.CONTROL_MODULE:
            # The message is DriveInstruction
            my_message = DriveInstructions()
        elif request.header.source == Module.STATE_EST_MODULE:
            # The message is FormulaState
            my_message = FormulaState()
        elif request.header.source == Module.PERCEPTION_MODULE:
            if request.header.triggers[0].type_url == "boxes":
                # The message is PerceptionGroundTruth
                my_message = PerceptionGroundTruth()
            else:
                # The message is ConeMap
                my_message = ConeMap()

        if my_message is None:
            return MessageAck(ackmessage="Invalid Message Type")

        any_message.Unpack(my_message)
        print(type(my_message))
        return MessageAck(ackmessage="Got Message")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    fservice_pb2_grpc.add_MessagePassingServicer_to_server(
        MessagePassingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('Starting server')
    serve()
