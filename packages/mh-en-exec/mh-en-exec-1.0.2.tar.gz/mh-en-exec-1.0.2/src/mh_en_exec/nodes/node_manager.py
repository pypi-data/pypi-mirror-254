import logging

from .exceptions import NodeNotFoundError, PortNotFound
from .node_base import NodeBase
from .node_factory import NodeFactory


class NodeManager(object):
  _instance = None

  def __init__(self) -> None:
    super().__init__()
    self._factory = NodeFactory()
    self._nodes = {}
    self._logger = logging.getLogger(__name__.split('.')[0])

  @property
  def nodes(self) -> 'dict[str, NodeBase]':
    return self._nodes

  @classmethod
  def getInstance(cls) -> 'NodeManager':
    if cls._instance is None:
      cls._instance = NodeManager()
    return cls._instance

  def registerNodes(self, nodes):
    for node in nodes:
      self._factory.registerNode(node)

  def getNodesStructures(self) -> list:
    return self._factory.getNodesStructures()

  def createNodeInstance(self, id_, path, name) -> 'tuple[bool, str]':
    self._logger.debug(f'creating node[{path}] instance: {{id: {id_}, name: {name}}}')
    nodeClass = None
    try:
      nodeClass = self._factory.getNodeClass(path)
    except NodeNotFoundError as e:
      errorMessage = str(e)
      self._logger.error(errorMessage)
      return False, errorMessage
    if id_ in self._nodes:
      errorMessage = f'The node with the id "{id_}" already exists'
      self._logger.error(errorMessage)
      return False, errorMessage
    node = nodeClass(id_, name)
    self._nodes[id_] = node
    return True, None

  def updateNodePortValues(self, id_, ports) -> 'tuple[bool, str]':
    self._logger.debug(f'updating port values: {{id: {id_}, ports: {ports}}}')
    node = self._nodes.get(id_, None)
    if not node:
      errorMessage = f'The node with the id {id_} does not exist'
      self._logger.error(errorMessage)
      return False, errorMessage

    if ports:
      try:
        node.updatePortValues(ports)
      except PortNotFound as e:
        errorMessage = str(e)
        self._logger.error(errorMessage)
        return False, errorMessage
    return True, None

  def executeNode(self, id_, portName, values) -> 'tuple[bool, str, dict, dict]':
    self._logger.debug(f'executing node: {{id: {id_}, portName: {portName}, ports: {values}}}')
    node = self._nodes.get(id_, None)
    if not node:
      errorMessage = f'The node with the id {id_} does not exist'
      self._logger.error(errorMessage)
      return False, errorMessage, None, None

    try:
      outputs = node.execute(portName, values)
      locals = node.getSerializedLocals()
    except KeyboardInterrupt as e:
      raise e
    except Exception as e:
      errorMessage = str(e)
      # self._logger.error(errorMessage)
      self._logger.exception(errorMessage)
      return False, errorMessage, None, None
    return True, '', locals, outputs

  def removeNode(self, id_) -> 'tuple[bool, str]':
    self._logger.debug(f'removing node: {{id: {id_}}}')
    if id_ not in self._nodes:
      errorMessage = f'The node with the id {id_} does not exist'
      self._logger.error(errorMessage)
      return False, errorMessage

    del self._nodes[id_]
    return True, None
