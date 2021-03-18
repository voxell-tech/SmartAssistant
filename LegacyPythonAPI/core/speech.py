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

from gtts import gTTS
import pyaudio, audioop
import pyttsx3
import speech_recognition as sr
import pydub
import wave




class Speech(object):

  def __init__(self, Agent):
    self.engine = pyttsx3.init()
    self.Agent = Agent

    # Initialize the count number so that when speaking tts,
    # we won't use the same mp3 file at the same time
    self.count = 0
    self.min_thresh = 45
    self.max_thresh = 60
    self.thresh_interval = self.max_thresh - self.min_thresh

  def TTS(self, text, lang="en", slow=False):
    '''
    input any text you wish the computer to speak
    note that this module needs an internet connection to be able to run
    '''
    # use tacotron 2
    mp3_file = f"{self.Agent.TEMP_PATH}\\tts_{self.count}.mp3"
    wav_file = f"{self.Agent.TEMP_PATH}\\tts_{self.count}.wav"
    avatar_file = f"{self.Agent.TEMP_PATH}\\avatar.txt"

    tts = gTTS(text, lang=lang, slow=slow)
    tts.save(mp3_file)
    # convert mp3 to wav so that we can get information about the wav file
    mp3 = pydub.AudioSegment.from_mp3(mp3_file)
    mp3.export(wav_file, format="wav")
    f = wave.open(wav_file,"rb")

    CHANNELS = f.getnchannels()
    FORMAT = self.Agent.Mic.audio.get_format_from_width(f.getsampwidth())
    RATE = f.getframerate()
    CHUNK = 1024

    stream = self.Agent.Mic.audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

    #read data
    data = f.readframes(CHUNK)

    #play stream
    while data:
      rms = audioop.rms(data, CHANNELS)

      if rms > self.max_thresh: # limit the rms to 60 max
        rms = self.max_thresh
      elif rms < self.min_thresh: # limit the rms to 60 min
        rms = self.min_thresh

      # self.Agent.Socket.send_msg(f"$spawnRate#{(rms-self.min_thresh)/self.thresh_interval}")
      stream.write(data)  
      data = f.readframes(CHUNK)

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    # pygame.mixer.init()
    # pygame.mixer.music.load(mp3_file)
    # pygame.mixer.music.play()

    if self.count == 0:
      self.count += 1
    elif self.count == 1:
      self.count -= 1

  def STT(self, audio_f, lang="en"):
    r = sr.Recognizer()
    self.Agent._print2('Recognizing speech...')

    with sr.AudioFile(audio_f) as source:
      audio = r.record(source)  # read the entire audio file

    text = r.recognize_google(audio, language="en", show_all=True)
    if text:
      return text["alternative"]
    else:
      return []

