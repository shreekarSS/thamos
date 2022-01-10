# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.7.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdviserResultResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'AdviserResultResponseMetadata',
        'result': 'AdviserResultResponseResult'
    }

    attribute_map = {
        'metadata': 'metadata',
        'result': 'result'
    }

    def __init__(self, metadata=None, result=None):  # noqa: E501
        """AdviserResultResponse - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._result = None
        self.discriminator = None
        self.metadata = metadata
        self.result = result

    @property
    def metadata(self):
        """Gets the metadata of this AdviserResultResponse.  # noqa: E501


        :return: The metadata of this AdviserResultResponse.  # noqa: E501
        :rtype: AdviserResultResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AdviserResultResponse.


        :param metadata: The metadata of this AdviserResultResponse.  # noqa: E501
        :type: AdviserResultResponseMetadata
        """

        self._metadata = metadata

    @property
    def result(self):
        """Gets the result of this AdviserResultResponse.  # noqa: E501


        :return: The result of this AdviserResultResponse.  # noqa: E501
        :rtype: AdviserResultResponseResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AdviserResultResponse.


        :param result: The result of this AdviserResultResponse.  # noqa: E501
        :type: AdviserResultResponseResult
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdviserResultResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdviserResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
