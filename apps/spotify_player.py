import numpy as np, requests, math, time, threading
from PIL import Image, ImageDraw
from io import BytesIO

class SpotifyScreen:
    def __init__(self, spotify_module):
        self.spotify_module = spotify_module
        self.canvas_width = 64
        self.canvas_height = 64

        self.new_art_url = ''
        self.current_art_url = ''
        self.current_art_image = None

        self.thread = threading.Thread(target=self.get_current_playback_async)
        self.thread.start()

    def get_current_playback_async(self):
        time.sleep(3)
        while True:
            self.new_art_url = self.spotify_module.get_current_playing_song_art()
            time.sleep(1)
        
    def generate_frame(self):
        if (not self.new_art_url):
            return None
        if self.current_art_url != self.new_art_url:
            self.current_art_url = self.new_art_url
            response = requests.get(self.current_art_url)
            img = Image.open(BytesIO(response.content))
            self.current_art_image = img.resize((self.canvas_width, self.canvas_height))
            frame = Image.new("RGB", (self.canvas_width, self.canvas_height), (0,0,0))
            draw = ImageDraw.Draw(frame)
            frame.paste(self.current_art_image, (0,0))
            return frame
        else:
            frame = Image.new("RGB", (self.canvas_width, self.canvas_height), (0,0,0))
            draw = ImageDraw.Draw(frame)
            frame.paste(self.current_art_image, (0,0))
            return frame
