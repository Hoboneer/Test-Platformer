import pdb  # For debugging purposes
import sys
import pygame as pg

from constants import *
from custom_events import *
from player import Player
from platform import Platform

from profilehooks import profile

## TODO: Make game simulate at a constant time-step/delta and draw calls vary

class Game:
    def __init__(self):
        self.done = False

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()

        self.clock = pg.time.Clock()
        self.fps = MAX_FPS
        self.caption = CAPTION

        self.sprites = pg.sprite.Group()

        self.player = Player(PLAYER_START)
        self.platform = Platform(PLATFORM_POS)

        self.sprites.add(self.player, self.platform)

    def display_fps(self):
        pg.display.set_caption(self.caption.format(self.clock.get_fps()))

    def event_loop(self, dt):
        # keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.player.handle_keydown_input(event, dt)
            elif event.type == pg.KEYUP:
                self.player.handle_keyup_input(event, dt)
            elif event.type == PlayerJumpEvent.type:
                self.handle_jump_event()

    def handle_jump_event(self):
        # print("jumped")
        self.player.y += 1  # Nudge player down 1 px

        # if self.player.rect.colliderect(self.platform) or not self.player.is_airborne:
        if not self.player.is_airborne:
            self.player.jump()

        self.player.y -= 1

    def draw(self):
        self.screen.fill(WHITE)
        self.sprites.draw(self.screen)
        pg.display.update()

    def apply_gravity(self, dt, *sprites):
        # Place this function in its own class?? -- a component for `GameManager`-type classes
        for sprite in sprites:
            if sprite.is_airborne:
                sprite.physics_component.apply_force_to_y(GRAVITY)

                if sprite.bottom_y > self.screen_rect.bottom:
                    self.player.bottom_y = self.screen_rect.bottom
                    self.set_grounded(sprite)

    def set_grounded(self, sprite):
        # TODO: Fix the fact that this is called over and over, just uncomment the print to see what I mean
        # print("grounded")
        sprite.is_jumping = sprite.is_airborne    = False
        sprite.physics_component.velocity.y = sprite.physics_component.acceleration.y = 0

    def update(self, dt):
        # TODO: Change the input to checking collisions with collidable sprites in a group
        if not self.player.rect.bottom == self.screen_rect.bottom:
            self.player.is_airborne = True
        self.apply_gravity(dt, self.player)
        self.sprites.update(dt)

    # @profile
    def main_loop(self):
        while not self.done:
            dt = self.clock.tick(self.fps) / 1000
            self.event_loop(dt)
            self.update(dt)
            self.draw()
            self.display_fps()

        self.close()

    def close(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    Game().main_loop()