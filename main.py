from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
from modules import spotify_module
from apps import spotify_player, gif_player
from PIL import Image
import time, os, configparser

def main():
    canvas_width = 64
    canvas_height = 64

    # connect to spotify
    sp_module = spotify_module.SpotifyModule()
    spotify_screen = spotify_player.SpotifyScreen(sp_module)

    # load gif
    config_file_name = os.path.join(os.path.dirname(__file__), 'apps/gifs.ini')
    gif_screen = gif_player.GifScreen()
    gif_config = configparser.ConfigParser()
    gif_config.read(config_file_name)
    gif_screen.init_gif(gif_config['bowser'])


    # setup matrix
    options = RGBMatrixOptions()
    options.hardware_mapping = 'regular'
    options.rows = canvas_width
    options.cols = canvas_height
    options.brightness = 100 
    options.gpio_slowdown = 2
    options.limit_refresh_rate_hz = 100
    options.drop_privileges = False
    matrix = RGBMatrix(options = options)

    shutdown_delay = 30
    black_screen = Image.new("RGB", (canvas_height, canvas_width), (0,0,0))

    # generate image
    while(True):
        #frame = spotify_screen.generate_frame()
        frame = gif_screen.generate_frame()
        if frame is None:
            frame = black_screen
        matrix.SetImage(frame)
        time.sleep(0.08)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)