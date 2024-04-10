import random


class TestRandomGenerator:
    def __init__(self, initial_seed=42): 
        self.seed = initial_seed

    def next(self):
        # Use the current seed to generate a choice
        random.seed(self.seed)
        choice = random.choice(["left", "right"])
        # Update the seed in a predictable manner
        self.seed += 1  # Increment the seed to change the random sequence next time
        return choice
