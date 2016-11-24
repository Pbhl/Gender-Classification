import random

from collections import defaultdict
from sys import argv

WORD_SEP = ' '

class MarkovName:
  def __init__(self, input_file):
    """ input file should have one name per line"""
    markov_file = open(input_file, 'r')
    # markov chain is a dictionary from {(letter) to list-of-letters-seen-after}
    # {c: 'aaoehhhhh   '}
    self.chain = defaultdict(list)
    names = (line for line in markov_file if not line[0] == '#')
    for name in names:
      # Alice
      proper_name = name.lower().strip()
      # alice
      pairs = zip(proper_name, proper_name[1:],proper_name[2:],proper_name[3:])
      #pairs = [(a, l, i), (l, i, c), (i, c, e)]
      for first, second, third, fourth in pairs:
          self.chain[first+second].append(third+fourth)
      # +1 for e as last character
      self.chain[proper_name[-2]+proper_name[-1]].append(WORD_SEP)
      # +1 for a as first character
      self.chain[WORD_SEP].append(proper_name[0]+proper_name[1])

  def generate_name(self):
    name = []
    current = WORD_SEP  # used to mark both first and last character
    while not (current == WORD_SEP and name):
      current = random.choice(self.chain[current])
      name.append(current)

    return ''.join(name).strip().capitalize()
    
gen=MarkovName('namelist.txt')
for i in range(1000):
    print(gen.generate_name())