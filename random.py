import random

# List of names to choose from
names = ['John', 'Emma', 'David', 'Sophie', 'James', 'Lily', 'Tom', 'Olivia', 'Mike', 'Emily']

# Function to generate a random playing 11
def generate_playing_11():
    # Shuffle the list of names
    random.shuffle(names)
    
    # Choose the first 11 names from the shuffled list
    playing_11 = names[:11]
    
    # Print the playing 11
    print("Playing 11:")
    for i, player in enumerate(playing_11):
        print(i+1, player)

# Example usage:
generate_playing_11()
