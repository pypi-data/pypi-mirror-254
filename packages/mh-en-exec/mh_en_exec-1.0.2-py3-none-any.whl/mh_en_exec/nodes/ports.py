from collections import OrderedDict
from copy import copy

from mh_en_exec.resource import ResourceManager

from .common import PointWithUnit, RectWithUnit, VectorWithUnit


class Descriptor:
  def __init__(self, name=None):
    self.name = name

  def __set__(self, instance, value):
    instance.__dict__[self.name] = value

  def __get__(self, instance, type=None):
    if instance is None:
      return None
    return instance.__dict__[self.name]

  def __delete__(self, instance):
    raise AttributeError("Can't delete")


class Any():
  pass


class Action(object):
  def __init__(self, result=False):
    self.result = result


class Typed(Descriptor):
  ty = object

  def __set__(self, instance, value):
    if value is not None and not isinstance(value, self.ty) and self.ty != Any:
      import traceback
      traceback.print_stack()
      raise TypeError('Expected %s' % self.ty)
    super().__set__(instance, value)

  def __serialize__(self, instance):
    if instance is None:
      return None
    if instance.__dict__[self.name] is None:
      return None
    if self.ty in (int, float, bool, str, list, Any):
      return copy(instance.__dict__[self.name])
    else:
      return copy(instance.__dict__[self.name].__dict__)

  def __deserialize__(self, instance, value):
    if instance is None:
      return None
    if self.ty in (int, float, bool, str, Any):
      instance.__dict__[self.name] = value
    else:
      if instance.__dict__[self.name] is None:
        instance.__dict__[self.name] = self.ty()
      for key, val in value.items():
        instance.__dict__[self.name].__dict__[key] = val
    return instance.__dict__[self.name]


class NodeLinkMeta(type):
  @classmethod
  def __prepare__(cls, name, bases):
    return OrderedDict()

  def __new__(cls, name, bases, clsdict):
    valueKey = None
    fields = []
    for key, val in clsdict.items():
      if isinstance(val, Descriptor):
        clsdict[key].name = key
        valueKey = key
        fields.append(key)
    clsobj = super().__new__(cls, name, bases, dict(clsdict))

    def _serialize(self):
      return clsdict['_value'].__serialize__(self)

    def _deserialize(self, value):
      return clsdict['_value'].__deserialize__(self, value)
    setattr(clsobj, 'serialize', _serialize)
    setattr(clsobj, 'deserialize', _deserialize)
    if valueKey:
      setattr(clsobj, '_value_type', clsdict[valueKey].ty)
    return clsobj


class NodeLink(object, metaclass=NodeLinkMeta):
  _value = Typed()

  def __init__(self, defaultValue=None):
    self._value = None
    if defaultValue is not None:
      if isinstance(defaultValue, dict):
        self._value = self.deserialize(defaultValue)
      else:
        self._value = defaultValue
    self.defaultValue = self.serialize()
    self.port = None

  def copy(self):
    obj = self.__class__(self.defaultValue)
    if hasattr(self, 'key'):
      obj.key = self.key
    return obj

  @property
  def value(self):
    """
    Port value property
    """
    return self._value

  @value.setter
  def value(self, value):
    self._value = value
    if hasattr(self, 'key'):
      self.onValueChanged(self.key, self.serialize())

  def toDict(self):
    return dict(
        key=getattr(self, 'key', ''),
        default_value=self.defaultValue,
        type_name=self.__class__.__name__
    )

  def onValueChanged(self, key, value):
    raise NotImplementedError()


class NodeInputBase(NodeLink):
  pass


class NodeOutputBase(NodeLink):
  pass


class NodeLocalBase(NodeLink):
  pass


class Cv2Image(Typed):
  ty = str


class AnyType(Typed):
  ty = Any


class StringType(Typed):
  ty = str


class ListType(Typed):
  ty = list


class Boolean(Typed):
  ty = bool


class Integer(Typed):
  ty = int


class Float(Typed):
  ty = float


class RectangleType(Typed):
  ty = RectWithUnit


class ActionType(Typed):
  ty = Action


class PointType(Typed):
  ty = PointWithUnit


class PointsType(Typed):
  ty = list


class VectorType(Typed):
  ty = VectorWithUnit

  def _extractValueKeys(self) -> tuple:
    return (('x', Float), ('y', Float), ('unit', StringType), ('magnitude', Float))

  def __serialize__(self, instance):
    if instance.__dict__[self.name] is None:
      return None
    v = instance.__dict__[self.name]
    return {'x': v.x, 'y': v.y, 'unit': v.unit, 'magnitude': v.magnitude}

  def __deserialize__(self, instance, value):
    instance.__dict__[self.name] = VectorWithUnit(value['x'], value['y'], value['unit'])
    return instance.__dict__[self.name]


class BooleanNodeInput(NodeInputBase):
  """
  Boolean node input port class
  """
  _value = Boolean()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: bool
    """
    return self._value


class BooleanNodeOutput(NodeOutputBase):
  """
  Boolean node output port class
  """
  _value = Boolean()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: bool
    """
    return self._value


class BooleanNodeLocal(NodeLocalBase):
  """
  Boolean node local port class
  """
  _value = Boolean()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: bool
    """
    return self._value


class IntegerNodeInput(NodeInputBase):
  """
  Integer node input port class
  """
  _value = Integer()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: int
    """
    return self._value


class IntegerNodeOutput(NodeOutputBase):
  """
  Integer node output port class
  """
  _value = Integer()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: int
    """
    return self._value


class IntegerNodeLocal(NodeLocalBase):
  """
  Integer node local port class
  """
  _value = Integer()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: int
    """
    return self._value


class FloatNodeInput(NodeInputBase):
  """
  Float node input port class
  """
  _value = Float()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: float
    """
    return self._value


class FloatNodeOutput(NodeOutputBase):
  """
  Float node output port class
  """
  _value = Float()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: float
    """
    return self._value


class FloatNodeLocal(NodeLocalBase):
  """
  Float node local port class
  """
  _value = Float()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: float
    """
    return self._value


class ImageNodeInput(NodeInputBase):
  """
  Image node input port class
  """
  _value = Cv2Image()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: image id
    :rtype: str
    """
    return self._value


class ImageNodeOutput(NodeOutputBase):
  """
  Image node output port class
  """
  _value = Cv2Image()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: image id
    :rtype: str
    """
    return self._value


class ImageNodeLocal(NodeLocalBase):
  """
  Image node local port class
  """
  _value = Cv2Image()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: OpenCV image
    :rtype: Mat
    """
    resourceManager = ResourceManager.getInstance()
    res = resourceManager.getResource(self._value)
    if res is not None:
      return res[2]
    return None


class RectangleNodeInput(NodeInputBase):
  """
  Rectangle node input port class
  """
  _value = RectangleType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: rectangle
    :rtype: RectWithUnit
    """
    return self._value


class RectangleNodeOutput(NodeOutputBase):
  """
  Rectangle node output port class
  """
  _value = RectangleType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: rectangle
    :rtype: RectWithUnit
    """
    return self._value


class RectangleNodeLocal(NodeLocalBase):
  """
  Rectangle node local port class
  """
  _value = RectangleType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: rectangle
    :rtype: RectWithUnit
    """
    return self._value


class PointNodeInput(NodeInputBase):
  """
  Point node input port class
  """
  _value = PointType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: point
    :rtype: PointWithUnit
    """
    return self._value


class PointNodeOutput(NodeOutputBase):
  """
  Point node output port class
  """
  _value = PointType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: point
    :rtype: PointWithUnit
    """
    return self._value


class PointNodeLocal(NodeLocalBase):
  """
  Point node local port class
  """
  _value = PointType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: point
    :rtype: PointWithUnit
    """
    return self._value


class AnyNodeInput(NodeInputBase):
  """
  Any node input port class
  """
  _value = AnyType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: any
    """
    return self._value


class AnyNodeOutput(NodeOutputBase):
  """
  Any node output port class
  """
  _value = AnyType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: any
    """
    return self._value


class ActionNodeInput(NodeInputBase):
  """
  Action node input port class
  """
  _value = ActionType()

  def __init__(self, functionName='perform', args=[], defaultValue=Action()):
    super().__init__(defaultValue=defaultValue)
    self.functionName = functionName
    self.args = args

  def copy(self):
    return self.__class__(self.functionName, self.args, self.defaultValue)

  def toDict(self):
    result = super().toDict()
    result['functionName'] = self.functionName
    result['args'] = self.args
    return result

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: Action
    """
    return self._value


class ActionNodeOutput(NodeOutputBase):
  """
  Action node output port class
  """
  _value = ActionType()

  def __init__(self, defaultValue=Action()):
    super().__init__(defaultValue=defaultValue)

  def copy(self):
    return self.__class__(self.defaultValue)

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: Action
    """
    return self._value


class StringNodeLocal(NodeLocalBase):
  """
  String node local port class
  """
  _value = StringType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: str
    """
    return self._value


class StringNodeInput(NodeInputBase):
  """
  String node input port class
  """
  _value = StringType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: str
    """
    return self._value


class StringNodeOutput(NodeOutputBase):
  """
  String node output port class
  """
  _value = StringType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: value
    :rtype: str
    """
    return self._value


class VectorNodeInput(NodeInputBase):
  """
  Vector node input port class
  """
  _value = VectorType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: vector
    :rtype: VectorWithUnit
    """
    return self._value


class VectorNodeOutput(NodeOutputBase):
  """
  Vector node output port class
  """
  _value = VectorType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: vector
    :rtype: VectorWithUnit
    """
    return self._value


class VectorNodeLocal(NodeLocalBase):
  """
  Vector node local port class
  """
  _value = VectorType()

  @NodeLink.value.getter
  def value(self):
    """
    Port value property

    :return: vector
    :rtype: VectorWithUnit
    """
    return self._value


class ListNodeLocal(NodeLocalBase):
  _value = ListType()


class ListNodeInput(NodeInputBase):
  _value = ListType()


class ListNodeOutput(NodeOutputBase):
  _value = ListType()
