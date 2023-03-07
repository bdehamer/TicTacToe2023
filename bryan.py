team_name = 'bryan'
strategy_name = 'just picking spots tbh'
strategy_description = 'best spots'


def move(player, board, score):
  r = 0
  c = 0
  if board[0][0] == ' ':
    c=0
    r=0
  elif board[1][1] == ' ':
    c = 1
    r = 1
  elif board[0][2] == ' ':
    c = 2
    r = 0
  elif board[2][0] == ' ':
    r = 2
    c = 0
  elif board[0][1] == ' ':
    r = 0
    c = 1
  elif board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][2] == ' ':
    r=1
    c=2
  elif board[1][0] == ' ':
    r=1
    c=0
  else:
    r=2
    c=1
  
  return r, c
