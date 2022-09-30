import random
class Hilo:
    ''' Setting up the Hilo Game'''

    def __init__(self):
        '''New constuction of hilo game'''
        self.points = 300
        self.value = 0
        self.card = random.randint(1,13)

    def draw(self):
        '''Drawing cards'''
        self.value = random.randint(1, 13)
        
    

    


