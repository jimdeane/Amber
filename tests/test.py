import random

# Function to generate a random number from -5 to 5 with a 0.01 probability
# Function to check if a 1% chance event occurs
def check_event_occurrence():
    # Check for the 1% probability event
    return random.randint(0, 99) == 0

# Example usage
#event_occurred = check_event_occurrence()



# Example usage
for i in range(100):
    event_occurred = check_event_occurrence()
    print(event_occurred)

