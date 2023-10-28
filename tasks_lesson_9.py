import json

with open("city.list.json", "r", encoding="utf-8") as json_file:
    cites = json_file.read()

# Десериализация из JSON
cites_original = json.loads(cites)

# print(cites_original[0])

# Определить количество городов в файле.
count_cities = len(cites_original)
print('количество городов:', count_cities)
print()

# без 'пустых' объектов
count_cities = 0
for text in cites_original:
    if text['name'] != '' and text['country'] != '':
        count_cities += 1

print("количество городов:", count_cities, "без 'пустых' городов и стран")
print()

# Создать словарь, где ключ — это код страны, а значение — количество городов.
countries = []
for text in cites_original:
    if text['country'] not in countries:
        countries.append(text['country'])

cities_in_country = []
for country in countries:
    total = 0
    for text in cites_original:
        if text['country'] == country:
            total += 1
    cities_in_country.append(total)

count_cities_in_country = dict(zip(countries, cities_in_country))
print("Словарь количества городов в стране")
print(count_cities_in_country)
print()

# без 'пустых' объектов
countries = []
for text in cites_original:
    if text['country'] not in countries and text['country'] != '':
        countries.append(text['country'])

cities_in_country = []
for country in countries:
    total = 0
    for text in cites_original:
        if text['country'] == country and text['name'] != '':
            total += 1
    cities_in_country.append(total)

count_cities_in_country = dict(zip(countries, cities_in_country))
print("Словарь количества городов в стране без 'пустых' городов и стран")
print(count_cities_in_country)
# Проверка
# print(sum(cities_in_country))
print()

# Подсчитать количество городов в северном полушарии и в южном.

# Анализ файла показал, что под "name" записаны не только города!!
# Там скрываются и материки, а также встречаются и "пустышки"!

# Логически:
# - северное (N) - положительная широта;
# - южное (S) - отрицательная широта.
# Широта в базе 'lat'. Но, почему-то, на карте это не работает

count_n, count_s = 0, 0
for text in cites_original:
    if text['coord']['lat'] < 0:
        count_s += 1
    else:
        count_n += 1
print(f"Количество городов в северном полушарии {count_n} и южном {count_s}")
print("но есть сомнения по принадлежности к полушарию!!")
print()

# без 'пустых' объектов
count_n, count_s = 0, 0
for text in cites_original:
    if text['name'] != '' and text['country'] != '':
        if text['coord']['lat'] < 0:
            count_s += 1
        else:
            count_n += 1
print(f"Количество городов в северном полушарии {count_n} и южном {count_s} без 'пустых' городов и стран")
print("но есть сомнения по принадлежности к полушарию!!")
# print(count_s + count_n)
print()
