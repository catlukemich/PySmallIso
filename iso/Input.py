import pygame


class MouseListener:
    def mouse_button_down(self, event):
        pass

    def mouse_button_up(self, event):
        pass

    def mouse_motion(self, event):
        pass


class KeyboardListener:
    def key_down(self, event):
        pass

    def key_up(self, event):
        pass


class Input:
    def __init__(self):
        self.key_listeners = []
        self.mouse_listeners = []

    def add_mouse_listener(self, listener):
        self.mouse_listeners.append(listener)

    def add_keyboard_listener(self, listener):
        self.key_listeners.append(listener)

    def remove_mouse_listener(self, listener):
        self.mouse_listeners.remove(listener)

    def remove_keyboard_listener(self, listener):
        self.key_listeners.remove(listener)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for listener in self.mouse_listeners:
                consumed = listener.mouse_button_down(event)
                if consumed:
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            for listener in self.mouse_listeners:
                consumed = listener.mouse_button_up(event)
                if consumed:
                    break

        if event.type == pygame.MOUSEMOTION:
            for listener in self.mouse_listeners:
                consumed = listener.mouse_motion(event)
                if consumed:
                    break

        if event.type == pygame.KEYDOWN:
            for listener in self.key_listeners:
                consumed = listener.key_down(event)
                if consumed:
                    break

        if event.type == pygame.KEYUP:
            for listener in self.key_listeners:
                consumed = listener.key_up(event)
                if consumed:
                    break
