# -*- coding: utf-8 -*-
#поставим 8битную кодировку
import time
import pygame, random, sys
from pygame.locals import *
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
                return True
	else:
                return False
def die(screen): #функция врубается, когда ты умираешь
	pygame.display.update(); # это каждый заход восстанавливает экран (положение змейки, еды)
	pygame.time.wait(1000); # Небольшая пауза
	sys.exit(0) # и автоматический выход из программы.
xs = [110];
ys = [290];
random.seed(time.time())
dirs = 0; # это переменная отображает ход змейки 0 - вниз , 2 - вверх, 3 - влево, 1 - вправо
pygame.init(); #  initialize all imported pygame modules,короче эта штука расскрывает модули pygame
s=pygame.display.set_mode((600, 600)); # screen - наш экран размером ...
img = pygame.Surface((20, 20)); #размер каждой части змейки в отдельности
img.fill((0, 129, 64)); #цвет змейки
f = pygame.font.SysFont('Arial', 20); #шрифт
clock = pygame.time.Clock()
while True:
	clock.tick(20) #скорость движения змеи

	img.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	for e in pygame.event.get():
		if e.type == QUIT: #крестик - выход
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_UP and dirs != 0:
                                dirs = 2
			elif e.key == K_DOWN and dirs != 2:
                                dirs = 0
			elif e.key == K_LEFT and dirs != 1:
                                dirs = 3
			elif e.key == K_RIGHT and dirs != 3:
                                dirs = 1


	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: # врезалась ли змея
                die(s)
	i = len(xs)-1
	if dirs==0:
                ys[0] += 20
	elif dirs==1:
                xs[0] += 20
	elif dirs==2:
                ys[0] -= 20
	elif dirs==3:
                xs[0] -= 20
	for i in range(0, len(xs)):
		s.blit(img, (xs[i], ys[i])) # прорисовка змеи
	pygame.display.update() # обновление дисплея
