import requests

body = {}
body["osType"] = 2
body["clientVersion"] = "1.1.0"
headers = {}
r=requests.post("https://api.cggr-game.jp/version_check.php", data=body, headers=headers)
print(r.text)
