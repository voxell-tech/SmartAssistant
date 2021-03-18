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

import re
from nltk.tokenize import word_tokenize, sent_tokenize
import webbrowser

PRIORITY = 8

def handle(text, Mic, Agent):
  remove_words = ["google ", "Google ", "search ", "for "]
  for rw in remove_words:
    text = text.replace("google ", "")

  Mic.say(f"Here's what I found on google on '{text}'")
  query = "https://www.google.com/search?q="
  words = word_tokenize(text)
  phrase = "+".join(words)
  query += phrase
  webbrowser.open_new_tab(query)


def isValid(text):
  # check if text is valid
  return (bool(re.search(r"\bgoogle |search \b", text, re.IGNORECASE)))




if __name__ == "__main__":
  print(isValid("what is earth?"))

