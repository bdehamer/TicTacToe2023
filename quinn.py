team_name = 'quinn'
strategy_name = 'corner strategy'
strategy_description = 'start with with 3 corners'
import random as rand 

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
    
def move(player, board, score):
  other_spaces = [0, 1, 2]
  r = 0
  c = 1
  if board[0][0] == ' ':
    r = 0
    c = 0
  elif board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == ' ':
    r = 1
    c = 1
  elif board[1][1] == ' ':
    r = 1
    c = 1
  elif board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][2] == ' ':
    r = 1
    c = 2
  else:
    while board[r][c] == ' ':
         r = rand.choice(other_spaces)
         c = rand.choice(other_spaces)
         if board[r][c] == ' ':
           r = r
           c = c
          
  return r, c
    

  

