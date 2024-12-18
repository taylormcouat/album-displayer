import numpy as np, requests, math, time, threading, os
from PIL import Image, ImageDraw
from io import BytesIO

class GifScreen:
    def __init__(self):
        self.canvas_width = 64
        self.canvas_height = 64
        self.row_index = 0
        self.col_index = 0
        self.image = None
        self.n_rows = 0
        self.n_cols = 0
        self.tile_width = 0
        self.tile_height = 0

    def init_gif(self, gif_config):
        file_name = gif_config['file_name']
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.abspath(os.path.join(script_dir, '..', 'static', 'gifs', file_name))
        self.image = Image.open(image_path)
        self.n_rows = int(gif_config['n_rows'])
        self.n_cols = int(gif_config['n_cols'])
        self.tile_width = int(gif_config['tile_width'])
        self.tile_height = int(gif_config['tile_height'])

    def get_current_coordinate(self):
        x = self.col_index * self.tile_width
        y = self.row_index * self.tile_height
        return x, y

    def advance_coordinates(self):
        self.col_index = self.col_index + 1

        if (self.col_index == self.n_cols):
            self.row_index = self.row_index + 1
            self.col_index = 0
        if (self.row_index == self.n_rows):
            self.row_index = 0
        
    def generate_frame(self):
        if (not self.image):
            return None
        frame = Image.new("RGB", (self.canvas_width, self.canvas_height), (0,0,0))
        draw = ImageDraw.Draw(frame)
        x, y = self.get_current_coordinate()
        cropped_image = self.image.crop((x, y, x + self.tile_width, y + self.tile_height))
        frame.paste(cropped_image, ((self.canvas_width - self.tile_width)//2,(self.canvas_height - self.tile_height)//2))
        self.advance_coordinates()
        return frame