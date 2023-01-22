import itertools
import random

class RandomRangeGenerator:
    def __init__(self):
        self.previous_num = 0
    
    def get_random_range(self, n):
        # Generate n random ranges
        ranges = []
        for i in range(n):
            # Generate a random number between 1 and 100
            new_num = random.randint(1, 100)

            # Generate a random step size between 1 and 5
            step_size = random.randint(1, 5)

            # If this is the first call, return a range from 1 to the new random number
            if self.previous_num == 0:
                self.previous_num = new_num
                ranges.append(range(1, new_num+1, step_size))
            # Otherwise, return a range from the previous number to the new random number
            else:
                self.previous_num = new_num
                if self.previous_num < new_num:
                    ranges.append(range(self.previous_num, new_num+1, step_size))
                else:
                    ranges.append(range(self.previous_num, new_num-1, -1*step_size))
        
        # Combine the ranges into a single range object and return it
        return itertools.chain(*ranges)