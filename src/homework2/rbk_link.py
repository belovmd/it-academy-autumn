import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.shortcuts import render
import operator
import matplotlib.pyplot as plt


# получаем список слов по всем ссылкам
word_list =()
def i(r):
    url_1 = 'https://www.rbc.ru/'

    r = requests.get(url_1).text
    soup = BeautifulSoup(r)
    for link in soup.find_all("span", {"class": "main__feed__title"}):
        content = link.text
        if  content:         # если есть данные ссылки
            words = content.lower().split()
            for each_word in words:
                word_list.append(each_word)

    print(word_list)




