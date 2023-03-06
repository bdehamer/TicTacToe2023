import random
team_name = 'E2'
strategy_name = 'Center then Random'
strategy_description = 'Play center if available, then random'
    
def move(player, board, score):
  r = 1
  c = 1

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  return r, c