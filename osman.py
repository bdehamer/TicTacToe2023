team_name = 'osman'
strategy_name = 'Top Down'
strategy_description = 'Start at the top and go down till you cannot and go back up and repeat for the other columns.'

def move(player, board, score):
  r = 0
  c = 2
  
  while board[r][c] != ' ':
    r += 1
    if r > 2:
      r = 0
      c += 1
    if c > 2:
      c = 0

  return r, c