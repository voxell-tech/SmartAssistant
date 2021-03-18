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

import pkgutil

class Brain(object):

  """
  Instantiates a new Brain object, which cross-references user
  input with a list of modules. Note that the order of brain.modules
  matters, as the Brain will cease execution on the first module
  that accepts a given input.
  """

  def __init__(self, Agent):
    self.Agent = Agent
    self.Mic = self.Agent.Mic
    locations = self.Agent.MODULES_PATH
    if not isinstance(locations, list) and isinstance(locations, str):
      locations = [locations]
    self.modules = self.getModules(locations)

  def getModules(self, locations):
    """
    Dynamically loads all the modules in the modules folder and sorts
    them by the PRIORITY key. If no PRIORITY is defined for a given
    module, a priority of 0 is assumed.
    """
    self.Agent._print(f"\nLooking for modules in: {', '.join(locations)}")
    modules = []
    for finder, name, ispkg in pkgutil.walk_packages(locations):
      if not ispkg:
        try:
          loader = finder.find_module(name)
          mod = loader.load_module(name)
        except Exception as e:
          self.Agent._print2(e)
          self.Agent._print(f"Skipped module `{name}` due to an error.")
        else:
          if hasattr(mod, "isValid"):
            self.Agent._print(f"Found module `{name}`")
            modules.append(mod)
    modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY') else 0, reverse=True)

    return modules

  def query(self, text):
    """
    Passes user input to the appropriate module, testing it against
    each candidate module's isValid function.

    Arguments:
    text -- user input, typically speech, to be parsed by a module
    """
    for module in self.modules:
      if module.isValid(text):
        self.Agent._print(f"'{text}' is a valid phrase for module `{module.__name__}`")
        try:
          module.handle(text, self.Agent.Mic, self.Agent)
        except Exception as e:
          self.Agent._print2(e)
          self.Agent._print('Failed to execute module')
          self.Mic.say("I'm sorry. I had some trouble with that operation. Please try again later.")
        else:
          self.Agent._print(f"Handling of phrase '{text}' by module `{module.__name__}` completed")
        finally:
          return
    self.Agent._print(f"No module was able to handle any of these phrases: {text}")


if __name__ == "__main__":
  modules = []
  for finder, name, ispkg in pkgutil.walk_packages([r"p:\SmartAssistant\SmartAssistant\SABackend\client\modules"]):
    if not ispkg:
      try:
        loader = finder.find_module(name)
        mod = loader.load_module(name)
      except Exception as e:
        print(e)
        print(f"Skipped module `{name}` due to an error.")
      else:
        if hasattr(mod, "isValid"):
          print(f"Found module `{name}`")
          modules.append(mod)