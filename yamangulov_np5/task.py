import pandas as pd
import requests
from bs4 import BeautifulSoup
import vk_api

# задание 1 (основное + дополнительное)
KEYWORDS = ['тест', 'истории']
page_link = 'https://habr.com/ru/all/'
base_link = 'https://habr.com'

def get_habr_articles(page_link):
    res = requests.get(page_link)
    soup = BeautifulSoup(res.text)
    articles = soup.findAll('div', 'tm-article-snippet')
    return articles

def get_articles_data(articles, base_link):
    df = pd.DataFrame()
    for article in articles:
        title = article.find('a', 'tm-article-snippet__title-link').find('span').text
        date = article.find('span', 'tm-article-snippet__datetime-published').find('time').get('datetime')
        link = base_link + article.find('a', 'tm-article-snippet__title-link').get('href')
        res_article = requests.get(link)
        soup_article = BeautifulSoup(res_article.text, features='lxml')
        text = soup_article.find('div', 'article-formatted-body').find('div').text
        row = {'date' : date, 'title' : title, 'link' : link, 'text' : text}
        df = pd.concat([df, pd.DataFrame([row])]).reset_index(drop=True)
    return df

def get_filtered_articles_data(df, keywords):
    fitered_df = pd.DataFrame()
    for keyword in keywords:
        fitered_df_by_one_keyword = df[df.title.str.contains(keyword) | df.text.str.contains(keyword)]
        fitered_df = pd.concat([fitered_df, fitered_df_by_one_keyword])
    return fitered_df.reset_index(drop=True)

articles = get_habr_articles(page_link)
df = get_articles_data(articles, base_link)
fitered_df = get_filtered_articles_data(df, KEYWORDS)

print(fitered_df)

# задание 2 (основное)
url = 'https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data'
EMAIL = ['xxx@x.ru', 'yyy@y.ru']
headers_ = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Vaar-Header-App-Build-Version': '1.0.0',
    'Vaar-Header-App-Product-Name': 'hackcheck-web-avast',
    'Vaar-Version': '0'
}
json_ = {
    'emailAddresses': EMAIL
}
res = requests.post(url, json=json_, headers=headers_).json()['breaches']
df2 = pd.DataFrame()
for (key, value) in res.items():
    row = {'data' : value['publishDate'], 'source' : value['site'], 'description' : value['description']}
    df2 = pd.concat([df2, pd.DataFrame([row])]).reset_index(drop=True)
print(df2)

# задание 2 (дополнительное)
# самое понятное описание, как получить токен vk api, нашел вот здесь, в доках VK как-то все невнятно описано:
# https://dvmn.org/encyclopedia/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/
GROUP = 'netology'
TOKEN = 'your_token'

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_api.VkTools(vk_session)
# здесь все лимиты у меня почему-то не отработали, все равно выдается полный список,
# если не добавить счетчик в цикл по итератору ниже, выдаст много лишних записей, так что я просто обошел проблему
vk_res = vk.get_all_iter(method='wall.get', max_count=50, limit=50, values={'domain':GROUP, 'count': 50})
vk_df = pd.DataFrame()
i = 0
for res in vk_res:
    row = {'date' : res['date'], 'text' : res['text']}
    vk_df = pd.concat([vk_df, pd.DataFrame([row])]).reset_index(drop=True)
    i += 1
    if i == 50:
        break
print(vk_df.head(), len(vk_df))



