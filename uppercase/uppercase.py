import turtle

'''
Use turtle module to draw all upper case letters in alphabet

(8/31/2020): Currently assumes facing original direction (right). 
'''
class Upper:

    # set pointer off by default
    turtle.ht()


    def __init__(self, scale=100, spacing=15):
        self.scale = scale
        self.spacing = spacing

    def A(self):
        turtle.left(75)
        turtle.forward(self.scale)
        turtle.right(150)
        turtle.forward(self.scale)
        turtle.left(180)
        turtle.forward(self.scale * .45)
        turtle.left(75)
        turtle.forward(30)
    
    def B(self):
        turtle.left(90)
        turtle.forward(self.scale)
        turtle.right(90)
        turtle.circle(-25, 180)
        turtle.left(180)
        turtle.circle(-25, 180)
    
    def C(self):
        turtle.penup()
        x, y = turtle.pos()
        turtle.setpos(x + self.scale, y + (self.scale * 0.75))
        turtle.pendown()
        turtle.circle(-self.scale//2, -240)
    
    def D(self):
        pass
    
    def E(self):
        pass
    
    def F(self):
        pass
    
    def G(self):
        pass
    
    def H(self):
        pass
    
    def I(self):
        pass
    
    def J(self):
        pass
    
    def K(self):
        pass
    
    def L(self):
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
        pass
    
    def S(self):
        pass

    def T(self):
        pass
    
    def U(self):
        pass
    
    def V(self):
        pass
    
    def W(self):
        pass
    
    def X(self):
        pass
    
    def Y(self):
        pass
    
    def Z(self):
        pass