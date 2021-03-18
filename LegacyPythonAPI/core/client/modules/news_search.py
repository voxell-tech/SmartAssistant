import bs4
import requests
import re

def handle(text, Mic, Agent):
  """
    Responds to user-input, typically speech text, with a summary of
    the day's top news headlines, sending them to the user over email
    if desired.

    Arguments:
    text -- user-input, typically transcribed speech
    mic -- used to interact with the user (for both input and output)
    profile -- contains information related to the user (e.g., phone
           number)
  """
  remove_words = ["get", "me", "news", "google", "search", "about", "for"]
  for rw in remove_words:
    text = text.replace(rw, "")


  news_link = "https://www.google.com/search?tbm=nws&q="

  user_request = text

  res_news = requests.get(news_link + user_request)

  soup_news = bs4.BeautifulSoup(res_news.text, "html.parser")

  find_div = soup_news.find_all("div")

  find_title = soup_news.find_all(class_ = "zBAuLc")

  find_publisher = soup_news.find_all(class_ = "BNeawe UPmit AP7Wnd")

  find_date = soup_news.find_all(class_ = "r0bn4c rQMQod")


  title_list = []
  date_list = []
  publisher_list = []

  for i in find_title:
    title_list.append(i.getText())

  for i in find_publisher:
    publisher_list.append(i.getText())

  for i in find_date:
    if i == " · ":
      continue
    else:
      date_list.append(i.getText())

  date_list_2 = []

  for i in date_list:
    if i == " · ":
      continue
    else:
      date_list_2.append(i)
  


  results = "\n".join("Headline: {}    from {}     {}".format(x, y, z) for x, y, z in zip(title_list[0:5], publisher_list[0:5], date_list_2[0:5]))

  Agent._print2(results)
  Mic.say(results)


def isValid(text):
  # check if text is valid
  return (bool(re.search(r'\bget me news\b', text, re.IGNORECASE)))

