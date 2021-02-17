import json
import urllib3
import argparse
from rite_aid import zip_search, stores

parser = argparse.ArgumentParser()
parser.add_argument("zip_code", help="currently supported zips: 11204, 07302, 07960")
parser.add_argument("--shot", help="shot number to check availability for", default=1, type=int)
args = parser.parse_args()

def check_appointments(zip_code:str, shot_number:int = 1) -> list:
    with urllib3.PoolManager() as http:
        stores = zip_search[zip_code]
        BASE_URL = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_num}"
        
        availabilities = list()

        return {
            store : json.loads(
                http.request('GET', BASE_URL.format(store_num = store), headers={'User-Agent': 'Mozilla/5.0'}).data
            )['Data']['slots'][str(shot_number)] for store in stores 
        }

if __name__ == '__main__':
    results = check_appointments(zip_code=args.zip_code, shot_number=args.shot)
    for store in results:
        if results[store]:
            print(f"Availability at Rite Aid #{store}")
            print(f"Address:\t{stores[store]['address']}")
            print(f"Phone #:\t{stores[store]['phone_number']}")