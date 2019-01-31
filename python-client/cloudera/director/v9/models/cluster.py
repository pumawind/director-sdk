# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class Cluster(object):
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
        'name': 'str',
        'instances': 'list[Instance]',
        'services': 'list[Service]',
        'url': 'str',
        'instances_url': 'str',
        'health': 'Health',
        'feature_availability': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'instances': 'instances',
        'services': 'services',
        'url': 'url',
        'instances_url': 'instancesUrl',
        'health': 'health',
        'feature_availability': 'featureAvailability'
    }

    def __init__(self, name=None, instances=None, services=None, url=None, instances_url=None, health=None, feature_availability=None):  # noqa: E501
        """Cluster - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._instances = None
        self._services = None
        self._url = None
        self._instances_url = None
        self._health = None
        self._feature_availability = None
        self.discriminator = None

        self.name = name
        if instances is not None:
            self.instances = instances
        if services is not None:
            self.services = services
        if url is not None:
            self.url = url
        if instances_url is not None:
            self.instances_url = instances_url
        if health is not None:
            self.health = health
        if feature_availability is not None:
            self.feature_availability = feature_availability

    @property
    def name(self):
        """Gets the name of this Cluster.  # noqa: E501

        Cluster name  # noqa: E501

        :return: The name of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cluster.

        Cluster name  # noqa: E501

        :param name: The name of this Cluster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def instances(self):
        """Gets the instances of this Cluster.  # noqa: E501

        Instances comprising this cluster  # noqa: E501

        :return: The instances of this Cluster.  # noqa: E501
        :rtype: list[Instance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this Cluster.

        Instances comprising this cluster  # noqa: E501

        :param instances: The instances of this Cluster.  # noqa: E501
        :type: list[Instance]
        """

        self._instances = instances

    @property
    def services(self):
        """Gets the services of this Cluster.  # noqa: E501

        Services that belong to this cluster  # noqa: E501

        :return: The services of this Cluster.  # noqa: E501
        :rtype: list[Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Cluster.

        Services that belong to this cluster  # noqa: E501

        :param services: The services of this Cluster.  # noqa: E501
        :type: list[Service]
        """

        self._services = services

    @property
    def url(self):
        """Gets the url of this Cluster.  # noqa: E501

        Optional URL for cluster in Cloudera Manager  # noqa: E501

        :return: The url of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Cluster.

        Optional URL for cluster in Cloudera Manager  # noqa: E501

        :param url: The url of this Cluster.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def instances_url(self):
        """Gets the instances_url of this Cluster.  # noqa: E501

        Optional URL for cluster instances in Cloudera Manager  # noqa: E501

        :return: The instances_url of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._instances_url

    @instances_url.setter
    def instances_url(self, instances_url):
        """Sets the instances_url of this Cluster.

        Optional URL for cluster instances in Cloudera Manager  # noqa: E501

        :param instances_url: The instances_url of this Cluster.  # noqa: E501
        :type: str
        """

        self._instances_url = instances_url

    @property
    def health(self):
        """Gets the health of this Cluster.  # noqa: E501

        Overall cluster health  # noqa: E501

        :return: The health of this Cluster.  # noqa: E501
        :rtype: Health
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this Cluster.

        Overall cluster health  # noqa: E501

        :param health: The health of this Cluster.  # noqa: E501
        :type: Health
        """

        self._health = health

    @property
    def feature_availability(self):
        """Gets the feature_availability of this Cluster.  # noqa: E501

        Availability information for features  # noqa: E501

        :return: The feature_availability of this Cluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._feature_availability

    @feature_availability.setter
    def feature_availability(self, feature_availability):
        """Sets the feature_availability of this Cluster.

        Availability information for features  # noqa: E501

        :param feature_availability: The feature_availability of this Cluster.  # noqa: E501
        :type: dict(str, str)
        """
        allowed_values = ["UNKNOWN", "UNAVAILABLE", "AVAILABLE"]  # noqa: E501
        if not set(feature_availability.values()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values in `feature_availability` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(feature_availability.values()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._feature_availability = feature_availability

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
