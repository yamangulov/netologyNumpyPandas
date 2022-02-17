import pandas as pd

# задание 1
rdf = pd.read_csv('ratings.csv')

def qualify_class(value):
    if value <= 2:
        return 'низкий рейтинг'
    elif (value <= 4):
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'

rdf['class'] = rdf.rating.apply(qualify_class)

print(rdf.head(30))

# задание 2
# на всякий случай я предусмотрел вариант, когда в ключевых словах содержатся указатели на два и более регионов

kdf = pd.read_csv('keywords.csv')

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

def set_region(keyword):
    words = keyword.split(' ')
    regions = []
    for word in words:
        for key, value in geo_data.items():
            if word in value:
                regions.append(key)
    if len(regions) > 0:
        return ', '.join(regions)
    else:
        return 'undefined'

kdf['region'] = kdf.keyword.apply(set_region)

print(kdf[kdf.region != 'undefined'].head())

# задание 3
# rdf уже определен выше в задании 1
mdf = pd.read_csv('movies.csv')

years = range(1950, 2011)

def find_title(movieId):
    return mdf[mdf.movieId == movieId].title.values[0]

def production_year(title):
    for year in years:
        if str(year) in title:
            return year
    return 1900

rdf['title'] = rdf.movieId.apply(find_title)
rdf['year'] = rdf.title.apply(production_year)

def avr(row):
    return row.rating.mean()

result = rdf.groupby('year').apply(avr).sort_values(ascending=False)

print(result.head())