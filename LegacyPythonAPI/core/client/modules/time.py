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
from datetime import datetime
import random
import string

PRIORITY = 9

month_dict = {
  1: "January",
  2: "February",
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December"
}

def handle(text, Mic, Agent):
  """
  Abilities:
  - provide current time and date
  - calculate the time interval between 2 distinct time
  """

  # getting infos
  date, time = str(datetime.now()).split(" ")
  year, month, day = date.split("-")
  hour, minute, second = time.split(":")

  # converting them into numbers
  year, month, day = int(year), int(month), int(day)
  hour, minute, second = int(hour), int(minute), int(float(second))

  # getting letters, punctuations & space
  letters = list(string.ascii_letters)
  puncs = list(string.punctuation)
  puncs.remove(":")
  space = [" "]

  outputs = None
  if bool(re.search(r'\btime\b', text, re.IGNORECASE)):
    if hour >= 12:
      suffix = "pm"
    else:
      suffix = "am"
    outputs = [
      f"It is {hour}:{minute} {suffix} right now.",
      f"It's {hour}:{minute} {suffix}",
      f"The time is now {hour}:{minute} {suffix}"
      ]

  elif bool(re.search(r'\bday|date|month|year\b', text, re.IGNORECASE)):
    if str(day).endswith("1"):
      suffix = "st"
    elif str(day).endswith("2"):
      suffix = "nd"
    elif str(day).endswith("3"):
      suffix = "rd"
    else:
      suffix = "th"

    outputs = [
      f"Today is {day}{suffix} of {month_dict[month]}, {year}",
      f"It's {day}{suffix} of {month_dict[month]}, {year}",
      f"The date is {day}{suffix} of {month_dict[month]}, {year}"
      ]

  elif (bool(re.search(r'\bhow long\b', text, re.IGNORECASE)) and \
        bool(re.search(r'\buntil|till\b', text, re.IGNORECASE)) and \
        bool(re.search(r'\bclock|p.m.|a.m.|pm|am|:\b', text, re.IGNORECASE))):

    origin_text = text
    for s in letters + puncs + space:
        text = text.replace(s, "")

    if ":" in text:
      tar_hr, tar_min = text.split(":")
      tar_hr, tar_min = int(tar_hr), int(tar_min)

    else:
      tar_hr = int(text)
      tar_min = 0

    if bool(re.search(r'\bp.m.|pm|evening|night|afternoon\b', origin_text, re.IGNORECASE)) and tar_hr != 12:
      tar_hr += 12
    elif bool(re.search(r'\btomorrow\b', origin_text, re.IGNORECASE)):
      tar_hr += 24
    elif bool(re.search(r'\bnoon|midday\b', origin_text, re.IGNORECASE)):
      tar_hr = 12
    elif bool(re.search(r'\ba.m.|am|morning|dawn\b', origin_text, re.IGNORECASE)) and tar_hr == 12:
      tar_hr = 0

    diff_hr, diff_min, diff_sec = time_difference([hour, minute, second], [tar_hr, tar_min])

    if diff_hr == 1:
      hr = f"{diff_hr} hour"
    elif diff_hr > 1:
      hr = f"{diff_hr} hours"
    elif diff_hr == 0:
      hr = ""
    else:
      hr = ""

    if diff_min == 1:
      mint = f"{diff_min} minute"
    elif diff_min > 1:
      mint = f"{diff_min} minutes"
    elif diff_min == 0:
      mint = ""
    else:
      mint = ""

    if diff_sec == 1:
      sec = f"and {diff_sec} second"
    elif diff_sec > 1:
      sec = f"and {diff_sec} seconds"
    elif diff_sec == 0:
      sec = ""
    else:
      sec = ""


    outputs = [
      f"It will take {hr} {mint} {sec}.",
      f"It's {hr} {mint} {sec}."
      ]
  if outputs:
    Mic.say(random.choice(outputs))
  else:
    Mic.say(f"I'm sorry, I can't find an answer to this time related question.")


def isValid(text):
  """
    Returns True if input is related to the time.

    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\btime|day|date|month|year\b', text, re.IGNORECASE)) or (
          bool(re.search(r'\bhow long\b', text, re.IGNORECASE)) and \
          bool(re.search(r'\buntil|till\b', text, re.IGNORECASE)) and \
          bool(re.search(r'\bclock|p.m.|a.m.|pm|am|:|morning|dawn|evening|night|afternoon|noon|midday|tomorrow\b',
          text, re.IGNORECASE))
          )

def time_difference(curr_time, tar_time):
  ch, cm, cs = curr_time
  th, tm = tar_time

  if th < ch:
    th += 24

  total_diff_min = (th-ch)*60 + (tm-cm)
  diff_min = total_diff_min%60
  diff_hr = total_diff_min//60
  diff_sec = 60-cs

  return diff_hr, diff_min, diff_sec


if __name__ == '__main__':
  target_time = 16, 00

  date, time = str(datetime.now()).split(" ")
  year, month, day = date.split("-")
  hour, minute, second = time.split(":")
  year, month, day = int(year), int(month), int(day)
  hour, minute, second = int(hour), int(minute), int(float(second))

  print(f"The time is now {hour}:{minute}.")
  print(f"Today is {day}th of {month_dict[month]}, {year}")

  print(time_difference([hour, minute, second], target_time))

  print(isValid("how long is it until 7 a.m."))
  # print(isValid("how long is it until 7 o'clock?").string)

