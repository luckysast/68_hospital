import time

class NotSoRandom(object):
    def __init__(self,seed=42):
        self.seed = seed

    def random_shift(self):
        timestamp = int(round(time.time() * 1000))
        shift = str(timestamp)[-2:]
        if shift[0:1] == '0':
            shift = shift[1:2]
        return int(shift)



