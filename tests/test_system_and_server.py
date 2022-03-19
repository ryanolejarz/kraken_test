import pytest
from time import sleep

from tests.BaseTest import BaseTest


class TestSystemAndServer(BaseTest):

    def verify_system_status_response(self, result):
        result_keys = result.keys()
        expected_keys = ['status', 'timestamp']
        for key in expected_keys:
            assert key in result_keys, f'Expected key {key} not found.'

    def verify_server_time_response(self, result):
        result_keys = result.keys()
        expected_keys = ['unixtime', 'rfc1123']
        for key in expected_keys:
            assert key in result_keys, f'Expected key {key} not found.'

    @pytest.mark.smoke
    def test_system_online(self):
        """ tests the system status endpoint returns online status """
        result = self.get_system_status()
        status = result['status']
        assert status == 'online', f'Expected status online but got {status}'
        self.verify_system_status_response(result)

    @pytest.mark.smoke
    def test_system_status(self):
        """ tests the system status endpoint returns a valid response """
        result = self.get_system_status()
        status = result['status']
        valid_statuses = ['online', 'maintenance', 'cancel_only', 'post_only']
        assert status in valid_statuses, f'System returned invalid status {status}'
        self.verify_system_status_response(result)

    @pytest.mark.smoke
    def test_server_time(self):
        result = self.get_server_time()
        self.verify_server_time_response(result)

    @pytest.mark.regression
    def test_server_time_increasing(self):
        """ tests the server time is incrementing  """
        result_1 = self.get_server_time()
        sleep(1)
        result_2 = self.get_server_time()
        unix_time_1 = result_1['unixtime']
        unix_time_2 = result_2['unixtime']
        assert unix_time_2 > unix_time_1, f'Expected {unix_time_2} to be greater than {unix_time_1}'
