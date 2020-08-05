
# необходимо получить записи всей стены странице vk

import requests
import time
import datetime
import csv
import pandas
import matplotlib.pyplot as plt


wordlist = []
def getjson(url,data=None):
    response = requests.get(url,params=data)
    response = response.json()

    return response

def all_posts(access_token,owner_id, count = 100, offset = 0):
    all_posts = []
    while True:
        wall = getjson("https://api.vk.com/method/wall.get", {
            'owner_id': owner_id,
            'count': count,
            'access_token': access_token,
            'offset': offset,
            'v': '5.101'
        })
        count_posts = wall['response']['count']
        posts = wall['response']['items']
        all_posts.extend(posts)
        print(len(all_posts),count_posts)
        if len(all_posts)>=count_posts:         # длинна стены
            break
        else:
            offset +=100
            time.sleep(1)

    return all_posts,posts

def make_posts(all_posts):
    filteres_data = []

    for post in all_posts:

        try:
            date = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%d-%m-%Y')
        except:
            date = ''

        try:
            time = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%H:%M:%S')
        except:
            time = ''


        try:
            likes = post['likes']['count']
        except:
            likes = 0


        try:
            reposts = post['reposts']['count']
        except:
            reposts = 0

        try:
            comments = post['comments']['count']
        except:
            comments = 0

        try:
            views = post['views']['count']
        except:
            views = 0

        try:
            attachments = post['attachments'][0]['type']

        except:
            attachments = ''



        try:
            text = post['text']
        except:
            text = ''
        wordlist.append(text) #фильтруем текст в отдельный список

        filtered_post = {
            'date': date,
            'time':time,
            'likes':likes,
            'reposts':reposts,
            'comments':comments,
            'views':views,
            'attachments': attachments,
            'text':text

        }

        filteres_data.append(filtered_post)
    print(wordlist)
    return filteres_data


def panda_s(data):
    df = pandas.DataFrame(data)
    df.to_csv('{}.csv'.format(datetime.datetime.today().strftime('%F,%H-%M-%S'))
              ,index=False, encoding='utf-8')

    df.to_excel("path11.xlsx",index=False, encoding='utf-8')



owner_id = '11547416'
access_token = '5db3b53bf8e3e6fd1ce5e78ebbafec0b04455a4554ba40018ad035f9baef8a41cafd451dd773c7998158e'
count = 2000
offset = 0

all_posts, posts= all_posts(access_token,owner_id)

pposts =  make_posts(all_posts)

panda_s(pposts)


