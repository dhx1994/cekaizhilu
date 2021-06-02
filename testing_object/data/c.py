import yaml

with open("data.yml", encoding="utf-8") as f:
    data = yaml.safe_load(f.read())
test = data["data"]["/manage/systemAccount/getVerificationCode"]
print(test)
