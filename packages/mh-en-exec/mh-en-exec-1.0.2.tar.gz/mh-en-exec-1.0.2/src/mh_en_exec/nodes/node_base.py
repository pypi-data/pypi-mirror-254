import logging
from collections import OrderedDict

from ..resource import ResourceManager
from .constants import *
from .exceptions import PortNotFound
from .ports import (ActionNodeInput, ActionNodeOutput, ImageNodeInput, ImageNodeOutput,
                    NodeInputBase, NodeLocalBase, NodeOutputBase)
from .views import NodeViewBase


class NodeMeta(type):
  @classmethod
  def __prepare__(cls, name, bases):
    return OrderedDict()

  def __new__(cls, name, bases, clsdict):
    clsobj = super().__new__(cls, name, bases, dict(clsdict))
    inputs = getattr(clsobj, '_node_inputs_').copy() if hasattr(clsobj, '_node_inputs_') else OrderedDict()
    outputs = getattr(clsobj, '_node_outputs_').copy() if hasattr(clsobj, '_node_outputs_') else OrderedDict()
    locals = getattr(clsobj, '_locals_').copy() if hasattr(clsobj, '_locals_') else OrderedDict()
    views = getattr(clsobj, '_node_views').copy() if hasattr(clsobj, '_node_views') else {}
    for key, val in clsdict.items():
      if isinstance(val, NodeInputBase):
        val.key = key
        inputs[key] = val
      elif isinstance(val, NodeOutputBase):
        val.key = key
        outputs[key] = val
      elif isinstance(val, NodeLocalBase):
        val.key = key
        locals[key] = val
      elif isinstance(val, NodeViewBase):
        views[key] = val
    setattr(clsobj, '_node_inputs_', inputs)
    setattr(clsobj, '_node_outputs_', outputs)
    setattr(clsobj, '_locals_', locals)
    setattr(clsobj, '_node_views', views)
    return clsobj


class NodeBase(metaclass=NodeMeta):
  """
  The NodeBase class is the base class for the nodes
  To create external node, need to inherit this class and implement :func:`perform <mh_en_exec.nodes.NodeBase.perform>` function
  """
  NODE_NAME = 'Node Base'
  __package_path__ = 'external_node.data'
  __type__ = NODE_TYPE_DATA
  __can_be_public__ = False
  __disable__ = False

  def __init__(self, id_, name=NODE_NAME) -> None:
    super().__init__()
    self._logger = logging.getLogger(__name__.split('.')[0])
    self._id = id_
    self._name = name
    self._node_inputs = OrderedDict()
    self._node_outputs = OrderedDict()
    self._node_locals = OrderedDict()
    self._views = {}
    self._changed_values = {}
    for name, inpt in self._node_inputs_.items():
      self._addInput(name, inpt.copy())
    for name, outpt in self._node_outputs_.items():
      self._addOutput(name, outpt.copy())
    for name, local in self._locals_.items():
      self._addLocal(name, local.copy())
    for name, view in self._node_views.items():
      self._addView(name, view.copy())

  @classmethod
  def getNodePath(cls):
    return cls.__package_path__ + '.' + cls.__name__

  @classmethod
  def getNodeStructure(cls):
    return dict(
      classname=cls.__name__,
      name=cls.NODE_NAME,
      identifier=cls.getNodePath(),
      type=cls.__type__,
      is_public=cls.__can_be_public__,
      is_disabled=cls.__disable__,
      inputs=dict((k, v.toDict()) for k, v in cls._node_inputs_.items()),
      outputs=dict((k, v.toDict()) for k, v in cls._node_outputs_.items()),
      locals=dict((k, v.toDict()) for k, v in cls._locals_.items()),
      views=dict((k, v.toDict()) for k, v in cls._node_views.items())
    )

  @property
  def id(self) -> str:
    return self._id

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  def perform(self, *args, **kwargs) -> tuple:
    """
    | This function is called when a node is executed on the Machine Heads side.
    | Input port values will be set as arguments of this function.
    | Output port values need to be set as a return values of this function.
    | Return type:
    | In case of data node: `tuple[{output port values}]`
    | In case of action node: `bool, tuple[{output port values}]`
    | *first value of the action node return values is a bool value. If `True` `out_on_success` port will be called, if `False` `out_on_failure` port will be called*

    :raises NotImplementedError: In case of function is not overrode
    """
    raise NotImplementedError()

  def updatePortValues(self, ports):
    for key, value in ports.items():
      port = self._node_locals.get(key, None)
      if not port:
        port = self._node_inputs.get(key, None)
      if not port:
        port = self._node_outputs.get(key, None)
      if not port:
        # raise PortNotFound(f'Port {key} does not exist')
        self._logger.error(f'Port {key} does not exist')
        continue
      if value:
        port.deserialize(value)
      else:
        port.value = value

  def execute(self, portName, inputPorts):
    outputs = None
    inputArgs = []
    performFunction = self.perform
    self._logger.debug(f'execite function called. portName: {portName}, inputPorts: {inputPorts}')
    if portName:
      inputPort = self._node_inputs.get(portName, None)
      if inputPort and isinstance(inputPort, ActionNodeInput):
        inputArgs = inputPort.args
        performFunction = getattr(self, inputPort.functionName)
    inputsCount = len([inp for inp in self._node_inputs.values() if not isinstance(inp, ActionNodeInput)])
    inputs = self._prepareInputs(inputPorts)
    if len(inputs) != inputsCount:
      raise ValueError(f'Expected {inputsCount} input parameters, but there is {len(inputs)} in node {self.name}')
    try:
      self._logger.debug(f'Calling perform function: {performFunction}, args: {inputArgs}, kwargs: {inputs}')
      outputs = performFunction(*inputArgs, **inputs)
      self._logger.debug(f'Perform function called: {performFunction}')
    except NotImplementedError:
      return None
    except Exception as e:
      self._logger.exception('Node execution failed')
    self._logger.debug(f'_prepareOutputs: {outputs}')
    result = self._prepareOutputs(outputs)
    return result

  def getSerializedLocals(self) -> dict:
    result = {}
    for key, value in self._node_locals.items():
      result[key] = value.serialize()
    return result

  def _prepareInputs(self, values):
    if not values:
      return {}
    result = {}
    resourceManager = ResourceManager.getInstance()
    self._logger.debug('Preparing inputs...')
    self._logger.debug(f'values: {values}')
    for key, val in values.items():
      self._logger.debug(f'key: {key}, val: {val}')
      if val is not None:
        if isinstance(self._node_inputs[key], ImageNodeInput):
          self._logger.debug(f'{self._node_inputs[key]} is an instance of the ImageNodeInput')
          resource = resourceManager.getResource(val)
          if resource is None:
            result[key] = None
          else:
            result[key] = resource
        else:
          self._logger.debug(f'{self._node_inputs[key]} is not an instance of the ImageNodeInput')
          result[key] = self._node_inputs[key].deserialize(val)
      elif key in self._node_inputs:
        result[key] = self._node_inputs[key].defaultValue
      else:
        result[key] = None
    return result

  def _prepareOutputs(self, values):
    if not isinstance(values, tuple):
      values = (values,)
    self._logger.debug('Preparing outputs...')
    result = {}
    resourceManager = ResourceManager.getInstance()
    keys = list(self._node_outputs.keys())
    if values is not None and len(values) != len(keys):
      raise ValueError(f'Expected {len(keys)} output parameters, but there is {len(values)} in node {self.name}')
    for i, key in enumerate(keys):
      if isinstance(self._node_outputs[key], ImageNodeOutput):
        self._logger.debug(f'{self._node_outputs[key]} is an instance of the ImageNodeOutput')
        img = values[i]
        if img is not None:
          resId = resourceManager.createResource(img, ResourceManager.TYPE_CV2_IMAGE)
          self._node_outputs[key].value = resId
      else:
        self._logger.debug(f'{self._node_outputs[key]} is not an instance of the ImageNodeOutput')
        self._node_outputs[key].value = values[i] if values is not None else None
      result[key] = self._node_outputs[key].serialize()
    return result

  def _addInput(self, name, input):
    if not hasattr(input, 'key'):
      input.key = name
    input.onValueChanged = self._onPortValueChanged
    setattr(self, name, input)
    self._node_inputs[name] = input

  def _addOutput(self, name, output):
    if not hasattr(output, 'key'):
      output.key = name
    output.onValueChanged = self._onPortValueChanged
    setattr(self, name, output)
    self._node_outputs[name] = output

  def _addLocal(self, name, local):
    if not hasattr(local, 'key'):
      local.key = name
    local.onValueChanged = self._onPortValueChanged
    setattr(self, name, local)
    self._node_locals[name] = local

  def _addView(self, name, view):
    self._views[name] = view

  def _onPortValueChanged(self, key, value):
    self._changed_values[key] = value


class ActionNodeBase(NodeBase):
  """
  The ActionNodeBase class is the base class for the action nodes
  To create external action node, need to inherit this class and implement :func:`perform <mh_en_exec.nodes.ActionNodeBase.perform>` function
  """
  __package_path__ = 'external_node.actions'
  __type__ = NODE_TYPE_ACTION

  in_action = ActionNodeInput()
  out_on_success = ActionNodeOutput()
  out_on_failure = ActionNodeOutput()

  def _prepareOutputs(self, outputs):
    self._logger.debug('Preparing outputs...')
    if outputs is None:
      return None
    result = {}
    resourceManager = ResourceManager.getInstance()
    data_keys = [key for key, port in self._node_outputs.items() if not isinstance(port, ActionNodeOutput)]
    action_keys = [key for key, port in self._node_outputs.items() if isinstance(port, ActionNodeOutput)]
    node_result, values = outputs
    if node_result:
      port = self._node_outputs.get(self.out_on_success.key, None)
      if port:
        port.value.result = True
    else:
      port = self._node_outputs.get(self.out_on_failure.key, None)
      if port:
        port.value.result = True
    if values is not None and len(values) != len(data_keys):
      raise ValueError(f'Expected {len(data_keys)} output parameters, but there is {len(values)} in node {self.name}')
    for i, key in enumerate(data_keys):
      if isinstance(self._node_outputs[key], ImageNodeOutput):
        self._logger.debug(f'{self._node_outputs[key]} is an instance of the ImageNodeOutput')
        img = values[i]
        if img is not None:
          resId = resourceManager.createResource(img, ResourceManager.TYPE_CV2_IMAGE)
          port = self._node_outputs[key]
          port.value = resId
          result[key] = port.serialize()
      else:
        self._logger.debug(f'{self._node_outputs[key]} is not an instance of the ImageNodeOutput')
        port = self._node_outputs[key]
        port.value = values[i] if values is not None else None
        result[key] = port.serialize()
    for key in action_keys:
      port = self._node_outputs[key]
      result[key] = port.serialize()
      port.value.result = False
    return result
