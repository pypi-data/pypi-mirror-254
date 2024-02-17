class NodeViewBase(object):
  def __init__(self, linkName: str, label: str):
    self.linkName = linkName
    self.label = label

  def copy(self) -> 'NodeViewBase':
    return self.__class__(self.linkName, self.label)

  def toDict(self) -> dict:
    return dict(class_name=self.__class__.__name__, linkName=self.linkName, label=self.label)


class NodeCheckboxView(NodeViewBase):
  """
  The class for UI representation of a port that contains boolean value

  .. image:: img/views/checkbox_view.png

  *node that contains this view*

  :param linkName: The name of the boolean port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Value'):
    super().__init__(linkName, label)


class NodeComboboxView(NodeViewBase):
  """
  The class for the UI representation of the port and gives the ability to choose from several predefined values

  .. image:: img/views/combobox_view.png

  *node that contains this view*

  :param linkName: The name of the port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str
  :param values: list of the values that will be diplayed on the node
  :type values: list
  """
  def __init__(self, linkName: str, label: str, values: list):
    super().__init__(linkName, label)
    self.values = values

  def copy(self) -> 'NodeComboboxView':
    return self.__class__(self.linkName, self.label, self.values)

  def toDict(self) -> dict:
    value = super().toDict()
    value['values'] = self.values
    return value


class NodeFloatView(NodeViewBase):
  """
  The class for UI representation of a port that contains float value

  .. image:: img/views/float_view.png

  *node that contains this view*

  :param linkName: The name of the float port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Value'):
    super().__init__(linkName, label)


class NodeImageView(NodeViewBase):
  """
  The class for UI representation of a port that contains image value

  .. image:: img/views/image_view.png

  *node that contains this view*

  :param linkName: The name of the image port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Image'):
    super().__init__(linkName, label)


class NodeIntegerView(NodeViewBase):
  """
  The class for UI representation of a port that contains integer value

  .. image:: img/views/integer_view.png

  *node that contains this view*

  :param linkName: The name of the integer port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  :param readonly: The flag that determines whether the value can be changed by user
  :type readonly: bool, optional
  :param rangeTop: Maximum possible value
  :type rangeTop: int, optional
  :param rangeBottom: Minimum possible value
  :type rangeBottom: int, optional
  """
  def __init__(self, linkName: str, label: str = 'Value', readonly: bool = False, rangeTop: int = None, rangeBottom: int = None):
    super().__init__(linkName, label)
    self.readonly = readonly
    self.rangeTop = rangeTop
    self.rangeBottom = rangeBottom

  def copy(self) -> 'NodeIntegerView':
    return self.__class__(self.linkName, self.label, self.readonly, self.rangeTop, self.rangeBottom)

  def toDict(self) -> dict:
    value = super().toDict()
    value['readonly'] = self.readonly
    value['rangeTop'] = self.rangeTop
    value['rangeBottom'] = self.rangeBottom
    return value


class NodePairComboView(NodeViewBase):
  """
  The class for the UI representation of the port and gives the ability to choose from several predefined values

  .. image:: img/views/pair_combobox_view.png

  *node that contains this view*

  :param linkName: The name of the port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str
  :param items: dict of the values that will be displayed on the node. The key of the dict will be set to port as value and the value of the dict will be displayed on the node.
  :type items: dict
  """
  def __init__(self, linkName: str, label: str, items: dict):
    super().__init__(linkName, label)
    self.items = items

  def copy(self) -> 'NodePairComboView':
    return self.__class__(self.linkName, self.label, self.items)

  def toDict(self) -> dict:
    value = super().toDict()
    value['items'] = self.items
    return value


class NodePointView(NodeViewBase):
  """
  The class for UI representation of a port that contains :class:`PointWithUnit <mh_en_exec.nodes.common.PointWithUnit>` value

  .. image:: img/views/point_view.png

  *node that contains this view*

  :param linkName: The name of the point port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Point'):
    super().__init__(linkName, label)


class NodeRectView(NodeViewBase):
  """
  The class for UI representation of a port that contains :class:`RectWithUnit <mh_en_exec.nodes.common.RectWithUnit>` value

  .. image:: img/views/rect_view.png

  *node that contains this view*

  :param linkName: The name of the rect port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Rect'):
    super().__init__(linkName, label)


class NodeStringView(NodeViewBase):
  """
  The class for UI representation of a port that contains string value

  .. image:: img/views/string_view.png

  *node that contains this view*

  :param linkName: The name of the string port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Value'):
    super().__init__(linkName, label)


class NodeTextBoxView(NodeViewBase):
  """
  The class for UI representation of a port that contains multiline string value

  .. image:: img/views/textbox_view.png

  *node that contains this view*

  :param linkName: The name of the string port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Text', hint: str = None):
    super().__init__(linkName, label)
    self.hint = hint

  def copy(self) -> 'NodeTextBoxView':
    return self.__class__(self.linkName, self.label, self.hint)

  def toDict(self) -> dict:
    value = super().toDict()
    value['hint'] = self.hint
    return value


class NodeVectorView(NodeViewBase):
  """
  The class for UI representation of a port that contains :class:`VectorWithUnit <mh_en_exec.nodes.common.VectorWithUnit>` value

  .. image:: img/views/vector_view.png

  *node that contains this view*

  :param linkName: The name of the vector port for which this object will be the UI representation
  :type linkName: str
  :param label: The text that will be displayed on the node
  :type label: str, optional
  """
  def __init__(self, linkName: str, label: str = 'Vector'):
    super().__init__(linkName, label)
