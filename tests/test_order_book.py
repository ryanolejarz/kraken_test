import pytest

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestOrderBook(BaseTest):

    def verify_order_book_object(self, order_book):
        """ validates the data returned in the order book response """
        order_book_keys = order_book.keys()
        expected_keys = [
            {'key_name': 'asks', 'value_type': list},
            {'key_name': 'bids', 'value_type': list},
        ]
        for key in expected_keys:
            assert key['key_name'] in order_book_keys, f'Expected key {key} not found.'
            assert isinstance(order_book[key['key_name']], key['value_type']), \
                f'Expected {order_book[key["key_name"]]} to be type {key["value_type"]}'
        for ask in order_book['asks']:
            assert isinstance(ask[0], str), f'Expected {ask[0]} to be type str'
            assert isinstance(ask[1], str), f'Expected {ask[1]} to be type str'
            assert isinstance(ask[2], int), f'Expected {ask[2]} to be type int'
        for bid in order_book['bids']:
            assert isinstance(bid[0], str), f'Expected {bid[0]} to be type str'
            assert isinstance(bid[1], str), f'Expected {bid[1]} to be type str'
            assert isinstance(bid[2], int), f'Expected {bid[2]} to be type int'


    @pytest.mark.smoke
    def test_order_book(self):
        """ tests the order book result (including default count) """
        default_count = 100
        asset_pair = 'ADAUSD'
        result = self.get_order_book(asset_pair=asset_pair)
        self.verify_order_book_object(result[asset_pair])
        asks = len(result[asset_pair]['asks'])
        bids = len(result[asset_pair]['bids'])
        assert asks <= default_count, f'Expected <= {default_count} asks but found {asks}'
        assert bids <= default_count, f'Expected <= {default_count} bids but found {bids}'

    @pytest.mark.regression
    def test_min_and_max_counts(self):
        """ tests the min and max values of the count query param """
        counts = [1, 50]
        asset_pair = 'ADAUSD'
        for count in counts:
            result = self.get_order_book(asset_pair=asset_pair, count=count)
            asks = len(result[asset_pair]['asks'])
            bids = len(result[asset_pair]['bids'])
            assert asks <= count, f'Expected <= {count} asks but found {asks}'
            assert bids <= count, f'Expected <= {count} bids but found {bids}'

    @pytest.mark.errors
    def test_invalid_counts_return_default_count(self):
        """ tests the values outside of the range of the count query param """
        invalid_counts = [0, 501]
        default_count = 100
        asset_pair = 'ADAUSD'
        for count in invalid_counts:
            result = self.get_order_book(asset_pair=asset_pair, count=count)
            asks = len(result[asset_pair]['asks'])
            bids = len(result[asset_pair]['bids'])
            assert asks <= default_count, f'Expected <= {default_count} asks but found {asks}'
            assert bids <= default_count, f'Expected <= {default_count} bids but found {bids}'

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_known_order_books(self, asset_pair):
        """ tests order books for known asset pairs are found """
        count = 5
        result = self.get_order_book(asset_pair=asset_pair, count=count)
        self.verify_order_book_object(result[asset_pair])

    @pytest.mark.errors
    def test_invalid_order_book(self):
        """ tests when an order book is requested for an invalid asset pair """
        asset_pair = 'ABCXYZ'
        error = self.get_order_book(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.regression
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_ask_and_bid_sort_order(self, asset_pair):
        """ tests the asks and bids are sorted in the correct order (asks -> low to high, bids -> high to low """
        result = self.get_order_book(asset_pair=asset_pair)
        highest_ask = result[asset_pair]['asks'][0][0]
        highest_bid = result[asset_pair]['bids'][0][0]
        assert highest_ask > highest_bid, \
            f'Expected highest ask ({highest_ask}) to be greater than highest bid ({highest_bid})'

    @pytest.mark.regression
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_ask_greater_than_bid(self, asset_pair):
        """ tests that the highest ask price is higher than the highest bid price """
        result = self.get_order_book(asset_pair=asset_pair)
        asks = result[asset_pair]['asks']
        bids = result[asset_pair]['bids']
        for x in range(len(asks)):
            if x > 0:
                assert asks[x][0] > asks[x-1][0], f'Expected {asks[x][0]} to be higher than {asks[x-1][0]}'
        for x in range(len(bids)):
            if x > 0:
                assert bids[x][0] < bids[x-1][0], f'Expected {bids[x][0]} to be lower than {bids[x-1][0]}'
