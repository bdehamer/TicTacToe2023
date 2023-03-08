team_name = 'Salzano'
strategy_name = 'Working Strategy'
strategy_description = 'Takes the corners and tries to create two chances to win, as a bonus it confuses whoever tries to understand the code.'

    
def move(player, board, score):
  if player == "X":
    r = 0
    c = 0
    if board[r][c] == ' ':
      r = 0
      c = 0
    elif board[0][2] == ' ':
      r = 0
      c = 2
    elif board[0][2] == 'X':
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[2][0] == ' ':
      r = 2
      c = 0
    elif board[2][0] == 'X':
      if board[1][0] == ' ':
        r = 1
        c = 0
    else:
      if board[1][1] == ' ':
        r = 1
        c = 1
      elif board[2][2] == ' ':
        r = 2
        c = 2
      elif board[2][1] == ' ':
        r = 2
        c = 1
      elif board[1][2] == ' ':
        r = 1
        c = 2
  else:
    r = 0
    c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  return r,c
