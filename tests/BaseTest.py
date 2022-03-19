from utils import endpoints as api

class BaseTest:

    def setup(self):
        return

    def teardown(self):
        return

    def get_server_time(self, expect_error: bool = False) -> dict:
        """
        Returns the server time via the Get Server Time API
            Parameters:
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_server_time(expect_error=expect_error)

    def get_system_status(self, expect_error: bool = False) -> dict:
        """
        Returns the system status via the Get System Status API
            Parameters:
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_system_status(expect_error=expect_error)

    def get_all_assets(self, expect_error: bool = False) -> dict:
        """
        Returns all assets via the Get Asset Info API
            Parameters:
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetInfo): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_asset_info(expect_error=expect_error)

    def get_asset_info(self, asset: str, expect_error: bool = False) -> dict:
        """
        Returns asset info a single asset via the Get Asset Info API
            Parameters:
                asset (str): an asset
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetInfo): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_asset_info(asset=asset, expect_error=expect_error)

    def get_multiple_asset_info(self, assets: list, expect_error: bool = False) -> dict:
        """
        Returns asset info for multiple assets via the Get Asset Info API
            Parameters:
                assets (list): a list of assets
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetInfo): returned if expect_error = False (default)
                    asset (AssetInfo):
                        aclass (str): asset class
                        altname (str): alternate name
                        decimals (int): scaling decimal places for record keeping
                        display_decimals (int): scaling decimal places for output display
                error (list): returned if expect_error = True
        """
        return api.get_asset_info(assets=assets, expect_error=expect_error)

    def get_all_tradable_asset_pairs(self, expect_error: bool = False) -> dict:
        """
        Returns all asset pairs via the Get Tradable Asset Pairs API
            Parameters:
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetPairs): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_tradable_asset_pairs(expect_error=expect_error)

    def get_tradable_asset_pairs(self, asset_pair: str = None, asset_pairs: list = None,
                                 expect_error: bool = False) -> dict:
        """
        Returns tradable asset pair info via the Get Tradable Asset Pairs API
            Parameters:
                asset_pair (str): asset pairs to get data for
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetPairs): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_tradable_asset_pairs(asset_pair=asset_pair, asset_pairs=asset_pairs, expect_error=expect_error)

    def get_ticker_info(self, asset_pair: str = None, asset_pairs: list = None, expect_error: bool = False) -> dict:
        """
        Returns ticker info via the Get Ticker Info API
            Parameters:
                asset_pair (str): asset pair to get data for
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of AssetTickerInfo): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_ticker_info(asset_pair=asset_pair, asset_pairs=asset_pairs, expect_error=expect_error)

    def get_ohlc_data(self, asset_pair: str = None, interval: int = None,
                      since: int = None, expect_error: bool = False) -> dict:
        """
        Returns OHCL data via the Get OHLC Data API
            Parameters:
                asset_pair (str): asset pair to get data for
                interval (int): time frame interval in minutes
                since (int): return committed OHLC data since given ID
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict of TickData): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_ohlc_data(asset_pair=asset_pair, interval=interval, since=since, expect_error=expect_error)

    def get_order_book(self, asset_pair: str, count: int = 100, expect_error: bool = False) -> dict:
        """
        Returns order book data via the Get Order Book Data API
            Parameters:
                asset_pair (str): asset pair to get data for
                count (int): maximum number of asks/bids
                expect_error (bool): set to True to return error information (for testing negative cases)
            Returns:
                result (dict (OrderBook)): returned if expect_error = False (default)
                error (list): returned if expect_error = True
        """
        return api.get_order_book(asset_pair=asset_pair, count=count, expect_error=expect_error)

    def get_recent_trades(self, asset_pair: str, since: int = None, expect_error: bool = False) -> dict:
        """
        Returns recent trade data via the Get Recent Trades Data API
            Parameters:
                asset_pair (str): asset pair to get data for
                since (int): return trade data since given timestamp
            Returns:
                result (dict): returned if expect_error = False (default)
                    pair (dict of TickData)
                    last (int): ID to be used as since when polling for new trade data
                error (list): returned if expect_error = True
        """
        return api.get_recent_trades(asset_pair=asset_pair, since=since, expect_error=expect_error)

    def get_recent_spreads(self, asset_pair: str, since: int = None, expect_error: bool = False) -> dict:
        """
        Returns recent spread data via the Get Recent Spreads Data API
            Parameters:
                asset_pair (str): asset pair to get data for
                since (int): return trade data since given timestamp
            Returns:
                result (dict): returned if expect_error = False (default)
                    pair (dict of SpreaeData)
                    last (int): ID to be used as since when polling for new trade data
                error (list): returned if expect_error = True
        """
        return api.get_recent_spreads(asset_pair=asset_pair, since=since, expect_error=expect_error)

