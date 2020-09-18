

class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h



    def intersects(self, other):
        self_top_left_x = self.x
        self_top_left_y = self.y
        self_bottom_right_x = self.x + self.w
        self_bottom_right_y = self.y + self.h

        other_top_left_x = other.x
        other_top_left_y = other.y
        other_bottom_right_x = other.x + other.w
        other_bottom_right_y = other.y + other.h

        if self_bottom_right_x < other_top_left_x or other_bottom_right_x < self_top_left_x:
            return False
        if self_bottom_right_y < other_top_left_y or other_bottom_right_y < self_top_left_y:
            return False

        return True


if __name__ == "__main__":
    r1 = Rectangle(0,0, 10, 10)
    r2 = Rectangle(5, 11, 10, 10)

    print(r1.intersects(r2))