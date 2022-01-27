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

class BuildAnalysisResponseError(object):
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
        'base_image_analysis': 'BuildAnalysisResponseErrorBaseImageAnalysis',
        'output_image_analysis': 'BuildAnalysisResponseErrorOutputImageAnalysis',
        'build_log_analysis': 'BuildAnalysisResponseErrorOutputImageAnalysis'
    }

    attribute_map = {
        'base_image_analysis': 'base_image_analysis',
        'output_image_analysis': 'output_image_analysis',
        'build_log_analysis': 'build_log_analysis'
    }

    def __init__(self, base_image_analysis=None, output_image_analysis=None, build_log_analysis=None):  # noqa: E501
        """BuildAnalysisResponseError - a model defined in Swagger"""  # noqa: E501
        self._base_image_analysis = None
        self._output_image_analysis = None
        self._build_log_analysis = None
        self.discriminator = None
        self.base_image_analysis = base_image_analysis
        self.output_image_analysis = output_image_analysis
        self.build_log_analysis = build_log_analysis

    @property
    def base_image_analysis(self):
        """Gets the base_image_analysis of this BuildAnalysisResponseError.  # noqa: E501


        :return: The base_image_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :rtype: BuildAnalysisResponseErrorBaseImageAnalysis
        """
        return self._base_image_analysis

    @base_image_analysis.setter
    def base_image_analysis(self, base_image_analysis):
        """Sets the base_image_analysis of this BuildAnalysisResponseError.


        :param base_image_analysis: The base_image_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :type: BuildAnalysisResponseErrorBaseImageAnalysis
        """
        if base_image_analysis is None:
            raise ValueError("Invalid value for `base_image_analysis`, must not be `None`")  # noqa: E501

        self._base_image_analysis = base_image_analysis

    @property
    def output_image_analysis(self):
        """Gets the output_image_analysis of this BuildAnalysisResponseError.  # noqa: E501


        :return: The output_image_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :rtype: BuildAnalysisResponseErrorOutputImageAnalysis
        """
        return self._output_image_analysis

    @output_image_analysis.setter
    def output_image_analysis(self, output_image_analysis):
        """Sets the output_image_analysis of this BuildAnalysisResponseError.


        :param output_image_analysis: The output_image_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :type: BuildAnalysisResponseErrorOutputImageAnalysis
        """
        if output_image_analysis is None:
            raise ValueError("Invalid value for `output_image_analysis`, must not be `None`")  # noqa: E501

        self._output_image_analysis = output_image_analysis

    @property
    def build_log_analysis(self):
        """Gets the build_log_analysis of this BuildAnalysisResponseError.  # noqa: E501


        :return: The build_log_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :rtype: BuildAnalysisResponseErrorOutputImageAnalysis
        """
        return self._build_log_analysis

    @build_log_analysis.setter
    def build_log_analysis(self, build_log_analysis):
        """Sets the build_log_analysis of this BuildAnalysisResponseError.


        :param build_log_analysis: The build_log_analysis of this BuildAnalysisResponseError.  # noqa: E501
        :type: BuildAnalysisResponseErrorOutputImageAnalysis
        """
        if build_log_analysis is None:
            raise ValueError("Invalid value for `build_log_analysis`, must not be `None`")  # noqa: E501

        self._build_log_analysis = build_log_analysis

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
        if issubclass(BuildAnalysisResponseError, dict):
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
        if not isinstance(other, BuildAnalysisResponseError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
