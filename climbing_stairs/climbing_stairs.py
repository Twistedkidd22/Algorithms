#!/usr/bin/python

import sys

def climbing_stairs(n, cache = []):
    def climb(n, step, move):
        step += move
        if step == n:
            return 1
        elif step > n:
            return 0
        else:
            return climb(n, step, 1) + climb(n, step, 2) + climb(n, step, 3)
    return climb(n, 0, 0)





if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
