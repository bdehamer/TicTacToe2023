team_name = 'farmer'
strategy_name = 'farmer strategy'
strategy_description = 'Take the L'


def move(player, board, score):
  if board[1][1] == ' ':
    c = 1
    r = 1
  # middle, top middle, top right
  elif board[1][1] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][1] == player and board[0][1] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #middle, top middle, top left
  elif board[1][1] == player and board[0][1] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #Middle, left middle, and top left
  elif board[1][1] == player and board[0][0] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  #Middle, top middle, left middle
  elif board[1][1] == player and board[0][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[1][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[1][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  else:
    r = 0
    c = 0
      
      
      

  return r, c