'''
Class: CPSC 427
Team Member 1: Nathan Magrogan
Team Member 2: none
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: othello.py
code for an othello game, lets playes go back and fourth
making moves in othello
'''

import copy
import time
import math

#some constants
VALID_COLUMN = ["a","b","c","d","e","f","g","h"]
VALID_ROW = [1,2,3,4,5,6,7,8]
VALID_ROW_CHAR = ["1","2","3","4","5","6","7","8"]
MAX_LEVEL = 5

BOARD_A = [["X","a","b","c","d","e","f","g","h","X"],
           ["1","_","_","_","_","_","_","_","_","X"],
           ["2","_","_","_","_","_","_","_","_","X"],
           ["3","_","_","_","_","_","_","_","_","X"],
           ["4","_","_","_","W","B","_","_","_","X"],
           ["5","_","_","_","B","W","_","_","_","X"],
           ["6","_","_","_","_","_","_","_","_","X"],
           ["7","_","_","_","_","_","_","_","_","X"],
           ["8","_","_","_","_","_","_","_","_","X"],
           ["X","X","X","X","X","X","X","X","X","X"]]

BOARD_B = [["X","a","b","c","d","e","f","g","h","X"],
              ["1","_","_","_","_","_","_","_","_","X"],
              ["2","_","_","_","_","_","_","_","_","X"],
              ["3","_","_","_","_","_","_","_","_","X"],
              ["4","_","_","_","B","W","_","_","_","X"],
              ["5","_","_","_","W","B","_","_","_","X"],
              ["6","_","_","_","_","_","_","_","_","X"],
              ["7","_","_","_","_","_","_","_","_","X"],
              ["8","_","_","_","_","_","_","_","_","X"],
              ["X","X","X","X","X","X","X","X","X","X"]]


class Othello:
    #creates a starting board
    def __init__(self):
        self.board = BOARD_A
        #score where 0 is score for black and 1 is score for white
        self.score = [2,2]

    def swap_board(self):
        if self.board == BOARD_A:
            self.board = BOARD_B
        else:
            self.board = BOARD_A

    #displays the board
    def display_board(self):
            for row in self.board:
                print(row)
            print "Score B = " + str(self.score[0])
            print "Score W = " + str(self.score[1])
            print("")

    #asks for user input for a new pos to place a tile
    def input_pos(self,player_name):
        letter_pos = raw_input(player_name + " input column letter: " )
        while letter_pos not in VALID_COLUMN:
            letter_pos = raw_input("Invald only letters A-H: ")

        number_pos = input(player_name + " input row number: ")
        while number_pos not in VALID_ROW:
            number_pos = input("Invald only numbers 1-8: ")

        return letter_pos, number_pos

    #returns all adjacent tiles given a positon
    def get_adj_tiles(self,number_pos,letter_pos_int):
        adjacent_tiles = [self.board[number_pos+1][letter_pos_int], #below
                          self.board[number_pos-1][letter_pos_int], #above
                          self.board[number_pos][letter_pos_int+1], #right
                          self.board[number_pos][letter_pos_int-1], #left
                          self.board[number_pos+1][letter_pos_int+1], #below right
                          self.board[number_pos+1][letter_pos_int-1], #below left
                          self.board[number_pos-1][letter_pos_int+1], #up right
                          self.board[number_pos-1][letter_pos_int-1]] #up left
        return adjacent_tiles


    #generates next possible moves, returns a list of tuples
    def generate_next_moves(self,player_name):
        next_moves = []
        if player_name == "B":
            opposte_name = "W"
        else:
            opposte_name = "B"


        for i in range(1,9,1): #number
            for j in range(1,9,1): #letter
                if self.board[i][j] == "_":
                    adjacent_tiles = self.get_adj_tiles(i,j)
                    for k in range(len(adjacent_tiles)):
                        if adjacent_tiles[k] == opposte_name:
                            if k == 0:
                                for l in range(i+1,9,1):
                                    if self.board[l][j] == player_name:
                                        next_moves.append((i,j))
                                        break
                            elif k == 1:
                                for l in range(i-1,0,-1):
                                    if self.board[l][j] == player_name:
                                        next_moves.append((i,j))
                                        break
                            elif k == 2:
                                for l in range(j+1,9,1):
                                    if self.board[i][l] == player_name:
                                        next_moves.append((i,j))
                                        break
                            elif k == 3:
                                for l in range(j-1,0,-1):
                                    if self.board[i][l] == player_name:
                                        next_moves.append((i,j))
                                        break
                            elif k == 4:
                                l = 1
                                while self.board[i+l][j+l] != "X":
                                    if self.board[i+l][j+l] == player_name:
                                        next_moves.append((i,j))
                                        break
                                    l  = l +1
                            elif k == 5:
                                l = 1
                                while self.board[i+l][j-l] != "X" and self.board[i+l][j-l] not in VALID_COLUMN:
                                    if self.board[i+l][j-l] == player_name:
                                        next_moves.append((i,j))
                                        break
                                    l  = l +1
                            elif k == 6:
                                l = 1
                                while self.board[i-l][j+l] != "X" and self.board[i-l][j+l] not in VALID_COLUMN:
                                    if self.board[i-l][j+l] == player_name:
                                        next_moves.append((i,j))
                                        break
                                    l  = l +1
                            elif k == 7:
                                l = 1
                                #print (i,j)
                                while self.board[i-l][j-l] not in VALID_ROW_CHAR and self.board[i-l][j-l] not in VALID_COLUMN and self.board[i-l][j-l] != "X":
                                    #print self.board[i-l][j-l]
                                    if self.board[i-l][j-l] == player_name:
                                        next_moves.append((i,j))
                                        break
                                    l  = l +1


        return next_moves


    def flip_tiles(self,number_pos,letter_pos,player_name,old_board_config,old_score):

        flip_helper = [0,0,0,0,0,0,0,0]
        flip_helper2 = [0,0,0,0,0,0,0,0]

        if player_name == "B":
            opposite_name = "W"
        else:
            opposite_name = "B"

        adjacent_tiles = self.get_adj_tiles(number_pos,letter_pos)
        for i in range(len(adjacent_tiles)):
            if adjacent_tiles[i] == opposite_name:
                if i == 0:
                    for l in range(number_pos+1,9,1):
                        if self.board[l][letter_pos] == player_name:
                            if l == 8 or self.board[l+1][letter_pos] == "_" or self.board[l+1][letter_pos] == opposite_name:

                                for j in range(l,number_pos-1,-1):
                                    if self.board[j][letter_pos] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[j][letter_pos] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l


                if i == 1:
                    for l in range(number_pos-1,0,-1):
                        if self.board[l][letter_pos] == player_name:
                            if l == 1 or self.board[l-1][letter_pos] == "_" or self.board[l-1][letter_pos] == opposite_name:

                                for j in range(l,number_pos+1,1):
                                    if self.board[j][letter_pos] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[j][letter_pos] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l



                if i == 2:
                    for l in range(letter_pos+1,9,1):
                        if self.board[number_pos][l] == player_name:
                            if l == 8 or self.board[number_pos][l+1] == "_" or self.board[number_pos][l+1] == opposite_name:

                                for j in range(l,letter_pos-1,-1):
                                    if self.board[number_pos][j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos][j] = "$"

                                flip_helper[i] = 1
                                flip_helper2[i] = l

                if i == 3:
                    for l in range(letter_pos-1,0,-1):
                        if self.board[number_pos][l] == player_name:
                            if l == 1 or self.board[number_pos][l-1] == "_" or self.board[number_pos][l-1] == opposite_name :

                                for j in range(l,letter_pos+1,1):
                                    if self.board[number_pos][j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos][j] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l

                if i == 4:
                    l = 1
                    while self.board[number_pos+l][letter_pos+l] != "X":
                        if self.board[number_pos+l][letter_pos+l] == player_name:
                            #below if, need to add if next position is an edge piece
                            if self.board[number_pos+l+1][letter_pos+l+1] == "_" or self.board[number_pos+l+1][letter_pos+l+1] == opposite_name or self.board[number_pos+l+1][letter_pos+l+1] == "X":

                                for j in range(l,-1,-1):
                                    if self.board[number_pos+j][letter_pos+j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos+j][letter_pos+j] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l

                                        #self.board[number_pos+j][letter_pos+j] = player_name
                        l = l+1
                if i == 5:
                    l = 1
                    while self.board[number_pos+l][letter_pos-l] != "X" and self.board[number_pos+l][letter_pos-l] not in VALID_COLUMN:
                        if self.board[number_pos+l][letter_pos-l] == player_name:
                            if self.board[number_pos+l+1][letter_pos-l-1] == "_" or self.board[number_pos+l+1][letter_pos-l-1] == opposite_name or self.board[number_pos+l+1][letter_pos-l-1] in VALID_COLUMN or self.board[number_pos+l+1][letter_pos-l-1] == "X" :
                                for j in range(l,-1,-1):
                                    if self.board[number_pos+j][letter_pos-j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos+j][letter_pos-j] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l

                                        #self.board[number_pos+j][letter_pos-j] = player_name
                        l = l+1

                if i == 6:
                    l = 1
                    while self.board[number_pos-l][letter_pos+l] != "X" and self.board[number_pos-l][letter_pos+l] not in VALID_COLUMN:
                        if self.board[number_pos-l][letter_pos+l] == player_name:
                            if self.board[number_pos-l-1][letter_pos+l+1] == "_" or self.board[number_pos-l-1][letter_pos+l+1] == opposite_name or self.board[number_pos-l-1][letter_pos+l+1] in VALID_COLUMN or  self.board[number_pos-l-1][letter_pos+l+1] == "X" :

                                for j in range(l,-1,-1):
                                    if self.board[number_pos-j][letter_pos+j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos-j][letter_pos+j] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l
                                        #self.board[number_pos-j][letter_pos+j] = player_name

                        l = l+1

                if i == 7:
                    l = 1
                    while self.board[number_pos-l][letter_pos-l] not in VALID_ROW_CHAR and self.board[number_pos-l][letter_pos-l] not in VALID_COLUMN and self.board[number_pos-l][letter_pos-l] != "X":
                        if self.board[number_pos-l][letter_pos-l] == player_name:
                            if self.board[number_pos-l-1][letter_pos-l-1] == "_" or self.board[number_pos-l-1][letter_pos-l-1] == opposite_name or self.board[number_pos-l-1][letter_pos-l-1] == "X" or self.board[number_pos-l-1][letter_pos-l-1] in VALID_ROW_CHAR or self.board[number_pos-l-1][letter_pos-l-1] in VALID_COLUMN:
                                for j in range(l,-1,-1):
                                    if self.board[number_pos-j][letter_pos-j] == opposite_name:
                                        if player_name == "B":
                                            self.score[0] = self.score[0]+1
                                            self.score[1] = self.score[1]-1
                                        else:
                                            self.score[1] = self.score[1]+1
                                            self.score[0] = self.score[0]-1
                                    self.board[number_pos-j][letter_pos-j] = "$"


                                flip_helper[i] = 1
                                flip_helper2[i] = l
                                        #self.board[number_pos-j][letter_pos-j] = player_name

                        l = l+1

        return flip_helper,flip_helper2


    def flip2(self,number_pos,letter_pos,player_name,flip_helper,flip_helper2):


        if player_name == "B":
            opposite_name = "W"
        else:
            opposite_name = "B"

        for i in range(len(flip_helper)):
            if flip_helper[i] == 1:
                l = flip_helper2[i]
                if i == 0:
                    for j in range(l,number_pos-1,-1):
                        if self.board[j][letter_pos] == "$":
                            self.board[j][letter_pos] = player_name
                if i == 1:
                    for j in range(l,number_pos+1,1):
                        if self.board[j][letter_pos] == "$":
                            self.board[j][letter_pos] = player_name
                if i == 2:
                    for j in range(l,letter_pos-1,-1):
                        if self.board[number_pos][j] == "$":
                            self.board[number_pos][j] = player_name
                if i ==3:
                    for j in range(l,letter_pos+1,1):
                        if self.board[number_pos][j] == "$":
                            self.board[number_pos][j] = player_name
                if i == 4:
                    for j in range(l,-1,-1):
                        if self.board[number_pos+j][letter_pos+j] == "$":
                            self.board[number_pos+j][letter_pos+j] = player_name
                if i == 5:
                    for j in range(l,-1,-1):
                        if self.board[number_pos+j][letter_pos-j] == "$":
                            self.board[number_pos+j][letter_pos-j] = player_name
                if i == 6:
                    for j in range(l,-1,-1):
                        if self.board[number_pos-j][letter_pos+j] == "$":
                            self.board[number_pos-j][letter_pos+j] = player_name
                if i == 7:
                    for j in range(l,-1,-1):
                        if self.board[number_pos-j][letter_pos-j] == "$":
                            self.board[number_pos-j][letter_pos-j] = player_name

    #runs through a single turn for a player
    def player_turn(self,player_name,old_board_config,old_score):
        #gendrates legal moves, returns 1 if no legal moves
        legal_moves = self.generate_next_moves(player_name)
        if legal_moves == []:
            print "No valid moves"
            return 1

        #initial input
        letter_pos, number_pos = self.input_pos(player_name)
        letter_pos_int = VALID_COLUMN.index(letter_pos)+1
        move = (number_pos,letter_pos_int)

        #check input is in legal moves
        while move not in legal_moves:
            print "Invalid move, try agian"
            letter_pos,number_pos = self.input_pos(player_name)
            letter_pos_int = VALID_COLUMN.index(letter_pos)+1
            move = (number_pos,letter_pos_int)

        #puts tile on board
        self.board[number_pos][VALID_COLUMN.index(letter_pos)+1] = player_name

        #increment score for the tile that was placed
        if player_name == "B":
            self.score[0] = self.score[0]+1
        else:
            self.score[1] = self.score[1]+1

        #highlights tiles to be flipped, and increases score
        flip_helper,flip_helper2 = self.flip_tiles(number_pos,letter_pos_int,player_name,old_board_config,old_score)

        self.display_board()

        good_move = raw_input("Was this move done correctly? (y/n) ")
        while good_move not in ["y","n"]:
            good_move = raw_input("(y/n) ")

        #if move wasn't done correctly go back and reinput
        while good_move == "n":
            print "move not done correctly "
            self.board = copy.deepcopy(old_board_config)
            self.score = copy.deepcopy(old_score)
            self.display_board()

            letter_pos, number_pos = self.input_pos(player_name)
            letter_pos_int = VALID_COLUMN.index(letter_pos)+1

            move = (number_pos,letter_pos_int)

            while move not in legal_moves:
                print "Invalid move, try agian"
                letter_pos,number_pos = self.input_pos(player_name)
                letter_pos_int = VALID_COLUMN.index(letter_pos)+1
                move = (number_pos,letter_pos_int)


            #puts tile on board
            self.board[number_pos][VALID_COLUMN.index(letter_pos)+1] = player_name
            #increment score for the tile that was placed
            if player_name == "B":
                self.score[0] = self.score[0]+1
            else:
                self.score[1] = self.score[1]+1

            #flips whatever other tiles need to be flipped and changes score
            flip_helper,flip_helper2 = self.flip_tiles(number_pos,letter_pos_int,player_name,old_board_config,old_score)

            self.display_board()

            good_move = raw_input("Was this move done correctly? (y/n) ")
            while good_move not in ["y","n"]:
                good_move = raw_input("(y/n) ")

        #finishes flip by flipping highlighted tiles
        self.flip2(number_pos,letter_pos_int,player_name,flip_helper,flip_helper2)

        return 0
###################################################################################################
#start of adding in ab pruning

    def maxVal(graph,node,alpha,beta,level):
        print node
        level = level + 1
        if isinstance(node,int):
            return node
        if int(level) > int(DEPTH_BOUND):
            return ord(node)
        v = float("-inf")
        for child in graph.get(node):
            v1 = minVal(graph,child,alpha,beta,level)
            if v is None or v1 > v:
                v = v1
            if beta is not None:
                if v1 >= beta:
                    return v
            if alpha is None or v1 > alpha:
                alpha = v1
        return v

    def minVal(graph,node,alpha,beta,level):
        print node
        level = level + 1
        if isinstance(node,int):
            return node
        if int(level) > int(DEPTH_BOUND):
            return ord(node)
        v = float("inf")
        for child in graph.get(node):
            v1 = maxVal(graph,child,alpha,beta,level)
            if v is None or v1 < v:
                v = v1
            if alpha is not None:
                if v1 <= alpha:
                    return v
            if beta is None or v1 < beta:
                beta = v1
        return v

    def heuristic(self,player_name,board,level):
        # high value = good

        if player_name == "B":
            heuristic_val = board.score[0]
        else:
            heuristic_val = board.score[1]

        #subtracting for level, because higher level = bad
        #heuristic_val = heuristic_val - (2**level)

        #checking corner spots, really want corner spots
        if board.board[1][1] == player_name:
            heuristic_val = heuristic_val + 100
        if board.board[1][8] == player_name:
            heuristic_val = heuristic_val + 100
        if board.board[8][1] == player_name:
            heuristic_val = heuristic_val + 100
        if board.board[8][8] == player_name:
            heuristic_val = heuristic_val + 100

        #maybe add checking
        return heuristic_val

    def generate_next_board(self,player_name,next_moves,board_state):
        next_boards = []



        for move in next_moves:
            temp_board = copy.deepcopy(board_state)
            #old stuff dosnt matter, dont use it in this implementation
            old_score = 0
            old_board_config = 0

            flip_helper,flip_helper2 = temp_board.flip_tiles(move[0],move[1],player_name,old_board_config,old_score)
            temp_board.flip2(move[0],move[1],player_name,flip_helper,flip_helper2)
            next_boards.append(temp_board)


        return next_boards

    def get_scores(self,player_name,next_boards,level):
        scores = []
        for board in next_boards:
            scores.append(self.heuristic(player_name,board,level))

        return scores

    def make_graph(self,player_name,board,score):
        scores = []
        next_moves = []
        temp_board = copy.deepcopy(self)


        if player_name == "B":
            opposite_name = "W"
        else:
            opposite_name = "B"

        next_moves.append(temp_board.generate_next_moves(player_name))

        next_boards = self.generate_next_board(player_name, next_moves[0],temp_board)

        for board in next_boards:
            board.display_board()

        scores.append(self.get_scores(player_name,next_boards,1))

        #for board in next_boards:
        #    next_moves.append(board.generate_next_moves(player_name))

        print next_moves
        print scores
        exit()
        return graph



    def abprune(self,player_name):

        graph = self.make_graph(player_name,self.board,self.score)

        if player_name == "B":
            maxVal(graph,root,alpha,beta,level)
        else:
            minVal(graph,root,alpha,beta,level)



        return number_pos, letter_pos

# end of AI code
##################################################################################################
    def display_board2(self,board_state):
        for row in board_state.board:
            print(row)
        print "Score B = " + str(board_state.score[0])
        print "Score W = " + str(board_state.score[1])
        print("")

def main():

    game = Othello()

    #game.display_board()

    game.abprune("B")
    exit()

    change_board = raw_input("Would you like to change board config (y/n): " )
    if change_board == "y":
        game.swap_board()
        game.display_board()



    player_roles = raw_input("Do you want to be B or W? ")
    while player_roles not in ["B","W"]:
        player_roles = raw_input("invalid answer (B or W) ")


    if player_roles == "W":
        for i in range(30):
            print "AI: I am about to make a move"
            approve = raw_input("P do you approve (y/n)? ")
            while approve not in ["y","n"]:
                approve = raw_input("y/n: ")

            old_board_config = copy.deepcopy(game.board)
            old_score = copy.deepcopy(game.score)

            start = time.time()
            print "This is where AI would return (Letter,Number) of next move"
            end = time.time()
            print "Time AI took : " + str(end - start) + " s"

            if end-start > 10:
                print "AI took too long game over, player wins"
                exit()


            b_moves = game.player_turn("B",old_board_config,old_score)

            if b_moves == 1:
                print "AI: i cannot make a move :("

            game.display_board()

            old_board_config = copy.deepcopy(game.board)
            old_score = copy.deepcopy(game.score)
            print "P it is now your turn to make a move"
            w_moves = game.player_turn("W",old_board_config,old_score)

            if w_moves  == 1:
                print "player cannot make a move"

            if b_moves == 1 and w_moves == 1:
                print "no more possible moves, game over"
                break

            game.display_board()
    if player_roles == "B":
        for i in range(30):

            old_board_config = copy.deepcopy(game.board)
            old_score = copy.deepcopy(game.score)
            print "P it is now your turn to make a move"
            b_moves = game.player_turn("B",old_board_config,old_score)

            if b_moves  == 1:
                print "player cannot make a move"

            game.display_board()

            print "AI: I am about to make a move"
            approve = raw_input("P do you approve (y/n)? ")
            while approve not in ["y","n"]:
                approve = raw_input("y/n: ")

            old_board_config = copy.deepcopy(game.board)
            old_score = copy.deepcopy(game.score)

            start = time.time()
            print "This is where AI would return (Letter,Number) of next move"
            end = time.time()
            print "Time AI took : " + str(end - start) + " s"

            if end-start > 10:
                print "AI took too long game over, player wins"
                exit()


            w_moves = game.player_turn("W",old_board_config,old_score)

            if w_moves == 1:
                print "AI: i cannot make a move :("

            game.display_board()



            if b_moves == 1 and w_moves == 1:
                print "no more possible moves, game over"
                break

            game.display_board()





    print "B final score = " + str(game.score[0])
    print "W final score = " + str(game.score[1])

    if game.score[0] > game.score[1]:
        print "Black wins!"
    elif game.score[0] < game.score[1]:
        print "White wins!"
    else:
        print "tie game"




main()
