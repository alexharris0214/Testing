class Rect:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def increment_x(self, x):
        self.x +=x

    def increment_y(self, x):
        self.x +=1

x = Rect(3,4)
x.increment_x(3)
x.__init__(8,7)
print(x.x)

