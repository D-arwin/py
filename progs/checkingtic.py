"""Def a function that takes the board(list of lists)
Def check_win that takes in lines
    if all the elements of the row are the same AND they're not
    0 return winner
Build lists for each column
use check-win 

Build lists for each diagonal 
use check win

Iterate over the main list looking for empty spaces
    """
board = [[0,0,2],
         [0,0,0],
         [1,0,1]]
new_list = []
winner = 0
for element in board:
    new_list.extend(element)

if new_list[0] == new_list[1] == new_list[2]:
    winner = new_list[0]
    if winner != 0:
        print('The winner is', winner)
elif new_list[4] == new_list[5] == new_list[6]:
    winner = new_list[4]
    if winner != 0:
        print('The winner is', winner)
elif new_list[6] == new_list[7] == new_list[8]:
    winner = new_list[7]
    if winner != 0:
        print('The winner is', winner)
elif new_list[0] == new_list[3] == new_list[6]:
    winner = new_list[0]
    if winner != 0:
        print('The winner is', winner)
elif new_list[1] == new_list[4] == new_list[7]:
    winner = new_list[1]
    if winner != 0:
        print('The winner is', winner)
elif new_list[2] == new_list[5] == new_list[8]:
    winner = new_list[2]
    if winner != 0:
        print('The winner is', winner)
elif new_list[0] == new_list[4] == new_list[8]:
    winner = new_list[0]
    if winner != 0:
        print('The winner is', winner)
elif new_list[2] == new_list[4] == new_list[6]:
    winner = new_list[2]
    if winner != 0:
        print('The winner is', winner)
else:
    for row in board:
        for element in row:
            if element == 0:
                print('The game is not finished yet')
    print('It\'s a cat\'s game')