from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    x = 400
    y = 90
    while x < 800 - 21:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)
    while y < 600 - 46:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)
    while x > 0 + 21:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)
    pass

def move_circle():
    for i in range(360, -1, -1):
        i += 270
        clear_canvas_now()
        grass.draw(400, 30)
        x = 400 + 220 * math.cos(math.radians(i))
        y = 320 + 220 * math.sin(math.radians(i))
        character.draw(x, y)
        update_canvas()
        delay(0.01)

while True:
    move_rectangle()
    move_circle()


