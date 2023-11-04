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
# cities_in_country = dict()
# for text in cites_original:
#     if text['country'] not in cities_in_country:
#         cities_in_country[text['country']] = [text['name']]
#     else:
#         cities_in_country[text['country']].append(text['name'])
#
# print(cities_in_country)


# формирование словаре стран с городами
cities_in_country = dict()
for text in cites_original:
    if text['country'] not in cities_in_country:
        cities_in_country[text['country']] = [text]
    else:
        cities_in_country[text['country']].append(text)

# print(cities_in_country['SJ'])
# print()
# print(cities_in_country['IM'])
# print()

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

# for country in cities_in_country:
#     features = []
#     for city in cities_in_country[country]:
#         features.append(
#             {
#                 "type": "Feature",
#                 "id": city['id'],
#                 "geometry": {
#                     "type": "Point",
#                     "coordinates": [city['coord']['lon'], city['coord']['lat']],
#                 },
#                 "properties": {
#                     "iconCaption": city["name"],
#                     "marker-color": "#b51eff",
#                 },
#             }
#         )
#
#     geojson = {
#         "type": "FeatureCollection",  # Обязательный параметр
#         "features": features
#     }
#
#     # Сериализация в JSON
#     json_geojson: str = json.dumps(geojson, ensure_ascii=False)
#     file_name = 'geo_' + country
#     with open(file_name, "w", encoding="utf-8") as json_file:
#         json_file.write(json_geojson)


# Рабочий вариант с одной страной

# 'SJ' 'IM' 'RU'
features = []
country = 'IM'
for city in cities_in_country[country]:
    i = 1
    features.append(
        {
            "type": "Feature",
            "id": city['id'],
            "geometry": {
                "type": "Point",
                "coordinates": [city['coord']['lon'], city['coord']['lat']],
            },
            "properties": {
                "iconCaption": city["name"],
                "marker-color": "#b51eff",
            },
        }
    )

# print(len(cities_in_country[country]), len(cities_in_country[country]) // 100 + 1)
for i in range(len(cities_in_country[country]) // 100 + 1):
    geojson = {
        "type": "FeatureCollection",  # Обязательный параметр
        "features": features[100 * i:100*(i+1)]
    }

    # Сериализация в JSON
    json_geojson: str = json.dumps(geojson, ensure_ascii=False)
    if len(cities_in_country[country]) // 100 + 1 == 1:
        file_name = 'geo_' + country
    else:
        file_name = 'geo_' + country + '_' + '0' * (2 - len(str(i+1))) + str(i+1)
    with open(file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_geojson)
