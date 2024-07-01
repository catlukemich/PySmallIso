from .Input import *
from .ScrollConstraint import NoScrollConstraint

class Scroller(MouseListener):
    def __init__(self, viewport, input):
        self.rmb_down = False
        self.viewport = viewport
        self.input = input
        self.constraint = NoScrollConstraint()
        pass

    def enable(self):
        self.input.add_mouse_listener(self)

    def mouse_button_down(self, event):
        if event.button == 3:
            self.rmb_down = True

    def mouse_motion(self, event):
        if self.rmb_down:
            c = self.viewport.get_center()
            if event.rel[0] != 0:
                c.x += 0.1 * event.rel[0]
                c.y -= 0.1 * event.rel[0]
            if event.rel[1] != 0:
                c.x += 0.1 * event.rel[1]
                c.y += 0.1 * event.rel[1]

            if self.constraint.allow_scroll(c):
                self.viewport.set_center(c)

    def mouse_button_up(self, event):
        if event.button == 3:
            self.rmb_down = False

    def disable(self):
        self.input.remove_keyboard_listener(self)

    def set_constraint(self, constraint):
        self.constraint = constraint