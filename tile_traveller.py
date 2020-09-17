#First write a function that is simple, for example only returns the new position on the board, the rest
#will be done outside of functions. A loop will be used that prints out the positions on the board based on
#where the function tells the user he is positioned on the board. If and else statements will be used to decide
#whether or not no run the function or tell the user he chose an invalid direction.


N = '(N)orth'
E = '(E)ast'
S = '(S)outh'
W = '(W)est'

x_position, y_position = 1,1 #first position
available_moves = ('')
direction = ''

#I write a program that takes in the previous position, current direction and returns new position

def new_position(x_position, y_position, direction):
    
#I work with the positions (numbers) on the board
#I use variable.lower to make the program case insensitive

    if direction.lower() == 'n': #if 'n'/'N' user moves up one tile, x axis stays the same
        return x_position, y_position + 1 #function returns new position on the board
    elif direction.lower() == 'e': #if 'e'/'E' user moves one tile to the right, y stays the same
        return x_position + 1, y_position 
    elif direction.lower() == 's': #if south I move down one tile, x axis stays the same...
        return x_position, y_position - 1
    elif direction.lower() == 'w':
        return x_position - 1, y_position

while True:  #runs while move is acceptable, otherwise it prints 'not a valid direction'
    if direction.lower() in available_moves:
        if ((x_position == 1) and (y_position == 1)) or ((x_position == 2) and (y_position == 1)):
            print('You can travel: (N)orth.') #The tiles the only direction you can travel north are 1,1 + 2,1
            available_moves = ('n') #Prints out the next moves available
        if (x_position == 1) and (y_position == 2):#Works for tile 1,2
            print('You can travel: (N)orth or (E)ast or (S)outh.') 
            available_moves = ('n', 'e', 's') 
        if (x_position == 1) and (y_position == 3):#1,3
            print('You can travel: (E)ast or (S)outh.')
            available_moves = ('e', 's') 
        if ((x_position == 2) and (y_position == 2)) or ((x_position == 3) and (y_position == 3)):#2,2 + 3,3
            print('You can travel: (S)outh or (W)est.')
            available_moves = ('s', 'w') 
        if (x_position == 2) and (y_position == 3): #2,3
            print('You can travel: (E)ast or (W)est.')
            available_moves = ('e', 'w') 
        if (x_position == 3) and (y_position == 2):
            print('You can travel: (N)orth or (S)outh.')
            available_moves = ('n', 's') 
        if x_position == 3 and y_position == 1:#if position 3,1, then victory
            print ('Victory!')
            exit() #stop running program
 #all moves accounted for
            
    direction = str(input('Direction: ')) 
    if direction.lower() in available_moves: #ef direction er available fer forritið í gegn um fallið new_position
        x_position, y_position = new_position(x_position, y_position, direction)
        #The function takes in x and y position as well as direction, returns new position
    else: #If not an available move the program prints out 'Not a valid direction' and returns to the previous position
        print ('Not a valid direction!')
