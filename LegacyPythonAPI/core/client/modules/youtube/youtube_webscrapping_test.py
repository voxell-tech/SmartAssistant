from urllib import request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re



CHANNEL_FILTER = "&sp=EgIQAg%253D%253D"
VIDEO_FILTER = "&sp=EgIQAQ%253D%253D"

# soup = BeautifulSoup(page.content, 'html.parser')

def search_youtube(query, filter_id):
  channel_link = "https://www.youtube.com/results?search_query=" + query + filter_id
  print("search link:", channel_link)
  request_channel = requests.get(channel_link)

  # with open("./test.html", "w", encoding="utf-8") as f:
  #   f.write(request_channel.text)

  # print(request_channel.text)
  soup = BeautifulSoup("./test.html", "html.parser")

  # a = channel_soup.select("div ")

  # main_links = soup.find_all("div", {"id": "info-section"})
  # print(main_links)
  links = soup.find_all("div")
  print(links)

'''
  for url in links:
    print(url.get("href"))
    print()
  #print(type(channel_soup))
  # print(a)'''



if __name__ == "__main__":
  search_youtube("blackpink", CHANNEL_FILTER)


