from concurrent import futures

import grpc

import fservice_pb2_grpc
from timescaleDBAdapter import timescaleDBAdapter


class MessagePassingServicer(fservice_pb2_grpc.MessagePassingServicer):

    def __init__(self):
        self.dbadapter = timescaleDBAdapter()
        self.currentSimulation = 0

    def SimulationStart(self, request, context):
        self.currentSimulation = request.simulationid
        return MessageAck(f'Simlation {self.currentSimulation} started')

    def SimulationEnd(self, request, context):
        if request.simulationid != self.currentSimulation:
            return MessageAck(f'Error, simulation {request.simulationid} is not running')
        else:
            self.currentSimulation = request.simulationid
            return MessageAck(f'Simulation {request.simulationid} ended')

    def GetCarState(self, request, context):
        dict = {
            "position vector": (request.position.x, request.position.y),
            "position deviation vector": (request.position_deviation.x, request.position_deviation.y),
            "velocity vector": (request.velocity.x, request.velocity.y),
            "velocity deviation vector": (request.velocity_deviation.x, request.velocity_deviation.y),
            "theta": request.theta,
            "theta deviation": request.theta_deviation,
            "theta dot": request.theta_dot,
            "theta dot deviation" request.theta_dot_deviation:,
            "steering angle": request.steering_angle,
            "steering angle deviation": request.steering_angle_deviation,
            "acceleration":request.acceleration,
            "acceleration deviation": request.acceleration_deviation
        }
        self.dbadapter.insert_into_car_state(dict)
        return MessageAck("Got CarState")

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
        return MessageAck("Got TimedDriveInstructions")


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