from typing import Tuple, Union

from pygame.sprite import Sprite
from pygame.math import Vector2
import pygame as pg

from custom_events import PlayerJumpEvent
from constants import PLAYER_SIZE, PLAYER_COLOUR, GRAVITY, PLAYER_SPEED, PLAYER_JUMP_SPEED, PLAYER_START, PLAYER_MASS, PLAYER_MAX_VELOCITY
from components import PhysicsComponent

# This is pretty messy because of the newly added physics component, but that'll be fixed-
# soon hopefully because I want a `ComponentManager` class to deal with them :))

class Player(Sprite):
    def __init__(self, pos:Tuple[Union[int, float], Union[int, float]]):
        super().__init__()
        self.is_airborne      = True
        self.is_jumping       = False
        self.is_walking_right = False
        self.is_walking_left  = False

        self.rect = pg.Rect(pos, PLAYER_SIZE)
        self.pos = Vector2(self.rect.center)
        # TODO: Change access to a `ComponentManager` class to better handle components
        self.physics_component = PhysicsComponent(mass=PLAYER_MASS,
                                                  walk_force=PLAYER_SPEED,
                                                  jump_force=PLAYER_JUMP_SPEED,
                                                  max_velocity=PLAYER_MAX_VELOCITY)

        self.image = pg.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COLOUR)
        self.image.convert()

    def __str__(self):
        return "Pos: {};RectCenter: {};IsAirborne: {};IsJumping: {}".format(self.pos,
                                                                            self.rect.center,
                                                                            self.is_airborne,
                                                                            self.is_jumping)

    # Kinda ugly (this property chain); maybe place this in an ABC? or another component?

    @property
    def bottom_y(self):
        return self.rect.bottom

    @bottom_y.setter
    def bottom_y(self, other):
        self.rect.bottom = other
        self.pos.y = self.rect.centery

    @property
    def x(self):
        return self.pos.x

    @x.setter
    def x(self, other):
        self.pos.x = other
        self.rect.centerx = self.pos.x

    @property
    def y(self):
        return self.pos.y

    @y.setter
    def y(self, other):
        self.pos.y = other
        self.rect.centery = self.pos.y

    def reset(self):
        self.pos = Vector2(PLAYER_START)

        self.is_airborne      = True
        self.is_jumping       = False
        self.is_walking_right = False
        self.is_walking_left  = False

    def handle_keydown_input(self, event, dt):
        if event.key == pg.K_UP:
            self.request_jump()
        elif event.key == pg.K_LEFT:
            # self.walk(-self.speed, dt)
            print("toggle left on")
            self.is_walking_left = True
        elif event.key == pg.K_RIGHT:
            # self.walk(self.speed, dt)
            print("toggle right on")
            self.is_walking_right = True
        elif event.key == pg.K_SPACE:
            print(self)
        elif event.key == pg.K_BACKQUOTE:
            self.reset()
        elif event.key == pg.K_f:  # Display force info
            print("Forces:{};Accel:{};Vel:{};Pos:{}".format(self.physics_component.forces,self.physics_component.acceleration,self.physics_component.velocity,self.pos))

    def handle_keyup_input(self, event, dt):
        if event.key == pg.K_LEFT:
            print("toggle left off")
            self.is_walking_left = False
        elif event.key == pg.K_RIGHT:
            print("toggle right off")
            self.is_walking_right = False

    def walk(self, force_speed:Union[int, float]):
        # self.x += speed * dt
        # self.velocity.x +=
        self.physics_component.apply_force_to_x(force_speed)

    def request_jump(self):
        pg.event.post(PlayerJumpEvent)

    def jump(self):
        print("jumping on")
        self.is_airborne = self.is_jumping = True
        self.apply_force_to_y(-self.jump_speed)

    def update(self, dt):
        if self.is_jumping:
            # self.y -= self.jump_speed * dt
            # self.y -= self.velocity.y * dt
            pass  # Dunno whether it should keep adding velocity, prob not
        if self.is_walking_right:
            self.walk(self.physics_component.walk_force)
        if self.is_walking_left:
            self.walk(-self.physics_component.walk_force)

        self.physics_component.calculate_acceleration()
        self.physics_component.apply_accel(dt)
        self.physics_component.update_pos(self.pos, dt)

        # Update rect center to contain correct values
        self.rect.center = self.pos

    def draw(self, canvas):
        canvas.blit(self.image, self.pos)