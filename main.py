import glfw

def main():
	
	glfw.set_error_callback(error_callback)

	if not glfw.init():
		print("ERROR [-1]: Failed to initialize GLFW")
		return

	window = glfw.create_window(640, 360, "Window", None, None)

	if not window:
		glfw.terminate()
		return

	glfw.make_context_current(window)

	while not glfw.window_should_close(window):
		glfw.poll_events()
		glfw.swap_buffers(window)

	glfw.terminate()

def error_callback(code, description):
	print(f"ERROR [{code}]: {description.decode()}")

if __name__ == '__main__':
	main()