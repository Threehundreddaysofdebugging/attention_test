import random
from cfg import *


colors = ['green', 'red', 'white', 'blue', 'pink', 'cyan', 'violet']
colors_corr = ['зеленую', "красную", "белую", "синюю", "розовую", "голубую", "фиолетовую"]
directions_corr = ["слева", "снизу", "справа", 'сверху']
txt_places = [(.7 * WIDTH, .4 * HEIGHT), (.1 * WIDTH, .4 * HEIGHT),
              (.1 * WIDTH, .8 * HEIGHT), (.7 * WIDTH, .8 * HEIGHT)]

def translate(word):
    return colors[colors_corr.index(word)]

def create_level():
    color_cor = random.choice(colors_corr)
    direct_corr = random.choice(directions_corr)

    f = random.choice([True, False])
    if f:
        if direct_corr == directions_corr[0]:
            txt_place = random.choice([txt_places[0], txt_places[3]])
        if direct_corr == directions_corr[1]:
            txt_place = random.choice([txt_places[0], txt_places[1]])
        if direct_corr == directions_corr[2]:
            txt_place = random.choice([txt_places[1], txt_places[2]])
        if direct_corr == directions_corr[3]:
            txt_place = random.choice([txt_places[2], txt_places[3]])
        return txt_place, direct_corr, 'dir'
    else:
        a = colors.copy()
        a.__delitem__(colors.index(translate(color_cor)))
        color = random.choice(a)
        return color, color_cor, 'color'

