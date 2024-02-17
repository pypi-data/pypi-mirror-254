import json
from concurrent import futures

import grpc

from . import connection_pb2
from .connection_base import (ConnectionBase, ConnectionListenerBase,
                              ConnectionResourceListenerBase)
from .connection_pb2_grpc import (ConnectionGrpcServicer,
                                  add_ConnectionGrpcServicer_to_server)


class ConnectionGrpc(ConnectionBase, ConnectionGrpcServicer):
  def __init__(self, eventListener: ConnectionListenerBase, resourceListener: ConnectionResourceListenerBase):
    super().__init__(eventListener=eventListener, resourceListener=resourceListener)
    self.id = hex(id(self))

  # rpc GetNodeStructures(Empty) returns (GetNodeStructuresResponse) {}
  def GetNodeStructures(self, request, context):
    try:
      nodeStructures = self._getNodesStructuresEmit()
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.GetNodeStructuresResponse(serverId=self.id, jsonData=json.dumps(nodeStructures) if nodeStructures else None)

  # rpc GetCurrentExistingNodes(Empty) returns (GetCurrentExistingNodesResponse) {}
  def GetCurrentExistingNodes(self, request, context):
    try:
      nodes = self._getCurrentExistingNodesEmit()
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.GetCurrentExistingNodesResponse(serverId=self.id, jsonData=json.dumps(nodes) if nodes is not None else None)

  # rpc CreateNodeInstance(CreateNodeInstanceRequest) returns (CreateNodeInstanceResponse) {}
  def CreateNodeInstance(self, request, context):
    try:
      result, errorMessage = self._createNodeEmit(request.id, request.nodePath, request.name)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.CreateNodeInstanceResponse(serverId=self.id, result=result, errorMessage=errorMessage)

  # rpc UpdatePortValues(UpdatePortValuesRequest) returns (UpdatePortValuesResponse) {}
  def UpdatePortValues(self, request, context):
    portValues = json.loads(request.portValuesJson) if request.portValuesJson else None
    try:
      result, errorMessage = self._updatePortValues(request.id, portValues)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.UpdatePortValuesResponse(serverId=self.id, result=result, errorMessage=errorMessage)

  # rpc ExecuteNode(ExecuteNodeRequest) returns (ExecuteNodeResponse) {}
  def ExecuteNode(self, request, context):
    portValues = json.loads(request.inputPortValuesJson) if request.inputPortValuesJson else None
    try:
      result, errorMessage, locals, outputs = self._nodeExecutionEmit(request.id, request.portName, portValues)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.ExecuteNodeResponse(serverId=self.id, result=result, errorMessage=errorMessage, localPortValuesJson=json.dumps(locals) if locals else None, outputPortValuesJson=json.dumps(outputs) if outputs else None)

  # rpc RemoveNode(RemoveNodeRequest) returns (RemoveNodeResponse) {}
  def RemoveNode(self, request, context):
    try:
      result, errorMessage = self._removeNodeEmit(request.id)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.RemoveNodeResponse(serverId=self.id, result=result, errorMessage=errorMessage)

  # rpc SendResource(stream SendResourceRequest) returns (SendResourceResponse) {}
  def SendResource(self, request, context):
    try:
      result = self._resourceReceivedEmit(request.metadata.id, request.metadata.type, request.data.content)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.SendResourceResponse(serverId=self.id, result=result)

  # rpc GetResource(GetResourceRequest) returns (stream GetResourceResponse) {}
  def GetResource(self, request, context):
    try:
      id_, type_, data = self._getResourceEmit(request.id, request.remove)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.GetResourceResponse(serverId=self.id, metadata=connection_pb2.ResourceMetaData(id=id_, type=type_), data=connection_pb2.ResourceData(content=data))

  # rpc ReleaseResource(ReleaseResourceRequest) returns (ReleaseResourceResponse) {}
  def ReleaseResource(self, request, context):
    try:
      result, errorMessage = self._releaseResourceEmit(request.id)
    except Exception as e:
      self._logger.exception('Exception occured')
      raise e
    return connection_pb2.ReleaseResourceResponse(serverId=self.id, result=result, errorMessage=errorMessage)

  @classmethod
  def createServerInstance(cls, eventListener=None, resourceListener=None, port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ConnectionGrpcServicer_to_server(ConnectionGrpc(eventListener, resourceListener), server)
    server.add_insecure_port(f'[::]:{port}')
    return server


