from board import Board


if __name__ == "__main__":
    to_exit = False

    while not to_exit:
        print("What 'n' would you like to use?")
        a = input("\n> ")

        b = Board(int(a))

        c = input("\n> ")
        if (c == 'y') or (c == 'Y'):
            del b
        else:
            break