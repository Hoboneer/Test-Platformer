from pygame.math import Vector2

# --- Display Constants-ish --- #
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (600, 300)
MAX_FPS = 60
CAPTION = "TEST PLATFORMER - FPS: {:.2f}"
# --- END --- #

# --- Colours --- #
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
# --- END --- #

# These numbers are pretty temporary atm

# --- World Constants --- #
GRAVITY = 100
# --- END --- #

# --- Platform constants --- #
PLATFORM_COLOUR = BLUE
PLATFORM_WIDTH, PLATFORM_HEIGHT = PLATFORM_SIZE = (50, 20)
PLATFORM_X, PLATFORM_Y = PLATFORM_POS = (3*PLATFORM_WIDTH, SCREEN_HEIGHT-PLATFORM_HEIGHT-10)
# --- END --- #

# --- Player constants --- #
PLAYER_COLOUR = RED
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_SIZE = (25, 25)
# PLAYER_START_X, PLAYER_START_Y = PLAYER_START = (PLATFORM_X, 0)
PLAYER_START_X, PLAYER_START_Y = PLAYER_START = (15, 0)

PLAYER_SPEED      = 150
PLAYER_MAX_VELOCITY = Vector2(150, 50)  # 50 is an arbitrary number for now, 50 would also be the terminal velocity
PLAYER_JUMP_SPEED = 150

PLAYER_MASS = 5
# --- END --- #

