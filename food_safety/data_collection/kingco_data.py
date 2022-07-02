import requests
import json
import pandas as pd

import urllib

king_co_endpoint = 'https://data.kingcounty.gov/resource/f29f-zza5.json'

def get_rating_from_name(name):

    name_upper = name.upper()
    where_clause = f"name like '%{name_upper}%'"
    where_encoded = urllib.parse.quote(where_clause)

    base_url = 'https://data.kingcounty.gov/resource/f29f-zza5.json'

    url = base_url + '?$where=' + where_encoded
    print(url)

    resp = requests.get(url)
    data = json.loads(resp.text)

    return data