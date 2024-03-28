import random
import string
import os
import time

numwords = 3   # Change this to the number of words you want to pick

file_path = "wordlist.txt"  # Change this to the path of your text file


### Clear console method
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

### Pick n random words from list
def pick_words(file_path, numwords):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
            words = [word.strip() for word in words]
            if numwords > len(words):
                print("Error: Not enough words in the file.")
                return []
            
            chosen_words = random.sample(words, numwords)
            
            return chosen_words
    except FileNotFoundError:
        print("Error: File not found.")
        return []

picked_words = pick_words(file_path, numwords)
    
### Print random character grid
gridsize = numwords*2

longestword = ""
for word in picked_words:
    if len(word) > len(longestword):
        longestword = word

if gridsize <= len(longestword):
    gridsize = len(longestword) + 2 

def generate_random_grid(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    grid = [[random.choice(characters) for _ in range(gridsize*2)] for _ in range(gridsize+1)]
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

for i in range(gridsize//2):
    clear_console()
    random_grid = generate_random_grid(gridsize)
    print_grid(random_grid)
    time.sleep(0.05)

### Insert words into grid

clear_console()

linespread = int(gridsize/numwords)

cur_line = linespread-1
for word in picked_words:
    play = 2*(gridsize - len(word))
    cur_letter = random.randint(1,play)
    for letter in word:
        random_grid[cur_line][cur_letter] = f"\033[31m{letter}\033[0m"
        cur_letter += 1
    cur_line += linespread


print_grid(random_grid)

ab = ["a", "b", "c"]
print()
    
