ASSETS = [
    {
        'aclass': 'currency',
        'altname': 'ADA',
        'decimals': 8,
        'display_decimals': 6,
        'type': 'crypto'
    },
    {
        'aclass': 'currency',
        'altname': 'DOT',
        'decimals': 10,
        'display_decimals': 8,
        'type': 'crypto'
    },
    {
        'aclass': 'currency',
        'altname': 'SHIB',
        'decimals': 5,
        'display_decimals': 0,
        'type': 'crypto'
    },
    {
        'aclass': 'currency',
        'altname': 'USD',
        'decimals': 4,
        'display_decimals': 2,
        'type': 'fiat'
    },
    {
        'aclass': 'currency',
        'altname': 'EUR',
        'decimals': 4,
        'display_decimals': 2,
        'type': 'fiat'
    }
]


ASSET_PAIRS = [ coin['altname'] + fiat['altname'] for coin in ASSETS if coin['type'] == 'crypto' for fiat in ASSETS if fiat['type'] == 'fiat']