team_name = 'quinn'
strategy_name = 'quinn strat'
strategy_description = 'start with corners'
import random as rand 

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
    
def move(player, board, score):
  r = 0
  c = 0
  x = 2
  other_spaces = [0, 1, 2]
  corner_r = [2, 0]
  corner_c= [2, 0]
  for i in corner_r:
    for s in corner_c:
     if board[i][s] == ' ':
      r = i
      c = s
     else:
       while x > 1:
         r = rand.choice(other_spaces)
         c = rand.choice(other_spaces)
         if board[r][c] == ' ':
           r = r
           c = c
           x = 0
  return r, c
  

