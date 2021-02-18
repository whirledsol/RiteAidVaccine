import os
import datetime
from rite_aid.appointments import check_appointments
from rite_aid.messenger import Messenger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("zip_code", help="currently supported zips: 11204, 07302, 07960")
parser.add_argument(
    "--shot", help="shot number to check availability for", default=1, type=int
)
args = parser.parse_args()

if __name__ == "__main__":
    results = check_appointments(zip_code=args.zip_code, shot_number=args.shot)
    messenger = Messenger()
    print(f"\nStarting Run: {datetime.datetime.now()}\n")
    for store in results:
        if results[store]:
            print(f"\t#{store}: AVAILABLE")
            messenger.notify_availability(store)
        else:
            print(f"\t#{store}: No Availabilities")