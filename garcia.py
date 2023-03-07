import random
team_name = 'garcia'
strategy_name = 'holy strategy'
strategy_description = 'cross'
    
def move(player, board, score):
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif board[0][1] == ' ' and board[2][1] == ' ':
    r = 0
    c = 1
  elif board[0][1] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[1][0] == ' ' and board[1][2] == ' ':
    r = 1
    c = 0
  elif board[1][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  return r,c

''' 
  
  return r, c
    if board[1][1] == ' ':
      r = 1
      c = 1
    elif board[0][0] == ' ' and board[2][2] == ' ':
      r = 0
      c = 0
    elif board[0][0] == player and board[2][2] == ' ':
      r = 2
      c = 2
    elif board[0][2] == ' ' and board[2][0] == ' ':
      r = 0
      c = 2
    elif board[0][2] == player and board[2][0] == ' ':
      r = 2
      c = 0
  print(r,c)
  print_board(board)
  return r,c
'''
  
    

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])