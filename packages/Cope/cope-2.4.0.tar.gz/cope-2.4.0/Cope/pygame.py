"""
Functions & classes that extend the pygame
"""
from .misc import RedirectStd
from typing import Union
try:
    # Don't print the annoying "welcome from the pygame community!" message
    with RedirectStd():
        import pygame
except: pass
else:
    # TODO: tests
    def rotateSurface(surface:pygame.Surface, angle:float, pivot:Union[tuple, list, pygame.math.Vector2], offset:pygame.math.Vector2):
        """ Rotate the surface around the pivot point.

            Args:
                surface (pygame.Surface): The surface that is to be rotated.
                angle (float): Rotate by this angle.
                pivot (tuple, list, pygame.math.Vector2): The pivot point.
                offset (pygame.math.Vector2): This vector is added to the pivot.
        """

        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.
