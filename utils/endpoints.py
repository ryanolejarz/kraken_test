import json
import requests

from config import API_URL, API_VERSION

def _base_api_request(endpoint: str, req_type: str, data: dict = None, expect_error: bool = False) -> dict:
    """
    _base_api_request is to be called by all endpoint functions. It handles validation of the request
    as well as asserting the expected status code and error count.

    :param endpoint: api endpoint (not including base path)
    :param req_type: request type (get, del, patch, post, put)
    :param data: request body/data
    :param expect_error: returns the "error" object from the response body when True (for testing negative cases)
    :return: returns "result" from the response body by default (expect_error = False)
    """

    url = f'{API_URL}/{endpoint}'
    headers = {}

    assert req_type in ['get', 'del', 'patch', 'post', 'put'], f'Invalid request type {req_type}'
    if req_type == 'get':
        response = requests.get(url=url, headers=headers, data=data)
    elif req_type == 'patch':
        response = requests.patch(url=url, headers=headers, data=data)
    elif req_type == 'post':
        response = requests.post(url=url, headers=headers, data=data)
    elif req_type == 'put':
        response = requests.put(url=url, headers=headers, data=data)
    elif req_type == 'del':
        response = requests.delete(url=url, headers=headers, data=data)

    response_body = json.loads(response.text)
    status_code = response.status_code

    assert status_code == 200, f'Expected status code 200 but got {status_code}'

    error = response_body['error']
    if expect_error:
        assert len(error) > 0, 'Expected error(s) but none found'
        return error
    else:
        assert len(error) == 0, f'Expected no errors but found {len(error)}.\n {error}'
        result = response_body['result']
        return result

def get_server_time(expect_error: bool = False) -> dict:
    """ Get Server Time endpoint """
    endpoint = 'public/Time'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_system_status(expect_error: bool = False) -> dict:
    """ Get System Status endpoint """
    endpoint = 'public/SystemStatus'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_asset_info(asset: str = None, assets: list = None, expect_error: bool = False) -> dict:
    """ Get Asset Info endpoint """
    endpoint = 'public/Assets'
    if asset or assets:
        endpoint = f'{endpoint}?asset='
        if asset:
            endpoint = endpoint + asset
        elif assets:
            for asset in assets:
                endpoint = endpoint + f'{asset},'
            endpoint = endpoint[:-1] if endpoint[-1] == ',' else endpoint
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_tradable_asset_pairs(asset_pair: str = None, asset_pairs: list = None, expect_error: bool = False) -> dict:
    """ Get Tradable Asset Pairs endpoint """
    endpoint = 'public/AssetPairs'
    if asset_pair or asset_pairs:
        endpoint = f'{endpoint}?pair='
        if asset_pair:
            endpoint = endpoint + asset_pair
        elif asset_pairs:
            for pair in asset_pairs:
                endpoint = endpoint + f'{pair},'
            endpoint = endpoint[:-1] if endpoint[-1] == ',' else endpoint
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_ticket_info(asset_pair: str = None, asset_pairs: list = None, expect_error: bool = False) -> dict:
    """ Get Ticker Info endpoint """
    endpoint = f'public/Ticker'
    if asset_pair or asset_pairs:
        endpoint = f'{endpoint}?pair='
        if asset_pair:
            endpoint = endpoint + asset_pair
        elif asset_pairs:
            for pair in asset_pairs:
                endpoint = endpoint + f'{pair},'
            endpoint = endpoint[:-1] if endpoint[-1] == ',' else endpoint
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_ohlc_data(asset_pair: str, interval: int = None, since: int = None, expect_error: bool = False) -> dict:
    """ Get OHLC Data endpoint """
    endpoint = f'public/OHLC?pair={asset_pair}'
    if interval is not None:
        endpoint = endpoint + f'&interval={interval}'
    if since is not None:
        endpoint = endpoint + f'&since={since}'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_order_book(asset_pair: str, count: int = 100, expect_error: bool = False) -> dict:
    """ Get Order Book endpoint """
    endpoint = f'public/Depth?pair={asset_pair}&count={count}'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_recent_trades(asset_pair: str, since: int = None, expect_error: bool = False) -> dict:
    """ Get Recent Trades endpoint """
    endpoint = f'public/Trades?pair={asset_pair}'
    if since is not None:
        endpoint = endpoint + f'&since={since}'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)

def get_recent_spreads(asset_pair: str, since: int = None, expect_error: bool = False) -> dict:
    """ Get Recent Spreads endpoint """
    endpoint = f'public/Spread?pair={asset_pair}'
    if since is not None:
        endpoint = endpoint + f'&since={since}'
    req_type = 'get'
    return _base_api_request(endpoint=endpoint, req_type=req_type, expect_error=expect_error)
