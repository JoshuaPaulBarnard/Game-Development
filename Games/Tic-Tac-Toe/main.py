####################################################################
####                Tic-Tac-Toe
####        Author:  Joshua Paul Barnard
####






from copy import deepcopy
import random
import numpy as np
import math


score = {"Human":0, "Computer":0, "Stalemate": 0}
#initial_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def check_two_row( board_state, symbol, recommend_move = False ):
    ##  Initialize Local Variables
    players_symbol = symbol
    players_two_in_line = 0
    potential_moves = []

    ##  Determine if Player can get two in a row
    ##  Top Row
    if board_state[0][0] == players_symbol and board_state[0][1] == players_symbol and board_state[0][2] == " ":
        players_two_in_line += 1
        potential_moves.append(9)
    if board_state[0][0] == " " and board_state[0][1] == players_symbol and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[0][1] == " " and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(8)
    ##  Middle Row
    if board_state[1][0] == players_symbol and board_state[1][1] == players_symbol and board_state[1][2] == " ":
        players_two_in_line += 1
        potential_moves.append(6)
    if board_state[1][0] == " " and board_state[1][1] == players_symbol and board_state[1][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(4)
    if board_state[1][0] == players_symbol and board_state[1][1] == " " and board_state[1][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    ##  Bottom Row
    if board_state[2][0] == players_symbol and board_state[2][1] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)
    if board_state[2][0] == " " and board_state[2][1] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(1)
    if board_state[2][0] == players_symbol and board_state[2][1] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(2)
    ##  Diagonal (top left to bottom right)
    if board_state[0][0] == players_symbol and board_state[1][1] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)
    if board_state[0][0] == " " and board_state[1][1] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[1][1] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    ##  Diagonal (Bottom Left to Top Right)
    if board_state[2][0] == players_symbol and board_state[1][1] == players_symbol and board_state[0][2] == " ":
        players_two_in_line += 1
        potential_moves.append(9)
    if board_state[2][0] == " " and board_state[1][1] == players_symbol and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(1)
    if board_state[2][0] == players_symbol and board_state[1][1] == " " and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    ##  Column One
    if board_state[0][0] == players_symbol and board_state[1][0] == players_symbol and board_state[2][0] == " ":
        players_two_in_line += 1
        potential_moves.append(1)
    if board_state[0][0] == " " and board_state[1][0] == players_symbol and board_state[2][0] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[1][0] == " " and board_state[2][0] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(4)
    ##  Column Two
    if board_state[0][1] == players_symbol and board_state[1][1] == players_symbol and board_state[2][1] == " ":
        players_two_in_line += 1
        potential_moves.append(2)
    if board_state[0][1] == " " and board_state[1][1] == players_symbol and board_state[2][1] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(8)
    if board_state[0][1] == players_symbol and board_state[1][1] == " " and board_state[2][1] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    ##  Column Three
    if board_state[0][2] == players_symbol and board_state[1][2] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)
    if board_state[0][2] == " " and board_state[1][2] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(9)
    if board_state[0][2] == players_symbol and board_state[1][2] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)

    if recommend_move is False:
        return players_two_in_line

    if recommend_move is True:
        return potential_moves
        #if 1 <= recommended_move <= 9:
        #    return recommended_move
        #elif recommended_move == 0:
        #    return False


def check_one_row( board_state, symbol ):
    ##  Initialize Local Variables
    players_symbol = symbol
    players_one_in_line = 0

    ##  Calculate players_one_in_line
    if board_state[0][0] == players_symbol and board_state[0][1] == " " and board_state[0][2] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[0][1] == players_symbol and board_state[0][2] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[0][1] == " " and board_state[0][2] == players_symbol:
        players_one_in_line += 1

    if board_state[1][0] == players_symbol and board_state[1][1] == " " and board_state[1][2] == " ":
        players_one_in_line += 1
    if board_state[1][0] == " " and board_state[1][1] == players_symbol and board_state[1][2] == " ":
        players_one_in_line += 1
    if board_state[1][0] == " " and board_state[1][1] == " " and board_state[1][2] == players_symbol:
        players_one_in_line += 1

    if board_state[2][0] == players_symbol and board_state[2][1] == " " and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[2][0] == " " and board_state[2][1] == players_symbol and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[2][0] == " " and board_state[2][1] == " " and board_state[2][2] == players_symbol:
        players_one_in_line += 1

    if board_state[0][0] == players_symbol and board_state[1][1] == " " and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[1][1] == players_symbol and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[1][1] == " " and board_state[2][2] == players_symbol:
        players_one_in_line += 1

    if board_state[2][0] == players_symbol and board_state[1][1] == " " and board_state[0][2] == " ":
        players_one_in_line += 1
    if board_state[2][0] == " " and board_state[1][1] == players_symbol and board_state[0][2] == " ":
        players_one_in_line += 1
    if board_state[2][0] == " " and board_state[1][1] == " " and board_state[0][2] == players_symbol:
        players_one_in_line += 1

    if board_state[0][0] == players_symbol and board_state[1][0] == " " and board_state[2][0] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[1][0] == players_symbol and board_state[2][0] == " ":
        players_one_in_line += 1
    if board_state[0][0] == " " and board_state[1][0] == " " and board_state[2][0] == players_symbol:
        players_one_in_line += 1

    if board_state[0][1] == players_symbol and board_state[1][1] == " " and board_state[2][1] == " ":
        players_one_in_line += 1
    if board_state[0][1] == " " and board_state[1][1] == players_symbol and board_state[2][1] == " ":
        players_one_in_line += 1
    if board_state[0][1] == " " and board_state[1][1] == " " and board_state[2][1] == players_symbol:
        players_one_in_line += 1

    if board_state[0][2] == players_symbol and board_state[1][2] == " " and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[0][2] == " " and board_state[1][2] == players_symbol and board_state[2][2] == " ":
        players_one_in_line += 1
    if board_state[0][2] == " " and board_state[1][2] == " " and board_state[2][2] == players_symbol:
        players_one_in_line += 1

    return players_one_in_line


def allmax( input_array ):
    if len(input_array) == 0:
        return []
    positions_of_max_values = [0]
    the_max_values = input_array[0]
    for counter_i in range(1, len(input_array)):
        if input_array[counter_i] > the_max_values:
            positions_of_max_values = [counter_i]
            the_max_values = input_array[counter_i]
        elif input_array[counter_i] == the_max_values:
            positions_of_max_values.append(counter_i)
    return positions_of_max_values


##  Return the evaluation score for the entire board.
def evaluate_board(board_state, current_player, as_3d_array = False):
    ##  Initialize Local Variables
    opponents_symbol = ""

    ##  Determine Opponents Symbol
    if current_player == "X":
        opponents_symbol = "O"
    elif current_player == "O":
        opponents_symbol = "X"

    evaluation_values = []
    for row_counter in range( len(board_state) ):
        for column_counter in range( len(board_state) ):
            if board_state[row_counter][column_counter] == " ":
                eval_one1 = check_one_row(board_state, current_player)
                eval_one2 = check_one_row(board_state, opponents_symbol)
                eval_two1 = check_two_row(board_state, current_player, False)
                eval_two2 = check_two_row(board_state, opponents_symbol, False)
                eval_value = (3 * eval_two1 + eval_one1) - (3 * eval_two2 + eval_one2)
            else:
                eval_value = -math.inf
            evaluation_values.append(eval_value)
    print("evaluation_values:  ", evaluation_values)
    if as_3d_array is True:
        evaluation_values = np.reshape(evaluation_values, [3,3] )
        return evaluation_values
    else:
        return evaluation_values


##  Returns the location (int: from 1 to 9) for the best (provided) move
def agents_move( board_state, symbol ):
    ##  Initialize Local Variables
    agents_symbol = symbol
    recommended_move = 0

    ##  Determine Opponents Symbol
    if agents_symbol == "X":
        opponents_symbol = "O"
    elif agents_symbol == "O":
        opponents_symbol = "X"
    else:
        return( print("Error:  agents_move determining symbol."))

    ##  Always take center, if open.
    if board_state[1][1] == ' ':
        recommended_move = 5
        return recommended_move

    ##  Determine if Player can win, and then do so.
    if check_two_row( board_state, agents_symbol, False ) > 0:
        potential_moves = check_two_row( board_state, agents_symbol, True )
        recommended_move = random.choice( potential_moves )
        return recommended_move

    ##  Determine if Opponent is about to win, and then stop them.
    if check_two_row( board_state, opponents_symbol, False ) > 0:
        potential_moves = check_two_row( board_state, opponents_symbol, True )
        recommended_move = random.choice( potential_moves )
        return recommended_move

    ##  Evaluate which location is best.
    ##  At this point the agent already knows that the opponent does not have two pieces in a row,
    ##    so now our agents top priority is to get two pieces in a single row.
    evaluated_board = allmax( evaluate_board(board_state, agents_symbol) )
    evaluated_move = random.choice( evaluated_board )

    ##  Parse the recommended best move to a valid input value.
    if evaluated_move == 0:
        recommended_move = 7
    elif evaluated_move == 1:
        recommended_move = 8
    elif evaluated_move == 2:
        recommended_move = 9
    elif evaluated_move == 3:
        recommended_move = 4
    elif evaluated_move == 4:
        recommended_move = 5
    elif evaluated_move == 5:
        recommended_move = 6
    elif evaluated_move == 6:
        recommended_move = 1
    elif evaluated_move == 7:
        recommended_move = 2
    elif evaluated_move == 8:
        recommended_move = 3

    ##  Validate the recommended move before passing it along
    if is_move_valid(recommended_move, board_state) is True:
        return recommended_move
    else:
        return print("Error:  Validating agents move, recommended_move:   ", recommended_move)


class GameNode:
    def __init__(self, board = None, player = "X"):
        ##  Initialize the Starting board, and create a blank board if none is provided.
        if board is None:
            board = []
            for counter_i in range(3):
                board.append( [" " for counter_j in range(3)] )
        self.board = board
        self.player = player

    def __str__(self):
        row_strings = [" | ".join(row) for row in self.board]
        return ("\n" + '-'*9 + "\n").join(row_strings)

    def winner(self):
        ##  Check for horizontal win conditions
        for row_counter in range(3):
            if self.board[row_counter][0] == self.board[row_counter][1] == self.board[row_counter][2] != " ":
                return self.board[row_counter][0]
        ##  Check for vertical win conditions
        for column_counter in range(3):
            if self.board[0][column_counter] == self.board[1][column_counter] == self.board[2][column_counter] != " ":
                return self.board[0][column_counter]
        ##  Check for diagonal win conditions
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[1][1]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            return self.board[1][1]
        ##  Check for a stalemate
        if " " not in "".join(["".join(row) for row in self.board]):
            return 'stalemate'

    def memory(self):
        if self.winner() is not None:
            return
        ##  Potential boards
        for row_counter in range(3):
            for column_counter in range(3):
                if self.board[row_counter][column_counter] == " ":
                    next_board = deepcopy(self.board)
                    next_board[row_counter][column_counter] = self.player
                    ##  Change player symbol
                    if self.player == "X":
                        next_player = "O"
                    elif self.player == "O":
                        next_player = "X"
                    print(next_board)
                    yield GameNode( board = next_board, player = next_player )

    def children(self):
        if self.winner() is not None:
            return
        ##  Potential boards
        for row_counter in range(3):
            for column_counter in range(3):
                if self.board[row_counter][column_counter] == " ":
                    next_board = deepcopy(self.board)
                    next_board[row_counter][column_counter] = self.player
                    ##  Change player symbol
                    if self.player == "X":
                        next_player = "O"
                    elif self.player == "O":
                        next_player = "X"
                    print(next_board)
                    yield GameNode( board = next_board, player = next_player )

        return None


def declare_winner( endgame_result, players_symbol ):
    ##  Determine which player is human and their symbol
    if players_symbol == "X":
        human = "X"
        computer = "O"
    elif players_symbol == "O":
        human = "O"
        computer = "X"
    else:
        return print("Error in declare_winner function.")

    ##  Print out the game results.
    print("\nGame Over.\n")
    if endgame_result == human:
        #score[0] = score[0] + 1
        score["Human"] += 1
        print(" ****  The Human Player Has Won!  ****")
    elif endgame_result == computer:
        #score[1] = score[1] + 1
        score["Computer"] += 1
        print(" ****  The computer player won  ****")
    elif endgame_result == "stalemate":
        #score[2] = score[2] + 1
        score["Stalemate"] += 1
        print(" ****  This game was a Tie  **** ")

    ##  Display score board
    print("\nScore Board:")
    print("Human Player: ", score["Human"])
    print("Computer Player: ", score["Computer"])
    print("Stalemates: ", score["Stalemate"])

    ##  Prompt to start a new game
    restart = input("\nDo want to play Again?(y/n): ")
    if restart == "y" or restart == "Y"or restart == "yes"or restart == "Yes":
        print("--------------------------------------------------------------------------------------------------")
        game()
    else:
        print("\nGood Bye.")


##  Function to check if human input is unoccupied on the current game's board.
def is_move_valid( move_to_check, current_game_board ):
    print(move_to_check)
    if move_to_check < 1 or move_to_check > 9:
        return False
    if move_to_check == 1:
        if current_game_board[2][0] != ' ':
            return False
    elif move_to_check == 2:
        if current_game_board[2][1] != ' ':
            return False
    elif move_to_check == 3:
        if current_game_board[2][2] != ' ':
            return False
    elif move_to_check == 4:
        if current_game_board[1][0] != ' ':
            return False
    elif move_to_check == 5:
        if current_game_board[1][1] != ' ':
            return False
    elif move_to_check == 6:
        if current_game_board[1][2] != ' ':
            return False
    elif move_to_check == 7:
        if current_game_board[0][0] != ' ':
            return False
    elif move_to_check == 8:
        if current_game_board[0][1] != ' ':
            return False
    elif move_to_check == 9:
        if current_game_board[0][2] != ' ':
            return False
    return True

def game():
    ##  Display welcome message.
    print("Welcome to Joshua Barnard's node-based game of Tic Tac Toe!")
    print("The Ai is using an algorithm based on the equation: (3*X2 + X1) - (3*O2 + O1)")
    print("Just use numbers 1 through 9 to play.")
    print("It is recommended to use a keyboard's numpad (as 1 is for the lower left corner, 5 is the center tile, "
          "and 9 is the upper right corner)")
    human_player = "Human Player"
    computer_player = "Computer Player"

    ##  Choose which player goes first
    first_player = random.choice( [random.choice([0, 1]), random.choice([0, 1])] )

    ##   Assign the player symbols.
    if first_player == 0:
        player1 = "Human player"
        human_symbol = "X"
        player2 = "Computer player"
    elif first_player == 1:
        player1 = "Computer player"
        player2 = "Human player"
        human_symbol = "O"
    else:
        return print("Error with choice of first player")

    ##  Display the symbols of each player
    print(player1 + " is X, and " + player2 + " is O.")
    players_turn = player1

    ##   Start the game
    current_game = GameNode()

    for game_loop_counter in range( 9 ):
        print("It is the " + players_turn + "'s move.")
        print( current_game )

        ##  Receive the humans input
        if players_turn == "Human player":
            ##  Here the human enters their move.
            print("Please choose which tile to move to.")
            players_move = eval(input())

            ##  We check to see if the human entered a valid input value.
            while players_move < 1 or players_move > 9:
                print("Please enter a number between 1 and 9, with 5 representing the center of the board.")
                players_move = eval(input())

            ##  Check to see if the tile is already taken or not.
            while is_move_valid(players_move, current_game.board) is False:
                print("That tile is already taken, please choose another.")
                players_move = eval(input())

        ##  Receive the computers move
        if players_turn == "Computer player":
            players_move = agents_move( current_game.board, current_game.player )

        ##  Now we commit the players move to the current board state.
        if players_move == 1:
            current_game.board[2][0] = current_game.player
        elif players_move == 2:
            current_game.board[2][1] = current_game.player
        elif players_move == 3:
            current_game.board[2][2] = current_game.player
        elif players_move == 4:
            current_game.board[1][0] = current_game.player
        elif players_move == 5:
            current_game.board[1][1] = current_game.player
        elif players_move == 6:
            current_game.board[1][2] = current_game.player
        elif players_move == 7:
            current_game.board[0][0] = current_game.player
        elif players_move == 8:
            current_game.board[0][1] = current_game.player
        elif players_move == 9:
            current_game.board[0][2] = current_game.player
        else:
            return print("Error in committing players move, players_move:  ", players_move)
        print("--------------------------------------------------------------------------------------------------")

        ##  Check end game requirements
        if current_game.winner() is not None:
            print( current_game )
            return declare_winner( current_game.winner(), human_symbol )

        ##  Change the symbol for the next player
        if current_game.player == "X":
            current_game.player = "O"
        elif current_game.player == "O":
            current_game.player = "X"

        ##  Change to the next players turn
        if players_turn == "Human player":
            players_turn = "Computer player"
        elif players_turn == "Computer player":
            players_turn = "Human player"



if __name__ == "__main__":
    game()

