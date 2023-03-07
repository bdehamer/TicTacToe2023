import random
team_name = 'McDonough'
strategy_name = 'McD strat'
strategy_description = 'Play the corners and then finish the line.'

def move(player, board, score):
  if board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == ' ':
    r= 1
    c=1
  elif board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][2] == ' ':
    r= 2
    c=2
  elif board[0][1] == ' ':
    r= 0
    c= 1
  elif board[2][0] == ' ':
    r= 2
    c= 0
  elif board[1][2] == ' ':
    r= 1 
    c=2

  else: 
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  return r, c