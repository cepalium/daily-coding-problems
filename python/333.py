# --------------------------
# Author: Tuan Nguyen
# Date created: 20200410
#!333.py
# --------------------------
"""
At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 
To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
"""
import pandas as pd 

class Party:
    def __init__(self, attendees=[]):
        self.attendees = attendees
        self.num_attendees = len(attendees)
        self.know_matrix = pd.DataFrame(False, columns=attendees, index=attendees)

    def build_acquaintance(self, a, people):
        """ set True for people that a knows """
        for somebody in people:
            self.know_matrix.at[a, somebody] = True

    def knows(self, a, b):
        """ return True if a knows b; False otherwise"""
        return self.know_matrix.at[a, b]

    def find_celebrity(self):
        """ return the celebrity in the party """
        suspected_individuals = self.attendees.copy()
        # reduce the list of suspected-as-celebrity list of attendees 
        while len(suspected_individuals) > 2:
            a = suspected_individuals.pop()
            b = suspected_individuals.pop()
            if self.knows(a, b):  # a knows b -> a cannot be the celeb
                suspected_individuals.append(b)
            else:  # a doesn't know b -> b cannot be the celeb
                suspected_individuals.append(a)
        # last 2 suspected people: who is the celeb?
        a = suspected_individuals.pop()
        b = suspected_individuals.pop()
        if self.knows(a, b):  # a knows b -> b is the celeb
            return b
        return a  # a doesn't know b -> a is the celeb

# ---- test -----
def test():
    party = Party(attendees=["alice", "bob", "charlie", "Elvis Presley"])
    party.build_acquaintance("alice", ["bob", "Elvis Presley"])
    party.build_acquaintance("bob", ["charlie", "Elvis Presley"])
    party.build_acquaintance("charlie", ["alice", "bob", "Elvis Presley"])
    assert party.find_celebrity() == "Elvis Presley"

if __name__ == "__main__":
    test()