import requests
import json

resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
raw_data = resp.content
json_result = json.loads(raw_data)
print(json_result["lines"][0])