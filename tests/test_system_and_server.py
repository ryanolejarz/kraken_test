import pytest

from time import sleep

from tests.BaseTest import BaseTest


class TestSystemAndServer(BaseTest):

    @pytest.mark.smoke
    def test_system_status(self):
        """ tests the system status endpoint returns online status """
        result = self.get_system_status()
        status = result['status']
        assert status == 'online', f'Expected status online but got {status}'

    @pytest.mark.smoke
    def test_server_time(self):
        result = self.get_server_time()
        expected_keys = ['unixtime', 'rfc1123']
        result_keys = result.keys()
        for key in expected_keys:
            assert key in result_keys, f'Expected key {key} not found in result'

    @pytest.mark.regression
    def test_server_time_increasing(self):
        """ tests the server time is incrementing  """
        result_1 = self.get_server_time()
        sleep(1)
        result_2 = self.get_server_time()
        unix_time_1 = result_1['unixtime']
        unix_time_2 = result_2['unixtime']

        assert unix_time_2 > unix_time_1, f'Expected {unix_time_2} to be greater than {unix_time_1}'