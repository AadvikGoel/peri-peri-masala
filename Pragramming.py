class Rectangle():
    def __init__(self,l, w):
        self.lenght = 1
        self.width = w

    def rectangle_area(self):
        return self.lenght*self.width
newRectangle = Rectangle(12, 10)

print("Dimension of Rectangle - Length : %d Width : %d" % (newRectangle.length, newRectangle.width))

print("Area of Rectangle :", newRectangle.rectangle_area())


