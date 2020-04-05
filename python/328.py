# --------------------------
# Author: Tuan Nguyen
# Date created: 20200405
#!328.py
# --------------------------
"""
In chess, the Elo rating system is used to calculate player strengths based on game results.

A simplified description of the Elo system is as follows. 
Every player begins at the same score. 
For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is.
For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.

Implement this system.
"""
class EloRatingSystem:
    """ the Elo rating system is used to calculate player strengths based on game results """
    def __init__(self, initial_rating=1000, exchange_rate=0.05):
        self.ratings = dict()
        self.initial_rating = initial_rating
        self.exchange_rate = exchange_rate  # the rate of difference point to transfer from loser to winner
    
    def get_rating(self, p):
        """ return the current rating of player p """
        if p not in self.ratings.keys():
            raise ValueError("Player not exist")
        return self.ratings[p]

    def add_player(self, p):
        """ add new player p with initial score into ratings """
        if p in self.ratings.keys():
            raise ValueError("Player exists!")
        self.ratings[p] = self.initial_rating
    
    def match_result(self, p1, p2, winner):
        """ update new ratings for 2 players p1 & p2 """
        if winner != p1 and winner != p2:
            raise ValueError("Invalid winner")
        if p1 not in self.ratings.keys():
            self.add_player(p1)
        if p2 not in self.ratings.keys():
            self.add_player(p2)
        # update new ratings
        diff = abs(self.ratings[p1] - self.ratings[p2])
        loser = p2 if winner == p1 else p1
        self.ratings[winner] += self._transfer_score(diff)  # winner plus 
        self.ratings[loser] -= self._transfer_score(diff)  # loser minus

    def _transfer_score(self, difference):
        """ return the amount of point to transfer """
        if difference != 0:
            return difference * self.exchange_rate
        else:  # 2 players have the same rating
            return 1

def test():
    elo_system = EloRatingSystem()
    elo_system.add_player("a")
    elo_system.add_player("b")
    assert elo_system.get_rating("a") == elo_system.get_rating("b")
    assert elo_system.get_rating("a") == 1000
    elo_system.match_result(p1="a", p2="b", winner="a")
    assert elo_system.get_rating("a") > elo_system.get_rating("b")
    assert elo_system.get_rating("a") == 1001

if __name__ == "__main__":
    test()