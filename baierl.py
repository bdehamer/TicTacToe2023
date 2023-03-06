team_name = 'baierl'
strategy_name = 'Center -> corners -> last open'
strategy_description = 'Play the center, fill the corners, then play the last open spots'

def move(player, board, score):
  i = 0
  corners = [[0, 2, 0, 2],
             [2, 2, 0, 0]] #in order of top right, bottom right, top left, bottom left

  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c
    
  while i < 4:
    r = corners[0][i]
    c = corners[1][i]

    if board[r][c] == ' ':
      return r, c
    i += 1
    
  if i == 4: # if at least three corners are filled
    while board[r][c] != ' ':
      c -= 1
      if c < 0:
        c = 2  
        r -= 1
        if r < 0:
          r = 2
  return r, c