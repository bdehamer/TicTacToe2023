team_name = 'osman'
strategy_name = 'Top Down'
strategy_description = 'Start at the top and go down till you cannot and go back up and repeat for the other columns.'

def move(player, board, score):
  r = 0
  #change to random column
  c = 0
  #make so that it goes down at which ever column and then continues on till it has tried all three columns
  while board[r][c] != ' ':
    r += 1
    if r > 2 and c > 0:
      r = 0
      c = 2
    if r > 2:
      r = 0
      c += 1
    if c > 2:
      r = 0

  return r, c