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


class Metrics(object):
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
        'cluster_name': 'str',
        'time_series_metrics': 'dict(str, TimeSeriesResponseList)'
    }

    attribute_map = {
        'cluster_name': 'clusterName',
        'time_series_metrics': 'timeSeriesMetrics'
    }

    def __init__(self, cluster_name=None, time_series_metrics=None):  # noqa: E501
        """Metrics - a model defined in Swagger"""  # noqa: E501

        self._cluster_name = None
        self._time_series_metrics = None
        self.discriminator = None

        self.cluster_name = cluster_name
        if time_series_metrics is not None:
            self.time_series_metrics = time_series_metrics

    @property
    def cluster_name(self):
        """Gets the cluster_name of this Metrics.  # noqa: E501

        Cluster name  # noqa: E501

        :return: The cluster_name of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this Metrics.

        Cluster name  # noqa: E501

        :param cluster_name: The cluster_name of this Metrics.  # noqa: E501
        :type: str
        """
        if cluster_name is None:
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")  # noqa: E501

        self._cluster_name = cluster_name

    @property
    def time_series_metrics(self):
        """Gets the time_series_metrics of this Metrics.  # noqa: E501

        Named metrics tracked for this cluster  # noqa: E501

        :return: The time_series_metrics of this Metrics.  # noqa: E501
        :rtype: dict(str, TimeSeriesResponseList)
        """
        return self._time_series_metrics

    @time_series_metrics.setter
    def time_series_metrics(self, time_series_metrics):
        """Sets the time_series_metrics of this Metrics.

        Named metrics tracked for this cluster  # noqa: E501

        :param time_series_metrics: The time_series_metrics of this Metrics.  # noqa: E501
        :type: dict(str, TimeSeriesResponseList)
        """

        self._time_series_metrics = time_series_metrics

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
        if not isinstance(other, Metrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other