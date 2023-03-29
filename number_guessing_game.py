'''
the module has a class definition: Num_Guessing_Game
'''
import random

class Num_Guessing_Game:
    '''
    '''
    def __init__(self,player_1,player_2,player_3,player_4):
        '''
        Create list of types of players

        Parameters
        ----------
        player_1 : Player
        player_2 : MinPlayer
        player_3 : MiddlePlayer
        player_4 : LearningPlayer

        Returns
        -------
        None.

        '''
        self._players = [player_1,player_2,player_3,player_4]
        
    def play(self):
        '''
        make each player plays the game once

        Returns
        -------
        None.

        '''
        n = random.randint(1,100)
        for player in self._players:
            str = ''
            while str != 'correct':
                g=player.guess()
                if g > n:
                    str='too high'
                elif g < n:
                    str='too low'
                elif g == n:
                    str='correct'
                player.outcome(str)
    
            
            
    
                
            
        
