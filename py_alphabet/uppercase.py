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
        self.left(75)
        self.forward(self.scale)
        self.right(150)
        self.forward(self.scale)
        self.left(180)
        self.forward(self.scale * .45)
        self.left(75)
        self.forward(30)
        self._set_next_letter_start()
    
    def B(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-25, 180)
        self.left(180)
        self.circle(-25, 180)
        self._set_next_letter_start()
    
    def C(self):
        self._set_next_letter_start()
        pass
    
    def D(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale // 2, 180)
        self._set_next_letter_start()
    
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
        self._set_next_letter_start()
    
    def F(self):
        starting_x, starting_y = self.pos()
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.forward(self.scale // 2)
        self.move_without_draw(starting_x, starting_y + (self.scale // 2))
        self.forward(self.scale // 3)
        self._set_next_letter_start()
    
    def G(self):
        self._set_next_letter_start()
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
        self._set_next_letter_start()
    
    def I(self):
        self.forward(self.scale / 2)
        self.back(self.scale / 4)
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale / 4)
        self.left(180)
        self.forward(self.scale / 2)
        self._set_next_letter_start()
    
    def J(self):
        self._set_next_letter_start()
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
        self._set_next_letter_start()
    
    def L(self):
        self.forward(self.scale / 1.5)
        self.back(self.scale / 1.5)
        self.left(90)
        self.forward(self.scale)
        self._set_next_letter_start()
        pass
    
    def M(self):
        self._set_next_letter_start()
        pass
    
    def N(self):
        self._set_next_letter_start()
        pass
    
    def O(self):
        self._set_next_letter_start()
        pass
    
    def P(self):
        self._set_next_letter_start()
        pass
    
    def Q(self):
        self._set_next_letter_start()
        pass
    
    def R(self):
        self.left(90)
        self.forward(self.scale)
        self.right(90)
        self.circle(-self.scale // 4, 180)
        self.left(135)
        self.forward(self.scale * 0.7)
        self._set_next_letter_start()
    
    def S(self):
        self._set_next_letter_start()
        pass

    def T(self):
        self.move_without_draw(self.xcor() + self.scale / 2, self.ycor())
        self.left(90)
        self.forward(self.scale)
        self.left(90)
        self.forward(self.scale / 2)
        self.back(self.scale)
        self._set_next_letter_start()
    
    def U(self):
        self._set_next_letter_start()
        pass
    
    def V(self):
        starting_x, starting_y = self.pos()
        self.move_without_draw(starting_x, starting_y + self.scale)
        self.right(60)
        self.forward(self.scale)
        self.left(120)
        self.forward(self.scale)
        self._set_next_letter_start()
    
    def W(self):
        self._set_next_letter_start()
        pass
    
    def X(self):
        starting_x, _ = self.pos()
        self.left(60)
        self.forward(self.scale)
        self.move_without_draw(starting_x, self.ycor())
        self.right(120)
        self.forward(self.scale)
        self._set_next_letter_start()
    
    def Y(self):
        self._set_next_letter_start()
        pass
    
    def Z(self):
        self._set_next_letter_start()
        pass