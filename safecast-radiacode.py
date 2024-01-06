import csv
import json
import requests
import argparse

parser = argparse.ArgumentParser("safecast_radiacode")
parser.add_argument("filename", help="A .rctrk file exported from the radiacode app.")
parser.add_argument("apikey", help="Safecast apikey.")
args = parser.parse_args()

with open(args.filename, "r", encoding="utf8") as input_file:
    tsv_reader = csv.reader(input_file, delimiter="\t")

    # skip the first two rows
    next(tsv_reader)
    next(tsv_reader)

    for row in tsv_reader:
        (timestamp, time, latitude, longitude, accuracy, doserate, countrate, comment) = row
        f_doserate = float(doserate) / 100

        payload = {}

        # time has a space which needs to be replaced with a 'T'
        # time is in UTC+0000
        payload['captured_at'] = time.replace(" ", "T") + "+0000"
        payload['device_id'] = "247"
        payload['unit'] = "usv"
        payload['value'] = f"{f_doserate:.3f}"
        payload['latitude'] = latitude
        payload['longitude'] = longitude

        json_payload = json.dumps(payload)

        url = "https://api.safecast.org/en-US/measurements.json?api_key=" + args.apikey
        headers = { 'Content-Type': 'application/json' }

        response = requests.request("POST", url, headers=headers, data=json_payload)

        response.raise_for_status()

print("Finished!")
