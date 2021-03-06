# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.usage_api import UsageApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestUsageApi(unittest.TestCase):
    """UsageApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.usage_api.UsageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ingestion_policy(self):
        """Test case for create_ingestion_policy

        Create a specific ingestion policy  # noqa: E501
        """
        pass

    def test_delete_ingestion_policy(self):
        """Test case for delete_ingestion_policy

        Delete a specific ingestion policy  # noqa: E501
        """
        pass

    def test_export_csv(self):
        """Test case for export_csv

        Export a CSV report  # noqa: E501
        """
        pass

    def test_get_all_ingestion_policies(self):
        """Test case for get_all_ingestion_policies

        Get all ingestion policies for a customer  # noqa: E501
        """
        pass

    def test_get_ingestion_policy(self):
        """Test case for get_ingestion_policy

        Get a specific ingestion policy  # noqa: E501
        """
        pass

    def test_update_ingestion_policy(self):
        """Test case for update_ingestion_policy

        Update a specific ingestion policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
