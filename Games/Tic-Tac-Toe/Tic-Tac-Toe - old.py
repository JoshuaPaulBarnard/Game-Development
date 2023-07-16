from copy import deepcopy
import random
import numpy as np
import math



def allmax( input_array ):
    """
    This function receives a 1D list, and returns the positions of all the max values.

    :param input_array:
    :return:
    """
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

def check_two_row( board_state, players_symbol, recommend_move = False ):
    ##  Initialize Local Variables
    players_two_in_line = 0
    potential_moves = []

    ##  Determine if Player can get two in a row
    ##  Top Row
    if board_state[0][0] == " " and board_state[0][1] == players_symbol and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[0][1] == " " and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(8)
    if board_state[0][0] == players_symbol and board_state[0][1] == players_symbol and board_state[0][2] == " ":
        players_two_in_line += 1
        potential_moves.append(9)
    ##  Middle Row
    if board_state[1][0] == " " and board_state[1][1] == players_symbol and board_state[1][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(4)
    if board_state[1][0] == players_symbol and board_state[1][1] == " " and board_state[1][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    if board_state[1][0] == players_symbol and board_state[1][1] == players_symbol and board_state[1][2] == " ":
        players_two_in_line += 1
        potential_moves.append(6)
    ##  Bottom Row
    if board_state[2][0] == " " and board_state[2][1] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(1)
    if board_state[2][0] == players_symbol and board_state[2][1] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(2)
    if board_state[2][0] == players_symbol and board_state[2][1] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)
    ##  Diagonal (top left to bottom right)
    if board_state[0][0] == " " and board_state[1][1] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[1][1] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    if board_state[0][0] == players_symbol and board_state[1][1] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)
    ##  Diagonal (Bottom Left to Top Right)
    if board_state[2][0] == " " and board_state[1][1] == players_symbol and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(1)
    if board_state[2][0] == players_symbol and board_state[1][1] == " " and board_state[0][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    if board_state[2][0] == players_symbol and board_state[1][1] == players_symbol and board_state[0][2] == " ":
        players_two_in_line += 1
        potential_moves.append(9)
    ##  Column One
    if board_state[0][0] == " " and board_state[1][0] == players_symbol and board_state[2][0] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(7)
    if board_state[0][0] == players_symbol and board_state[1][0] == " " and board_state[2][0] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(4)
    if board_state[0][0] == players_symbol and board_state[1][0] == players_symbol and board_state[2][0] == " ":
        players_two_in_line += 1
        potential_moves.append(1)
    ##  Column Two
    if board_state[0][1] == " " and board_state[1][1] == players_symbol and board_state[2][1] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(8)
    if board_state[0][1] == players_symbol and board_state[1][1] == " " and board_state[2][1] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(5)
    if board_state[0][1] == players_symbol and board_state[1][1] == players_symbol and board_state[2][1] == " ":
        players_two_in_line += 1
        potential_moves.append(2)
    ##  Column Three
    if board_state[0][2] == " " and board_state[1][2] == players_symbol and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(9)
    if board_state[0][2] == players_symbol and board_state[1][2] == " " and board_state[2][2] == players_symbol:
        players_two_in_line += 1
        potential_moves.append(6)
    if board_state[0][2] == players_symbol and board_state[1][2] == players_symbol and board_state[2][2] == " ":
        players_two_in_line += 1
        potential_moves.append(3)

    if recommend_move is False:
        return players_two_in_line
    else:
        potential_move = random.choice(potential_moves)
        return potential_move


##  Add to Agent_Node
def check_one_row( board_state, players_symbol ):
    ##  Initialize Local Variables
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


##  Return the evaluation score for the entire board.
def evaluate_board(board_state, current_player, as_3d_array = False, verbose = False):
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
    if verbose is True:
        print("Check:  evaluation_values:  ", evaluation_values)
    if as_3d_array is True:
        evaluation_values = np.reshape(evaluation_values, [3,3] )
        return evaluation_values
    else:
        return evaluation_values



##  Should be inside TicTacToe_Node() but temporarily removed as it was not working properly.
def check_win(board, test = ""):
    ##  Check for horizontal win conditions
    for row_counter in range(3):
        if board[row_counter][0] == board[row_counter][1] == board[row_counter][2] == test:
            return True
    ##  Check for vertical win conditions
    for column_counter in range(3):
        if board[0][column_counter] == board[1][column_counter] == board[2][column_counter] == test:
            return True
    ##  Check for diagonal win conditions
    if board[0][0] == board[1][1] == board[2][2] == test:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == test:
        return True
    else:
        return False


def testWinMove(game, symbol, row, column, verbose = False):
    board_copy = deepcopy( game.board )
    board_copy[row][column] = symbol
    if verbose is True:
        print("Check:  testWinMove:  board_copy:  ", board_copy)
        print("Check:  testWinMove:  symbol:  ", symbol)
    return check_win(board_copy, symbol)


def testForkMove(game, symbol, row, column):
    # Determines if a move opens up a fork
    board_copy = deepcopy( game.board )
    board_copy[row][column] = symbol
    winningMoves = 0
    for row in range( len( board_copy ) ):
        for column in range( len( board_copy ) ):
            if testWinMove(game, symbol, row, column) and board_copy[column] == ' ':
                winningMoves += 1
    if winningMoves >= 2:
        return True
    else:
        False



def determine_opponent( player_symbol ):
    ##  Determine Opponents Symbol
    if player_symbol == "X":
        return "O"
    elif player_symbol == "O":
        return "X"
    else:
        return( print("Error:  agents_move determining symbol."))



def best_move( game, pass_along = False ):
    ##  Initialize Local Variables
    game_state = deepcopy( game )
    player = deepcopy( game.player )

    ##  Get the best move for the current turn, and commit it to the local copy
    next_move = agents_move( game_state )
    commit_move(next_move, game_state.board, player)
    game_state.change_turns()
    if pass_along == True:
        return game_state
    else:
        return next_move



def next_best_move( game, will_win = False, pass_along = False, show = False ):
    ##  Initialize Local Variables
    game_state = deepcopy( game )
    player = deepcopy( game.player )

    ##  Get the best move for the current turn, and commit it to the local copy
    game_state1 = best_move( game_state, True )
    game_state2 = best_move( game_state1, True )

    if pass_along == True:
        return game_state2
    elif show == True:
        return print( game_state2 )
    elif will_win == True:
        if game_state2.check_win( player = game_state2.player ) == True:
            return True
    else:
        return game_state2





##  Change to Agent_Node() class
##  Returns the location (int: from 1 to 9) for the best (provided) move
def agents_move( game ):
    ##  Initialize Local Variables
    recommended_move = 0
    game_state = deepcopy( game )
    board_state = deepcopy( game.board )
    agent_symbol = deepcopy( game.player )
    #print("Error:  agents_move received board_state:  ", board_state)

    ##  Determine Opponents Symbol
    opponents_symbol = determine_opponent( agent_symbol )

    ##  Always take center, if open.
    if board_state[1][1] == ' ':
        recommended_move = 5
        return recommended_move

    ##  Determine if the agent can win, and then do so.
    if check_two_row( board_state, agent_symbol, False ) > 0:
        recommended_move  = check_two_row( board_state, agent_symbol, True )
        print("Check:  If agent can win, do so")
        return recommended_move

    ##  Determine if Opponent is about to win, and then stop them.
    if check_two_row( board_state, opponents_symbol, False ) > 0:
        recommended_move = check_two_row( board_state, opponents_symbol, True )
        print("Check:  if opponent can win, stop them")
        return recommended_move

    ##  Determine if the agent can form a fork, then do so.
    for row in range( len( board_state ) ):
        for column in range( len( board_state ) ):
            if board_state[row][column] == ' ' and testForkMove(game, agent_symbol, row, column) is True:
                    return column

    ##  Determine if the opponent can form a fork, then stop them.
    for row in range( len( board_state ) ):
        for column in range( len( board_state ) ):
            if column == ' ' and testForkMove(game, opponents_symbol, row, column) is True:
                return column

    ##  Evaluate which location is best.
    ##  The objective is to make the agent capable of choosing a location that will create a 2 in row for itself.
    ##  Currently, it has no long-term goalmaking capabilities, and just chooses a location at random.
    evaluated_board = allmax( evaluate_board(board_state, agent_symbol) )
    evaluated_move = random.choice( evaluated_board )

    ##  Parse the recommended best move to a valid input value.
    recommended_move = board_parser( evaluated_move )

    # Return the agents move
    return recommended_move


class TicTacToe_Node:
    def __init__(self, board = None, player = "X", turn = 1):
        ##  Initialize the Starting board, and create a blank board if none is provided.
        if board is None:
            board = []
            for counter_i in range(3):
                board.append( [" " for counter_j in range(3)] )
        self.board = board
        self.player = player
        self.turn = turn

    def __str__(self):
        row_strings = [" | ".join(row) for row in self.board]
        return ("\n" + '-'*9 + "\n").join(row_strings)

    def check_win(self, player = ""):
        ##  Check for horizontal win conditions
        for row_counter in range(3):
            if self.board[row_counter][0] == self.board[row_counter][1] == self.board[row_counter][2] == player:
                return True
        ##  Check for vertical win conditions
        for column_counter in range(3):
            if self.board[0][column_counter] == self.board[1][column_counter] == self.board[2][column_counter] == player:
                return True
        ##  Check for diagonal win conditions
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True
        else:
            return False

    def check_draw(self):
        ##  Check for a stalemate
        if " " not in "".join(["".join(row) for row in self.board]):
            return True
        else:
            return False

    def change_turns(self):
        ##  Change the symbol for the next player
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"
        ##  Increment the games turn counter
        self.turn += 1

    def whos_turn(self):
        x_count = 0
        o_count = 0
        for rows in self.board:
            for columns in rows:
                if columns == "X":
                    x_count += 1
                elif columns == "O":
                    o_count += 1
        if x_count <= o_count:
            return "X"
        else:
            return "O"

    def get_board_copy(self):
        # Make a duplicate of the board. When testing moves we don't want to
        # change the actual board
        board_copy = []
        for counter in self.board:
            board_copy.append(counter)
        return board_copy


def change_players( player ):
    ##  Change the symbol for the next player
    if player == "X":
        return "O"
    elif player == "O":
        return "X"



##  Currently broken, as endgame_result has been removed and must be replaced (by adding to node and using .player)
##  Add to Game_Node class
def declare_winner( current_player, humans_symbol ):
    ##  Determine which player is human and their symbol
    if humans_symbol == "X":
        human = "X"
        computer = "O"
    elif humans_symbol == "O":
        human = "O"
        computer = "X"
    else:
        return print("Error: in declare_winner function.")

    ##  Print out the game results.
    print("\nGame Over.\n")
    if current_player == human:
        score["Human"] += 1
        print(" ****  The Human Player Has Won!  ****")
    elif current_player == computer:
        score["Computer"] += 1
        print(" ****  The computer player won  ****")
    elif current_player == "stalemate":
        score["Stalemate"] += 1
        print(" ****  This game was a Tie  **** ")

    ##  Display score board
    print("\nScore Board:")
    print("Human Player: ", score["Human"])
    print("Computer Player: ", score["Computer"])
    print("Stalemates: ", score["Stalemate"])

    ##  Prompt to start a new game
    restart = input("\nDo want to play Again?(y/n): ")
    if restart == "y" or restart == "Y" or restart == "yes" or restart == "Yes":
        print("--------------------------------------------------------------------------------------------------")
        game()
    else:
        print("\nGood Bye.")


##  Add to Game_Node class
##  Function to check if the players move input is valid, and maps to an unoccupied tile in the game's board.
def is_move_valid( move_to_check, current_game_board, verbose = False ):
    if verbose is True:
        print("Check Function: is_move_valid; check variable:  ", move_to_check)
    if move_to_check < 1 or move_to_check > 9:
        return False
    elif move_to_check == 1:
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
    else:
        return True


def board_parser( players_move ):
    ##  Parse the recommended best move to a valid input value.
    if players_move == 0:
        return 7
    elif players_move == 1:
        return 8
    elif players_move == 2:
        return 9
    elif players_move == 3:
        return 4
    elif players_move == 4:
        return 5
    elif players_move == 5:
        return 6
    elif players_move == 6:
        return 1
    elif players_move == 7:
        return 2
    elif players_move == 8:
        return 3


def commit_move( players_move, board, symbol):
        if players_move == 1:
            board[2][0] = symbol
        elif players_move == 2:
            board[2][1] = symbol
        elif players_move == 3:
            board[2][2] = symbol
        elif players_move == 4:
            board[1][0] = symbol
        elif players_move == 5:
            board[1][1] = symbol
        elif players_move == 6:
            board[1][2] = symbol
        elif players_move == 7:
            board[0][0] = symbol
        elif players_move == 8:
            board[0][1] = symbol
        elif players_move == 9:
            board[0][2] = symbol
        else:
            return print("Error:  in committing players move, players_move:  ", players_move)


##  This is the beginnings of the Game_Node(), which is not complete yet
#   It will be able to handle 0 to 2 human players and keep track of the score internally.
class Game_Node():
    def __init__(self, human_players = None, score = None):
        if score == None:
            score = {"Human": 0, "Computer": 0, "Stalemate": 0}
        self.human_players = human_players
        self.score = score

    def welcome_message(self):
        ##  Display welcome message.
        print("Welcome to Joshua Paul Barnard's game of Tic Tac Toe!")
        print("The Ai is using an algorithm based on the equation: (3*X2 + X1) - (3*O2 + O1)")
        print("Just use numbers 1 through 9 to play.")
        print("It is recommended to use a keyboard's numpad (as 1 is for the lower left corner, 5 is the center tile, "
              "and 9 is the upper right corner)")
        #print("Please choose the number of human players, from zero to two:")


##  This is the game() function which controls the input/output and progression of the TicTacToe_Node()
def game():
    ##  Display welcome message.
    print("Welcome to Joshua Barnard's game of Tic Tac Toe!")
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
        return print("Error: with choice of first player")

    ##  Display the symbols of each player
    print(player1 + " is X, and " + player2 + " is O.")
    players_turn = player1

    ##   Start the game
    current_game = TicTacToe_Node()

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
            players_move = agents_move( current_game )

        ##  Now we commit the players move to the current board state.
        if is_move_valid(players_move, current_game.board) is False:
            return print("Error:  Invalid players_move:  ", players_move)
        else:
            commit_move( players_move, current_game.board, current_game.player )
            print("--------------------------------------------------------------------------------------------------")

        ##  Check end game requirements
        if current_game.check_draw() is True:
            print( current_game )
            return declare_winner( "stalemate", human_symbol )
        elif current_game.check_win(player = "X") is True or current_game.check_win(player = "O") is True:
            print( current_game )
            return declare_winner( current_game.player, human_symbol )

        ##  Change the symbol for the next player
        current_game.change_turns()

        ##  Change to the next players turn
        if players_turn == "Human player":
            players_turn = "Computer player"
        elif players_turn == "Computer player":
            players_turn = "Human player"

    return current_game


##  Start Game
score = {"Human": 0, "Computer": 0, "Stalemate": 0}
game()



