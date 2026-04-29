# CMPSC-132: Final Project
# Tic-Tac-Toe Game
by Samantha Hulick

Project Description:

Two-player Tic-Tac-Toe game that uses a 3x3 playing board. The game utilizes the terminal to alternate turns between the players, 'X' and 'O', keeping track of the wins for each player.

Instructions:

1. Copy the file "Tic_Tac_Toe_Code.py"
2. Open a terminal/command prompt. Upon first running the program and before each turn, the terminal will display the score, the board (represented as a list of lists), who's turn it is, as well as an input field for the row and column of the play.
3. Respond to the command prompts that ask for the row and column index of the play. In order for a play to be marked on the board, the row and column of the play must be between 0-2, or else the play will be ruled invalid and the terminal will re-ask the player.
4. If one player wins by connecting 3 in a row (either horizontally, vertically, or diagonally), the overall score will be updated. 
5. Upon one player winning or a draw occuring, the terminal will prompt the player to type any variation of 'YES' if they want to play another game and further increase the score. After each game, the next starting player will be the loser of the previous game, or in the case of a draw it will be the opposite of whoever started the last game.
6. However, if the player types anything other than yes to continuing the game, the game will end.