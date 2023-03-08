team_name = 'lelevier'
strategy_name = 'Lelevier Strategy'
strategy_description = 'The Google Strategy'
    
def move(player, board, score):
  if board [2][2] == ' ' and board [2][2] != player:
    r=2
    c=2
  elif board [2][0] == ' ' and board [2][0] != player:
    r=2
    c=0
  elif board [0][2] == ' ' and board [0][2] != player:
    r=0
    c=2
  elif board [0][0] == ' ' and board [0][0] != player:
    r=0
    c=0
    
  if board [1][1] == ' ' and board [1][1] != player:
    r=1
    c=1
  elif board [0][1] == ' ' and board [0][1] != player:
    r=0
    c=1
  elif board [2][1] == ' ' and board [2][1] != player:
    r=2
    c=1
  elif board [1][0] == ' ' and board [1][0] != player:
    r=1
    c=0
  elif board [1][2] == ' ' and board [1][2] != player:
    r=1
    c=2

  return r,c
    
  
  