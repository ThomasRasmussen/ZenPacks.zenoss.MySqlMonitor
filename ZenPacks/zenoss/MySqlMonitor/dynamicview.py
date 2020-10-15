##############################################################################
#
# Copyright (C) Zenoss, Inc. 2019, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

"""DynamicView adapters."""

from ZenPacks.zenoss.DynamicView import TAG_ALL, TAG_IMPACTED_BY, TAG_IMPACTS
from ZenPacks.zenoss.DynamicView.model.adapters import BaseRelationsProvider


class DeviceRelationsProvider(BaseRelationsProvider):
    """Relations provider for all devices."""

    def relations(self, type=TAG_ALL):
        if type in (TAG_ALL, TAG_IMPACTS):
            if self._adapted.aqBaseHasAttr("mysql_servers"):
                for mysql_server in self._adapted.mysql_servers():
                    yield self.constructRelationTo(mysql_server, TAG_IMPACTS)


class MySQLServerRelationsProvider(BaseRelationsProvider):
    """Relations provider for MySQL server components."""

    def relations(self, type=TAG_ALL):
        if type in (TAG_ALL, TAG_IMPACTED_BY):
            device = self._adapted.mysql_host()
            if device:
                yield self.constructRelationTo(device, TAG_IMPACTED_BY)

        if type in (TAG_ALL, TAG_IMPACTS):
            for database in self._adapted.databases():
                yield self.constructRelationTo(database, TAG_IMPACTS)


class MySQLDatabaseRelationsProvider(BaseRelationsProvider):
    """Relations provider for MySQL database components."""

    def relations(self, type=TAG_ALL):
        if type in (TAG_ALL, TAG_IMPACTED_BY):
            server = self._adapted.server()
            if server:
                yield self.constructRelationTo(server, TAG_IMPACTED_BY)
