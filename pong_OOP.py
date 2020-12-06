import pygame
import random

pygame.init()

class paddle:
	
	def __init__(self, x, y, speed, top_boundary, bottom_boundary, hitbox, picture):
		self.x = x
		self.y = y
		self.speed = speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
		self.hitbox = hitbox
		self.picture = picture
		

	def load_picture(self):
		
		screen.blit(pygame.image.load(self.picture), (self.x, self.y))


	def check_boundary(self):
		if self.y < self.top_boundary:
			self.y = self.top_boundary
		if self.y > self.bottom_boundary:
			self.y = self.bottom_boundary


	def moveup(self):
		self.y -= self.speed

	def movedown(self):
		self.y += self.speed

	def move_hitbox(self):
		self.hitbox = [i for i in range(round(self.y), round(self.y) + 64)]

	def check_pressed_keys(self):

		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			leftpaddle.moveup()
		if keys[pygame.K_s]:
			leftpaddle.movedown()
			
		if keys[pygame.K_UP]:
			rightpaddle.moveup()
		if keys[pygame.K_DOWN]:
			rightpaddle.movedown()
		

class Ball:

	def __init__(self, x, y, max_speed, x_speed, y_speed, top_boundary, bottom_boundary, left_boundary, right_boundary, hitbox, picture):
		self.x = x
		self.y = y
		self.max_speed = max_speed
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
		self.left_boundary = left_boundary
		self.right_boundary = right_boundary
		self.hitbox = hitbox
		self.picture = picture


	def load_picture(self):
		screen.blit(pygame.image.load(self.picture), (self.x, self.y))

	def move(self):
		self.x += self.x_speed
		self.y += self.y_speed


	def check_boundary(self):
		if self.y < self.top_boundary:
			self.y_speed *= -1
		if self.y > self.bottom_boundary:
			self.y_speed *= -1

		if self.x < self.left_boundary:
			self.x_speed *= -1
		if self.x > self.right_boundary:
			self.x_speed *= -1

	def move_hitbox(self):
		self.hitbox = [i for i in range(round(self.y), round(self.y) + 32)]

	def bounce(self):
		self.x_speed *= -1


	def check_hitbox(self):
		if round(self.x) in range(73, 77): 	# left paddle main x
			for i in self.hitbox:
				if i in leftpaddle.hitbox:
					self.x_speed *= -1
					break

		if round(self.x) in range(690, 695): 	# right paddle main x
			for i in self.hitbox:
				if i in rightpaddle.hitbox:
					self.x_speed *= -1
					break

	def new_speed(self): # used for adding more balls
		self.max_speed = 5
		self.x_speed = random.choice([2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8])
		self.y_speed = self.max_speed - self.x_speed
		self.x_speed *= random.choice([-1, 1]) 
		self.y_speed *= random.choice([-1, 1])
		
	def recenter(self):
		if self.x < self.left_boundary or self.x > self.right_boundary:
			self.x = 400
			self.y = 268
			leftpaddle.y, rightpaddle.y = 250, 250

			self.new_speed()


class text:

	def __init__(self, x, y, font, color, str_score, int_score):
		self.x = x
		self.y = y
		self.font = font 
		self.color = color
		self.str_score = str_score
		self.int_score = int_score

	def convert_score_types(self):
		self.str_score = str(self.int_score)

	def change_int_score(self):
		if ball.x < ball.left_boundary:
			right_score.int_score += 1
		if ball.x > ball.right_boundary:
			left_score.int_score += 1

	def load_score(self):
		self.score = self.font.render(self.str_score, False, self.color)
		screen.blit(self.score, (self.x, self.y))


def check_update_score():
	if ball.x < ball.left_boundary:
		right_score.int_score += 1
	if ball.x > ball.right_boundary:
		left_score.int_score += 1


fpsClock = pygame.time.Clock()
fps = 60
color = (50, 164, 168)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
left_int_score = 0
right_int_score = 0


ball_max_speed = 5
ball_x_speed = random.choice([2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8])
ball_y_speed = ball_max_speed - ball_x_speed
ball_x_speed *= random.choice([-1, 1]) 
ball_y_speed *= random.choice([-1, 1])

ball = Ball(400, 268, ball_max_speed, ball_x_speed, ball_y_speed, 0, 568, 0, 768, [i for i in range(round(400), round(400) + 32)], 'pongball.png')
leftpaddle = paddle(30, 250, 2, 0, 536, [i for i in range(round(250), round(250) + 64)], 'paddle.png')
rightpaddle = paddle(705, 250, 2, 0, 536, [i for i in range(round(250), round(250) + 64)], 'paddle.png')
left_score = text(250, 50, pygame.font.SysFont('Times New Roman', 42), (0, 0, 0), '0', 0)
right_score = text(550, 50, pygame.font.SysFont('Times New Roman', 42), (0, 0, 0), '0', 0)



running = True
while running:

	
	
	

	screen.fill(color)

	leftpaddle.load_picture()
	rightpaddle.load_picture()
	ball.load_picture()

	left_score.convert_score_types()
	left_score.load_score()

	right_score.convert_score_types()
	right_score.load_score()
	
	
	leftpaddle.check_boundary()
	leftpaddle.check_pressed_keys()
	leftpaddle.move_hitbox()
	
	rightpaddle.check_boundary()
	rightpaddle.check_pressed_keys()
	rightpaddle.move_hitbox()

	ball.check_boundary()
	ball.check_hitbox()
	ball.move()
	ball.move_hitbox()


	check_update_score()
	
		


	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	fpsClock.tick(fps)
