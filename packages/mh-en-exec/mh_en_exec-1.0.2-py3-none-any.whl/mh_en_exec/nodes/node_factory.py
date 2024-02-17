from .node_base import NodeBase
from .exceptions import NodeRegistrationError, NodeNotFoundError

class NodeFactory(object):
  def __init__(self) -> None:
    super().__init__()
    self._nodes = {}
    self._names = {}

  def registerNode(self, node: NodeBase):
    if node is None:
      raise ValueError('node param is invalid')

    name = node.NODE_NAME
    node_path = node.getNodePath()

    if name in self._names:
      raise NodeRegistrationError(f'Node name "{name}" is already registered')

    if self._nodes.get(node_path.lower()):
      raise NodeRegistrationError(f'Node "{node_path}" is already registered')

    self._nodes[node_path.lower()] = node
    self._names[name] = node_path.lower()

  def getNodesStructures(self) -> list:
    result = []
    for identifier, node in self._nodes.items():
      result.append(node.getNodeStructure())
    return result

  def getNodeClass(self, path) -> NodeBase:
    if not self.isPathValid(path):
      raise ValueError('invalid path')

    nodeClass = self._nodes.get(path.lower(), None)
    if not nodeClass:
      raise NodeNotFoundError(f'Node {path} was not found')
    return nodeClass

  def isPathValid(self, path: str):
    if not path:
      return False

    return path.find(' ') == -1
