print("X is Player 1")
print("O is Player 2")
print("Start with player 1")

loc = [[1, " "], [2, " "], [3, " "], [4, " "], [5, " "], [6, " "], [7, " "], [8, " "], [9, " "]]
player = "x"
pls = ["x", "o"]
draw = False


def res():
    global loc, player
    loc = [[1, " "], [2, " "], [3, " "], [4, " "], [5, " "], [6, " "], [7, " "], [8, " "], [9, " "]]
    player = "x"


def layout():
    line = ""
    for i in range(0, 9):
        if (i + 1) % 3 == 0:
            line = line + f" {loc[i][1]}"
            print(line)
            line = ""
        else:
            line = line + f" {loc[i][1]} |"


def check():
    global draw
    for i in pls:
        for j in range(0, 7, 3):
            if loc[j][1] == i:
                if loc[j + 1][1] == i:
                    if loc[j + 2][1] == i:
                        print(f"{i} wins")
                        return 1
                else:
                    break
        for j in range(0, 3):
            if loc[j][1] == i:
                if loc[j + 3][1] == i:
                    if loc[j + 6][1] == i:
                        print(f"{i} wins")
                        return 1
                else:
                    break

        if loc[0][1] == i:
            if loc[4][1] == i:
                if loc[8][1] == i:
                    print(f"{i} wins")
                    return 1
            else:
                break

        if loc[2][1] == i:
            if loc[4][1] == i:
                if loc[6][1] == i:
                    print(f"{i} wins")
                    return 1
            else:
                break

        for j in range(0, 9):
            if loc[j][1] == " ":
                draw = False
                break
            else:
                draw = True


while 1:
    layout()
    if check() == 1:
        restart = input("Restart the game y or n: ")
        if restart == 'y':
            res()
            continue
        else:
            break
    if draw:
        draw = False
        print("Its draw")
        restart = input("Restart the game y or n: ")
        if restart == 'y':
            res()
            continue
        else:
            break
    try:
        pos = int(input("Enter a box number: "))
        if pos == 0 or pos > 9:
            raise ValueError
    except ValueError:
        print("U have to enter a valid integer or enter valid box number(1-9)")
    else:
        loc[pos - 1][1] = player
        if player == "x":
            player = "o"
        else:
            player = "x"
