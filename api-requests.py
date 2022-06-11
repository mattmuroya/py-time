import json
import requests

res = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

print(json.dumps([({"Name": x["name"], "URL": x["web_url"]})
      for x in res.json()], indent=4))
