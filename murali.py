import random
team_name = 'Murali'
strategy_name = 'murali strategy'
strategy_description = 'take the middle and move up or down and strike through.'

def move(player, board, score):
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif board[0][1] == ' ' and board[2][1] == ' ':
    r = 0
    c = 0
  elif board[0][1] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[1][2] == ' ' and board[2][2] == ' ':
    r = 1
    c = 2
  elif board[1][2] == player and board[2][2] == ' ':
    r = 2
    c = 2
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  return r, c