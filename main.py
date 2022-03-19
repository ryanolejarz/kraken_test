from tests.BaseTest import BaseTest


test = BaseTest()
#print(test.get_all_tradable_asset_pairs())
print(test.get_tradable_asset_pairs(asset_pair='ADAUSD'))
# print(test.get_tradable_asset_pairs(asset_pairs=['ADAUSD','SHIBUSD']))