from turtle import Turtle


class Alphabet(Turtle):
    '''
    Alphabet drawing base class. Use Upper or Lower to actually draw.
    '''
    def __init__(self, scale=100, spacing=15, pointer_on=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.spacing = spacing

        # set pointer off by default
        if not pointer_on:
            self.ht()

    def move_without_draw(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()
