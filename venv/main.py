import pygame
from funcs import *


def start_screen():
    intro_text = ["Правила игры", '',
                  'Уважаемый Игрок! Вам будут предложены текстовое',
                  'задание и кликабельные варианты ответа к нему',
                  "Точно выполняйте текстовые инструкции, иначе - ",
                  "проигрыш. Если вы не успели дать ответ за отведённое",
                  "время - проигрыш.",
                  'Приятной игры!']
    fon = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 25)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

def game_over_screen():
    intro_text = ['GAME OVER', '',
                  "Ваш результат:" + str(cur_score).rjust(3),
                  "Лучший результат:" + str(best_score).rjust(3), "",
                  '(нажмите любую кнопку чтобы сыграть снова)']
    fon = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 25)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
size = WIDTH, HEIGHT = 501, 501
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Тест на внимательность')

FPS = 30
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

cur_score = 0
best_score = 0
timer, text = 7, 'time' + '7'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font_big = pygame.font.SysFont('Consolas', 30)
font_small = pygame.font.SysFont('Consolas', 21)

running = True
start_screen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            timer -= 1
            if timer > 0:
                text = 'time' + str(timer).rjust(3)
            else:
                if cur_score > best_score:
                    best_score = cur_score
                game_over_screen()
                cur_score = 0
                timer = 7
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    all_sprites.draw(screen)
    screen.fill((0, 0, 0))
    screen.blit(font_big.render(text, True, (255, 255, 255)), (int(.33 * WIDTH), int(.05 * HEIGHT)))
    pygame.display.flip()
    clock.tick(FPS)

terminate()