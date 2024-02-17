from abc import ABC, abstractmethod
import logging


class ConnectionListenerBase(ABC):
  @abstractmethod
  def onGetNodesStructures(self) -> list:
    ...

  @abstractmethod
  def onGetCurrentNodes(self) -> dict:
    ...

  @abstractmethod
  def onCreateNode(self, id_, path, name) -> 'tuple[bool, str]':
    ...

  @abstractmethod
  def onUpdatePortValues(self, id_, values) -> 'tuple[bool, str]':
    ...

  @abstractmethod
  def onNodeExecution(self, id_, portName, values) -> 'tuple[bool, str, dict, dict]':
    ...

  @abstractmethod
  def onRemoveNode(self, id_) -> 'tuple[bool, str]':
    ...


class ConnectionResourceListenerBase(ABC):
  @abstractmethod
  def onResourceReceive(self, id_, type_, data) -> bool:
    ...

  @abstractmethod
  def onGetResource(self, id_, remove) -> 'tuple[str, str, bytes]':
    ...

  @abstractmethod
  def onReleaseResource(self, id_) -> 'tuple[bool, str]':
    ...


class ConnectionBase(object):
  def __init__(self, eventListener=None, resourceListener=None):
    self._eventListener = eventListener
    self._resourceListener = resourceListener
    self._logger = logging.getLogger(__name__.split('.')[0])

  @property
  def eventListener(self) -> ConnectionListenerBase:
    return self._eventListener

  @eventListener.setter
  def eventListener(self, value):
    self._eventListener = value

  @property
  def resourceListener(self) -> ConnectionResourceListenerBase:
    return self._resourceListener

  @resourceListener.setter
  def resourceListener(self, value):
    self._resourceListener = value

  def _getNodesStructuresEmit(self) -> list:
    if self.eventListener:
      return self.eventListener.onGetNodesStructures()
    return None

  def _getCurrentExistingNodesEmit(self) -> dict:
    if self.eventListener:
      return self.eventListener.onGetCurrentNodes()
    return None

  def _createNodeEmit(self, id_, path, name):
    if self.eventListener:
      return self.eventListener.onCreateNode(id_, path, name)
    errorMessage = 'Event listener not set'
    self._logger.error(errorMessage)
    return False, errorMessage

  def _updatePortValues(self, id_, values):
    if self.eventListener:
      return self.eventListener.onUpdatePortValues(id_, values)
    errorMessage = 'Event listener not set'
    self._logger.error(errorMessage)
    return False, errorMessage

  def _nodeExecutionEmit(self, id_, portName, values):
    if self.eventListener:
      return self.eventListener.onNodeExecution(id_, portName, values)
    errorMessage = 'Event listener not set'
    self._logger.error(errorMessage)
    return False, errorMessage, None, None

  def _removeNodeEmit(self, id_):
    if self.eventListener:
      return self.eventListener.onRemoveNode(id_)
    errorMessage = 'Event listener not set'
    self._logger.error(errorMessage)
    return False, errorMessage

  def _resourceReceivedEmit(self, id_, type_, data):
    if self.resourceListener:
      return self.resourceListener.onResourceReceive(id_, type_, data)
    return None

  def _getResourceEmit(self, id_, remove):
    if self.resourceListener:
      return self.resourceListener.onGetResource(id_, remove)
    return None

  def _releaseResourceEmit(self, id_):
    if self.resourceListener:
      return self.resourceListener.onReleaseResource(id_)
    errorMessage = 'Event listener not set'
    self._logger.error(errorMessage)
    return False, errorMessage
