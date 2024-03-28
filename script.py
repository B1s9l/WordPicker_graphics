import random
import string
import os
import time

### Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

### Pick n random words from list
def pick_words(file_path, n):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
            # Remove newline characters from the end of each word
            words = [word.strip() for word in words]
            
            if n > len(words):
                print("Error: Not enough words in the file.")
                return []
            
            # Pick n random words
            chosen_words = random.sample(words, n)
            return chosen_words
    except FileNotFoundError:
        print("Error: File not found.")
        return []


file_path = 'wordlist.txt'  # Change this to the path of your text file
n = 20   # Change this to the number of words you want to pick

x = n

picked_words = pick_words(file_path, x)
    
### Print random character grid

n = n*2
def generate_random_grid(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    grid = [[random.choice(characters) for _ in range(n*2)] for _ in range(n+1)]
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

for i in range(n//2):
    clear_console()
    random_grid = generate_random_grid(n)
    print_grid(random_grid)
    time.sleep(0.05)

### Insert words into grid

clear_console()

cur_line = 1
for word in picked_words:
    play = 2*(n - len(word))
    cur_letter = random.randint(1,play)
    for letter in word:
        random_grid[cur_line][cur_letter] = f"\033[31m{letter}\033[0m"
        cur_letter += 1
    cur_line += 2


print_grid(random_grid)

    
