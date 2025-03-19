import json

# 讀取設定檔
with open("config.json", "r") as config_file:
    config = json.load(config_file)

API_KEY = config["API_KEY"]

print(f"機器人啟動成功！API 金鑰：{API_KEY}")
