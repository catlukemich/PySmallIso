class ScrollConstraint:

    def allow_scroll(self, new_center):
        return True


class NoScrollConstraint(ScrollConstraint):

    def allow_scroll(self, new_center):
        return True


class RectScrollConstraint(ScrollConstraint):

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def allow_scroll(self, new_center):
        if -self.width / 2 < new_center.x < self.width / 2 and -self.length / 2 < new_center.y < self.length / 2:
            return True
        else:
            return False