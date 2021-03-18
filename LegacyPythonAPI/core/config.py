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

# loads configuration for smart assistant
import yaml

with open("config.yml") as f:
    config_dict = yaml.load(f, Loader=yaml.FullLoader)

config_dict["AFFIRM"] = [
  "Alright.",
  "OK!",
  f"As you wish, {config_dict['user_firstname']}!",
  "Right away!",
  "As you wish.",
  "So be it."
  ]

config_dict["REJECT"] = [
  "Sorry, it's over my limit.",
  "I can't.",
  "It's impossible.",
  "I am unable to do it!",
  "I can't complete that task."
  ]

config_dict["GREET"] = [
  f"Yes, {config_dict['user_firstname']}?",
  "What's up?",
  "Yes?",
  "Anything?"
  ]

if __name__ == '__main__':
  # for c in config_dict:
  #   print(f"{c}: {config_dict[c]}")
  # print(config_dict)

  with open("config.yml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
