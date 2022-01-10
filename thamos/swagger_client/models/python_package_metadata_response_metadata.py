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

class PythonPackageMetadataResponseMetadata(object):
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
        'author': 'str',
        'author_email': 'str',
        'classifier': 'list[str]',
        'download_url': 'str',
        'home_page': 'str',
        'keywords': 'str',
        'license': 'str',
        'maintainer': 'str',
        'maintainer_email': 'str',
        'metadata_version': 'str',
        'name': 'str',
        'platform': 'list[str]',
        'requires_dist': 'list[str]',
        'summary': 'str',
        'version': 'str',
        'requires_python': 'str',
        'description_content_type': 'str',
        'project_url': 'str',
        'provides_extra': 'str'
    }

    attribute_map = {
        'author': 'author',
        'author_email': 'author_email',
        'classifier': 'classifier',
        'download_url': 'download_url',
        'home_page': 'home_page',
        'keywords': 'keywords',
        'license': 'license',
        'maintainer': 'maintainer',
        'maintainer_email': 'maintainer_email',
        'metadata_version': 'metadata_version',
        'name': 'name',
        'platform': 'platform',
        'requires_dist': 'requires_dist',
        'summary': 'summary',
        'version': 'version',
        'requires_python': 'requires_python',
        'description_content_type': 'description_content_type',
        'project_url': 'project_url',
        'provides_extra': 'provides_extra'
    }

    def __init__(self, author=None, author_email=None, classifier=None, download_url=None, home_page=None, keywords=None, license=None, maintainer=None, maintainer_email=None, metadata_version=None, name=None, platform=None, requires_dist=None, summary=None, version=None, requires_python=None, description_content_type=None, project_url=None, provides_extra=None):  # noqa: E501
        """PythonPackageMetadataResponseMetadata - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._author_email = None
        self._classifier = None
        self._download_url = None
        self._home_page = None
        self._keywords = None
        self._license = None
        self._maintainer = None
        self._maintainer_email = None
        self._metadata_version = None
        self._name = None
        self._platform = None
        self._requires_dist = None
        self._summary = None
        self._version = None
        self._requires_python = None
        self._description_content_type = None
        self._project_url = None
        self._provides_extra = None
        self.discriminator = None
        self.author = author
        self.author_email = author_email
        self.classifier = classifier
        self.download_url = download_url
        self.home_page = home_page
        self.keywords = keywords
        self.license = license
        self.maintainer = maintainer
        self.maintainer_email = maintainer_email
        self.metadata_version = metadata_version
        self.name = name
        self.platform = platform
        self.requires_dist = requires_dist
        self.summary = summary
        self.version = version
        self.requires_python = requires_python
        self.description_content_type = description_content_type
        self.project_url = project_url
        self.provides_extra = provides_extra

    @property
    def author(self):
        """Gets the author of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the author’s name  # noqa: E501

        :return: The author of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PythonPackageMetadataResponseMetadata.

        A string containing the author’s name  # noqa: E501

        :param author: The author of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def author_email(self):
        """Gets the author_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the author’s e-mail address  # noqa: E501

        :return: The author_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this PythonPackageMetadataResponseMetadata.

        A string containing the author’s e-mail address  # noqa: E501

        :param author_email: The author_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if author_email is None:
            raise ValueError("Invalid value for `author_email`, must not be `None`")  # noqa: E501

        self._author_email = author_email

    @property
    def classifier(self):
        """Gets the classifier of this PythonPackageMetadataResponseMetadata.  # noqa: E501


        :return: The classifier of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._classifier

    @classifier.setter
    def classifier(self, classifier):
        """Sets the classifier of this PythonPackageMetadataResponseMetadata.


        :param classifier: The classifier of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: list[str]
        """
        if classifier is None:
            raise ValueError("Invalid value for `classifier`, must not be `None`")  # noqa: E501

        self._classifier = classifier

    @property
    def download_url(self):
        """Gets the download_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the URL from which this version of the distribution can be downloaded  # noqa: E501

        :return: The download_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this PythonPackageMetadataResponseMetadata.

        A string containing the URL from which this version of the distribution can be downloaded  # noqa: E501

        :param download_url: The download_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if download_url is None:
            raise ValueError("Invalid value for `download_url`, must not be `None`")  # noqa: E501

        self._download_url = download_url

    @property
    def home_page(self):
        """Gets the home_page of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the URL for the distribution’s home page  # noqa: E501

        :return: The home_page of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this PythonPackageMetadataResponseMetadata.

        A string containing the URL for the distribution’s home page  # noqa: E501

        :param home_page: The home_page of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if home_page is None:
            raise ValueError("Invalid value for `home_page`, must not be `None`")  # noqa: E501

        self._home_page = home_page

    @property
    def keywords(self):
        """Gets the keywords of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A list of additional keywords to be used to assist searching for the distribution in a larger catalog   # noqa: E501

        :return: The keywords of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PythonPackageMetadataResponseMetadata.

        A list of additional keywords to be used to assist searching for the distribution in a larger catalog   # noqa: E501

        :param keywords: The keywords of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if keywords is None:
            raise ValueError("Invalid value for `keywords`, must not be `None`")  # noqa: E501

        self._keywords = keywords

    @property
    def license(self):
        """Gets the license of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Text indicating the license covering the distribution  # noqa: E501

        :return: The license of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this PythonPackageMetadataResponseMetadata.

        Text indicating the license covering the distribution  # noqa: E501

        :param license: The license of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if license is None:
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def maintainer(self):
        """Gets the maintainer of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the maintainer’s name at a minimum; additional contact information may be provided   # noqa: E501

        :return: The maintainer of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """Sets the maintainer of this PythonPackageMetadataResponseMetadata.

        A string containing the maintainer’s name at a minimum; additional contact information may be provided   # noqa: E501

        :param maintainer: The maintainer of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if maintainer is None:
            raise ValueError("Invalid value for `maintainer`, must not be `None`")  # noqa: E501

        self._maintainer = maintainer

    @property
    def maintainer_email(self):
        """Gets the maintainer_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A string containing the maintainer’s e-mail address  # noqa: E501

        :return: The maintainer_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._maintainer_email

    @maintainer_email.setter
    def maintainer_email(self, maintainer_email):
        """Sets the maintainer_email of this PythonPackageMetadataResponseMetadata.

        A string containing the maintainer’s e-mail address  # noqa: E501

        :param maintainer_email: The maintainer_email of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if maintainer_email is None:
            raise ValueError("Invalid value for `maintainer_email`, must not be `None`")  # noqa: E501

        self._maintainer_email = maintainer_email

    @property
    def metadata_version(self):
        """Gets the metadata_version of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Version of the file format  # noqa: E501

        :return: The metadata_version of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """Sets the metadata_version of this PythonPackageMetadataResponseMetadata.

        Version of the file format  # noqa: E501

        :param metadata_version: The metadata_version of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if metadata_version is None:
            raise ValueError("Invalid value for `metadata_version`, must not be `None`")  # noqa: E501

        self._metadata_version = metadata_version

    @property
    def name(self):
        """Gets the name of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Name of the distribution  # noqa: E501

        :return: The name of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PythonPackageMetadataResponseMetadata.

        Name of the distribution  # noqa: E501

        :param name: The name of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def platform(self):
        """Gets the platform of this PythonPackageMetadataResponseMetadata.  # noqa: E501


        :return: The platform of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PythonPackageMetadataResponseMetadata.


        :param platform: The platform of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: list[str]
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def requires_dist(self):
        """Gets the requires_dist of this PythonPackageMetadataResponseMetadata.  # noqa: E501


        :return: The requires_dist of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._requires_dist

    @requires_dist.setter
    def requires_dist(self, requires_dist):
        """Sets the requires_dist of this PythonPackageMetadataResponseMetadata.


        :param requires_dist: The requires_dist of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: list[str]
        """
        if requires_dist is None:
            raise ValueError("Invalid value for `requires_dist`, must not be `None`")  # noqa: E501

        self._requires_dist = requires_dist

    @property
    def summary(self):
        """Gets the summary of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        A one-line summary of what the distribution does  # noqa: E501

        :return: The summary of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PythonPackageMetadataResponseMetadata.

        A one-line summary of what the distribution does  # noqa: E501

        :param summary: The summary of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def version(self):
        """Gets the version of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        version of the distribution  # noqa: E501

        :return: The version of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PythonPackageMetadataResponseMetadata.

        version of the distribution  # noqa: E501

        :param version: The version of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def requires_python(self):
        """Gets the requires_python of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Python requirements for the distribution  # noqa: E501

        :return: The requires_python of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._requires_python

    @requires_python.setter
    def requires_python(self, requires_python):
        """Sets the requires_python of this PythonPackageMetadataResponseMetadata.

        Python requirements for the distribution  # noqa: E501

        :param requires_python: The requires_python of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if requires_python is None:
            raise ValueError("Invalid value for `requires_python`, must not be `None`")  # noqa: E501

        self._requires_python = requires_python

    @property
    def description_content_type(self):
        """Gets the description_content_type of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Content-Type of description text  # noqa: E501

        :return: The description_content_type of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description_content_type

    @description_content_type.setter
    def description_content_type(self, description_content_type):
        """Sets the description_content_type of this PythonPackageMetadataResponseMetadata.

        Content-Type of description text  # noqa: E501

        :param description_content_type: The description_content_type of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if description_content_type is None:
            raise ValueError("Invalid value for `description_content_type`, must not be `None`")  # noqa: E501

        self._description_content_type = description_content_type

    @property
    def project_url(self):
        """Gets the project_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        URL to project  # noqa: E501

        :return: The project_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._project_url

    @project_url.setter
    def project_url(self, project_url):
        """Sets the project_url of this PythonPackageMetadataResponseMetadata.

        URL to project  # noqa: E501

        :param project_url: The project_url of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if project_url is None:
            raise ValueError("Invalid value for `project_url`, must not be `None`")  # noqa: E501

        self._project_url = project_url

    @property
    def provides_extra(self):
        """Gets the provides_extra of this PythonPackageMetadataResponseMetadata.  # noqa: E501

        Provided extra of the distribution  # noqa: E501

        :return: The provides_extra of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._provides_extra

    @provides_extra.setter
    def provides_extra(self, provides_extra):
        """Sets the provides_extra of this PythonPackageMetadataResponseMetadata.

        Provided extra of the distribution  # noqa: E501

        :param provides_extra: The provides_extra of this PythonPackageMetadataResponseMetadata.  # noqa: E501
        :type: str
        """
        if provides_extra is None:
            raise ValueError("Invalid value for `provides_extra`, must not be `None`")  # noqa: E501

        self._provides_extra = provides_extra

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
        if issubclass(PythonPackageMetadataResponseMetadata, dict):
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
        if not isinstance(other, PythonPackageMetadataResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
