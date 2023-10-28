import json

with open("city.list.json", "r", encoding="utf-8") as json_file:
    cites = json_file.read()

# Десериализация из JSON
cites_original = json.loads(cites)

# Необходимо сформировать geojson файл с координатами городов для одной страны.

# Создание списка стран
countries = []
for text in cites_original:
    if text['country'] not in countries:
        countries.append(text['country'])

print(countries)
print()
