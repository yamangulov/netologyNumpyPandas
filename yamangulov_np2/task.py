import pandas as pd

rdf = pd.read_csv('ratings.csv')
rdf = rdf[rdf.rating == 5.0]
rdf = pd.DataFrame(rdf['movieId'].value_counts().head(1))
movieId = rdf.movieId.index.values[0]
movieQuantity = rdf.movieId.values[0]
mdf = pd.read_csv('movies.csv')
movieName = mdf[mdf.movieId == movieId].title.values[0]
print(f'Фильму {movieName} было выставлено максимальное значение оценок 5.0 - {movieQuantity}')

pdf = pd.read_csv('power.csv')
pdf = pdf[
    ((pdf.country == 'Lithuania') | (pdf.country == 'Latvia') | (pdf.country == 'Estonia')) &
                ((pdf.category == 4) | (pdf.category == 12) | (pdf.category == 21)) &
                pdf.year.ge(2005) & pdf.year.le(2010) & pdf.quantity > 0
    ]
sum_ = sum(pdf.quantity)
print(sum_)

page_url = 'https://fortrader.org/quotes'
tdf = pd.read_html(page_url)
print(tdf)