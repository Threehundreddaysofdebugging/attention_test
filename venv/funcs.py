import os
import sys
import pygame
import random
from cfg import *


def terminate():
    # функция, завершающая игру и программу
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    # загрузка изображения из папки data
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def create_rect(coords, rnd=False, size=50):
    # создание pygame.Rect размера size по координатам
    if rnd:
        random.shuffle(coords)
    res = []
    for i in coords:
        r = pygame.Rect(i[0], i[1], size, size)
        res.append(r)
    return res


def render_text(screen, txt, coords, color='white'):
    # вывод многострочного текста, пердставленного списком строк
    font = pygame.font.Font(None, 25)
    text_coord = 40
    for line in txt:
        if txt.index(line) == 1:
            string_rendered = font.render(line, 1, pygame.Color(color))
        else:
            string_rendered = font.render(line, 1, pygame.Color('white'))
        rect = string_rendered.get_rect()
        rect.x = coords[0]
        rect.y = coords[1]
        text_coord += 10
        rect.top = text_coord
        text_coord += rect.height
        screen.blit(string_rendered, rect)


def start_screen(screen, clock):
    # начальный экран с правилами
    intro_text = ["ПРАВИЛА ИГРЫ", '',
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


def game_over_screen(screen, cur_score, best_score, clock):
    # конечный экран с выводом счета, лучшего счета за этот запуск
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
