from ursina import *
game = Ursina()
class settings(object):
	def __init__(self):
		self.title = 'My First Game'
		self.show_fps = False
		self.fullscreen = False
		self.borderless = True
		self.show_x = True
		self.keys = {}
		self.keys['forward'] = 'w'
		self.keys['backword'] = 's'
		self.keys['left'] = 'a'
		self.keys['right'] = 'd'
		self.keys['up'] = 'space'
		self.keys['down'] = 'shift'
data = settings()
window.title = data.title
window.fps_counter.enabled = data.show_fps
window.borderless = data.borderless
window.fullscreen = data.fullscreen
window.exit_button.visable = data.show_x #without this i
cube = Entity(model='cube', color=color.orange, scale=(2,2,2)) #without this  will be hard to see if we are moving
def update(): #this is called whenever a update happens hence the name
	if held_keys[data.keys['forward']]:
		camera.position += (0, 0, time.dt*2)
	if held_keys[data.keys['backword']]:
		camera.position -= (0, 0, time.dt*2)
	elif held_keys[data.keys['left']]:
		camera.position -= (time.dt*2,0,0)
	elif held_keys[data.keys['right']]:
		camera.position += (time.dt*2, 0, 0)
	if held_keys[data.keys['up']]:
		camera.position += (0,0,time.dt*2)
	if held_keys[data.keys['down']]:
		camera.position -= (0,0,time.dt*2)
game.run()
#in the next video i will have fixed it and you will be able to see the window
#in this video we will add movment
#in the next video we will be able to look around with the mouse!