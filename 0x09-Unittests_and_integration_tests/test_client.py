#!/usr/bin/env python3
"""_summary_
This script defines tests for client.py file
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test a resources without external called
    Args:
        unittest ([type]): [description]
    """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('requests.get')
    def test_org(self, param, mock_get):
        """ mock request HTTP without external called
        Args:
            param ([type]): [description]
            mock_get ([type]): [description]
        """
        json_test = {
            'type': 'OK'
        }
        mock_get.return_value.json.return_value = json_test
        response = GithubOrgClient(param)
        response.org
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """ test a private method to filter data from json
        """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) \
                as mock_org:
            mock_org.return_value = {
                'unknown': 'Ok',
                'repos_url': 'http://'
            }
            my_instance = GithubOrgClient('org')
            value = my_instance.org
            self.assertEqual(my_instance._public_repos_url, value['repos_url'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test the initial parameters
        Args:
            repo ([type]): [description]
            license_key ([type]): [description]
            expected ([type]): [description]
        """
        ret = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(ret, expected)
