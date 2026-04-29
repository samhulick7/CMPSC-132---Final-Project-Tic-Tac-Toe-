# CMPSC 132 Final Project:
# Tic-Tac-Toe Game 
# Created by Samantha Hulick
# Github Username: samhulick7

class TicTacToe():
     
    def __init__(self):
        self.board = [[' ',' ',' '], # This is the playing board
                      [' ',' ',' '],
                      [' ',' ',' ']]
        self.turn_counter = 0
        self.x_win_count = 0
        self.o_win_count = 0
        

    def print_board(self):
        
        print(f"SCORE:\nX: {self.x_win_count} O: {self.o_win_count}")
        print("--------------\n")
        for row in self.board:
            print(row, "\n")
        print("--------------")

    def play(self):
        
        game_end = False

        while not game_end: # Allows multiple games & turns to be played

            self.print_board()

            valid_move = False

            while not valid_move: # Loop continues until a valid input is given

                try:

                    if self.turn_counter % 2 == 0:
                        player = "X"
                        print("It's X's turn!")
                    else:
                        player = "O"
                        print("It's O's turn!")

                    row = int(input("Please enter the row (0-2): "))
                    column = int(input("Please enter the column (0-2): "))

                    if (row < 0) or(row > 2) or (column < 0) or (column > 2): # Input out of range, asks the player again
                        print("\n" * 10)
                        self.print_board()
                        print("Input must be between 0 and 2, please try again.")
                    elif (self.board[row][column] != ' '): # Space already filled, asks the player again
                        print("\n" * 10)
                        self.print_board()
                        print("That space is already filled, please try again.")
                    else:
                        valid_move = True

                except ValueError: # If input is anything else other than an integer
                    print("\n" * 10)
                    self.print_board()
                    print("Input must be an integer, please try again")
            
                
            self.board[row][column] = player
            self.turn_counter += 1

            print("\n" * 10) # Creates space between boards (for better visibility)

            if self.check_winner(player):
                
                self.print_board()
                
                print(f"WINNER: {player}!") # Displays the winner and their rolling number of wins
                if player == "X":
                    print(f"{player}'s Number of Wins: {self.x_win_count}")
                elif player == "O":
                    print(f"{player}'s Number of Wins: {self.o_win_count}")

                if not self.replay():
                    game_end = True # Exits the while loop

            elif self.is_draw():
                
                self.print_board()

                print(f"DRAW!")

                if not self.replay():
                    game_end = True # Exits the while loop

            # When there is no winner or no draw, the game continues like normal

    
    def check_winner(self, player):
        
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]: # Horizontal win
                self.increase_win_count(player)
                return True
            elif player == self.board[0][i] == self.board[1][i] == self.board[2][i]: # Vertical win
                self.increase_win_count(player)
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]: # Diagonal win (top left to bottom right)
            self.increase_win_count(player)
            return True
        elif player == self.board[0][2] == self.board[1][1] == self.board[2][0]: # Diagonal win (top right to bottom left)
            self.increase_win_count(player)
            return True 
        
        return False # No winner yet
            
    def increase_win_count(self, player):
        
        if player == "X":
            self.x_win_count += 1
        elif player == "O":
            self.o_win_count += 1


    def is_draw(self):
        
        return self.is_full()

    def is_full(self):
        
        for row in self.board:
            for item in row:
                if item == ' ':
                    return False
        return True
    
    def replay(self):
        play_again = input("Type YES to play again!: ").upper() # Any capitalization of 'yes' continues the games
        
        if play_again == "YES":
            self.clear_board()
            print("\n" * 10)
            return True
        else:
            print("Thank you for playing!") # End of games
            return False


    def clear_board(self):
        
        self.board = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        
        # I chose not to reset self.turn_counter = 0 so that the loser of each game will start the next game
        



# Start of Game
print("\nWelcome to Tic-Tac-Toe! \nType in your terminal to play:\n")
game = TicTacToe()
game.play()