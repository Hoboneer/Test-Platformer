from typing import Union
from pygame.math import Vector2

IntOrFloat = Union[int, float]


class BaseComponent:
    # Implement some shared interface maybe?
    def __init__(self):
        pass


class PhysicsComponent(BaseComponent):
    """A class using physics to calculate the correct velocities from forces
    acted upon it."""
    # Main game class doesn't implement friction yet :/ gotta work on that
    def __init__(self,
                 mass: IntOrFloat,
                 walk_force: IntOrFloat,
                 jump_force: IntOrFloat,
                 max_velocity: Vector2):
        super().__init__()

        self.mass = mass
        self.walk_force = walk_force
        self.jump_force = jump_force

        self.max_velocity = max_velocity
        self.forces = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()

    # --- ACCELERATION APPLICATION --- #
    def apply_accel(self, dt:float) -> None:
        self.velocity += self.acceleration * dt

        # Keeping velocity in bounds
        if self.velocity.x > self.max_velocity.x:
            self.velocity.x = self.max_velocity.x
        elif self.velocity.y > self.max_velocity.y:
            self.velocity.y = self.max_velocity.y
    # --- END --- #

    # --- FORCE APPLICATION --- #
    def apply_force_to_x(self, force:IntOrFloat) -> None:
        # self.acceleration.x += force / self.mass
        self.forces.x += force

    def apply_force_to_y(self, force:IntOrFloat) -> None:
        # self.acceleration.y += force / self.mass
        self.forces.y += force

    def apply_force_vector(self, force_vector:Vector2) -> None:
        # self.acceleration += force / self.mass
        self.forces += force
    # --- END --- #

    # --- ENDING PHYSICS APPLICATIONS --- #
    def calculate_acceleration(self) -> None:
        # CALLED AT END OF ALL FORCE APPLICATIONS
        self.acceleration = self.forces / self.mass
        self.forces = Vector2(0, 0)  # Clearing the forces acting upon this object

    def update_pos(self, pos:Vector2, dt:float) -> Vector2:
        """Returns it just in case anyone actually want it.
        MAY BE DEPRECATED"""
        pos += self.velocity * dt
        return pos
    # --- END --- #