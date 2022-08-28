game = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
def print_game(game_screen):
    print("----------")
    for char in game_screen:
        print(" | ".join(char))
        print("----------")
print_game(game)

def check_won(game_screen, string):
    if game_screen[0][0] == game_screen[0][1] == game_screen[0][2] == string:
        return True
    if game_screen[1][0] == game_screen[1][1] == game_screen[1][2] == string:
        return True
    if game_screen[2][0] == game_screen[2][1] == game_screen[2][2] == string:
        return True
    if game_screen[0][0] == game_screen[1][0] == game_screen[2][0] == string:
        return True
    if game_screen[0][1] == game_screen[1][1] == game_screen[2][1] == string:
        return True
    if game_screen[0][2] == game_screen[1][2] == game_screen[2][2] == string:
        return True
    if game_screen[0][0] == game_screen[1][1] == game_screen[2][2] == string:
        return True
    if game_screen[0][2] == game_screen[1][1] == game_screen[2][0] == string:
        return True


def check_full(game_screen):
    if game_screen[0][0] == "*":
        return True
    elif game_screen[0][1] == "*":
        return True
    elif game_screen[0][1] == "*":
        return True
    elif game_screen[1][0] == "*":
        return True
    elif game_screen[1][1] == "*":
        return True
    elif game_screen[1][2] == "*":
        return True
    elif game_screen[2][0] == "*":
        return True
    elif game_screen[2][1] == "*":
        return True
    elif game_screen[2][2] == "*":
        return True
    else:
        return False
i = 1

while i == 1:
    x = 1
    while x == 1:
        print("X is  your turn:")
        X_row = int(input("in row: "))-1
        X_col = int(input("in col: "))-1
        if X_row < 0 or X_row > 2 or X_col < 0 or X_col > 2:
            print("Error!!! Try again")
        elif game[X_row][X_col] == "X" or game[X_row][X_col] == "O":
            print("its already chose Try again")
        else:
            game[X_row][X_col] = "X"
            x = 0
    print_game(game)
    if check_won(game, "X"):
        print("GAME OVER X WON")
        i = 0
        break
    if not check_full(game):
        print("A draw, no one won")
        i = 0
        break
    y = 1
    while y == 1:
        print("O is  your turn:")
        O_row = int(input("in row: "))-1
        O_col = int(input("in col: "))-1
        if O_row < 0 or O_row > 2 or O_col < 0 or O_col > 2:
            print("Error!!! Try again")
        elif game[O_row][O_col] == "X" or game[O_row][O_col] == "O":
            print("its already chosen Try again")
        else:
            game[O_row][O_col] = "O"
            y = 0
    print_game(game)
    if check_won(game, "O"):
        print("GAME OVER O WON")
        i = 0
