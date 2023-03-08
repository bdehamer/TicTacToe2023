team_name = 'farmer'
strategy_name = 'L strategy'
strategy_description = 'Makes an L'
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  if board[1][1] == ' ':
    c = 1
    r = 1
  # middle, top middle, top right
  elif board[1][1] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][1] == player and board[0][1] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #middle, top middle, top left
  elif board[1][1] == player and board[0][1] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[0][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #Middle, left middle, and top left
  elif board[1][1] == player and board[0][0] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[0][0] == player and board[1][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  #Middle, left middle, bottom left
  elif board[1][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[1][0] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[1][0] == player and board[2][0] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[1][0] == player and board[2][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[1][0] == player and board[2][0] == player and board[0][0] == ' ':
    r = 0
    c = 0
#Middle, bottom middle, bottom left
  elif board[1][1] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[1][1] == player and board[2][1] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[2][1] == player and board[2][0] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[2][1] == player and board[2][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[2][1] == player and board[2][0] == player and board[0][1] == ' ':
    r = 0
    c = 1
  #middle, bottom middle, bottom right
  elif board[1][1] == player and board[2][1] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[2][1] == player and board[2][2] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[2][1] == player and board[2][2] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[2][1] == player and board[2][0] == player and board[0][1] == ' ':
    r = 0
    c = 1
  #Middle, right middle, top right
  elif board[1][1] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[1][2] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[1][1] == player and board[1][2] == player and board[0][2] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[1][1] == player and board[1][2] == player and board[0][2] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[1][2] == player and board[0][2] == player and board[1][0] == ' ':
    r = 1
    c = 0
  #Middle, right middle, bottom right
  elif board[1][1] == player and board[1][2] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][1] == player and board[1][2] == player and board[2][2] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[1][1] == player and board[1][2] == player and board[2][2] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[1][2] == player and board[2][2] == player and board[0][2] == ' ':
    r = 0
    c = 2
  #Middle, top middle, left middle
  elif board[1][1] == player and board[0][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[1][0] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[1][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #Middle, top middle, right middle
  elif board[1][1] == player and board[0][1] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[0][1] == player and board[1][2] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[1][2] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][1] == player and board[0][1] == player and board[1][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  #Middle, left middle, bottom middle
  elif board[1][1] == player and board[1][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[1][1] == player and board[1][0] == player and board[2][1] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][1] == player and board[1][0] == player and board[2][1] == player and board[1][2] == ' ':
    r = 1
    c = 2
  #Middle, right middle, bottom middle
  elif board[1][1] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][1] == player and board[1][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[1][1] == player and board[1][2] == player and board[2][1] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][1] == player and board[1][0] == player and board[2][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  #Bottom left, bottom middle, left middle
  elif board[2][0] == ' ':
    r = 2
    c = 0
  elif board[2][0] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[2][0] == player and board[2][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[2][0] == player and board[2][1] == player and board[1][0] == player and board[2][2] == ' ':
    r = 2
    c = 2
  elif board[2][0] == player and board[2][1] == player and board[1][0] == player and board[0][0] == ' ':
    r = 0
    c = 0
  #Bottom right, bottom middle, right middle
  elif board[2][2] == ' ':
    r = 2
    c = 2
  elif board[2][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  elif board[2][2] == player and board[2][1] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[2][2] == player and board[2][1] == player and board[1][2] == player and board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][2] == player and board[2][1] == player and board[1][2] == player and board[2][0] == ' ':
    r = 2
    c = 0
  #Top right, middle right, top middle
  elif board[0][2] == ' ':
    r = 0
    c = 2
  elif board[0][2] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[0][2] == player and board[1][2] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[0][2] == player and board[1][2] == player and board[0][1] == player and board[0][0] == ' ':
    r = 0
    c = 0
  elif board[0][2] == player and board[1][2] == player and board[0][1] == player and board[2][2] == ' ':
    r = 2
    c = 2
  #Top left, top middle, middle left
  elif board[0][0] == ' ':
    r = 0
    c = 0
  elif board[0][0] == player and board[0][1] == ' ':
    r = 0
    c = 1
  elif board[0][0] == player and board[0][1] == player and board[1][0] == ' ':
    r = 1
    c = 0
  elif board[0][0] == player and board[0][1] == player and board[1][0] == player and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[0][0] == player and board[0][1] == player and board[1][0] == player and board[0][2] == ' ':
    r = 0
    c = 2




  else:
    r = 0
    c = 0
      
      
      

  return r, c