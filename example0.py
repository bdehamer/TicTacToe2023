team_name = 'E0'
strategy_name = 'Next Open'
strategy_description = 'Play the next open spot.'
    
def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  
  return r, c