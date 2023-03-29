'''
this module has 4 class definitions:
    Player, Minplayer, Middleplayer, Learning player that represent four types of players for the number guessing game
'''
import random

class Player:
    '''
    this class represents players who randomly selects number from the range
    '''
    def __init__(self):
        '''
        Create instance variables keeping track of the range of possible integers, the number of guesses, etc

        Returns
        -------
        None.

        '''
        self._lowerbound = 1
        self._upperbound = 100
        self._guess = 0
        self._count = 0
        self._games = []

    def guess(self):
        '''
        choose x randomly from the possible range

        Returns
        -------
        int
            a random guess of number

        '''
        self._guess = random.randint(self._lowerbound,self._upperbound)    
        return self._guess
    
    def outcome(self, str):
        '''
        get the outcome of the guess

        Parameters
        ----------
        str : str
            whether the guess is high, low or correct

        Returns
        -------
        None.

        '''
        self._count += 1
        if str == 'too low':
            self._lowerbound = self._guess + 1
        elif str == 'too high':
            self._upperbound = self._guess - 1
        elif str == 'correct':
            self._games.append(self._count)
            self._lowerbound = 1
            self._upperbound = 100
            self._count = 0

    def record(self, n):
        '''
        provide the number of guesses made for the last n games played

        Parameters
        ----------
        n : int
            last n games played

        Returns
        -------
        list
            number of guesses made for the last n games

        '''
        return self._games[-n:]
    
class MinPlayer:
    '''
    this class represents players who choose the smallest integer from the possible range
    '''
    def __init__(self):
        '''
        Create instance variables keeping track of the range of possible integers, the number of guesses, etc

        Returns
        -------
        None.

        '''
        self._lowerbound = 1
        self._upperbound = 100
        self._count = 0
        self._games = []
    
    def guess(self):
        '''
        choose the smallest integer from the possible range

        Returns
        -------
        int
            smallest number

        '''
        return self._lowerbound
    
    def outcome(self, str):
        '''
        get the outcome of the guess

        Parameters
        ----------
        str : str
            whether the guess is high, low or correct

        Returns
        -------
        None.

        '''
        self._count += 1
        if str == 'too low':
            self._lowerbound += 1
        elif str == 'correct':
            self._games.append(self._count)
            self._lowerbound = 1
            self._upperbound = 100
            self._count = 0
        
    def record(self,n):
        '''
        provide the number of guesses made for the last n games played

        Parameters
        ----------
        n : int
            last n games played

        Returns
        -------
        list
            number of guesses made for the last n games

        '''
        return self._games[-n:]
    
class MiddlePlayer:
    '''
    this class represents players who choose the middle integer from the possible range
    '''
    def __init__(self):
        '''
        Create instance variables keeping track of the range of possible integers, the number of guesses, etc

        Returns
        -------
        None.

        '''
        self._lowerbound = 1
        self._upperbound = 100
        self._count = 0
        self._guess = 0
        self._games = []
        
    def guess(self):
        '''
        choose the middle number of the possible range

        Returns
        -------
        int
            middle number

        '''
        self._guess = int((self._lowerbound + self._upperbound)/2)
        return self._guess
    
    def outcome(self, str):
        '''
        get the outcome of the guess

        Parameters
        ----------
        str : str
            whether the guess is high, low or correct

        Returns
        -------
        None.

        '''
        self._count += 1
        if str == 'too low':
            self._lowerbound = self._guess + 1
        elif str == 'too high':
            self._upperbound = self._guess - 1
        elif str == 'correct':
            self._games.append(self._count)
            self._lowerbound = 1
            self._upperbound = 100
            self._count = 0
            
    def record(self,n):
        '''
        provide the number of guesses made for the last n games played

        Parameters
        ----------
        n : int
            last n games played

        Returns
        -------
        list
            number of guesses made for the last n games

        '''
        return self._games[-n:]

class LearningPlayer:
    '''
    this class represents players inspired by reinforcement learning
    '''
    def __init__(self):
        '''
        Create instance variables keeping track of the range of possible integers, the number of guesses, etc

        Returns
        -------
        None.

        '''
        self._lowerbound = 1
        self._upperbound = 100
        self._count = 0
        self._guess = 0
        self._games = []
        self._update = {}
        self._estimated_num_guesses = {}
        for i in range(1,101):
            for j in range(1,101):
                self._estimated_num_guesses[(i,j)] = {}
                for k in range (i,j+1):
                    self._estimated_num_guesses[(i,j)][k] = max(j-k+1, k-i+1)
                    
    def guess(self):
        '''
        choose the random number from the possible range based on probability in estimate_num_guesses

        Returns
        -------
        int
            random number based on probability

        '''
        choice = list(self._estimated_num_guesses[(self._lowerbound,self._upperbound)].keys())
        num_guesses = list(self._estimated_num_guesses[(self._lowerbound,self._upperbound)].values())
        chance = [1 / x**5 for x in num_guesses]
        guess = random.choices(choice, weights=(chance))
        self._guess = guess[0] # get the num in the list since random.choice return a list
        return self._guess
         
    def outcome(self, str):
        '''
        get the outcome of the guess and update the estimate_num_guesses

        Parameters
        ----------
        str : str
            whether the guess is high, low or correct

        Returns
        -------
        None.

        '''
        self._count += 1
        if str == 'too low':
            self._update[(self._lowerbound,self._upperbound)] = [self._guess]
            self._lowerbound = self._guess + 1
        elif str == 'too high':
            self._update[(self._lowerbound,self._upperbound)] = [self._guess]
            self._upperbound = self._guess - 1
        elif str == 'correct':
            self._games.append(self._count)
            self._update[(self._lowerbound,self._upperbound)] = [self._guess]
            for values in self._update.values(): # add additional guesses to each choice
                values.append(self._count)
                self._count -= 1
            for bound,values in self._update.items():
                n = self._estimated_num_guesses[bound][values[0]]
                self._estimated_num_guesses[bound][values[0]] = 0.8 * n + 0.2 * values[1]
            assert self._count == 0
            self._lowerbound = 1
            self._upperbound = 100
            self._update = {}
            
    def record(self,n):
        '''
        provide the number of guesses made for the last n games played

        Parameters
        ----------
        n : int
            last n games played

        Returns
        -------
        list
            number of guesses made for the last n games

        '''
        return self._games[-n:]
            
            
        
                
        
            