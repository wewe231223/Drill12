import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    global balls
    balls = [Ball(random.randint(0,1600),60,0) for _ in range(50)]
    game_world.add_objects(balls,1)

    Zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(Zombies,1)

    # collision pair resist
    game_world.add_collision_pairs("boy:ball",boy,None)
    game_world.add_collision_pairs("playerball:zombie",None,None)
    game_world.add_collision_pairs("player:zombie",boy,None)

    for ball in balls:
        game_world.add_collision_pairs("boy:ball",None,ball)


    for zombie in Zombies:
        game_world.add_collision_pairs("playerball:zombie",None,zombie)
        game_world.add_collision_pairs("player:zombie",None,zombie)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    game_world.handle_collisions()



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

