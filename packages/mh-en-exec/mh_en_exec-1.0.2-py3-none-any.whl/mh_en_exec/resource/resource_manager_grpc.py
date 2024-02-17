import logging
import re
from abc import ABC, abstractclassmethod, abstractmethod

import cv2
import numpy


class Resource(object):
  """
  The Resource class contains various data related to resource

  :ivar id: Resource id
  :vartype id: str
  :ivar type: Resource type
  :vartype id: str
  :ivar data: Resource data. Type of this variable depends on the `type` variable
  :vartype data: any

  .. warning::
    | Currently only `cv2img` type is supported
    | `cv2img`: OpenCV image
  """
  def __init__(self, id_, type_, data) -> None:
    self.id = id_
    self.type = type_
    self.data = data


class ResourceManagerBase(ABC):
  _instance = None

  def __init__(self) -> None:
    super().__init__()

  @abstractclassmethod
  def getInstance(cls) -> 'ResourceManagerBase':
    ...


class ResourceManager(ResourceManagerBase):
  """
  Resource manager class. Using this class resources can be accessed.
  """
  TYPE_CV2_IMAGE = 'cv2img'
  _instance = None

  def __init__(self) -> None:
    self._resources = {}
    self._logger = logging.getLogger(__name__.split('.')[0])

  @classmethod
  def getInstance(cls) -> 'ResourceManager':
    """
    Returns resource manager instance
    """
    if cls._instance is None:
      cls._instance = ResourceManager()
    return cls._instance

  @property
  def resources(self) -> 'dict[str, Resource]':
    """
    Returns resources dictionary

    :return: resources
    :rtype: dict[str, Resource]
    """
    return self._resources

  def createResource(self, data, type_: str, id_: str = None, overwrite: bool = False) -> str:
    """
    Creates resource.

    :param data: resource data
    :type data: any
    :param type_: resource type
    :type type_: str
    :param id_: resource id. If it's None id will be generated
    :type id_: str, optional
    :param overwrite: flag that indicates whether an existing resource will be overwritten
    :type overwrite: bool, optional

    :return: created resource id
    :rtype: str
    """
    if data is None:
      raise ValueError('Data is None')
    if id_ and not self.isResourceId(id_):
      raise ValueError(f'Create resource failed, Invalid id: {id_}')
    resId = 'res_{}'.format(
        self._generateUniqueString(8)) if id_ is None else id_
    self._logger.debug(f'Creating resource with id: {id_}')
    if self._isIdExists(resId):
      if not overwrite:
        raise ValueError(f'Create resource failed, id: {id_} already exist')
    if type_ == self.TYPE_CV2_IMAGE:
      self._resources[resId] = Resource(resId, type_, data)
      return resId
    else:
      self._logger.error(f'Currently, resource "{type_}" not supported')
    return None

  def createResourceFromBytes(self, data: bytes, type_: str, id_: str = None, overwrite: bool = False):
    """
    Creates resource from bytes.

    :param data: resource data
    :type data: bytes
    :param type_: resource type
    :type type_: str
    :param id_: resource id. If it's None id will be generated
    :type id_: str, optional
    :param overwrite: flag that indicates whether an existing resource will be overwritten
    :type overwrite: bool, optional

    :return: created resource id
    :rtype: str
    """
    if data is None:
      raise ValueError('Data is None')
    if id_ and not self.isResourceId(id_):
      raise ValueError(f'Create resource failed, Invalid id: {id_}')
    resId = f'res_{self._generateUniqueString(8)}' if id_ is None else id_
    if self._isIdExists(resId):
      if not overwrite:
        # raise ValueError(f'Create resource failed, id: {id_} already exist')
        return resId
    if type_ == self.TYPE_CV2_IMAGE:
      img = cv2.imdecode(numpy.frombuffer(data, numpy.uint8), cv2.IMREAD_COLOR)
      self._resources[resId] = Resource(resId, type_, img)
      return resId
    else:
      self._logger.error(f'Currently, resource "{type_}" not supported')
    return None

  def getResource(self, id_: str) -> 'tuple[str, str, object]':
    """
    Returns resource data

    :param id_: resource id
    :type id_: str

    :return: Resource. Tuple of {id, type, data}. Data depends on the resource type
    :rtype: tuple[str, str, object]
    """
    res = self._resources.get(id_, None)
    if res:
      return res.data
    return None

  def getResourceBytes(self, id_: str) -> 'tuple[str, str, bytes]':
    """
    Returns resource data in bytes

    :param id_: resource id
    :type id_: str

    :return: Resource. Tuple of {id, type, databytes}
    :rtype: tuple[str, str, bytes]
    """
    res = self._resources.get(id_, None)
    if res:
      is_success, im_buf_arr = cv2.imencode(".png", res.data)
      if is_success:
        return (res.id, res.type, im_buf_arr.tobytes())
    return None

  def removeResource(self, id_: str) -> bool:
    """
    Removes resource from resource list

    :param id_: resource id
    :type id_: str

    :return: result
    :rtype: bool
    """
    if id_ not in self._resources:
      self._logger.error(f'Resource "{id_}" does not exist')
      return False
    del self._resources[id_]
    return True

  def isResourceId(self, id):
    """
    Verifies resource id

    :param id: resource id
    :type id: str

    :return: result. True if id is valid, False if id is invalid
    :rtype: bool
    """
    return id and re.match('res_[a-zA-Z0-9]{8}$', id) is not None

  def _generateUniqueString(self, length):
    import uuid
    return uuid.uuid4().hex[:length].upper()

  def _isIdExists(self, id_):
    if id_ in self._resources:
      return True
    return False
