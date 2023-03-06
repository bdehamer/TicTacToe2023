team_name = 'E0'
strategy_name = 'Best'
strategy_description = 'Play the best.'

import random
def move(player, board, score):
  if player == 'X':
    r = 0
    c = 0
    if board[r][c] != ' ':
      r = 2
      c = 2
    else:
      if board[r][c] != ' ':
        r = 2
        c = 0
      else:
        if board[1][0] != ' ':
          r = 2
          c = 1
        else:
          r = 1
          c = 0
          if board[r][c] != ' ':
            r = random.randint(0,2)
            c = random.randint(0,2)
      
  else:
    r = 1
    c = 1
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
      
    
  
  return r, c