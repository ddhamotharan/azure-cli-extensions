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

from msrest.serialization import Model


class Usage(Model):
    """The usage data for a usage request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param unit: The unit of the metric. Possible values include: 'Count',
     'Bytes', 'Seconds', 'Percent', 'CountPerSecond', 'BytesPerSecond',
     'Milliseconds'
    :type unit: str or ~azure.mgmt.cosmosdb.models.UnitType
    :ivar name: The name information for the metric.
    :vartype name: ~azure.mgmt.cosmosdb.models.MetricName
    :ivar quota_period: The quota period used to summarize the usage values.
    :vartype quota_period: str
    :ivar limit: Maximum value for this metric
    :vartype limit: long
    :ivar current_value: Current value for this metric
    :vartype current_value: long
    """

    _validation = {
        'name': {'readonly': True},
        'quota_period': {'readonly': True},
        'limit': {'readonly': True},
        'current_value': {'readonly': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'MetricName'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'limit': {'key': 'limit', 'type': 'long'},
        'current_value': {'key': 'currentValue', 'type': 'long'},
    }

    def __init__(self, *, unit=None, **kwargs) -> None:
        super(Usage, self).__init__(**kwargs)
        self.unit = unit
        self.name = None
        self.quota_period = None
        self.limit = None
        self.current_value = None