# --------------------------
# Author: Tuan Nguyen
# Date created: 20191104
#!175.py
# --------------------------
"""
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. 
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

import random


def markov_chain(transitions, start, num_steps):
    """Run the Markov chain starting from start for num_steps
    and compute the number of times we visited each state."""

    cur = start  # initialize current state at start

    # initialize {state_name: visit_time}
    visit = {tran[0]: 0 for tran in transitions}

    # create the next-state dictionary:
    # for each item, key=current state, value=dict of {next state: cdf}
    chain = {}
    for tran in transitions:
        cur_state, next_state, prob = tran[0], tran[1], tran[2]
        if cur_state not in chain.keys():
            chain[cur_state] = {next_state: prob}
        else:
            prev_prob = list(chain[cur_state].values())[-1]
            chain[cur_state][next_state] = prob + prev_prob

    # run the markov chain for num_steps
    for i in range(num_steps):
        random_prob = random.random()
        for nxt, cdf in chain[cur].items():
            if random_prob < cdf:  # jump to next state if valid
                cur = nxt
                visit[nxt] += 1  # increment visit at next state
                break

    return visit


def markovChain_test():
    print(
        markov_chain(
            transitions=[
                ("a", "a", 0.9),
                ("a", "b", 0.075),
                ("a", "c", 0.025),
                ("b", "a", 0.15),
                ("b", "b", 0.8),
                ("b", "c", 0.05),
                ("c", "a", 0.25),
                ("c", "b", 0.25),
                ("c", "c", 0.5),
            ],
            start="a",
            num_steps=5000,
        )
    )


if __name__ == "__main__":
    markovChain_test()
