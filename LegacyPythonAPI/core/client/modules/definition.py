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
import nltk
from PyDictionary import PyDictionary

PRIORITY = 8

def handle(text, Mic, Agent):
  """
  Abilities:
  - report the status of the Smart Assistant (will soon be deprecated
    for AI to reply)
  """
  # tokenize the sentence into words
  tokens = nltk.tokenize.word_tokenize(text)

  # key text that we want to identify
  keys = ["of", "define"]
  # to store the target word
  word = list()

  # loop through each tokens (words) until a key text is found
  for i, t in enumerate(tokens):
    if t in keys:
      # assign target word when key is found
      word = tokens[i+1:]
      break

  if word:
    # join word tokens into target_word
    target_word = " ".join(word)

    # initalize dictionary
    dictionary = PyDictionary()
    try:
      # find dictionary meaning
      result = dictionary.meaning(target_word)
      result_keys = list(result.keys())

      Mic.say(result[result_keys[0]][0])
    except Exception as e:
      Agent._print2(e)


def isValid(text):
  # check if text is valid
  return (
    (
      bool(re.search(r"\bmeaning\b", text, re.IGNORECASE)) or \
        bool(re.search(r"\bdefinition\b", text, re.IGNORECASE)) or \
        bool(re.search(r"\bdefine\b", text, re.IGNORECASE))
    )
  )




if __name__ == "__main__":
  text = "Hi, how are you?"
  tokens = nltk.tokenize.word_tokenize(text)
  print(tokens)
