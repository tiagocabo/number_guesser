import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

# set frame size
gameDisplay = pygame.display.set_mode((display_width, display_height))

# window name
pygame.display.set_caption('My first game!')

# game time
clock = pygame.time.Clock()

# load image
dinoImg = pygame.image.load('images/googleDino.png')
dinoImg = pygame.transform.scale(dinoImg, (50, 30))

def display_score(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render('score: ' + str(count), True, black)
	gameDisplay.blit(text, [0,0])

def dino(x, y):
	# puts the image on a frame
	gameDisplay.blit(dinoImg, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return  textSurface, textSurface.get_rect()

def show_text(text):
	largeText = pygame.font.Font('freesansbold.ttf', 20)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width / 2), (display_height / 2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
def message_display(text):
	show_text(text)
	time.sleep(2)
	game_loop()

def crash(count):
	message_display(f'You Crashed. Good Luck next Time. score: {count}')

def thing(thing_x, thing_y, thing_w, thing_h, color):
	obtacle = pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

def game_loop():
	x = (display_width * 0.1)
	y = (display_height * 0.8)
	y_change = 0

	thing_start_y = random.randrange(0, display_height)
	thing_start_x = display_width + 300
	thing_speed = 7
	thing_w = 100
	thing_h = 100
	level_Frag = False
	level_time = 0
	count = 0
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			print('Crash status: ', gameExit)
			print(event)
			if event.type == pygame.KEYDOWN:
				print('KEYDOWN PRESSED ')
				if event.key == pygame.K_UP:
					print('KEY LEFT PRESSED ')
					y_change = int(-10)
				elif event.key == pygame.K_DOWN:
					y_change = int(10)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = int(0)

		print('curren x change: ', y_change)
		y += y_change

		gameDisplay.fill(white)
		# pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

		# thing(thing_x, thing_y, thing_w, thing_h, color)
		thing(thing_start_x, thing_start_y, thing_w, thing_h, black)
		thing_start_x -= thing_speed


		# add condition for whenever the blocks reach the end of the window
		if thing_start_x <= 0:
			thing_start_x = display_width
			thing_start_y = random.randrange(0, display_height)
			count += 1

			if count % 3 == 0 and count != 0:
				thing_speed += 1
				level_Frag = True
				level_time = 0

		if level_Frag:
			show_text('level up')
			level_time += 1

		if level_time > 20:
			level_Frag = False

		display_score(count)
		dino(x, y)

		if y > display_height - 30 or y < 0:
			crash(count)

		if x + 50 >= thing_start_x and ((thing_start_y + thing_h >= y  >= thing_start_y)
		                                or (thing_start_y < y + 30 <= thing_start_y + thing_h)) :
			crash(count)

		# increase frame change
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()