import pygame
from funcs import *
from levels import *


class Arrow(pygame.sprite.Sprite):
    def __init__(self, rect, direction, is_corr=False):
        super().__init__(all_sprites)
        self.rect = rect
        self.is_corr = is_corr
        img = pygame.transform.scale(load_image('green-arrow.jpg'), (100, 100))
        self.image = img
        if direction == 'сверху':
            self.image = pygame.transform.rotate(img, 90)
        elif direction == 'слева':
            self.image = pygame.transform.rotate(img, 180)
        elif direction == 'снизу':
            self.image = pygame.transform.rotate(img, 270)
        elif direction == 'справа':
            self.image = pygame.transform.rotate(img, 0)

    def update(self, *args):
        if args and self.rect.collidepoint(*(args[0])):
            if self.is_corr:
                pygame.event.post(gener_ev)
            else:
                pygame.event.post(lose_ev)
                pygame.event.post(gener_ev)


class Button(pygame.sprite.Sprite):
    def __init__(self, rect, color, is_corr=False):
        super().__init__(all_sprites)
        self.color = pygame.Color(color)
        self.rect = rect
        self.is_corr = is_corr
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA, 32)

    def update(self, *args):
        self.image.fill(self.color)
        if args and self.rect.x < args[0][0] < self.rect.x + self.rect.width and \
                self.rect.y < args[0][1] < self.rect.y + self.rect.height:
            if self.is_corr:
                pygame.event.post(gener_ev)
            else:
                pygame.event.post(lose_ev)
                pygame.event.post(gener_ev)


pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Тест на внимательность')

GENERATE = pygame.USEREVENT + 1
LOSE = pygame.USEREVENT + 2
gener_ev = pygame.event.Event(GENERATE)
lose_ev = pygame.event.Event(LOSE)

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

buttons_place = [(int(.15 * WIDTH), int(.4 * HEIGHT)), (int(.8 * WIDTH), int(.4 * HEIGHT)),
                 (int(.15 * WIDTH), int(.65 * HEIGHT)), (int(.8 * WIDTH), int(.65 * HEIGHT))]

arrows_place = [(int(WIDTH / 2 - 150), int(HEIGHT / 2 - 50)), (int(WIDTH / 2 - 50), int(HEIGHT / 2 + 50)),
                (int(WIDTH / 2 + 50), int(HEIGHT / 2 - 50)), (int(WIDTH / 2 - 50), int(HEIGHT / 2 - 100 - 50))]

cur_score = -1
best_score = 0
text_counter = 'score' + str(cur_score).rjust(3)
timer, text_timer = 5, 'time' + '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font_big = pygame.font.SysFont('Consolas', 30)

start_screen(screen, clock)
running = True
pygame.event.post(gener_ev)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            timer -= 1
            if timer > 0:
                text_timer = 'time' + str(timer).rjust(3)
            else:
                if cur_score > best_score:
                    best_score = cur_score
                game_over_screen(screen, cur_score, best_score, clock)
                cur_score = 0
                text_counter = 'score' + str(cur_score).rjust(3)
                timer = 5
        if event.type == LOSE:
            if cur_score > best_score:
                best_score = cur_score
            game_over_screen(screen, cur_score, best_score, clock)
            cur_score = -1
            text_counter = 'score' + str(cur_score).rjust(3)
            timer = 5
        if event.type == GENERATE:
            all_sprites.empty()
            cur_score += 1
            text_counter = 'score' + str(cur_score).rjust(3)

            wrong, correct, type = create_level()
            if type == 'color':
                rects = create_rect(buttons_place, True)
                qwest = ['выберите', correct, 'кнопку']
                for i in range(2):
                    if i == 1:
                        Button(rects[i], translate(correct), True)
                    else:
                        Button(rects[i], wrong)
            elif type == 'dir':
                rects = create_rect(arrows_place, size=100)
                qwest = ["выберите ", "стрелку", correct]
                for i in range(4):
                    if i == directions_corr.index(correct):
                        Arrow(rects[i], directions_corr[i], True)
                    else:
                        Arrow(rects[i], directions_corr[i])
            timer = 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event.pos)

    all_sprites.update()
    if isinstance(wrong, str):
        render_text(screen, qwest, (10, 10), color=wrong)
    elif isinstance(wrong, tuple):
        render_text(screen, qwest, wrong)

    all_sprites.draw(screen)
    screen.blit(font_big.render(text_timer, True, (255, 255, 255)), (int(.33 * WIDTH), int(.05 * HEIGHT)))
    screen.blit(font_big.render(text_counter, True, (255, 255, 255)), (int(.33 * WIDTH), int(.9 * HEIGHT)))

    pygame.display.flip()
    clock.tick(FPS)
    screen.fill((0, 0, 0))
terminate()
