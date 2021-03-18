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

from googleapiclient.discovery import build

class Youtube_Util(object):

  def __init__(self, Agent):
    self.filepath = Agent.YT_PATH + "/youtube.apikey"
    self.api_key = open(self.filepath, "r", encoding="utf-8").read()

    self.youtube = build("youtube", "v3", developerKey=self.api_key)

  def find_latest_video(self, channel_name, max_results):
    #To search and obtain channel id
    channel_search_request = self.youtube.search().list(
      part = "snippet",
      q = channel_name,
      type = "channel",
    )

    channel_search_response = channel_search_request.execute()


    #Getting channel ID
    chan_id_list = []

    for items in channel_search_response["items"]:
      chan_id_list.append(items["id"]["channelId"])


    main_chan_id = chan_id_list[0]

    #Getting video ID
    vids_id_search_request = self.youtube.search().list(
      part = "snippet",
      channelId = main_chan_id,
      order = "date"
    )
    vids_id_search_response = vids_id_search_request.execute()

    #Group the videos id into list
    vids = []

    for items in vids_id_search_response["items"]:
      vids.append(items["id"]["videoId"])

    #To obtain video info from video id
    video_request = self.youtube.videos().list(
      part =" contentDetails, snippet, statistics",
      id = ",".join(vids)
    )
    video_response = video_request.execute()

    return(video_response["items"]) 


  def filter_video_response(self, video_response=dict(), filter_type=[]):
    """
    filter_video_response(video_response, ["snippet", "title"])
    """
    results = list()
    for items in video_response:
      results.append(items[filter_type[0]][filter_type[1]])

    return results

