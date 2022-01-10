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

class PythonPackageVersionMetadataResponseMetadata(object):
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
        'packages': 'list[str]',
        'index_url': 'str',
        'package_name': 'str',
        'package_version': 'str',
        'dependencies': 'object',
        'importlib_metadata': 'PythonPackageVersionMetadataResponseMetadataImportlibMetadata'
    }

    attribute_map = {
        'packages': 'packages',
        'index_url': 'index_url',
        'package_name': 'package_name',
        'package_version': 'package_version',
        'dependencies': 'dependencies',
        'importlib_metadata': 'importlib_metadata'
    }

    def __init__(self, packages=None, index_url=None, package_name=None, package_version=None, dependencies=None, importlib_metadata=None):  # noqa: E501
        """PythonPackageVersionMetadataResponseMetadata - a model defined in Swagger"""  # noqa: E501
        self._packages = None
        self._index_url = None
        self._package_name = None
        self._package_version = None
        self._dependencies = None
        self._importlib_metadata = None
        self.discriminator = None
        self.packages = packages
        self.index_url = index_url
        self.package_name = package_name
        self.package_version = package_version
        self.dependencies = dependencies
        self.importlib_metadata = importlib_metadata

    @property
    def packages(self):
        """Gets the packages of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501

        Python packages (modules) the given package provides  # noqa: E501

        :return: The packages of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this PythonPackageVersionMetadataResponseMetadata.

        Python packages (modules) the given package provides  # noqa: E501

        :param packages: The packages of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: list[str]
        """
        if packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def index_url(self):
        """Gets the index_url of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501

        Index URL from where the given package comes from  # noqa: E501

        :return: The index_url of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._index_url

    @index_url.setter
    def index_url(self, index_url):
        """Sets the index_url of this PythonPackageVersionMetadataResponseMetadata.

        Index URL from where the given package comes from  # noqa: E501

        :param index_url: The index_url of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if index_url is None:
            raise ValueError("Invalid value for `index_url`, must not be `None`")  # noqa: E501

        self._index_url = index_url

    @property
    def package_name(self):
        """Gets the package_name of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501

        Name of the Python package  # noqa: E501

        :return: The package_name of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this PythonPackageVersionMetadataResponseMetadata.

        Name of the Python package  # noqa: E501

        :param package_name: The package_name of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be `None`")  # noqa: E501

        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501

        Version of the Python package  # noqa: E501

        :return: The package_version of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this PythonPackageVersionMetadataResponseMetadata.

        Version of the Python package  # noqa: E501

        :param package_version: The package_version of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if package_version is None:
            raise ValueError("Invalid value for `package_version`, must not be `None`")  # noqa: E501

        self._package_version = package_version

    @property
    def dependencies(self):
        """Gets the dependencies of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501

        Dependency information  # noqa: E501

        :return: The dependencies of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: object
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this PythonPackageVersionMetadataResponseMetadata.

        Dependency information  # noqa: E501

        :param dependencies: The dependencies of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: object
        """
        if dependencies is None:
            raise ValueError("Invalid value for `dependencies`, must not be `None`")  # noqa: E501

        self._dependencies = dependencies

    @property
    def importlib_metadata(self):
        """Gets the importlib_metadata of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501


        :return: The importlib_metadata of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :rtype: PythonPackageVersionMetadataResponseMetadataImportlibMetadata
        """
        return self._importlib_metadata

    @importlib_metadata.setter
    def importlib_metadata(self, importlib_metadata):
        """Sets the importlib_metadata of this PythonPackageVersionMetadataResponseMetadata.


        :param importlib_metadata: The importlib_metadata of this PythonPackageVersionMetadataResponseMetadata.  # noqa: E501
        :type: PythonPackageVersionMetadataResponseMetadataImportlibMetadata
        """
        if importlib_metadata is None:
            raise ValueError("Invalid value for `importlib_metadata`, must not be `None`")  # noqa: E501

        self._importlib_metadata = importlib_metadata

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
        if issubclass(PythonPackageVersionMetadataResponseMetadata, dict):
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
        if not isinstance(other, PythonPackageVersionMetadataResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
