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

import requests
import urllib

class Util(object):

  def __init__(self, verbose):
    self.verbose = verbose
    self.current_log = ""

  @classmethod
  def checkInternet(self):
    url = 'http://www.google.com/'
    timeout = 5
    try:
      _ = requests.get(url, timeout=timeout)
      return True
    except requests.ConnectionError:
      return  False

  def _print(self, content):
    if self.verbose >= 1:
      self.current_log = content
      print(content)

  def _print2(self, content):
    if self.verbose >= 2:
      self.current_log = content
      print(content)

  @classmethod
  def generateTinyUrl(self, url):
    """
    Generates a compressed URL.
    Arguments:
        URL -- the original URL to-be compressed
    """
    target = "http://tinyurl.com/api-create.php?url=" + url
    response = urllib.request.urlopen(target)
    return response.read().decode("utf-8")

if __name__ == "__main__":
  print(Util.generateTinyUrl("google.com"))