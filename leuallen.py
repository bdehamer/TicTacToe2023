import random
team_name = 'leuallen'
strategy_name = 'leuallen strategy'
strategy_description = 'corner, center, coner?'


def move(player, board, score):
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif board[0][0] == ' ' and board[2][0] == ' ':
    r = 0
    c = 0
  elif board[0][0] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[2][2] == ' ' and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][2] == player and board[0][2] == ' ':
    r = 2
    c = 2
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  return r, c
