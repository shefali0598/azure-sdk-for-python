# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class LogAnalyticsOperations(object):
    """LogAnalyticsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. Current version is 2017-04-02. Constant value: "2020-09-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-09-01"

        self.config = config

    def get_log_analytics_metrics(
            self, resource_group_name, profile_name, metrics, date_time_begin, date_time_end, granularity, group_by=None, continents=None, country_or_regions=None, custom_domains=None, protocols=None, custom_headers=None, raw=False, **operation_config):
        """Get log report for AFD profile.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param metrics:
        :type metrics: list[str]
        :param date_time_begin:
        :type date_time_begin: datetime
        :param date_time_end:
        :type date_time_end: datetime
        :param granularity: Possible values include: 'PT5M', 'PT1H', 'P1D'
        :type granularity: str
        :param group_by:
        :type group_by: list[str]
        :param continents:
        :type continents: list[str]
        :param country_or_regions:
        :type country_or_regions: list[str]
        :param custom_domains:
        :type custom_domains: list[str]
        :param protocols:
        :type protocols: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MetricsResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.MetricsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_log_analytics_metrics.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['metrics'] = self._serialize.query("metrics", metrics, '[str]', div=',')
        query_parameters['dateTimeBegin'] = self._serialize.query("date_time_begin", date_time_begin, 'iso-8601')
        query_parameters['dateTimeEnd'] = self._serialize.query("date_time_end", date_time_end, 'iso-8601')
        query_parameters['granularity'] = self._serialize.query("granularity", granularity, 'str')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query("group_by", group_by, '[str]', div=',')
        if continents is not None:
            query_parameters['continents'] = self._serialize.query("continents", continents, '[str]', div=',')
        if country_or_regions is not None:
            query_parameters['countryOrRegions'] = self._serialize.query("country_or_regions", country_or_regions, '[str]', div=',')
        if custom_domains is not None:
            query_parameters['customDomains'] = self._serialize.query("custom_domains", custom_domains, '[str]', div=',')
        if protocols is not None:
            query_parameters['protocols'] = self._serialize.query("protocols", protocols, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('MetricsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_log_analytics_metrics.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getLogAnalyticsMetrics'}

    def get_log_analytics_rankings(
            self, resource_group_name, profile_name, rankings, metrics, max_ranking, date_time_begin, date_time_end, custom_domains=None, custom_headers=None, raw=False, **operation_config):
        """Get log analytics ranking report for AFD profile.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param rankings:
        :type rankings: list[str]
        :param metrics:
        :type metrics: list[str]
        :param max_ranking:
        :type max_ranking: float
        :param date_time_begin:
        :type date_time_begin: datetime
        :param date_time_end:
        :type date_time_end: datetime
        :param custom_domains:
        :type custom_domains: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RankingsResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.RankingsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_log_analytics_rankings.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['rankings'] = self._serialize.query("rankings", rankings, '[str]', div=',')
        query_parameters['metrics'] = self._serialize.query("metrics", metrics, '[str]', div=',')
        query_parameters['maxRanking'] = self._serialize.query("max_ranking", max_ranking, 'float')
        query_parameters['dateTimeBegin'] = self._serialize.query("date_time_begin", date_time_begin, 'iso-8601')
        query_parameters['dateTimeEnd'] = self._serialize.query("date_time_end", date_time_end, 'iso-8601')
        if custom_domains is not None:
            query_parameters['customDomains'] = self._serialize.query("custom_domains", custom_domains, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RankingsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_log_analytics_rankings.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getLogAnalyticsRankings'}

    def get_log_analytics_locations(
            self, resource_group_name, profile_name, custom_headers=None, raw=False, **operation_config):
        """Get all available location names for AFD log analytics report.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ContinentsResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.ContinentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_log_analytics_locations.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ContinentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_log_analytics_locations.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getLogAnalyticsLocations'}

    def get_log_analytics_resources(
            self, resource_group_name, profile_name, custom_headers=None, raw=False, **operation_config):
        """Get all endpoints and custom domains available for AFD log report.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourcesResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.ResourcesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_log_analytics_resources.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ResourcesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_log_analytics_resources.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getLogAnalyticsResources'}

    def get_waf_log_analytics_metrics(
            self, resource_group_name, profile_name, metrics, date_time_begin, date_time_end, granularity, actions=None, group_by=None, rule_types=None, custom_headers=None, raw=False, **operation_config):
        """Get Waf related log analytics report for AFD profile.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param metrics:
        :type metrics: list[str]
        :param date_time_begin:
        :type date_time_begin: datetime
        :param date_time_end:
        :type date_time_end: datetime
        :param granularity: Possible values include: 'PT5M', 'PT1H', 'P1D'
        :type granularity: str
        :param actions:
        :type actions: list[str]
        :param group_by:
        :type group_by: list[str]
        :param rule_types:
        :type rule_types: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: WafMetricsResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.WafMetricsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_waf_log_analytics_metrics.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['metrics'] = self._serialize.query("metrics", metrics, '[str]', div=',')
        query_parameters['dateTimeBegin'] = self._serialize.query("date_time_begin", date_time_begin, 'iso-8601')
        query_parameters['dateTimeEnd'] = self._serialize.query("date_time_end", date_time_end, 'iso-8601')
        query_parameters['granularity'] = self._serialize.query("granularity", granularity, 'str')
        if actions is not None:
            query_parameters['actions'] = self._serialize.query("actions", actions, '[str]', div=',')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query("group_by", group_by, '[str]', div=',')
        if rule_types is not None:
            query_parameters['ruleTypes'] = self._serialize.query("rule_types", rule_types, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('WafMetricsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_waf_log_analytics_metrics.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getWafLogAnalyticsMetrics'}

    def get_waf_log_analytics_rankings(
            self, resource_group_name, profile_name, metrics, date_time_begin, date_time_end, max_ranking, rankings, actions=None, rule_types=None, custom_headers=None, raw=False, **operation_config):
        """Get WAF log analytics charts for AFD profile.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within
         the resource group.
        :type profile_name: str
        :param metrics:
        :type metrics: list[str]
        :param date_time_begin:
        :type date_time_begin: datetime
        :param date_time_end:
        :type date_time_end: datetime
        :param max_ranking:
        :type max_ranking: float
        :param rankings:
        :type rankings: list[str]
        :param actions:
        :type actions: list[str]
        :param rule_types:
        :type rule_types: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: WafRankingsResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.WafRankingsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AfdErrorResponseException<azure.mgmt.cdn.models.AfdErrorResponseException>`
        """
        # Construct URL
        url = self.get_waf_log_analytics_rankings.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['metrics'] = self._serialize.query("metrics", metrics, '[str]', div=',')
        query_parameters['dateTimeBegin'] = self._serialize.query("date_time_begin", date_time_begin, 'iso-8601')
        query_parameters['dateTimeEnd'] = self._serialize.query("date_time_end", date_time_end, 'iso-8601')
        query_parameters['maxRanking'] = self._serialize.query("max_ranking", max_ranking, 'float')
        query_parameters['rankings'] = self._serialize.query("rankings", rankings, '[str]', div=',')
        if actions is not None:
            query_parameters['actions'] = self._serialize.query("actions", actions, '[str]', div=',')
        if rule_types is not None:
            query_parameters['ruleTypes'] = self._serialize.query("rule_types", rule_types, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AfdErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('WafRankingsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_waf_log_analytics_rankings.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getWafLogAnalyticsRankings'}
