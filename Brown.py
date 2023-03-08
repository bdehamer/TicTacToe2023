team_name = 'Brown'
strategy_name = 'Corner'
strategy_description = 'Corner, middle, cry '
import random
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    if board[0][0] == ' ':
      r = 0
      c = 0
      return r, c
     
    elif board[0][2] == ' ':
      r = 0
      r = 2
      return r, c
      
    elif board[1][1] == ' ':
      r = 1
      c = 1
      return r, c
    
    elif board[2][2] == ' ':
      r = 2
      c = 2
      return r, c
    
    elif board[2][0] == ' ':
      r = 2
      c = 0
      return r, c
    
    if board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
      return r, c
    
    
    

  
  return r, c