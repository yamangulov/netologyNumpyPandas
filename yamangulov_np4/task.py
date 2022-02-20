import pandas as pd

# задание 1
log = pd.read_csv('visit_log.csv', sep=';')

def set_source_type(row):
    if (row.traffic_source == 'yandex') | (row.traffic_source == 'google'):
        return 'organic'
    elif(row.traffic_source == 'paid') | (row.traffic_source == 'email'):
        if(row.region == 'Russia'):
            return 'ad'
        else:
            return 'other'
    else:
        return row.traffic_source

log['source_type'] = log.apply(set_source_type, axis=1)

print(log.head())

# задание 2
urls = pd.read_csv('URLs.txt')
pattern = r'\/(\d){8}-'
urls = urls[urls.url.str.contains(pattern)]
print(urls.head())

# задание 3
df = pd.read_csv('ratings.csv')

df = df.groupby('userId').agg({'userId' : 'count', 'timestamp' : ['max', 'min']})
df = df[df['userId']['count'] > 100]
df['timelife'] = df['timestamp']['max'] - df['timestamp']['min']

print(df.head())

# задание 4
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

tab_1 = rzd.merge(auto, on='client_id', how='outer').merge(air, on='client_id', how='outer')
print(tab_1)
tab_2 = tab_1.merge(client_base, on='client_id', how='outer')
print(tab_2)



