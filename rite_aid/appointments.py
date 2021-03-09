import json
import urllib3

def check_appointments(stores,shot_number:int = 1) -> dict:
    with urllib3.PoolManager() as http:
        BASE_URL = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_num}"

        return {
            address : json.loads(
                http.request('GET', BASE_URL.format(store_num = storenum), headers={'User-Agent': 'Mozilla/5.0'}).data
            )['Data']['slots'][str(shot_number)] for storenum,address in stores.items() 
        }