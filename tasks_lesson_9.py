import json

with open("city.list.json", "r", encoding="utf-8") as json_file:
    cites = json_file.read()

# Десериализация из JSON
address_original = json.loads(cites)

print(address_original[:2])
