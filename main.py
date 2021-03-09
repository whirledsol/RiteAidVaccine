import os
import datetime
import json
from rite_aid.appointments import check_appointments
from rite_aid.messenger import Messenger
import argparse
from pathlib import Path



def main():
    print(f"\nStarting Run: {datetime.datetime.now()}\n")
    args = parse()
    stores = load_store_info()
    results = check_appointments(stores,shot_number=args.shot)
    messenger = Messenger()

    available_count = 0
    for store in results:
        if results[store]:
            print(f"\t{store}: AVAILABLE")
            messenger.notify_availability(store)
            available_count+=1
        else:
            print(f"\t{store}: No Availabilities")
    
    if(available_count == 0):
        print('Sorry, nothing found.')
        
    print('###### PROGRAM END ######')

def message_test():
    messenger = Messenger()
    messenger.notify_availability("TEST")

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shot", help="shot number to check availability for", default=1, type=int
    )
    return parser.parse_args()


def load_store_info(path:str='stores.json'):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, path)
    with open(file_path, 'r') as store_info:
        return json.load(store_info)




if __name__ == "__main__":
    main()