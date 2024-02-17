from .main import _createServer

_server = None


def start(nodes, port=50051):
  """
  Start external node server

  :param nodes: list of node classes
  :type nodes: list[NodeBase]
  :param port: server port number
  :type port: int
  """
  global _server
  _server = _createServer(nodes, port)
  _server.start()


def exec(nodes, port=50051):
  """
  Start external node server and wait for termination

  :param nodes: list of node classes
  :type nodes: list[NodeBase]
  :param port: server port number
  :type port: int
  """
  global _server
  _server = _createServer(nodes, port)
  _server.start()
  _server.wait_for_termination()
