##############################################################################
#
# Copyright (C) Zenoss, Inc. 2019, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap

try:
    from ZenPacks.zenoss.DynamicView.tests import DynamicViewTestCase
except ImportError:
    import unittest

    @unittest.skip("tests require DynamicView >= 1.7.0")
    class DynamicViewTestCase(unittest.TestCase):
        """TestCase stub if DynamicViewTestCase isn't available."""


class DynamicViewTests(DynamicViewTestCase):
    """DynamicView tests."""

    # ZenPacks to initialize for testing purposes.
    zenpacks = [
        "ZenPacks.zenoss.MySqlMonitor",
    ]

    # Expected impact relationships.
    expected_impacts = """
    [linux1]->[linux1/server1]
    [linux1/server1]->[linux1/database1]
    """

    # Devices to create.
    device_data = {
        "linux1": {
            "deviceClass": "/Server/Linux",
            "dataMaps": [
                RelationshipMap(
                    modname="ZenPacks.zenoss.MySqlMonitor.MySQLServer",
                    relname="mysql_servers",
                    objmaps=[ObjectMap({"id": "server1"})]),

                RelationshipMap(
                    modname="ZenPacks.zenoss.MySqlMonitor.MySQLDatabase",
                    compname="mysql_servers/server1",
                    relname="databases",
                    objmaps=[ObjectMap({"id": "database1"})]),
            ],
        },

        "lpar1device": {
            "deviceClass": "/Server/SSH/AIX",
            "zPythonClass": "ZenPacks.zenoss.AixMonitor.Device",
            "dataMaps": [ObjectMap({"systemId": "findme-lpar1"})],
        }
    }

    def test_impacts(self):
        self.check_impacts()
