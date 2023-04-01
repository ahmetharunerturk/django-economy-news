from django.shortcuts import render
import requests

def index(request):
    r = requests.get('https://newsapi.org/v2/everything?q=economy&sortBy=popularity&pageSize=15&apiKey=') #https://newsapi.org/register
    res = r.json()
    data = res['articles']
    author = []
    title = []
    source = []
    date = []
    url = []
    description = []
    image=[]
    for i in data:
        author.append(i['author'])
        title.append(i['title'])
        source.append(i['source']['name'])
        date.append(i['publishedAt'])
        url.append(i['url'])
        image.append(i['urlToImage'])
        description.append(i['description'])
    news = zip(author,title,description,date,url,source,image)
    return render(request, 'index.html', {'news': news})


