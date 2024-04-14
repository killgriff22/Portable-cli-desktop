import os
os.environ['SDL_VIDEODRIVER'] = 'fbcon'
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
import MultiTerm
display_size = MultiTerm.os.get_terminal_size()
screen = MultiTerm.Screen(display_size,(0,0))