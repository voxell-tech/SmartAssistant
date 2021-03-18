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

from .notifier import Notifier
from .brain import Brain
import random

class Conversation(object):

  def __init__(self, Agent):
    self.Agent = Agent
    self.Brain = Brain(self.Agent)
    self.Notifier = Notifier(self.Agent)

  def handleForever(self):
    # main loop of the Agent
    stop_condition = False
    text = None

    while not stop_condition:
      data = self.Agent.Mic.stream.read(self.Agent.Mic.CHUNK)
      # check the surrounding volume
      if self.Agent.Mic.fetch_threshold(data):
        # check if hotword was spoken
        detection = self.Agent.Mic.passive_listen(self.Agent.hotwords)

        if detection:
          # greet when hotword is detected
          self.Agent._print(f"Hotword '{self.Agent.name}' detected!")
          self.Agent.Mic.say(random.choice(self.Agent.GREET))
          question = self.Agent.Mic.active_listen()

          if question:
            self.Brain.query(question)
          else:
            self.Agent.Mic.say("Pardon?")
            question = self.Agent.Mic.active_listen()
            if question:
              self.Brain.query(question)
            else:
              pass

