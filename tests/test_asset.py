import pytest

from utils.test_data import ASSETS
from tests.BaseTest import BaseTest


class TestAsset(BaseTest):

    def verify_asset_object(self, asset):
        """ validates the data returned in the asset response """
        asset_keys = asset.keys()
        expected_keys = [
            {'key_name': 'aclass', 'value_type': str},
            {'key_name': 'altname', 'value_type': str},
            {'key_name': 'decimals', 'value_type': int},
            {'key_name': 'display_decimals', 'value_type': int}
        ]
        for key in expected_keys:
            assert key['key_name'] in asset_keys, f'Expected key {key} not found.'
            assert isinstance(asset[key['key_name']], key['value_type']), \
                f'Expected {asset[key["key_name"]]} to be type {key["value_type"]}'

    @pytest.mark.smoke
    def test_single_asset(self):
        """ tests when a single asset is requested """
        asset = 'ADA'
        result = self.get_asset_info(asset=asset)
        assert asset in result.keys(), f'{asset} not found in result.'
        self.verify_asset_object(result[asset])

    @pytest.mark.smoke
    def test_multiple_assets(self):
        """ tests when multiple assets are requested """
        assets = ['ADA', 'DOT']
        result = self.get_asset_info(assets=assets)
        for asset in assets:
            assert asset in result.keys(), f'{asset} not found in result.'
            self.verify_asset_object(result[asset])

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_obj", ASSETS)
    def test_get_assets(self, asset_obj):
        """ tests when all assets are requested """
        asset = asset_obj['altname']
        if asset_obj['type'] == 'fiat':
            asset = 'Z' + asset
        result = self.get_all_assets()
        assert asset in result.keys(), f'{asset} not found in result.'
        self.verify_asset_object(result[asset])

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_obj", ASSETS)
    def test_asset_info(self, asset_obj):
        """ tests the returned data for each asset is as expected """
        asset = asset_obj['altname']
        result = self.get_asset_info(asset=asset)
        if asset_obj['type'] == 'fiat':
            asset_info = result[f'Z{asset_obj["altname"]}']
        else:
            asset_info = result[asset]
        assert asset_info['aclass'] == asset_obj['aclass'], \
            f'Expected aclass to be {asset_obj["aclass"]} but was {asset_info["aclass"]}'
        assert asset_info['altname'] == asset_obj['altname'], \
            f'Expected altname to be {asset_obj["alt_name"]} but was {asset_info["altname"]}'
        assert asset_info['decimals'] == asset_obj['decimals'], \
            f'Expected decimals to be {asset_obj["decimals"]} but was {asset_info["decimals"]}'
        assert asset_info['display_decimals'] == asset_obj['display_decimals'], \
            f'Expected display_decimals to be {asset_obj["display_decimals"]} but was {asset_info["display_decimals"]}'

    @pytest.mark.errors
    def test_invalid_asset(self):
        """ tests when an invalid asset is requested """
        asset = 'XXX'
        error = self.get_asset_info(asset=asset, expect_error=True)
        expected_error = 'EQuery:Unknown asset'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'
