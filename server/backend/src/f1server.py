import datetime
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
        self.dbadapter.insert_new_experiment({
            "exp_id": request.simulationid,
            "created_at": datetime.datetime.fromtimestamp((timestamp := request.timestamp).seconds + timestamp.nanos / 1e9, tz=datetime.timezone.utc)
        })
        return MessageAck(ackmessage=f'Simulation {self.currentSimulation} started')

    def SimulationEnd(self, request, context):
        print(request)
        if request.simulationid != self.currentSimulation:
            return MessageAck(ackmessage=f'Error, simulation {request.simulationid} is not running')
        else:
            self.currentSimulation = request.simulationid
            self.dbadapter.finish_experiment({
                "exp_id": request.simulationid,
                "finished_at": datetime.datetime.fromtimestamp(
                    (timestamp := request.timestamp).seconds + timestamp.nanos / 1e9, tz=datetime.timezone.utc)
            })
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
            any_message.Unpack(my_message)
            dict = {
                "exp_id": self.currentSimulation,
                "gas": my_message.gas,
                "brakes": my_message.brakes,
                "steering": my_message.steering,
                "optimal_speed": my_message.optimal_speed,
                "time_stamp": datetime.datetime.fromtimestamp((timestamp := request.header.timestamp).seconds + timestamp.nanos / 1e9, tz=datetime.timezone.utc)
            }
            self.dbadapter.insert_into_drive_instructions(dict)
            return MessageAck(ackmessage="Got Drive Instruction Message")

        elif request.header.source == Module.STATE_EST_MODULE:
            # The message is FormulaState
            my_message = FormulaState()
            any_message.Unpack(my_message)
            dict = {
                "exp_id": self.currentSimulation,
                "position_vector": (my_message.current_state.position.x, my_message.current_state.position.y),
                "position_deviation_vector": (my_message.current_state.position_deviation.x, my_message.current_state.position_deviation.y),
                "velocity_vector": (my_message.current_state.velocity.x, my_message.current_state.velocity.y),
                "velocity_deviation_vector": (my_message.current_state.velocity_deviation.x, my_message.current_state.velocity_deviation.y),
                "theta": my_message.current_state.theta,
                "theta_deviation": my_message.current_state.theta_deviation,
                "theta_dot": my_message.current_state.theta_dot,
                "theta_dot_deviation": my_message.current_state.theta_dot_deviation,
                "steering_angle": my_message.current_state.steering_angle,
                "steering_angle_deviation": my_message.current_state.steering_angle_deviation,
                "acceleration": my_message.current_state.acceleration,
                "acceleration_deviation": my_message.current_state.acceleration_deviation,
                "time_stamp": datetime.datetime.fromtimestamp(
                    (timestamp := request.header.timestamp).seconds + timestamp.nanos / 1e9, tz=datetime.timezone.utc)
            }
            self.dbadapter.insert_into_car_state(dict)
            return MessageAck(ackmessage="Got Car State Message")

        elif request.header.source == Module.PERCEPTION_MODULE:
            if request.header.triggers[0].type_url == "boxes":
                # The message is PerceptionGroundTruth
                my_message = PerceptionGroundTruth()
            else:
                # The message is ConeMap
                my_message = ConeMap()

        print(type(my_message))
        return MessageAck(ackmessage="Message Not Supported")


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
