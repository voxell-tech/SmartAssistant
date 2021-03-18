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

from youtube import youtube_utils
import re

v = ""
PRIORITY = 8.

def handle(text, Mic, Agent):
  """
  Abilities:
  - return youtube data obtained from youtube API
  """
  text = text.lower()
  remove_words = ["channel", "latest", "uploads", "videos", "video", "upload", "newest", "new", "youtube"]
  for rw in remove_words:
    text = text.replace(rw, "")

  yt_util = youtube_utils.Youtube_Util(Agent)
  user_video = yt_util.find_latest_video(text, 20)

  try:
    video_result = yt_util.filter_video_response(user_video, ["snippet", "title"] )

    latest_vids = ", ".join(video_result[:-1])
    latest_vids += ",and " + video_result[-1]

    Agent._print2(video_result)
    Mic.say(f"The latest videos by {text} is {latest_vids}.")
  except:
    Mic.say("I am sorry, I can't find any videos related to this channel...")

def isValid(text):
  # check if text is valid
  return (bool(re.search(r'\byoutube\b', text, re.IGNORECASE)))



if __name__ == '__main__':
  print(isValid("YouTube"))
  
