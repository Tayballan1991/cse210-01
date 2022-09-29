import random
class Die:
    ''' Die is a small cube with dots to simbolize numbers 1 dot 
    for the nubmer one and so on.
    The point of the game is to add up the number on all 5 dice that 
    is facing up.
    '''
    def __init__(self):
        '''New constuction of Die.'''
        self.value = 0
        self.points = 0
    
    def roll(self):
        '''Each roll should give new numbers on the die and calculate
        the total'''
        self.value = random.randit(1, 6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0