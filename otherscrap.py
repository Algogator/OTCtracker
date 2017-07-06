import requests, bs4
res = requests.get('https://www.otcmarkets.com/stock/FNMA/quote')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
print(noStarchSoup.select('.quoteData'))
