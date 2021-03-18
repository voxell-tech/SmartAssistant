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

PRIORITY = 8

def handle(text, Mic, Agent):
  """
  Abilities:
  - report the status of the Smart Assistant (will soon be deprecated
    for AI to reply)
  """
  Mic.say("Everything is copacetic!")


def isValid(text):
  # check if text is valid
  return (
    (
      bool(re.search(r"\bhow |how\"s |what |what\"s \b", text, re.IGNORECASE)) and \
      bool(re.search(r"\b going| doing\b", text, re.IGNORECASE))
    ) or \
    bool(re.search(r"\bstatus\b", text, re.IGNORECASE))
  )




if __name__ == "__main__":
  print(isValid("How is eveything going?"))
