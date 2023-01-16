import grpc
import fservice_pb2_grpc
import fservice_pb2 as messages
from Perception import Perception
from StateEstimation import StateEstimation
from Control import Control

class Logger:

    channel = grpc.insecure_channel('localhost:50051')
    stub = fservice_pb2_grpc.MessagePassingStub(channel)
    messages = []

    @classmethod
    def newExperiment(cls, simid):
        startMsg = messages.SimulationStartRequest()
        startMsg.simulationid = simid
        ack = cls.stub.SimulationStart(startMsg)
        cls.messages.append(ack.ackmessage)

    @classmethod
    def endExperiment(cls, simid):
        endMsg = messages.NotifySimulationEnd()
        endMsg.simulationid = simid
        ack = cls.stub.SimulationStart(endMsg)
        cls.messages.append(ack.ackmessage)

    @classmethod
    def log(cls, message):
        # right now this is NOT CORRECT. the message can be one of 4 types, which are:
        # 1: DriveInstructions - from control
        # 2: FormulaState - from state estimation
        # 3: ConeMap - from perception
        # 4: PerceptionGroundTruth - from perception

        if isinstance(message, Perception):
            pass
        elif isinstance(message, StateEstimation):
            pass
        else:
            pass





