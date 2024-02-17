import logging
from .connection import (ConnectionGrpc, ConnectionListenerBase,
                         ConnectionResourceListenerBase)
from .nodes import NodeManager
from .resource import ResourceManager


class _ConnectionListener(ConnectionListenerBase):
  def __init__(self) -> None:
    self._nodesManager = NodeManager.getInstance()
    self._logger = logging.getLogger(__name__.split('.')[0])

  def onGetNodesStructures(self) -> list:
    self._logger.debug(f'onGetNodesStructures')
    return self._nodesManager.getNodesStructures()

  def onGetCurrentNodes(self) -> dict:
    result = {}
    for key, node in self._nodesManager.nodes.items():
      result[key] = node.getNodePath()
    return result

  def onCreateNode(self, id_, path, name) -> 'tuple[bool, str]':
    return self._nodesManager.createNodeInstance(id_, path, name)

  def onUpdatePortValues(self, id_, ports) -> 'tuple[bool, str]':
    return self._nodesManager.updateNodePortValues(id_, ports)

  def onNodeExecution(self, id_, portName, inputPorts) -> 'tuple[bool, str, dict, dict]':
    return self._nodesManager.executeNode(id_, portName, inputPorts)

  def onRemoveNode(self, id_) -> 'tuple[bool, str]':
    return self._nodesManager.removeNode(id_)


class _ConnectionResourceListener(ConnectionResourceListenerBase):
  def __init__(self) -> None:
    self._resourceManager = ResourceManager.getInstance()
    self._logger = logging.getLogger(__name__.split('.')[0])

  def onResourceReceive(self, id_, type_, data) -> bool:
    # print('onResourceReceive')
    # print(f'id: {id_}, type: {type_}, datalen: {len(data)}')
    self._logger.debug(f'onResourceReceive id: {id_}, type: {type_}')
    result = self._resourceManager.createResourceFromBytes(
        data, type_, id_=id_)
    # print(f'result: {result}')
    return result is not None

  def onGetResource(self, id_, remove) -> 'tuple[str, str, bytes]':
    # print('onGetResource')
    # print(f'id: {id_}, remove: {remove}')
    self._logger.debug(f'onGetResource id: {id_}, remove: {remove}')
    result = self._resourceManager.getResourceBytes(id_)
    if remove:
      self._resourceManager.removeResource(id_)
    return result

  def onReleaseResource(self, id_) -> 'tuple[bool, str]':
    self._logger.debug(f'onReleaseResource id: {id_}')
    if id_ not in self._resourceManager.resources:
      return False, 'Resource does not exist'
    self._resourceManager.removeResource(id_)
    return True, ''


def _createServer(nodes, port):
  logger = logging.getLogger(__name__.split('.')[0])
  ch = logging.StreamHandler()
  formatter = logging.Formatter(
      '%(asctime)s %(levelname)s [%(name)s] %(message)s')
  ch.setFormatter(formatter)
  logger.addHandler(ch)

  nodesManager = NodeManager.getInstance()
  nodesManager.registerNodes(nodes)

  logger.debug('creating grpc server')
  _listener = _ConnectionListener()
  _resourceListener = _ConnectionResourceListener()
  server = ConnectionGrpc.createServerInstance(
      _listener, _resourceListener, port=port)
  return server
