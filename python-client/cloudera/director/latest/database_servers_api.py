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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudera.director.common.client import ApiClient


class DatabaseServersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, environment, external_database_server_template, **kwargs):  # noqa: E501
        """Create a new external database server  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create(environment, external_database_server_template, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param ExternalDatabaseServerTemplate external_database_server_template: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_with_http_info(environment, external_database_server_template, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(environment, external_database_server_template, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, environment, external_database_server_template, **kwargs):  # noqa: E501
        """Create a new external database server  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_with_http_info(environment, external_database_server_template, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param ExternalDatabaseServerTemplate external_database_server_template: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server_template']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `create`")  # noqa: E501
        # verify the required parameter 'external_database_server_template' is set
        if ('external_database_server_template' not in params or
                params['external_database_server_template'] is None):
            raise ValueError("Missing the required parameter `external_database_server_template` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'external_database_server_template' in params:
            body_params = params['external_database_server_template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Delete an external database server by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Delete an external database server by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_with_http_info(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `delete`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_database_server_usage(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server usage by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_database_server_usage(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServerUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_database_server_usage_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_database_server_usage_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
            return data

    def get_database_server_usage_with_http_info(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server usage by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_database_server_usage_with_http_info(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServerUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_database_server_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `get_database_server_usage`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `get_database_server_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExternalDatabaseServerUsage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_redacted(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_redacted(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_redacted_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_redacted_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
            return data

    def get_redacted_with_http_info(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_redacted_with_http_info(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_redacted" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `get_redacted`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `get_redacted`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExternalDatabaseServer',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server status by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_status(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_status_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
            return data

    def get_status_with_http_info(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server status by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_status_with_http_info(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `get_status`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `get_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Status',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_template_redacted(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server template by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_template_redacted(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServerTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_template_redacted_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_template_redacted_with_http_info(environment, external_database_server, **kwargs)  # noqa: E501
            return data

    def get_template_redacted_with_http_info(self, environment, external_database_server, **kwargs):  # noqa: E501
        """Get an external database server template by name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_template_redacted_with_http_info(environment, external_database_server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :return: ExternalDatabaseServerTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_template_redacted" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `get_template_redacted`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `get_template_redacted`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}/template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExternalDatabaseServerTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, environment, **kwargs):  # noqa: E501
        """List all externalDatabaseServers  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list(environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_with_http_info(environment, **kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(environment, **kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, environment, **kwargs):  # noqa: E501
        """List all externalDatabaseServers  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_with_http_info(environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, environment, external_database_server, updated_template, **kwargs):  # noqa: E501
        """Update an existing external database server (unsupported)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update(environment, external_database_server, updated_template, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :param ExternalDatabaseServerTemplate updated_template: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_with_http_info(environment, external_database_server, updated_template, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(environment, external_database_server, updated_template, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, environment, external_database_server, updated_template, **kwargs):  # noqa: E501
        """Update an existing external database server (unsupported)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_with_http_info(environment, external_database_server, updated_template, async=True)
        >>> result = thread.get()

        :param async bool
        :param str environment: (required)
        :param str external_database_server: (required)
        :param ExternalDatabaseServerTemplate updated_template: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment', 'external_database_server', 'updated_template']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `update`")  # noqa: E501
        # verify the required parameter 'external_database_server' is set
        if ('external_database_server' not in params or
                params['external_database_server'] is None):
            raise ValueError("Missing the required parameter `external_database_server` when calling `update`")  # noqa: E501
        # verify the required parameter 'updated_template' is set
        if ('updated_template' not in params or
                params['updated_template'] is None):
            raise ValueError("Missing the required parameter `updated_template` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment' in params:
            path_params['environment'] = params['environment']  # noqa: E501
        if 'external_database_server' in params:
            path_params['externalDatabaseServer'] = params['external_database_server']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'updated_template' in params:
            body_params = params['updated_template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/d6.2/environments/{environment}/databaseServers/{externalDatabaseServer}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.latest.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
