from utils import endpoints as api

class BaseTest:

    def setup(self):
        return

    def teardown(self):
        return

    def get_server_time(self, expect_error: bool = False):
        return api.get_server_time(expect_error=expect_error)

    def get_system_status(self, expect_error: bool = False):
        return api.get_system_status(expect_error=expect_error)

    def get_all_assets(self, expect_error: bool = False):
        return api.get_asset_info(expect_error=expect_error)

    def get_asset_info(self, asset: str = None, assets: list = None, expect_error: bool = False):
        return api.get_asset_info(asset=asset, assets=assets, expect_error=expect_error)

    def get_all_tradable_asset_pairs(self, expect_error: bool = False):
        return api.get_tradable_asset_pairs(expect_error=expect_error)

    def get_tradable_asset_pairs(self, asset_pair: str = None, asset_pairs: list = None, expect_error: bool = False):
        return api.get_tradable_asset_pairs(asset_pair=asset_pair, asset_pairs=asset_pairs, expect_error=expect_error)

    def get_ticket_info(self, asset_pair: str = None, asset_pairs: list = None, expect_error: bool = False):
        return api.get_ticket_info(asset_pair=asset_pair, asset_pairs=asset_pairs, expect_error=expect_error)

    def get_ohlc_data(self, asset_pair: str = None, interval: int = None, since: int = None, expect_error: bool = False):
        return api.get_ohlc_data(asset_pair=asset_pair, interval=interval, since=since, expect_error=expect_error)

    def get_order_book(self, asset_pair: str, count: int = 100, expect_error: bool = False):
        return api.get_order_book(asset_pair=asset_pair, count=count, expect_error=expect_error)

    def get_recent_trades(self, asset_pair: str, since: int = None, expect_error: bool = False):
        return api.get_recent_trades(asset_pair=asset_pair, since=since, expect_error=expect_error)

    def get_recent_spreads(self, asset_pair: str, since: int = None, expect_error: bool = False):
        return api.get_recent_spreads(asset_pair=asset_pair, since=since, expect_error=expect_error)

