class Rectangle:
    def __init__(self,list_of_dots=[]):
        vector1 = [0,0]
        vector2 = [0,0]
        vector3 = [0,0]
        vector1[0] = list_of_dots[1][0] - list_of_dots[0][0]
        vector1[1] = list_of_dots[1][1] - list_of_dots[0][1]
        vector2[0] = list_of_dots[2][0] - list_of_dots[0][0]
        vector2[1] = list_of_dots[2][1] - list_of_dots[0][1]
        vector3[0] = list_of_dots[3][0] - list_of_dots[0][0]
        vector3[1] = list_of_dots[3][1] - list_of_dots[0][1]
        scalyar1 = int()
        scalyar2 = int()
        scalyar3 = int()
        scalyar1 = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        scalyar2 = vector1[0] * vector3[0] + vector1[1] * vector3[1]
        scalyar3 = vector3[0] * vector2[0] + vector3[1] * vector2[1]
        if scalyar1 == 0 :
            self.dot1 = list_of_dots[0]
            self.dot2 = list_of_dots[1]
            self.dot3 = list_of_dots[3]
            self.dot4 = list_of_dots[2]
        if scalyar2 == 0:
            self.dot1 = list_of_dots[0]
            self.dot2 = list_of_dots[1]
            self.dot3 = list_of_dots[2]
            self.dot4 = list_of_dots[3]
        if scalyar3 == 0 :
            self.dot1 = list_of_dots[0]
            self.dot2 = list_of_dots[2]
            self.dot3 = list_of_dots[1]
            self.dot4 = list_of_dots[3]
        self.a = ((self.dot1[0] - self.dot2[0]) ** 2 + (self.dot1[1] - self.dot2[1])) ** (1/2)
        self.b = ((self.dot1[0] - self.dot4[0]) ** 2 + (self.dot1[1] - self.dot4[1])) ** (1/2)
    def perimetr(self):
        return 2 * (self.a + self.b)
    def sq(self):
        return self.a * self.b

abcd = Rectangle([[0,0],[0,1],[2,0],[2,1]])
print(abcd.perimetr())
print(abcd.sq())