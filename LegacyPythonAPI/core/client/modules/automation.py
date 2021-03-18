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

import os, sys
import re
from logix_control import controller

def handle(text, mic, profile):
  """
  Reports the current time based on the user's timezone.

  Arguments:
  text -- user-input, typically transcribed speech
  mic -- used to interact with the user (for both input and output)
  profile -- contains information related to the user (e.g., phone number)
  """

  tz = getTimezone(profile)
  now = datetime.datetime.now(tz=tz)
  service = DateService()
  response = service.convertTime(now)
  mic.say("It is %s right now." % response)


def isValid(text):
  # check if text is valid
  return bool(re.search(r'\bswitch (off|on)?\b', text, re.IGNORECASE))


# class Automation(IntentionClassifier):

#   def __init__(self):
#     pass



if __name__ == '__main__':
  print(isValid("switch on the lights"))