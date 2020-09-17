#https://github.com/sjofn17/TileTraveller/blob/master/tile_traveller.py
N = 'n'
E = 'e'
S = 's'
W = 'w'

def move(direction, col, row):
#Returns updated col, row given the direction
    if direction == N:
        row += 1
    elif direction == S:
        row -= 1
    elif direction == E:
        col += 1
    elif direction == W:
        col -= 1
    return(col, row)    

def is_victory(col, row):
#Return true is player is in the victory cell
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == N:
            print("(N)orth", end='')
        elif ch == E:
            print("(E)ast", end='')
        elif ch == S:
            print("(S)outh", end='')
        elif ch == W:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
#Returns valid directions as a string given the supplied location
    if col == 1 and row == 1:   # (1,1)
        valid_directions = N
    elif col == 1 and row == 2: # (1,2)
        valid_directions = N+E+S
    elif col == 1 and row == 3: # (1,3)
        valid_directions = E+S
    elif col == 2 and row == 1: # (2,1)
        valid_directions = N
    elif col == 2 and row == 2: # (2,2)
        valid_directions = S+W
    elif col == 2 and row == 3: # (2,3)
        valid_directions = E+W
    elif col == 3 and row == 2: # (3,2)
        valid_directions = N+S
    elif col == 3 and row == 3: # (3,3)
        valid_directions = S+W
    return valid_directions

def play_one_move(col, row, valid_directions):
#Plays one move of the game Return if victory has been obtained and updated col,row
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

# The main program starts here
victory = False
row = 1
col = 1

valid_directions = N
print_directions(valid_directions)

while not victory:
    victory, col, row = play_one_move(col, row, valid_directions)
    if victory:
        print("Victory!")
    else:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
