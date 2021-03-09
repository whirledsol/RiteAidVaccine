import os
import datetime
import json
from rite_aid.appointments import check_appointments
from rite_aid.messenger import Messenger
import argparse
from dotenv import load_dotenv
load_dotenv()

def main():
    args = parse()
    stores = load_store_info()
    results = check_appointments(stores,shot_number=args.shot)
    messenger = Messenger()
    print(f"\nStarting Run: {datetime.datetime.now()}\n")
    for store in results:
        if results[store]:
            print(f"\t#{store}: AVAILABLE")
            messenger.notify_availability(store)
        else:
            print(f"\t#{store}: No Availabilities")


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