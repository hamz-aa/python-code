from random import randrange


def display_board(board):
    for i in range(3):
        print("+-------+-------+-------+\n"
              "|       |       |       |\n",
              "|   ", board[i][0], "   |   ", board[i][1], "   |   ", board[i][2], "   |\n",
              "|       |       |       |\n", sep="", end="")
    print("+-------+-------+-------+\n", sep="", end="")
    print()


def enter_move(board):
    flag = False
    while not flag:
        move = int(input("Enter you move : "))
        if 0 < move < 10:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = "0"
                        flag = True
                        return board
        if not flag:
            print("Invalid Move...\nTry Again!")


def make_list_of_free_fields(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "0" and board[i][j] != "X":
                tup = (i, j)
                free_squares.append(tup)
    return free_squares


def victory_for(board, sign):
    for i in range(3):
        victory = 0
        for j in range(3):
            if board[i][j] == sign:
                victory += 1
                if victory == 3:
                    return True

    for i in range(3):
        victory = 0
        for j in range(3):
            if board[j][i] == sign:
                victory += 1
                if victory == 3:
                    return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


def draw_move(board):
    board_num = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    global m
    if m == 1:
        board[1][1] = "X"
        m = 0
        return board
    while True:
        c = randrange(1, 10)
        val = board_num[c]
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            return board
        for i in range(len(free_fields)):
            if free_fields[i] == val:
                board[val[0]][val[1]] = "X"
                return board


m = 1
board = [[0 for i in range(3)] for j in range(3)]
count = 1
for i in range(3):
    for j in range(3):
        board[i][j] = count
        count += 1

print("\n\tWelcome to TicTacToe\n\tCreated By Hamza Ahmed\n\nGame Board")
display_board(board)
input("Press any key to start the game...")
while True:
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        print("Game Over...")
        break
    board = draw_move(board)
    print("Computer's Turn")
    display_board(board)
    board_status = victory_for(board, "X")
    free_fields = make_list_of_free_fields(board)
    if board_status:
        print("Computer Wins!")
        break
    if not board_status and not free_fields:
        print("Draw...")
        break
    print("Your Turn")
    board = enter_move(board)
    display_board(board)
    board_status = victory_for(board, "0")
    free_fields = make_list_of_free_fields(board)
    if board_status:
        print("You Win!")
        break
    if not board_status and not free_fields:
        print("Draw...")
        break

