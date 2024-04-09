class Test_To_Get_Arrested_Generator:
    def __init__(self):
        self.directions = ["left"] * 19  # Simplified repetition
        self.index = 0  # Keep track of the current index

    def next(self):
        # Return the next direction based on the current index, then increment the index
        if self.index < len(self.directions):
            direction = self.directions[self.index]
            self.index += 1
            return direction
        else:
            raise StopIteration  # Or return None, or loop the index back to 0 for infinite cycling
