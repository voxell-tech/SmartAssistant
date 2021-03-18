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
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.getcwd())

# Agent main directory
APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
APP_PATH = os.path.join(APP_PATH, "core")

# general pathways
TEMP_PATH = os.path.join(APP_PATH, "temp")
CLIENT_PATH = os.path.join(APP_PATH, "client")
MODULES_PATH = os.path.join(CLIENT_PATH, "modules")

# sub modules pathways
CONTROLLER_PATH = os.path.join(MODULES_PATH, "logix_control")
DL_PATH = os.path.join(MODULES_PATH, "deep_learning")
YT_PATH = os.path.join(MODULES_PATH, "youtube")

# sub^2 modules pathways
CHATBOT_PATH = os.path.join(DL_PATH, "chatbot")
LOGIX_PATH = os.path.join(CONTROLLER_PATH, "pylogix")

if __name__ == '__main__':
  print("APP PATH:", APP_PATH)
  print("TEMP PATH:", TEMP_PATH)
  print("CLIENT PATH:", CLIENT_PATH)
  print("MODULES PATH:", MODULES_PATH)
  print("CONTROLLER PATH:", CONTROLLER_PATH)
  print("DL PATH:", DL_PATH)
  print("LOGIX PATH:", LOGIX_PATH)
  print("CHATBOT PATH:", CHATBOT_PATH)
