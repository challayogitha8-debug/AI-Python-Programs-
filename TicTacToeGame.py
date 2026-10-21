import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None
        n = len(self.board)

        # Checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break

            if win:
                return win

        # Checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break

            if win:
                return win

        # Checking first diagonal
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break

        if win:
            return win

        # Checking second diagonal
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break

        if win:
            return win

        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'

        while True:
            print(f"\nPlayer {player} turn")
            self.show_board()

            # Taking user input
            row, col = list(
                map(
                    int,
                    input("Enter row and column numbers to fix spot: ").split()
                )
            )

            # Fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # Checking whether current player has won
            if self.is_player_win(player):
                print(f"\nPlayer {player} wins the game!")
                break

            # Checking whether the game is a draw
            if self.is_board_filled():
                print("\nMatch Draw!")
                break

            # Swapping the turn
            player = self.swap_player_turn(player)

        # Showing the final board
        print("\nFinal Board:")
        self.show_board()


# Starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
