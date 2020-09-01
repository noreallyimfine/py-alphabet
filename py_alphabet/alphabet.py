from turtle import Turtle


class Alphabet(Turtle):
    '''
    Alphabet drawing base class. Use Upper or Lower to actually draw.
    '''
    def __init__(self, scale=100, pointer_on=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.starting_x, self.starting_y = self.pos()

        # set pointer off by default
        if not pointer_on:
            self.ht()

    def move_without_draw(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()

    def _set_next_letter_start(self):
        new_x = self.starting_x + self.scale * 1.05
        self.move_without_draw(new_x, self.starting_y)
        self.starting_x, self.starting_y = self.pos()
        self.setheading(0.0)
