# Abstract class
class Updateable():
    def update(self):
        pass


class Updater():
    def __init__(self):
        self.updateables = []

    def addUpdateable(self, updateable):
        self.updateables.append(updateable)

    def removeUpdateable(self, updateable):
        self.updateables.remove(updateable)

    def update(self):
        for updateable in self.updateables:
            updateable.update()
