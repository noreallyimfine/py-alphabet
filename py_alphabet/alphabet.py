from turtle import Turtle, Screen


class Alphabet(Turtle):
    '''
    Alphabet drawing base class. Use Upper or Lower to actually draw.
    '''
    def __init__(self, scale=100, pointer_on=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.screen = Screen()
        self._starting_x = -((self.screen.screensize()[0] * .9)) 
        self._starting_y = ((self.screen.screensize()[1] * .6))
        self.move_without_draw(self._starting_x, self._starting_y)

        # set pointer off by default
        if not pointer_on:
            self.ht()

    def move_without_draw(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()

    def _set_next_letter_start(self, max_x, y):
        new_x = max_x + abs(max_x*.05)
        self.move_without_draw(new_x, y)
        self.setheading(0.0)
