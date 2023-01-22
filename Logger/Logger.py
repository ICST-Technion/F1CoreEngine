
import grpc

import fservice_pb2_grpc
import fservice_pb2 as messages


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
        ack = cls.stub.GetMessage(message)
        cls.messages.append(ack.ackmessage)






