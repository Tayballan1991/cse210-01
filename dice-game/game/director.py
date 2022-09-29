from game.die import die

class Director:
    '''The Directos is someone who is directs the game.
    
    Dice : A list of die instances
    is_playing : wether or not the game is being played
    score(int) : The score for one round of the game.
    total_score(int) : The total score for the game. '''

    def __init__(self):
        '''Getting a new director'''
        sef.dice - []
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        
        for i in range (5):
            die = Die()
            self.dice.append(die)
    
    def start_game(self):
        '''Beginning the game with the start loop'''

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        ''' Ask the user if they are ready to roll'''
        roll_dice = input('Roll Dice [y/n]') 
        self.is_playing = (roll_dice == 'y')

    def do_updates(self):
        '''Updating the players score after each round.'''
        if not self.is_playing:
            return
        if i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
        self.total_score += self.score

    def do_outputs(self):
        '''Display the dice and score'''
        if not self.is_playing:
            return
        values = ''
        for i in range (len(self.dice)):
            die = self.dice[i]
            values += f'{die.value}'

        print(f'You rolled: {values}')
        print(f'Your score is: {self.total_score}')
        self.is_playing == (self.score > 0)