import pygame
import random
from words import wordlist

pygame.init()
clock = pygame.time.Clock()


width, height = 1480, 800
background_colour = (255,255,255)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Hangman')
screen.fill(background_colour)

# Hangman imgs

IMAGES = []
level = 0

for x in range(7):
  image = pygame.image.load(f'img/Hangman{x}.png').convert()
  IMAGES.append(image)

pygame.display.flip()

# Buttons

size = 60
distance_x = 400
distance_y = 570
boxes = []

for row in range(2):
  for col in range(13):
    x = ((col * 20) + 20) + (size * col) + distance_x
    y = ((row * 20) + 20) + (size * row) + distance_y
    box = pygame.Rect(x,y,size,size)
    boxes.append(box)

buttons = []
Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0

for box in boxes:
  button = [box,Characters[i]]
  buttons.append(button)
  i += 1

# Word
word = random.choice(wordlist)
guessed_list = []
print(word)

# Font
font = pygame.font.SysFont('arial', 30)
wordfont = pygame.font.SysFont('arial', 100)

# Game

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(IMAGES[level], (-100,0))

  for box in boxes:
    pygame.draw.rect(screen,(0,0,0), box, 5)

  for box, letter in buttons:
    text = font.render(letter, True, (0,0,0))
    rect = text.get_rect(center = (box.x + 30, box.y + 30))
    screen.blit(text, rect)

  display_text = ""

  for letter in word:
    if letter in guessed_list:
      display_text += letter + " "
    else:
      display_text += "_ "

  display = wordfont.render(display_text, True, (0,0,0))
  screen.blit(display, (600, 250))

  pygame.display.update()
  clock.tick(30)
