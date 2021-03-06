'''
    Kenneth Bailey
    3/17/18

    Usage --> "python3 install_ffmpeg.py"

    Notes:
        - Run before first run of any scripts if you are on a mac or linux system. 
        - Installs necessary files required to transcode video

'''

import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
