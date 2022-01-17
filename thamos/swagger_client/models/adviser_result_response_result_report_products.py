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

class AdviserResultResponseResultReportProducts(object):
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
        'advised_manifest_changes': 'list[object]',
        'advised_runtime_environment': 'RuntimeEnvironment',
        'dependency_graph': 'AdviserResultResponseResultReportDependencyGraph',
        'justification': 'Justification',
        'project': 'object',
        'score': 'float'
    }

    attribute_map = {
        'advised_manifest_changes': 'advised_manifest_changes',
        'advised_runtime_environment': 'advised_runtime_environment',
        'dependency_graph': 'dependency_graph',
        'justification': 'justification',
        'project': 'project',
        'score': 'score'
    }

    def __init__(self, advised_manifest_changes=None, advised_runtime_environment=None, dependency_graph=None, justification=None, project=None, score=None):  # noqa: E501
        """AdviserResultResponseResultReportProducts - a model defined in Swagger"""  # noqa: E501
        self._advised_manifest_changes = None
        self._advised_runtime_environment = None
        self._dependency_graph = None
        self._justification = None
        self._project = None
        self._score = None
        self.discriminator = None
        self.advised_manifest_changes = advised_manifest_changes
        self.advised_runtime_environment = advised_runtime_environment
        self.dependency_graph = dependency_graph
        self.justification = justification
        self.project = project
        self.score = score

    @property
    def advised_manifest_changes(self):
        """Gets the advised_manifest_changes of this AdviserResultResponseResultReportProducts.  # noqa: E501

        Advised changes to manifest files  # noqa: E501

        :return: The advised_manifest_changes of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: list[object]
        """
        return self._advised_manifest_changes

    @advised_manifest_changes.setter
    def advised_manifest_changes(self, advised_manifest_changes):
        """Sets the advised_manifest_changes of this AdviserResultResponseResultReportProducts.

        Advised changes to manifest files  # noqa: E501

        :param advised_manifest_changes: The advised_manifest_changes of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: list[object]
        """
        if advised_manifest_changes is None:
            raise ValueError("Invalid value for `advised_manifest_changes`, must not be `None`")  # noqa: E501

        self._advised_manifest_changes = advised_manifest_changes

    @property
    def advised_runtime_environment(self):
        """Gets the advised_runtime_environment of this AdviserResultResponseResultReportProducts.  # noqa: E501


        :return: The advised_runtime_environment of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: RuntimeEnvironment
        """
        return self._advised_runtime_environment

    @advised_runtime_environment.setter
    def advised_runtime_environment(self, advised_runtime_environment):
        """Sets the advised_runtime_environment of this AdviserResultResponseResultReportProducts.


        :param advised_runtime_environment: The advised_runtime_environment of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: RuntimeEnvironment
        """

        self._advised_runtime_environment = advised_runtime_environment

    @property
    def dependency_graph(self):
        """Gets the dependency_graph of this AdviserResultResponseResultReportProducts.  # noqa: E501


        :return: The dependency_graph of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: AdviserResultResponseResultReportDependencyGraph
        """
        return self._dependency_graph

    @dependency_graph.setter
    def dependency_graph(self, dependency_graph):
        """Sets the dependency_graph of this AdviserResultResponseResultReportProducts.


        :param dependency_graph: The dependency_graph of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: AdviserResultResponseResultReportDependencyGraph
        """
        if dependency_graph is None:
            raise ValueError("Invalid value for `dependency_graph`, must not be `None`")  # noqa: E501

        self._dependency_graph = dependency_graph

    @property
    def justification(self):
        """Gets the justification of this AdviserResultResponseResultReportProducts.  # noqa: E501


        :return: The justification of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: Justification
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """Sets the justification of this AdviserResultResponseResultReportProducts.


        :param justification: The justification of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: Justification
        """
        if justification is None:
            raise ValueError("Invalid value for `justification`, must not be `None`")  # noqa: E501

        self._justification = justification

    @property
    def project(self):
        """Gets the project of this AdviserResultResponseResultReportProducts.  # noqa: E501


        :return: The project of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: object
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this AdviserResultResponseResultReportProducts.


        :param project: The project of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: object
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def score(self):
        """Gets the score of this AdviserResultResponseResultReportProducts.  # noqa: E501

        Score of the computed product  # noqa: E501

        :return: The score of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this AdviserResultResponseResultReportProducts.

        Score of the computed product  # noqa: E501

        :param score: The score of this AdviserResultResponseResultReportProducts.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

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
        if issubclass(AdviserResultResponseResultReportProducts, dict):
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
        if not isinstance(other, AdviserResultResponseResultReportProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other