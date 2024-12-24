import pygame
import sys
import random
import math



pygame.init()
info = pygame.display.Info()
w, h = info.current_w, info.current_h
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
pygame.display.set_caption('physics, math, code & fun')

pygame.mixer.init()
beep = pygame.mixer.Sound("beep.mp3")
font = pygame.font.SysFont('Arial', 100)
clock = pygame.time.Clock()


delta_time = 0.0
dt = 0.001
t = 0

A1 = 50.0
k1 = 0.01
omega1 = 1.0

A2 = 50.0
k2 = 0.01
omega2 = -1.0

points1 = []
points2 = []
points3 = []


def wave(screen, color):
    global t, A1, k1, omega1, A2, k2, omega2
    global pygame
    global points1, points2
    points1.clear()
    points2.clear()
    points3.clear()
    
    for x in range(0, w):
        f1 = A1 * math.cos(k1 * x - omega1 * t)
        f2 = A2 * math.cos(k2 * x - omega2 * t)
        points1.append((x, f1 + h/4))
        points2.append((x, f2 + 2 * h/4))
        points3.append((x, (f1 + f2) + 3 * h/4))
        
    pygame.draw.lines(screen, (200, 50, 50), False, points1, 10)
    pygame.draw.lines(screen, (100, 250, 50), False, points2, 10)
    pygame.draw.lines(screen, (100, 120, 250), False, points3, 10)
    
    
def Update(screen):
    global delta_time
    global dt
    global t
    global h,w, k1, omega1, A1
    
    text = font.render(f'(top wave) k = {k1:.2f}, w = {omega1:.2f} and A = {A1:.2f}', True, (255,255,255))
    screen.blit(text, pygame.Rect(60, 0, 400,300))
    
    wave(screen, (200, 50, 50))

     
    delta_time = clock.tick(60) / 1000
    pygame.display.flip()
    t += 0.01
    
    
isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isEnd = True
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_k]:
        k1 += 0.001
        
    if keys[pygame.K_l]:
        k1 -= 0.001
        
    if keys[pygame.K_d]:
        A1 += 1
        
    if keys[pygame.K_a]:
        A1 -= 1
        
    if keys[pygame.K_w]:
        omega1 += 0.01
        
    if keys[pygame.K_s]:
        omega1 -= 0.01
        
    if keys[pygame.K_v]:
        omega2 = random.uniform(0.0, 5.0)
        A2 = random.uniform(5.0, 50.0)
        k2 = random.uniform(0.0, 0.1)        
    
    screen.fill((0,0,0))       
    Update(screen)
    
pygame.quit()
sys.exit()
