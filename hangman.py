import pygame
import random
from words import wordlist as wl

pygame.init()
pygame.font.init()

width, height = 900, 900
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hangman")

screen.fill((255,255,255))
pygame.display.flip()

FPS = 30
clock = pygame.time.Clock()

word = random.choice(wl)
print(word)

def get_word():
    return word

def new_game():
    screen.fill((255, 255, 255))
    pygame.display.flip()
    pygame.draw.rect(screen, (0,0,0), (50,700,300,15))
    pygame.draw.rect(screen, (0, 0, 0), (200, 0, 15, 700))
    pygame.draw.rect(screen, (0, 0, 0), (200, 0, 300, 15))
    pygame.draw.rect(screen, (0, 0, 0), (500, 0, 15, 40))
    pygame.display.update()
    unknown_word = ""
    for x in get_word():
        unknown_word += "_ "
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render(unknown_word, False, (220, 20, 60))
    screen.blit(text, (100, 750))
    pygame.display.update()

def draw_body(error):
    if error == 0:
        pygame.draw.circle(screen, (220,20,60), (505,100), 65)
        pygame.display.update()
    elif error == 1:
        pygame.draw.line(screen, (220,20,60), (505,100), (505,350),15)
        pygame.display.update()
    elif error == 2:
        pygame.draw.line(screen, (220,20,60), (600,200), (505,250),15)
        pygame.display.update()
    elif error == 3:
        pygame.draw.line(screen, (220,20,60), (400,200), (505,250),15)
        pygame.display.update()
    elif error == 4:
        pygame.draw.line(screen, (220,20,60), (400,500), (505,350),15)
        pygame.display.update()
    elif error == 5:
        pygame.draw.line(screen, (220,20,60), (610,500), (505,350),15)
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render(get_word(), False, (220,20,60))
        screen.blit(text, (275,500))
        pygame.display.update()

new_game()
draw_body(0)
draw_body(1)
draw_body(2)
draw_body(3)
draw_body(4)
draw_body(5)

run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


