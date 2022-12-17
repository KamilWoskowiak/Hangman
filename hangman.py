import pygame
from pygame.locals import *
import random
from words import wordlist

def draw_btns(buttons):
    for button, letter in buttons:
        btn_text = fontbtn.render(letter, True, black)
        btn_text_rect = btn_text.get_rect(center=(button.x + 30, button.y + 30))
        pygame.draw.rect(screen, black, button, 2)
        screen.blit(btn_text, btn_text_rect)


def display_guess():
    display_word = ""

    for letter in word:
        if letter in guessed:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = font.render(display_word, True, black)
    screen.blit(text, (540, 250))


pygame.init()
width, height = 1480, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

game_over = False

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# images
images = []
level = 0

for i in range(7):
    image = pygame.image.load(f"img/hangman{i}.png").convert()
    images.append(image)

# buttons
size = 60
distance_x = 400
distance_y = 570
BOXES = []

for row in range(2):
    for col in range(13):
        x = ((col * 20) + 20) + (size * col) + distance_x
        y = ((row * 20) + 20) + (size * row) + distance_y
        box = pygame.Rect(x, y, size, size)
        BOXES.append(box)

buttons = []
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0

for box in BOXES:
    button = ([box, characters[i]])
    buttons.append(button)
    i += 1

# fonts
fontbtn = pygame.font.SysFont("arial", 30)
font = pygame.font.SysFont("arial", 100)

# word
word = random.choice(wordlist).upper()
guessed = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            clicked_pos = event.pos

            for button, letter in buttons:
                if button.collidepoint(clicked_pos):
                    guessed.append(letter)

                    if letter not in word:
                        level += 1

                    if level == 6:
                        game_over = True

                    buttons.remove([button, letter])

    screen.fill(white)
    screen.blit(images[level], (-100, 0))
    draw_btns(buttons)
    display_guess()

    won = True

    for letter in word:
        if letter not in guessed:
            won = False

    if won:
        game_over = True
        display_text = "YOU WON - " + word
    else:
        display_text = "YOU LOST - " + word

    pygame.display.update()

    if game_over:
        screen.fill(white)
        game_over_text = font.render(display_text, True, black)
        game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
