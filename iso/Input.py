import pygame


class MouseListener:
    def mouseButtonDown(self, event):
        pass

    def mouseButtonUp(self, event):
        pass

    def mouseMotion(self, event):
        pass


class KeyboardListener:
    def keyDown(self, event):
        pass

    def keyUp(self, event):
        pass


class Input:
    def __init__(self):
        self.key_listeners = []
        self.mouse_listeners = []

    def addMouseListener(self, listener):
        self.mouse_listeners.append(listener)

    def addKeyboardListener(self, listener):
        self.key_listeners.append(listener)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for listener in self.mouse_listeners:
                consumed = listener.mouseButtonDown(event)
                if consumed:
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            for listener in self.mouse_listeners:
                consumed = listener.mouseButtonUp(event)
                if consumed:
                    break

        if event.type == pygame.MOUSEMOTION:
            for listener in self.mouse_listeners:
                consumed = listener.mouseMotion(event)
                if consumed:
                    break

        '''if event.type == pygame.MOUSEWHEEL:
            for listener in self.mouse_listeners:
                consumed = listener.mouseWheel(event)
                if consumed: 
                    break '''

        if event.type == pygame.KEYDOWN:
            for listener in self.key_listeners:
                consumed = listener.keyDown(event)
                if consumed:
                    break

        if event.type == pygame.KEYUP:
            for listener in self.key_listeners:
                consumed = listener.keyUp(event)
                if consumed:
                    break
