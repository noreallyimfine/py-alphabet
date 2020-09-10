from .alphabet import Alphabet

'''
Use self module to draw all lower case letters in alphabet

'''
class Lower(Alphabet):
    '''
    Use this class to draw lowercase letters.

    OPTIONAL ARGS: 
    '''
    def __init__(self, scale=100, pointer_on=False, *args, **kwargs):
        super().__init__(scale, pointer_on, *args, **kwargs)