from w03game.hilo import Hilo
class Director:
    '''Creating a Director to control the game.'''

    def __init__(self):
        '''Creating game director'''
        self.card = []
        self.is_playing = True
        self.score = 300
        self.total_score = 300
        self.card = random.randint (1,13)



    def start_game(self):
        '''Setting up the start of the game.'''

        while self.is_playing:
            self.get_inputs()
            self.get_updates()
            self.get_outputs()

    def get_inputs(self):

        print(f'Your first card is: {self.card}')
        high_low = input('Will the next card be HIGH or LOW [h / l]?')
        if high_low == 'h':
            

