import random
team_name = 'Rascon'
strategy_name = 'right wing'
strategy_description = 'Go for right column then random'

def place_random(r, c, opp, board, player):
  r = random.randint(0,2)
  c = random.randint(0,2)
  if board[r][c] != player or opp:
    return r, c
  else:
    place_random(r, c, opp, board, player)
    
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  if board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][2] == ' ':
    r = 1
    c = 2
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  return r, c

