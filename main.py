import glfw
import OpenGL.GL as gl
from src import Game, Globals

def main():

	glfw.set_error_callback(error_callback)

	if not glfw.init():
		print("ERROR [-1]: Failed to initialize GLFW")
		return

	monitor = glfw.get_primary_monitor()
	mode = glfw.get_video_mode(monitor)
	glfw.window_hint(glfw.DECORATED, False)

	scale = 0.45
	Globals.WINDOW_WIDTH = int(mode.size[0]*scale)
	Globals.WINDOW_HEIGHT = int(mode.size[1]*scale)

	window = glfw.create_window(Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT, "Window", None, None)	
	glfw.set_window_pos(window, int(mode.size[0]*(1-scale)/2), int(mode.size[1]*(1-scale)/2))

	if not window:
		glfw.terminate()
		return

	glfw.set_key_callback(window, input_callback)

	glfw.make_context_current(window)

	Globals.GAME_INSTANCE = Game()

	while not glfw.window_should_close(window):

		
		width, height = glfw.get_framebuffer_size(window)
		gl.glViewport(0, 0, width, height)
		gl.glClear(gl.GL_COLOR_BUFFER_BIT)
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		gl.glOrtho(0, width, height, 0, 0, 1)
		gl.glMatrixMode(gl.GL_MODELVIEW)
		gl.glLoadIdentity()
		Globals.GAME_INSTANCE.draw()

		glfw.poll_events()
		glfw.swap_buffers(window)

	glfw.destroy_window(window)
	glfw.terminate()

def error_callback(code, description):
	print(f"ERROR [{code}]: {description.decode()}")

def input_callback(window, key, scancode, action, mods):
	# print(f"Key: {key}  |  Scancode: {scancode}  |  Action: {action}  | Mods: {mods}")

	if key == glfw.KEY_Q and action == glfw.PRESS:
		glfw.set_window_should_close(window, True)
		# print("Closing the window")

	if key == glfw.KEY_RIGHT and action != glfw.RELEASE:
		Globals.GAME_INSTANCE.player.loc = (Globals.GAME_INSTANCE.player.loc[0] + 1, Globals.GAME_INSTANCE.player.loc[1])
	elif key == glfw.KEY_LEFT and action != glfw.RELEASE:
		Globals.GAME_INSTANCE.player.loc = (Globals.GAME_INSTANCE.player.loc[0] - 1, Globals.GAME_INSTANCE.player.loc[1])

	if key == glfw.KEY_DOWN and action != glfw.RELEASE:
		Globals.GAME_INSTANCE.player.loc = (Globals.GAME_INSTANCE.player.loc[0], Globals.GAME_INSTANCE.player.loc[1] + 1)
	elif key == glfw.KEY_UP and action != glfw.RELEASE:
		Globals.GAME_INSTANCE.player.loc = (Globals.GAME_INSTANCE.player.loc[0], Globals.GAME_INSTANCE.player.loc[1] - 1)


if __name__ == '__main__':
	main()