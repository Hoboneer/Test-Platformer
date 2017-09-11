import pygame as pg


# Temporary solution; I intend to make my custom events be handled by special-
# classes including the global (as in game-wide) `EventManager` (or something),
# an `Observer`-`Observable` class relationship, etc.

_jump_event     = pg.USEREVENT+1
PlayerJumpEvent = pg.event.Event(_jump_event)
