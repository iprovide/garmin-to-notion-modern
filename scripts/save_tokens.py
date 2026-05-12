import json, base64, os

tokenstore = os.path.expanduser("~/.garmin_tokens")
o1 = json.load(open(os.path.join(tokenstore, "oauth1_token.json")))
o2 = json.load(open(os.path.join(tokenstore, "oauth2_token.json")))
bundle = json.dumps({"oauth1": o1, "oauth2": o2})
print(base64.b64encode(bundle.encode()).decode())
