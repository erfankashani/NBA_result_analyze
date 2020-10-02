import requests

DOWNLOAD_URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
TARGET_CSV_PATH = "../DATABASE/nba_all_elo.csv"

response = requests.get(DOWNLOAD_URL)

# check that the status was successful
response.raise_for_status()
with open(TARGET_CSV_PATH, 'wb') as f:
    f.write(response.content)
print('Download Ready.')
