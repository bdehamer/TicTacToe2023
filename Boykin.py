team_name = 'Boykin'
strategy_name = 'boykin strat'
strategy_description = 'Play the next open spot.'
    
def move(player, board, score):
  if board [1][1] == ' ':
    c = 1
    r = 1
  elif board[0][2] == ' ':
    c = 2
    r = 0
  elif board [0][0] == ' ':
    r = 0
    c = 0
  elif board [0][1] == ' ':
    c = 1
    r = 0
  elif board[2][2] == ' ':
    c = 2
    r = 2
  elif board [1][2] == ' ':
    c = 2
    r = 1
  elif board [2][0]== ' ':
    c = 0 
    r = 2
  elif board [2][1] == ' ':
    c = 1
    r = 2
  elif board [1][0] == ' ':
    c = 0
    r = 1
  return r, c