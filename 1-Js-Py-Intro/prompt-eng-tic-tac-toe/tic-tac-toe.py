import random 


def tic_tac_toe():
    board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    empty_space = ' '
    while empty_space in board[0] or board[1] or board[2]:
        print(board[0])
        print(board[1])
        print(board[2])  
        raw_row = int(input("Enter Row 1, 2, or 3: "))
        raw_column = int(input("Enter Column 1, 2, or 3: "))
        row = raw_row-1
        column = raw_column-1
        if not row in [0,1,2] and column not in [0,1,2]:
            print("That is an invalid guess, Try again!!")
            row = int(input("Enter Row 0, 1, or 2: "))
            column = int(input("Enter Column 0, 1, or 2: ")) 
        elif board[row][column] != ' ':
            print("That space is already taken, Try another square!!")
            row = int(input("Enter Row 0, 1, or 2: "))
            column = int(input("Enter Column 0, 1, or 2: "))
        else:
            board[row][column] = "X"

        winning_line = (board[0], board[1], board[2])
        if board[0][0] == board[0][1] == board[0][2] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[1][0] == board[1][1] == board[1][2] != ' ':
            return f"{board[1][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[2][0] == board[2][1] == board[2][2] != ' ':
            return f"{board[2][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][0] == board[1][0] == board[2][0] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][1] == board[1][1] == board[2][1] != ' ':
            return f"{board[1][1]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][2] == board[1][2] == board[2][2] != ' ':
            return f"{board[2][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][0] == board[1][1] == board[2][2] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][2] == board[1][1] == board[2][0] != ' ':
            return f"{board[0][2]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
    

        print("The Computer Chose")
        while empty_space in board[0] or board[1] or board[2]:
            comp_row = random.choice([0, 1, 2])
            comp_column = random.choice([0, 1, 2])
            if board[comp_row][comp_column] == ' ':
                board[comp_row][comp_column] = "O" 
                break

        
        if board[0][0] == board[0][1] == board[0][2] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[1][0] == board[1][1] == board[1][2] != ' ':
            return f"{board[1][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[2][0] == board[2][1] == board[2][2] != ' ':
            return f"{board[2][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][0] == board[1][0] == board[2][0] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][1] == board[1][1] == board[2][1] != ' ':
            return f"{board[1][1]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][2] == board[1][2] == board[2][2] != ' ':
            return f"{board[2][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][0] == board[1][1] == board[2][2] != ' ':
            return f"{board[0][0]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
        elif board[0][2] == board[1][1] == board[2][0] != ' ':
            return f"{board[0][2]} Wins!\n{winning_line[0]}\n{winning_line[1]}\n{winning_line[2]}"
    
    return "Its a Scratch! A tie in Tic Tac Toe is called a scratch, as in cat's scratch. Considering that a game will have no winner if played perfectly is a bit like playing with a cat. When both players are at a stalemate, the cat usually signals its finish with a quick scratch."
        
print(tic_tac_toe())
 
