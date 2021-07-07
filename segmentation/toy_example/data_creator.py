import numpy as np
import pygame
import os

x = 80
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

WHITE = (255, 255, 255)
GREY = (20, 20, 20)
LIGHT_GREY = (211, 211, 211)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
WHITE_INT = 16777215
BLACK_INT = 0

HEIGHT = 600
WIDE = 800
WORLD_SIZE = (WIDE, HEIGHT)

pygame.init()
screen = pygame.display.set_mode(WORLD_SIZE)
screen.fill(WHITE)

pygame.display.set_caption("Image Creator")


def get_surface():
    return np.copy(pygame.surfarray.pixels2d(screen))


def draw_rec(x, y, size, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))


# pygame.draw.polygon()


def draw_circle(radius, x, y, color):
    pygame.draw.circle(screen, color, radius=radius, center=[x, y])


def draw_ellipse(x, y, width, height, color):
    pygame.draw.ellipse(screen, color, pygame.Rect(x, y, width, height))


def draw_rec_outline(data):
    _, x, y, width, height = data
    pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, width, height), 1)


color_list = [RED, GREEN, BLUE, PURPLE]


def get_random_color():
    return np.random.randint(10, 200), np.random.randint(10, 200), np.random.randint(10, 200)


def paint_random_shape():
    r = np.random.randint(0, 3)
    x = np.random.randint(10, WIDE - 50)
    y = np.random.randint(10, HEIGHT - 50)
    if r == 0:
        s = np.random.randint(10, 50)
        draw_rec(x, y, s, get_random_color())
        return "rec", x, y, s, s
    elif r == 1:
        radius = np.random.randint(10, 26)
        draw_circle(radius, x, y, get_random_color())
        return "circle", x - radius, y - radius, radius*2, radius*2
    else:
        width = np.random.randint(60, 80)
        height = np.random.randint(20, 30)
        draw_ellipse(x, y, width, height, get_random_color())
        return "ellipse", x, y, width, height


clean_background = get_surface()

images = []
image_train = []

n = np.random.randint(1, 10)
for i in range(n):
    shape = paint_random_shape()
    image_train.append(shape)

images.append(get_surface())

for i in range(len(image_train)):
    data = image_train[i]
    draw_rec_outline(data)

pygame.display.flip()

while True:
    pass
