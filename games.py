# Simple chess game in console without external libraries

def create_board():
    # 8x8 chess board with pieces as initials (uppercase = white, lowercase = black)
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p"] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        ["P"] * 8,
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    return board

def print_board(board):
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(8 - i, end=" ")
        for piece in row:
            print(piece, end=" ")
        print(8 - i)
    print("  a b c d e f g h")

def position_to_index(pos):
    file = ord(pos[0]) - ord("a")
    rank = 8 - int(pos[1])
    return rank, file

def is_valid_position(pos):
    return (
        len(pos) == 2 and
        pos[0] in "abcdefgh" and
        pos[1] in "12345678"
    )

def move_piece(board, start, end):
    sr, sf = position_to_index(start)
    er, ef = position_to_index(end)
    piece = board[sr][sf]

    if piece == " ":
        print("No piece at start position.")
        return False

    if not (0 <= er < 8 and 0 <= ef < 8):
        print("Invalid move: out of bounds.")
        return False

    board[er][ef] = piece
    board[sr][sf] = " "
    return True

def main():
    board = create_board()
    turn = "white"

    while True:
        print_board(board)
        print(f"{turn.capitalize()}'s move")
        move = input("Enter move (e.g., e2 e4 or 'quit'): ").strip()

        if move.lower() == "quit":
            print("Game over.")
            break

        try:
            start, end = move.split()
            if not (is_valid_position(start) and is_valid_position(end)):
                raise ValueError

            sr, sf = position_to_index(start)
            piece = board[sr][sf]

            if (turn == "white" and not piece.isupper()) or (turn == "black" and not piece.islower()):
                print("Not your piece.")
                continue

            if move_piece(board, start, end):
                turn = "black" if turn == "white" else "white"
        except ValueError:
            print("Invalid input format. Use 'e2 e4'.")
            continue

if __name__ == "__main__":
    main()
