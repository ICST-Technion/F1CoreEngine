
import grpc

import fservice_pb2_grpc
import fservice_pb2 as messages


class Logger:

    messages = []
    channel = None
    stub = None
    simid = None

    class ExpectedOpenConnection(Exception):
        def __init__(self):
            super.__init__("expected an to have an open connection here.")
    
    @classmethod
    def connect(cls, dst_url = 'localhost:50051'):
        try:
            cls.channel = grpc.insecure_channel(dst_url)
        except TypeError as e:
            trailer = ""
            if hasattr(e, 'message'):
                trailer = " error message: '"+e.message+"'"
            raise Exception("failed to connect to destination server." + trailer)
        cls.stub = fservice_pb2_grpc.MessagePassingStub(cls.channel)
    
    @classmethod
    def newExperiment(cls, simid):
        if cls.simid is not None:
            raise Exception("newExperiment called before current experiment had ended.")

        cls.simid = simid
        startMsg = messages.SimulationStartRequest()
        startMsg.simulationid = simid
        startMsg.timestamp.GetCurrentTime()
        if cls.stub is None:
            raise Logger.ExpectedOpenConnection()
        ack = cls.stub.SimulationStart(startMsg)
        cls.messages.append(ack.ackmessage)

    @classmethod
    def endExperiment(cls):
        endMsg = messages.NotifySimulationEnd()
        endMsg.simulationid = cls.simid
        endMsg.timestamp.GetCurrentTime()
        if cls.stub is None:
            raise Logger.ExpectedOpenConnection()
        ack = cls.stub.SimulationEnd(endMsg)
        cls.messages.append(ack.ackmessage)
        cls.simid = None

    @classmethod
    def log(cls, message):
        if cls.stub is None:
            raise Logger.ExpectedOpenConnection()
        ack = cls.stub.GetMessage(message)
        cls.messages.append(ack.ackmessage)






