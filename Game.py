import pygame
import math
import random


#setup display
pygame.init()
WIDHT, HIGHT = 800, 500
win = pygame.display.set_mode((WIDHT, HIGHT))
pygame.display.set_caption("Hangman Game")

#Buttons setup
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDHT - (GAP + RADIUS*2)*13)/2)
starty = 400
a = 65
for i in range(26):
    x =startx + GAP * 2 + ((RADIUS * 2 + GAP)*(i % 13))
    y = starty + ((i // 13)*(GAP + RADIUS * 2))
    letters.append([x,y,chr(a + i),True])

#Font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#set up images
images = []
for i in range(7):
    image = pygame.image.load('hangman' + str(i) + '.png')
    images.append(image)

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Game wariable
hangman_status = 0
words = ["PYTHON", "PROGRAM", "DEVELOPER", "PYGAMES", "COMPUTER"]
word = random.choice(words)
quessed = []

#set up game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    #Draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDHT / 2 - text.get_width() / 2, 20))

    #Draw word
    display_word = ''
    for letter in word:
        if letter in quessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    #draw buttons
    for letter in letters:
        x,y,ltr,visible =letter
        if visible:
            pygame.draw.circle(win, BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150,100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDHT / 2 - text.get_width() / 2, HIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        quessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in quessed:
            won = False
            break
    if won:
        display_message("YOU WON!")
        break

    if hangman_status == 6:
        display_message("YOU LOST!")
        break


pygame.quit()


