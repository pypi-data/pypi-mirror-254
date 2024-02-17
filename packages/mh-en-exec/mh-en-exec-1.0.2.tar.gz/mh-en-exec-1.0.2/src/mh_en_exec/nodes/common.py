import math


class Size(object):
  """
  The Size class defines the size of a two-dimensional object using floating point precision.

  :param width: width
  :type width: float, optional
  :param height: height
  :type height: float, optional
  """
  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

  def __str__(self):
    return '{{width: {0}, height: {1}}}'.format(self.width, self.height)

  def __add__(self, other):
    return Size(self.width + other.width, self.height + other.height)

  def __sub__(self, other):
    return Size(self.width - other.width, self.height - other.height)

  def __eq__(self, other):
    return self.width == other.width and self.height == other.height


class Point(object):
  """
  The Point class defines the point in two-dimensional space using floating point precision.

  :param x: coordinate on the x-axis
  :type x: float, optional
  :param y: coordinate on the y-axis
  :type y: float, optional
  """
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '{{x: {0}, y: {1}}}'.format(self.x, self.y)

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  def __eq__(self, other):
    if other is None:
      return False
    return self.x == other.x and self.y == other.y


class PointWithUnit(Point):
  """
  The PointWithUnit class defines the point in two-dimensional space with particular unit using floating point precision.

  :param x: coordinate on the x-axis
  :type x: float, optional
  :param y: coordinate on the y-axis
  :type y: float, optional
  :param unit: coordinate unit
  :type unit: str, optional

  .. note::
    | *Coordinate Unit:*
    | 'px' - value in pixels
    | 'hu' - value in height units.
    | Ex. 1hu is `{height of the screen} / 100`
    | '%' - value in percentages.
    | Ex. 50% of the x is half of the width of the screen
  """

  POINT_UNIT_PX = 'px'
  POINT_UNIT_PER = '%'
  POINT_UNIT_HU = 'hu'

  def __init__(self, x=0, y=0, unit=POINT_UNIT_PX):
    super().__init__(x=x, y=y)
    self.unit = unit

  def __str__(self):
    return '{{x: {0}{2}, y: {1}{2}}}'.format(self.x, self.y, self.unit)

  def __add__(self, other):
    if self.unit != other.unit:
      raise ValueError('units of points is not equal')
    return PointWithUnit(self.x + other.x, self.y + other.y, self.unit)

  def __sub__(self, other):
    if self.unit != other.unit:
      raise ValueError('units of points is not equal')
    return PointWithUnit(self.x - other.x, self.y - other.y, self.unit)

  def __eq__(self, other):
    if other is None:
      return False
    return super().__eq__(other) and self.unit == other.unit

  @classmethod
  def lerp(cls, start, end, t):
    """
    Linearly interpolates between two points

    :param start: Start point
    :type start: PointWithUnit
    :param end: End point
    :type end: PointWithUnit
    :param t: value used to interpolate between `start` and `end`. Range between 0.0 and 1.0
    :type t: float
    """
    if start.unit != end.unit:
      raise ValueError('units of points is not equal')
    return PointWithUnit(start.x * (1.0 - t) + end.x * t, start.y * (1.0 - t) + end.y * t, start.unit)

  def toPx(self, size):
    """
    Returns PointWithUnit in pixel units

    :param size: Screen size
    :type size: Size

    :raises ValueError: In case of unknown unit value

    :return: point in pixel units
    :rtype: PointWithUnit
    """
    if size is None:
      return None
    if self.unit == self.POINT_UNIT_PX:
      return PointWithUnit(self.x, self.y, self.unit)
    elif self.unit == self.POINT_UNIT_PER:
      return PointWithUnit(size.width * (self.x / 100.0), size.height * (self.y / 100.0), self.POINT_UNIT_PX)
    elif self.unit == self.POINT_UNIT_HU:
      pxinhu = size.height / 100.0
      return PointWithUnit(self.x * pxinhu, self.y * pxinhu, self.POINT_UNIT_PX)
    else:
      raise ValueError('Unknown unit. unit: \"{}\"'.format(self.unit))


class Rect(object):
  """
  The Rect class defines the rectangle shape in two-dimensional space using floating point precision.

  :param left: leftmost coordinate on the x-axis
  :type left: float, optional
  :param top: topmost coordinate on the y-axis
  :type top: float, optional
  :param right: rightmost coordinate on the x-axis
  :type right: float, optional
  :param bottom: bottommost coordinate on the y-axis
  :type bottom: float, optional
  """
  def __init__(self, left=0, top=0, right=0, bottom=0):
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom

  def center(self):
    """
    Returns rectangle's center point

    :return: rectangle center
    :rtype: Point
    """
    size = self.size()
    return Point(self.left + (size.width / 2.0), self.top + (size.height / 2.0))

  def size(self):
    """
    Returns rectangle size

    :return: size
    :rtype: Size
    """
    return Size(self.right - self.left, self.bottom - self.top)

  def isInside(self, point):
    """
    Checks if the point is inside the rectangle

    :param point: point
    :type point: Point

    :return: True if inside and False if outside
    :rtype: bool
    """
    return point.x > self.left and point.x < self.right and point.y > self.top and point.y < self.bottom

  def isValid(self):
    """
    Checks if the rectangle is valid

    :return: True if valid and False if invalid
    :rtype: bool
    """
    if self.left == 0 and self.top == 0 and self.right == 0 and self.bottom == 0:
      return False
    if self.right <= self.left or self.bottom <= self.top:
      return False
    return True

  def getAxisSwapped(self):
    """
    Returns axis swapped rectangle

    :return: axis swapped rectangle
    :rtype: Rect
    """
    return Rect(self.top, self.left, self.bottom, self.right)

  def __add__(self, other):
    return Rect(self.left + other.left, self.top + other.top, self.right + other.right, self.bottom + other.bottom)

  def __sub__(self, other):
    return Rect(self.left - other.left, self.top - other.top, self.right - other.right, self.bottom - other.bottom)

  def __str__(self):
    return 'left: {}, top: {}, right: {}, bottom: {}'.format(self.left, self.top, self.right, self.bottom)

  def __mul__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return Rect(self.left * other, self.top * other, self.right * other, self.bottom * other)

  __rmul__ = __mul__


class RectWithUnit(Rect):
  """
  The RectWithUnit class defines the rectangle shape in two-dimensional space with particular unit using floating point precision.

  :param left: leftmost coordinate on the x-axis
  :type left: float, optional
  :param top: topmost coordinate on the y-axis
  :type top: float, optional
  :param right: rightmost coordinate on the x-axis
  :type right: float, optional
  :param bottom: bottommost coordinate on the y-axis
  :type bottom: float, optional
  :param unit: coordinate unit
  :type unit: str, optional

  .. note::
    | *Coordinate Unit:*
    | 'px' - value in pixels
    | 'hu' - value in height units.
    | Ex. 1hu is `{height of the screen} / 100`
    | '%' - value in percentages.
    | Ex. 50% of the x is half of the width of the screen
  """
  RECT_UNIT_PX = 'px'
  RECT_UNIT_PER = '%'
  RECT_UNIT_HU = 'hu'

  def __init__(self, left=0, top=0, right=0, bottom=0, unit=RECT_UNIT_PX):
    super().__init__(left, top, right, bottom)
    self.unit = unit

  def center(self):
    """
    Returns rectangle's center point

    :return: rectangle center
    :rtype: PointWithUnit
    """
    point = super().center()
    return PointWithUnit(point.x, point.y, self.unit)

  def isInside(self, point):
    """
    Checks if the point is inside the rectangle

    :param point: point
    :type point: PointWithUnit

    :raises ValueError: In case of unit value of the point is not the same as unit of the rectangle

    :return: True if inside and False if outside
    :rtype: bool
    """
    if hasattr(point, 'unit'):
      if point.unit != self.unit:
        raise ValueError(
            'Rect({}) and point({}) have different units'.format(self.unit, point.unit))
    else:
      if self.unit != self.RECT_UNIT_PX:
        raise ValueError('Rect({}) and point(px) have different units')
    return super().isInside(point)

  def isValid(self):
    """
    Checks if the rectangle is valid

    :return: True if valid and False if invalid
    :rtype: bool
    """
    if self.left == 0 and self.top == 0 and self.right == 0 and self.bottom == 0:
      return False
    if self.right <= self.left or self.bottom <= self.top:
      return False
    return True

  def getAxisSwapped(self):
    """
    Returns axis swapped rectangle

    :return: axis swapped rectangle
    :rtype: RectWithUnit
    """
    return RectWithUnit(self.top, self.left, self.bottom, self.right, self.unit)

  def __add__(self, other):
    if self.unit != other.unit:
      raise ValueError('units of rect is not equal')
    return RectWithUnit(self.left + other.left, self.top + other.top, self.right + other.right, self.bottom + other.bottom, self.unit)

  def __sub__(self, other):
    if self.unit != other.unit:
      raise ValueError('units of rect is not equal')
    return RectWithUnit(self.left - other.left, self.top - other.top, self.right - other.right, self.bottom - other.bottom, self.unit)

  def __str__(self):
    return 'left: {}, top: {}, right: {}, bottom: {}, unit: {}'.format(self.left, self.top, self.right, self.bottom, self.unit)

  def __mul__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return RectWithUnit(self.left * other, self.top * other, self.right * other, self.bottom * other, self.unit)

  def __eq__(self, other):
    if other is None:
      return False
    return self.unit == other.unit and self.left == other.left and self.top == other.top and self.right == other.right and self.bottom == other.bottom

  def toPx(self, size):
    """
    Returns RectWithUnit in pixel units

    :param size: Screen size
    :type size: Size

    :raises ValueError: In case of unknown unit value

    :return: rectangle in pixel units
    :rtype: RectWithUnit
    """
    if size is None:
      return None
    if not isinstance(size, Size) and not isinstance(size, tuple):
      raise ValueError('Invalid parameter. Expected instance of Size or tuple')
    w = size.width if isinstance(size, Size) else size[0]
    h = size.height if isinstance(size, Size) else size[1]
    if self.unit == self.RECT_UNIT_PX:
      return RectWithUnit(self.left, self.top, self.right, self.bottom, self.unit)
    elif self.unit == self.RECT_UNIT_PER:
      return RectWithUnit(w * (self.left / 100.0), h * (self.top / 100.0), w * (self.right / 100.0), h * (self.bottom / 100.0), self.RECT_UNIT_PX)
    elif self.unit == self.RECT_UNIT_HU:
      pxinhu = h / 100.0
      return RectWithUnit(self.left * pxinhu, self.top * pxinhu, self.right * pxinhu, self.bottom * pxinhu, self.RECT_UNIT_PX)
    else:
      raise ValueError('Unknown unit. unit: \"{}\"'.format(self.unit))

  def transform(self, delta, relSize=None):
    """
    Transforms rectangle to delta

    :param delta: delta rectangle
    :type delta: RectWithUnit
    :param relSize: Screen size
    :type relSize: Size

    :raises ValueError: In case of delta is not instance of RectWithUnit or relSize is not set in case of this rectangle is not in pixel unit

    :return: transformed rectangle
    :rtype: RectWithUnit
    """
    if delta is None:
      return None
    if not isinstance(delta, RectWithUnit):
      raise ValueError(
          'Invalid parameter. Expected instance of \"RectWithUnit\" class')
    size = self.size()
    deltaSize = delta.size()

    res = None
    if delta.unit == self.RECT_UNIT_PX:
      if self.unit != self.RECT_UNIT_PX and relSize is None:
        raise ValueError('Invalid parameter. Relative size is not specified')
      res = (self if self.unit == self.RECT_UNIT_PX else self.toPx(relSize)) + delta
    elif delta.unit == self.RECT_UNIT_PER:
      res = RectWithUnit()
      res.left = self.left + (size.width * (delta.left / 100.0))
      res.top = self.top + (size.height * (delta.top / 100.0))
      res.right = res.left + (size.width * (deltaSize.width / 100.0))
      res.bottom = res.top + (size.height * (deltaSize.height / 100.0))
      res.unit = self.unit
    elif delta.unit == self.RECT_UNIT_HU:
      huval = size.height / 100.0
      res = RectWithUnit()
      res.left = self.left + (delta.left * huval)
      res.top = self.top + (delta.top * huval)
      res.right = res.left + (size.width + (deltaSize.width * huval))
      res.bottom = res.top + (size.height + (deltaSize.height * huval))
      res.unit = self.unit
    return res

    # if self.unit == self.RECT_UNIT_PX:
    #   if delta.unit == self.RECT_UNIT_PX:
    #     return self + delta
    #   elif delta.unit == self.RECT_UNIT_PER:
    #     return RectWithUnit(self.left + (size.width * (delta.left / 100.0)),      self.top + (size.height * (delta.top / 100.0)),
    #                         self.left + (size.width * (deltaSize.width / 100.0)), self.top + (size.height * (deltaSize.height / 100.0)),
    #                         self.RECT_UNIT_PX)
    #   elif delta.unit == self.RECT_UNIT_HU:
    #     pxinhu = size.height / 100.0
    #     return RectWithUnit(self.left + (delta.left * pxinhu), self.top + (delta.top * pxinhu),
    #                         self.left + (size.width * (deltaSize.width * pxinhu)), self.top + (size.height * (deltaSize.height * pxinhu)), self.RECT_UNIT_PX)
    # elif self.unit == self.RECT_UNIT_PER:
    #   if delta.unit == self.RECT_UNIT_PX:
    #     return self.toPx(relSize) + delta
    #   elif delta.unit == self.RECT_UNIT_PER:
    #     return RectWithUnit(self.left + (size.width * (delta.left / 100.0)),      self.top + (size.height * (delta.top / 100.0)),
    #                         self.left + (size.width * (deltaSize.width / 100.0)), self.top + (size.height * (deltaSize.height / 100.0)),
    #                         self.RECT_UNIT_PER)
    #   elif delta.unit == self.RECT_UNIT_HU:
    #     perinhu = size.height / 100.0
    #     return RectWithUnit(self.left + (delta.left * pxinhu), self.top + (delta.top * pxinhu),
    #                         self.left + (size.width * (deltaSize.width * pxinhu)), self.top + (size.height * (deltaSize.height * pxinhu)), self.RECT_UNIT_PER)
    # elif self.unit == self.RECT_UNIT_HU:
    #   if delta.unit == self.RECT_UNIT_PX:
    #     if relSize is None:
    #       raise ValueError('Invalid parameter. Relative size is not specified')
    #     return self.toPx(relSize) + delta
    #   elif delta.unit == self.RECT_UNIT_PER:
    #     return RectWithUnit(self.left + (size.width * (delta.left / 100.0)),      self.top + (size.height * (delta.top / 100.0)),
    #                         self.left + (size.width * (deltaSize.width / 100.0)), self.top + (size.height * (deltaSize.height / 100.0)),
    #                         self.RECT_UNIT_HU)
    #   elif delta.unit == self.RECT_UNIT_HU:
    #     perinhu = size.height / 100.0
    #     return RectWithUnit(self.left + (delta.left * pxinhu), self.top + (delta.top * pxinhu),
    #                         self.left + (size.width * (deltaSize.width * pxinhu)), self.top + (size.height * (deltaSize.height * pxinhu)), self.RECT_UNIT_HU)
#
    # return None

  __rmul__ = __mul__


class Vector(object):
  """
  The Vector class defines the vector in two-dimensional space using floating point precision.

  :param x: coordinate on the x-axis
  :type x: float, optional
  :param y: coordinate on the y-axis
  :type y: float, optional
  """
  def __init__(self, x=0.0, y=0.0):
    super().__init__()
    self.x = x
    self.y = y

  @classmethod
  def fromPoint(cls, point: Point) -> 'Vector':
    """
    Returns Vector converted from point

    :raises ValueError: If the point does not exist

    :param point: Point in two-dimensional space
    :type point: Point
    """
    if point is None:
      raise ValueError('point does not exist')
    return cls(point.x, point.y)

  @classmethod
  def fromPoints(cls, origin: Point, point: Point) -> 'Vector':
    """
    Returns Vector calculated from two points

    :raises ValueError: If origin or point does not exist

    :param origin: Starting point in two-dimensional space
    :type origin: Point
    :param point: Terminal point in two-dimensional space
    :type point: Point
    """
    if origin is None:
      raise ValueError('origin does not exist')
    if point is None:
      raise ValueError('point does not exist')
    return cls(point.x - origin.x, point.y - origin.y)

  @property
  def magnitude(self):
    """
    Returns the length of this vector

    :return: length of this vector
    :rtype: float
    """
    return math.sqrt(self.x * self.x + self.y * self.y)

  def normalize(self):
    """
    Makes this vector have a magnitude of 1.0
    """
    length = math.fabs(math.sqrt((self.x * self.x) + (self.y * self.y)))
    self.x = self.x / length
    self.y = self.y / length

  def __str__(self):
    return '{{x: {0}, y: {1}}}'.format(self.x, self.y)

  def __add__(self, other: 'Vector'):
    return Vector(self.x + other.x, self.y + other.y)

  def __sub__(self, other: 'Vector'):
    return Vector(self.x - other.x, self.y - other.y)

  def __eq__(self, other: 'Vector'):
    if other is None:
      return False
    return self.x == other.x and self.y == other.y

  def __mul__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return Vector(self.x * other, self.y * other)

  __rmul__ = __mul__

  def __truediv__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return Vector(self.x / other, self.y / other)


class VectorWithUnit(Vector):
  """
  The VectorWithUnit class defines the vector in two-dimensional space with particular unit using floating point precision.

  :param x: coordinate on the x-axis
  :type x: float, optional
  :param y: coordinate on the y-axis
  :type y: float, optional
  :param unit: coordinate unit
  :type unit: str, optional

  .. note::
    | *Coordinate Unit:*
    | 'px' - value in pixels
    | 'hu' - value in height units.
    | Ex. 1hu is `{height of the screen} / 100`
    | '%' - value in percentages.
    | Ex. 50% of the x is half of the width of the screen
  """
  VECTOR_UNIT_PX = 'px'
  VECTOR_UNIT_PER = '%'
  VECTOR_UNIT_HU = 'hu'

  def __init__(self, x=0.0, y=0.0, unit=VECTOR_UNIT_PX, **kwargs):
    super().__init__(x, y)
    self.unit = unit

  @classmethod
  def fromPoint(cls, point: PointWithUnit) -> 'VectorWithUnit':
    """
    Returns VectorWithUnit converted from point

    :raises ValueError: If the point does not exist

    :param point: Point in two-dimensional space
    :type point: PointWithUnit
    """
    if point is None:
      raise ValueError('point does not exist')
    return cls(point.x, point.y, point.unit)

  @classmethod
  def fromPoints(cls, origin: PointWithUnit, point: PointWithUnit) -> 'VectorWithUnit':
    """
    Returns VectorWithUnit calculated from two points

    :raises ValueError: If starting point or terminal point does not exist, also if unit of two points is not same

    :param origin: Starting point in two-dimensional space
    :type origin: PointWithUnit
    :param point: Terminal point in two-dimensional space
    :type point: PointWithUnit
    """
    if origin is None:
      raise ValueError('origin does not exist')
    if point is None:
      raise ValueError('point does not exist')
    if origin.unit != point.unit:
      raise ValueError('units of points is not equal')
    return cls(point.x - origin.x, point.y - origin.y, origin.unit)

  def __str__(self):
    return '{{x: {0}, y: {1}, unit: {2}}}'.format(self.x, self.y, self.unit)

  def __add__(self, other: 'VectorWithUnit'):
    if self.unit != other.unit:
      raise ValueError('units of vectors is not equal')
    return VectorWithUnit(self.x + other.x, self.y + other.y, self.unit)

  def __sub__(self, other: 'VectorWithUnit'):
    if self.unit != other.unit:
      raise ValueError('units of vectors is not equal')
    return VectorWithUnit(self.x - other.x, self.y - other.y, self.unit)

  def __eq__(self, other: 'VectorWithUnit'):
    if other is None:
      return False
    return self.x == other.x and self.y == other.y and self.unit == other.unit

  def __mul__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return VectorWithUnit(self.x * other, self.y * other, self.unit)

  __rmul__ = __mul__

  def __truediv__(self, other):
    if not isinstance(other, int) and not isinstance(other, float):
      raise NotImplementedError()
    return VectorWithUnit(self.x / other, self.y / other, self.unit)
