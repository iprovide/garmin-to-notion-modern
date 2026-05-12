import json, os, sys

bundle_path = "/tmp/garmin_bundle.json"
tokenstore = os.path.expanduser("~/.garmin_tokens")

data = json.load(open(bundle_path))
os.makedirs(tokenstore, exist_ok=True)
json.dump(data["oauth1"], open(os.path.join(tokenstore, "oauth1_token.json"), "w"))
json.dump(data["oauth2"], open(os.path.join(tokenstore, "oauth2_token.json"), "w"))
print("Restored both token files successfully.")
