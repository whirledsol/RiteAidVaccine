import json
import urllib3

def check_appointments(zip_code:str, shot_number:int = 1) -> list:
    zip_search = {
        "11204": [
            3766, 10577, 10579, 10575, 10574, 4246, 4679, 4876, 4257, 3869
        ],
        "07302": [
            1661, 4812
        ],
        "07960": [
            10435, 219
        ]
    }

    with urllib3.PoolManager() as http:
        stores = zip_search[zip_code]
        BASE_URL = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_num}"

        return {
            store : json.loads(
                http.request('GET', BASE_URL.format(store_num = store), headers={'User-Agent': 'Mozilla/5.0'}).data
            )['Data']['slots'][str(shot_number)] for store in stores 
        }