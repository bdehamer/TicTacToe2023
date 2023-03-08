team_name = 'Pelletier'
strategy_name = 'Corners'
strategy_description = 'Play the next open spot.'
    
def move(player, board, score):
  r=1
  c=1
  if board[1][1] == ' ':
    r=1
    c=1
  elif board[0][2] ==' ':
    r=0
    c=2
  elif board [2][2] ==' ':
    r=2
    c=2
  elif board [2][0] ==' ':
    r=2
    c=0
  elif board [1][2] == ' ':
    r = 1
    c=2
  elif board [2][1] ==' ':
    r = 2
    c=1
  elif board[1][0] ==' ':
    r = 1
    c=0
  elif board [0][0]==' ':
    r=0
    c=0
  elif board[0][1] == ' ':
    r=0
    c=1
  return r,c
