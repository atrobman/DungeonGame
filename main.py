import glfw
import OpenGL.GL as gl
from src import Game

def main():

	glfw.set_error_callback(error_callback)

	if not glfw.init():
		print("ERROR [-1]: Failed to initialize GLFW")
		return

	monitor = glfw.get_primary_monitor()
	mode = glfw.get_video_mode(monitor)
	glfw.window_hint(glfw.DECORATED, False)

	scale = 0.45
	
	window = glfw.create_window(int(mode.size[0]*scale), int(mode.size[1]*scale), "Window", None, None)	
	glfw.set_window_pos(window, int(mode.size[0]*(1-scale)/2), int(mode.size[1]*(1-scale)/2))

	if not window:
		glfw.terminate()
		return

	glfw.set_key_callback(window, input_callback)

	glfw.make_context_current(window)

	game = Game()

	while not glfw.window_should_close(window):

		
		width, height = glfw.get_framebuffer_size(window)
		gl.glViewport(0, 0, width, height)
		gl.glClear(gl.GL_COLOR_BUFFER_BIT)
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		gl.glOrtho(0, width, 0, height, 0, 1)
		gl.glMatrixMode(gl.GL_MODELVIEW)
		gl.glLoadIdentity()
		gl.glRectdv()
		game.draw()

		glfw.poll_events()
		glfw.swap_buffers(window)

	glfw.destroy_window(window)
	glfw.terminate()

def error_callback(code, description):
	print(f"ERROR [{code}]: {description.decode()}")

def input_callback(window, key, scancode, action, mods):
	# print(f"Key: {key}  |  Scancode: {scancode}  |  Action: {action}  | Mods: {mods}")

	if key is glfw.KEY_Q and action is glfw.PRESS:
		glfw.set_window_should_close(window, True)
		# print("Closing the window")

if __name__ == '__main__':
	main()