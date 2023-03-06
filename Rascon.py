import random
team_name = 'Rascon'
strategy_name = 'Samuel you a****** you better not steal my strategy'
strategy_description = 'Blocking + idk'

def check_works(board, r, c):
  r = random.randint(0,2)
  c = random.randint(0,2)
  if board[r][c] != ' ':
    return r, c
  else:
    check_works(board, r, c,)

def move(player, board, score):

  r = 0
  c = 0

 
    #_____Checks_Corners_and_Center_____#
  if board[1][1] == ' ': #center
    r = 1
    c = 1
  elif board[0][0] == ' ': #top right
    r = 0
    c = 0
  elif board[0][2] == ' ': #top left
    r = 0
    c = 2
  elif board[2][0] == ' ': #bottom right
    r = 2
    c = 0
  elif board[2][2] == ' ': #bottom left
    r = 2
    c = 2

    #____Checks_for_possilbe_rows/colums_____#
  elif board[0][0] and board [2][0] == player or ' ': #mid left
    r = 1
    c = 0
  elif board[0][2] and board [2][2] == player or ' ': #mid right
    r = 1
    c = 2
  elif board[0][0] and board [0][2] == player or ' ': #mid top
    r = 0
    c = 1
  elif board[2][0] and board [2][2] == player or ' ': #mid bottom
    r = 2
    c = 1
    
  #_____Checks_and_Blocks_____#
  elif board[0][0] and board [2][0] != player: #mid left
    r = 1
    c = 0
  elif board[0][2] and board [2][2] != player: #mid right
    r = 1
    c = 2
  elif board[0][0] and board [0][2] != player: #mid top
    r = 0
    c = 1
  elif board[2][0] and board [2][2] != player: #mid bottom
    r = 2
    c = 1

  else:
    check_works(board, r, c)
  
  return r, c


