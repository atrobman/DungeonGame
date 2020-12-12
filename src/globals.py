from enum import Enum, auto

class Globals:
	#constants
	TILE_SIZE = 32



	#set once
	WINDOW_WIDTH = -1
	WINDOW_HEIGHT = -1



	#variables
	GAME_INSTANCE = None


class Game_State(Enum):

	MENU_SCREEN = auto()
	RUNNING = auto()
	INVENTORY_SCREEN = auto()