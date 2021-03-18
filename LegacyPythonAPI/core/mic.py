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

import pyaudio, audioop
from .utils import Util
import time
import wave
# import scipy.io.wavfile as wf
import numpy as np




class Mic(object):

  def __init__(self, Agent, CHUNK=1024, FORMAT=pyaudio.paInt16, CHANNELS=1, RATE=44100):
    self.Agent = Agent

    self.active_maxtime = 10
    self.active_timeout = 1
    self.passive_maxtime = 1
    self.threshold = 1500

    # configuration for `pyaudio`
    self.CHUNK = CHUNK
    self.FORMAT = FORMAT
    self.CHANNELS = CHANNELS
    self.RATE = RATE

    self.audio = pyaudio.PyAudio()
    self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
    self.wav_file = f"{self.Agent.TEMP_PATH}/sound.wav"

  def fetch_threshold(self, data):
    # Get the loudness of the surroundings
    rms = audioop.rms(data, self.CHANNELS)
    # returns True if we think that the sound is loud enough to indicate that a person is talking
    if rms >= self.threshold:
      return True
    else:
      return False

  def write_wav(self, frames):
    with wave.open(self.wav_file, "wb") as wf:
      wf.setnchannels(self.CHANNELS)
      wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
      wf.setframerate(self.RATE)
      wf.writeframes(b''.join(frames))

  def active_listen(self):
    # Starts recording until the the person stops speaking. (maxtime: 10s timeout: 1s)
    self.Agent._print2("Listening...")
    frames = []
    stop_condition = False
    start = time.time()
    when_loud = start

    while not stop_condition:
      data = self.stream.read(self.CHUNK)
      frames.append(data)

      # update last loud time
      if self.fetch_threshold(data) is True:
        when_loud = time.time()
      else:
        time_range = time.time() - when_loud
        time_used = time.time() - start

        # timeout stop
        if time_range >= self.active_timeout:
          stop_condition = True
        # maxtime stop
        elif time_used >= self.active_maxtime:
          stop_condition = True

    self.Agent._print2("Done listening!")

    # write into .wav file
    self.write_wav(frames)

    transcripts = self.Agent.Speech.STT(self.wav_file)
    if transcripts:
      return transcripts[0]["transcript"].lower()
    else:
      return None

  def passive_listen(self, hotwords):
    # records for a certain amount of time. (1s)
    self.Agent._print2("Listening...")
    frames = []
    stop_condition = False
    start = time.time()

    while not stop_condition:
      data = self.stream.read(self.CHUNK)
      frames.append(data)

      time_used = time.time() - start
      # maxtime stop
      if time_used >= self.passive_maxtime:
        stop_condition = True

    self.Agent._print2("Done listening!")

    # write into .wav file
    self.write_wav(frames)

    # detect hotword by looking at a bunch of word list that is pre-recorded at `hotwords.py`
    transcripts = self.Agent.Speech.STT(self.wav_file)
    if transcripts:
      return any(transcripts[0]["transcript"] in hw for hw in hotwords)
    else:
      return False

  def speak(self, text=None, filename=None):
    if filename:
      wf = wave.open(filename, "rb")
      data = wf.readframes(chunk)

      while data != '':
        stream.write(data)
        data = wf.readframes(chunk)


  def train_hotword(self):
    amount = self.Agent.hotword_train_amount
    hotwords = set()
    # records for a certain amount of time. (1s)
    print("\n===================================")
    print("          Training Hotword         ")
    print("===================================\n")
    print(f"Recording for {amount} times.")
    print(f"Start speaking once you see the word 'Listening...' | Total attempt(s): {amount}")
    print("\nStarting in: ")
    for i in range(3):
      print(3-i)
      time.sleep(1)

    for i in range(amount):
      print(f"\nAttempt: {i+1}")
      print("Listening...")
      frames = []

      stop_condition = False
      start = time.time()

      while not stop_condition:
        data = self.stream.read(self.CHUNK)
        frames.append(data)

        time_used = time.time() - start
        # maxtime stop
        if time_used >= self.passive_maxtime:
          stop_condition = True

      print("Done listening!")

      # write into .wav file
      self.write_wav(frames)

      transcripts = self.Agent.Speech.STT(self.wav_file)
      
      for t in transcripts:
        hotwords.add(t["transcript"])
      time.sleep(0.5)

    self.Agent._print("Writing to `hotwords.txt`...")
    with open("hotwords.txt", "w") as f:
      f.write("\n".join(list(hotwords)))

    print("\nTraining done!")
    print("===================================\n")

  def say(self, text, lang="en", slow=False):
    self.Agent.Speech.TTS(text, lang, slow)


if __name__ == '__main__':
  pa = pyaudio.PyAudio()
  print(pa.get_default_input_device_info())

