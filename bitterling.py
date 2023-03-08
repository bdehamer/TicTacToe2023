team_name = 'bitterling'
strategy_name = 'bitterling strategy'
strategy_description = "great"
import random
"""X plays 1st" """
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
    r = 1
    c = 1
   # r = random.randint(0,2)
    #c = random.randint(0,2)
    if board[0][0] == ' ' and board[0][0] != player:
      r = 0
      c = 0

    elif board[2][0] == ' ' and board[2][0] != player:
      r = 2
      c = 0  
    elif board[0][2] == ' ' and board[0][2] != player:
      r = 2
      c = 0  
    elif board[r][c] != ' ':
      
      r = random.randint(0,2)
      c = random.randint(0,2)
  #print_board(board)
    return r, c