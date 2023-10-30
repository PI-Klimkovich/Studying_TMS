import json

with open("city.list.json", "r", encoding="utf-8") as json_file:
    cites = json_file.read()

# Десериализация из JSON
cites_original = json.loads(cites)

# Необходимо сформировать geojson файл с координатами городов для одной страны.

# Создание списка стран
# countries = []
# for text in cites_original:
#     if text['country'] not in countries:
#         countries.append(text['country'])
# countries.sort()
#
# print(countries)
# print()
#
# cities_in_country = dict()
# for country in countries:
#     cities_in_country[country] = [text['name'] for text in cites_original if text['country'] == country]
#
# print(cities_in_country)

# Улучшенный алгоритм
cities_in_country = dict()
for text in cites_original:
    if text['country'] not in cities_in_country:
        cities_in_country[text['country']] = [text['name']]
    else:
        cities_in_country[text['country']].append(text['name'])

# print(cities_in_country)

# Сериализация в JSON
# json_country: str = json.dumps(country, ensure_ascii=False)
# print(type(json_country))
# print(json_country)
# with open("test.json", "w", encoding="utf-8") as json_file:
#    json_file.write(json_country)

# for country in countries:
#     file_name = 'geo_' + country
#     with open(file_name, "w", encoding="utf-8") as file:
#         for i in range(len(cities_in_country[country])):
#             file.write(cities_in_country[country][i] + '\n')
#   print(file_name)




print()

features = []


geojson = {
    "type": "FeatureCollection",  # Обязательный параметр
    "features": [  # Список данных для отображения на карте
        {
            "type": "Feature",  # Обязательный параметр
            "id": "cityID",  # Идентификатор берем из данных города
            "geometry": {
                "type": "Point",  # Обязательно Point, город будет меткой
                "coordinates": [-65.23, 123.11],
            },
            "properties": {
                "iconCaption": "name",      # Название города
                "marker-color": "#b51eff",  # Цвет метки
            },
        },
        ...  # Другие элементы коллекции
    ]
}

print(geojson)
