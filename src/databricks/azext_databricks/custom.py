# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument
from .aaz.latest.databricks.workspace import Create as _DatabricksWorkspaceCreate

import random
import string

from azure.cli.core.aaz import has_value


def id_generator(size=13, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class DatabricksWorkspaceCreate(_DatabricksWorkspaceCreate):

    def pre_operations(self):
        from msrestazure.tools import is_valid_resource_id, resource_id
        """Parse managed resource_group which can be either resource group name or id, generate a randomized name if not provided"""
        args = self.ctx.args
        subscription_id = self.ctx.subscription_id
        workspace_name = args.name.to_serialized_data()
        if has_value(args.managed_resource_group):
            managed_resource_group = args.managed_resource_group.to_serialized_data()

        if not has_value(args.managed_resource_group):
            args.managed_resource_group = resource_id(
                subscription=subscription_id,
                resource_group='databricks-rg-' + workspace_name + '-' + id_generator())
        elif not is_valid_resource_id(managed_resource_group):
            args.managed_resource_group = resource_id(
                subscription=subscription_id,
                resource_group=managed_resource_group)
