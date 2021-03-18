# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# The Original Code is Copyright (C) 2020 Voxell Technologies.
# All rights reserved.

# nothing has been changed yet
import feedparser
# from client import app_utils
import re
from semantic.numbers import NumberService


PRIORITY = 8


class Article:

  def __init__(self, title, url, publish):
    self.title = title
    self.url = url
    self.publish = publish


def getTopArticles(maxResults=None):
  d = feedparser.parse("http://news.google.com/?output=rss")

  count = 0
  articles = []
  for entry in d['entries']:
    articles.append(Article(entry['title'], entry['link'], entry["published"]))
    count += 1
    if maxResults and count > maxResults:
      break

  return articles


def handle(text, mic, Agent):
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
  articles = getTopArticles(3)
  mic.say("These are the top three news I found on Google News!")
  for a in articles:
    try:
      content, source = a.title.split(" - ")
      mic.say(f"News from {source}:")
      mic.say(content)
    except Exception as e:
      Agent._print2(e)
      Agent._print2(a.title, a.title.split(" - "))


def isValid(text):
  """
    Returns True if the input is related to the news.

    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\b(top news|headline)\b', text, re.IGNORECASE))

if __name__ == "__main__":
    pass