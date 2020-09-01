from .alphabet import Alphabet

'''
Use self module to draw all upper case letters in alphabet

(8/31/2020): Currently assumes facing original direction (right). 
'''
class Upper(Alphabet):
    '''
    Use this class to draw uppercase letters.

    OPTIONAL ARGS: 
    '''
    def __init__(self, scale=100, spacing=15, pointer_on=False, *args, **kwargs):
        super().__init__(scale, spacing, pointer_on, *args, **kwargs)


    def A(self):
        self.left(75)
        self.forward(self.scale)
        self.right(150)
        self.forward(self.scale)
        self.left(180)
        self.forward(self.scale * .45)
        self.left(75)
        self.forward(30)
    
    def B(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-25, 180)
        self.left(180)
        self.circle(-25, 180)
    
    def C(self):
        pass
    
    def D(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale // 2, 180)
    
    def E(self):
        starting_x, starting_y = self.pos()
        self.forward(self.scale // 2)
        self.move_without_draw(starting_x, starting_y)
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.forward(self.scale // 2)
        self.move_without_draw(starting_x, starting_y + (self.scale // 2))
        self.forward(self.scale // 3)
    
    def F(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.forward(self.scale // 2)
        self.move_without_draw(starting_x, starting_y + (self.scale // 2))
        self.forward(self.scale // 3)
    
    def G(self):
        pass
    
    def H(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.move_without_draw(starting_x, starting_y + self.scale // 2)
        self.right(90)
        self.forward(self.scale // 2)
        self.move_without_draw(starting_x + self.scale // 2, starting_y)
        self.left(90)
        self.forward(self.scale)
    
    def I(self):
        self.forward(self.scale / 2)
        self.back(self.scale / 4)
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale / 4)
        self.left(180)
        self.forward(self.scale / 2)
    
    def J(self):
        pass
    
    def K(self):
        self.left(90)
        self.forward(self.scale)
        self.back(self.scale / 2)
        self.right(45)
        self.forward(self.scale * .70)
        self.back(self.scale * .70)
        self.right(90)
        self.forward(self.scale * .70)
    
    def L(self):
        self.forward(self.scale / 1.5)
        self.back(self.scale / 1.5)
        self.left(90)
        self.forward(self.scale)
        pass
    
    def M(self):
        pass
    
    def N(self):
        pass
    
    def O(self):
        pass
    
    def P(self):
        pass
    
    def Q(self):
        pass
    
    def R(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale // 4, 180)
        self.left(135)
        self.forward(self.scale * 0.7)
    
    def S(self):
        pass

    def T(self):
        self.move_without_draw(self.xcor() + self.scale / 2, self.ycor())
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale / 2)
        self.back(self.scale)
    
    def U(self):
        pass
    
    def V(self):
        starting_x, starting_y = self.pos()
        self.move_without_draw(starting_x, starting_y + self.scale)
        self.right(60)
        self.forward(self.scale)
        self.left(120)
        self.forward(self.scale)
    
    def W(self):
        pass
    
    def X(self):
        starting_x, _ = self.pos()
        self.left(60)
        self.forward(self.scale)
        self.move_without_draw(starting_x, self.ycor())
        self.right(120)
        self.forward(self.scale)
    
    def Y(self):
        pass
    
    def Z(self):
        pass