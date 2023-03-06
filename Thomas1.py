import random
team_name = 'E1'
strategy_name = 'Random'
strategy_description = 'Play a random open spot.'
    
def move(player, board, score):
  r = random.randint(0,2)
  c = random.randint(0,2)

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  return r, c