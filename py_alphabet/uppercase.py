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
    def __init__(self, scale=100, pointer_on=False, *args, **kwargs):
        super().__init__(scale, pointer_on, *args, **kwargs)


    def A(self):
        _, starting_y = self.pos()
        self.left(75)
        self.forward(self.scale)
        self.right(150)
        self.forward(self.scale)
        max_x, _ = self.pos()
        self.left(180)
        self.forward(self.scale * .45)
        self.left(75)
        self.forward(30)
        self._set_next_letter_start(max_x, starting_y)
    
    def B(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-(self.scale * .25), 180)
        self.left(180)
        self.circle(-(self.scale * .25), 180)
        x, y = self.pos()
        max_x = x + (self.scale * .25)
        self._set_next_letter_start(max_x, y)
    
    def C(self):
        pass
    
    def D(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale * .5, 180)
        x, y = self.pos()
        max_x = x + (self.scale * .5)
        self._set_next_letter_start(max_x, y)
    
    def E(self):
        starting_x, starting_y = self.pos()
        self.forward(self.scale * .5)
        self.move_without_draw(starting_x, starting_y)
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.forward(self.scale * .5)
        self.move_without_draw(starting_x, starting_y + (self.scale * .5))
        self.forward(self.scale / 3)
        max_x = starting_x + (self.scale * .5)
        self._set_next_letter_start(max_x, starting_y)
    
    def F(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.forward(self.scale * .5)
        self.move_without_draw(starting_x, starting_y + (self.scale * .5))
        self.forward(self.scale * .33)
        max_x = starting_x + (self.scale * .5)
        self._set_next_letter_start(max_x, starting_y)
    
    def G(self):
        pass
    
    def H(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.move_without_draw(starting_x, starting_y + self.scale * .5)
        self.right(90)
        self.forward(self.scale * .5)
        self.move_without_draw(starting_x + self.scale * .5, starting_y)
        self.left(90)
        self.forward(self.scale)
        max_x, _ = self.pos()
        self._set_next_letter_start(max_x, starting_y)
    
    def I(self):
        starting_x, starting_y = self.pos()
        self.forward(self.scale * .5)
        self.back(self.scale * .25)
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale * .25)
        self.left(180)
        self.forward(self.scale * .5)
        max_x = starting_x + (self.scale * .5)
        self._set_next_letter_start(max_x, starting_y)
    
    def J(self):
        pass
    
    def K(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.back(self.scale * .5)
        self.right(45)
        self.forward(self.scale * .7)
        self.back(self.scale * .7)
        self.right(90)
        self.forward(self.scale * .7)
        max_x = starting_x + (self.scale * .7)
        self._set_next_letter_start(max_x, starting_y)
    
    def L(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.move_without_draw(starting_x, starting_y)
        self.right(90)
        self.forward(self.scale * .66)
        max_x = self.xcor() 
        self._set_next_letter_start(max_x, starting_y)
    
    def M(self):
        _, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(170)
        self.forward(self.scale)
        self.left(160)
        self.forward(self.scale)
        self.right(170)
        self.forward(self.scale)
        max_x = self.xcor()
        self._set_next_letter_start(max_x, starting_y)
    
    def N(self):
        _, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(170)
        self.forward(self.scale)
        self.left(170)
        self.forward(self.scale)
        max_x = self.xcor()
        self._set_next_letter_start(max_x, starting_y)
    
    def O(self):
        starting_x, starting_y = self.pos()
        self.move_without_draw(starting_x + self.scale / 2, starting_y + self.scale / 2)
        self.circle(self.scale / 2)
        max_x = starting_x + self.scale
        self._set_next_letter_start(max_x, starting_y)
    
    def P(self):
        pass
    
    def Q(self):
        pass
    
    def R(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale * .25, 180)
        self.left(135)
        self.forward(self.scale * 0.7)
        max_x = starting_x + (self.scale * .35)
        self._set_next_letter_start(max_x, starting_y)
    
    def S(self):
        pass

    def T(self):
        starting_x, starting_y = self.pos()
        self.move_without_draw(starting_x + (self.scale * .5), starting_y)
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale * .5)
        self.back(self.scale)
        max_x = starting_x + self.scale
        self._set_next_letter_start(max_x, starting_y)
    
    def U(self):
        pass
    
    def V(self):
        starting_x, starting_y = self.pos()
        self.move_without_draw(starting_x, starting_y + self.scale)
        self.right(60)
        self.forward(self.scale)
        self.left(120)
        self.forward(self.scale)
        max_x = starting_x + (self.scale * .6)
        self._set_next_letter_start(max_x, starting_y)
    
    def W(self):
        pass
    
    def X(self):
        starting_x, starting_y = self.pos()
        self.left(60)
        self.forward(self.scale)
        self.move_without_draw(starting_x, self.ycor())
        self.right(120)
        self.forward(self.scale)
        max_x = starting_x + (self.scale * .6)
        self._set_next_letter_start(max_x, starting_y)
    
    def Y(self):
        pass
    
    def Z(self):
        self.move_without_draw(self.xcor() + self.scale, self.ycor())
        self.forward(self.scale * .6)
        self.right(135)
        self.forward(self.scale)
        self.left(135)
        self.forward(self.scale * .6)
        max_x, y = self.pos()
        self._set_next_letter_start(max_x, y)