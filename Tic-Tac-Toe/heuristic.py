"""
Joshua Paul Barnard
"""


"""
Programming Assignment - #2
Question - #3
"""

"""
I implemented a Heuristic Alpha Beta Pruning MiniMax algorithm for my Tic Tac Toe game.
It is not as good as my Tic Tac Toe agent from HW#3, but I think it could be improved...
I think I did not implement the alpha-beta pruning correctly...
"""



from copy import deepcopy
import random
import numpy as np



def new_heuristicTable(rows = 3, columns = 3):
    heuristicTable = np.zeros((rows + 1, columns + 1))
    for index in range(0, rows + 1):
        heuristicTable[index, 0] = 10 ** index
        heuristicTable[0, index] = -10 ** index
    return heuristicTable




##  The functions evalute, minimax, and find_move are based on examples from:  https://github.com/jacobaustin123/tic-tac-toe-minimax
def heuristic_evaluation(board, player, other_player):
    """
    Utility state of board
    :param board:
    :param player:
    :param other_player:
    :return:
    """
    ##  Initialize local variables
    #heuristic       = [[0, -.25, -.5, -1], [.25, 0, 0, 0], [.5, 0, 0, 0], [1, 0, 0, 0]]
    heuristic       = new_heuristicTable()
    board_rows      = len( board )
    board_columns   = len( board[0] )
    score           = 0

    ##  Evaluate rows
    for row in range(3):
        player_score = sum(board[row][column] == player for column in range( board_columns ))
        opponent_score = sum(board[row][column] == other_player for column in range( board_columns ))
        score += heuristic[player_score][opponent_score]

    ##  Evaluate Columns
    for column in range(3):
        player_score = sum(board[row][column] == player for row in range( board_rows ))
        opponent_score = sum(board[row][column] == other_player for row in range( board_rows ))
        score += heuristic[player_score][opponent_score]

    ##  Evaluate diagonal right
    player_score = sum(board[row][row] == player for row in range( board_rows ))
    opponent_score = sum(board[row][row] == other_player for row in range( board_rows ))
    score += heuristic[player_score][opponent_score]

    ##  Evaluate diagonal left
    player_score = sum(board[row][2 - row] == player for row in range( board_rows ))
    opponent_score = sum(board[row][2 - row] == player for row in range( board_rows ))
    score += heuristic[player_score][opponent_score]

    return score


def minimax(board, player, players, max, depth = 0, tree_searches = 0, pruned_trees = 0):

    if players[0] == player:
        other_player = players[1]
    else:
        other_player = players[0]

    if check_win(board, player):
        return 1
    if check_win(board, ' '):
        return 0
    if check_win(board, other_player):
        return -1

    if depth == 0:
        score = heuristic_evaluation(board, player, other_player)
        return score

    best_score = -2

    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                if best_score >= max:
                    pruned_trees +=1
                    return best_score
                board[row][column] = player
                subscore = - minimax(board, other_player, players, - best_score, depth - 1)
                board[row][column] = ' '
                if subscore > best_score:
                    best_score = subscore

    tree_searches +=1

    if tree_searches % 100 == 0:
        print("number of complete searchs: {}, number of pruned branches: {}".format(tree_searches, pruned_trees))
    return best_score


def find_move(board, player, players, depth):

    if players[0] == player:
        other_player = players[1]
    else:
        other_player = players[0]

    best_score = -2
    index      = (0, 0)

    values = []
    for column in range(3):
        for row in range(3):
            if board[row][column] == ' ':
                board[row][column] = player
                subscore = - minimax(board, other_player, players, - best_score, depth)
                values.append(subscore)
                board[row][column] = ' '
                if subscore > best_score:
                    index = (row, column)
                    best_score = subscore
            else: values.append(-10)

    return index, values


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

    ##  Always take center, when its available.
    if board_state[1][1] == ' ':
        recommended_move = 5
        return recommended_move

    evaluated_move = find_move( board_state, agent_symbol, ["X", "O"], 9 - game_state.turn)[0]

    ##  Parse the recommended best move to a valid input value.
    recommended_move = board_parser( evaluated_move )

    # Return the agents move
    return recommended_move


def board_parser( players_move ):
    ##  Parse the recommended best move to a valid input value.
    if players_move == (0, 0):
        return 7
    elif players_move == (0, 1):
        return 8
    elif players_move == (0, 2):
        return 9
    elif players_move == (1, 0):
        return 4
    elif players_move == (1, 1):
        return 5
    elif players_move == (1, 2):
        return 6
    elif players_move == (2, 0):
        return 1
    elif players_move == (2, 1):
        return 2
    elif players_move == (2, 2):
        return 3


##  Should be inside TicTacToe_Node() but temporarily removed as it was not working properly.
def check_win(board, test = ' '):
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


##  Add to Agent_Node()
def testWinMove(game, symbol, row, column):
    board_copy = deepcopy( game.board )
    board_copy[row][column] = symbol
    print("Check:  testWinMove:  board_copy:  ", board_copy)
    print("Check:  testWinMove:  symbol:  ", symbol)
    return check_win(board_copy, symbol)


def determine_opponent( player_symbol ):
    ##  Determine Opponents Symbol
    if player_symbol == "X":
        return "O"
    elif player_symbol == "O":
        return "X"
    else:
        return( print("Error:  agents_move determining symbol."))


class TicTacToe_Node:
    def __init__(self, board = None, player = "X", turn = 1, score = None):
        ##  Initialize the Starting board, and create a blank board if none is provided.
        if board is None:
            board = []
            for row in range(3):
                board.append( [" " for column in range(3)] )
        ##  Initialize the starting score board, or create a new score board if it is the first game.
        if score is None:
            score = {"Human": 0, "Computer": 0, "Stalemate": 0}
        self.board  = board
        self.player = player
        self.turn   = turn
        self.score  = score

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
def is_move_valid( move_to_check, current_game_board ):
    print("Check:  is_move_valid:  ", move_to_check)
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


##  This is the game() function which controls the input/output and progression of the TicTacToe_Node()
def game():
    ##  Display welcome message.
    print("Welcome to Joshua Barnard's game of Tic Tac Toe!")
    print("This Ai is using an Alpha Beta Pruning MiniMax Algorithm")
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

        ##  Change the symbol for the next player and increment turn counter
        current_game.change_turns()

        ##  Change to the next players turn
        if players_turn == "Human player":
            players_turn = "Computer player"
        elif players_turn == "Computer player":
            players_turn = "Human player"

    return current_game


##  Start the game
score = {"Human": 0, "Computer": 0, "Stalemate": 0}
game()

