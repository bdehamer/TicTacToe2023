team_name = 'jeremiah'
strategy_name = 'Storm'
strategy_description = 'Check for possible wins or losses and then play accordingly.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  
def move(player, board, score):
  if player == 'X' and score == 0:
    r = 1
    c = 1
  
  if board[0][1] == ' ':
    r = 0
    c = 1
  #top left
  elif ((board[0][1] and board[0][2] == ' ') or (board[2][0] and board[1][0] != ' ') or (board[1][1] and board[2][2] != ' ')) and (board[0][0] == ' '):
    r = 0
    c = 0
  #top middle
  elif ((board[0][0] and board[0][2] != ' ') or (board[2][1] and board[1][1] != ' ')) and (board[0][1] == ' '):
    r = 0
    c = 1
  #top right
  elif ((board[0][0] and board[0][1] != ' ') or (board[2][0] and board[1][1] != ' ') or (board[2][2] and board[1][2] != ' ') or (board[0][1] and board[2][1] != ' ')) and (board[0][2] == ' '):
    r = 0
    c = 2
  #middle left
  elif ((board[1][1] and board[1][2] != ' ') or (board[0][0] and board[2][0] != ' ')) and (board[1][0] == ' '):
    r = 1
    c = 0
  #middle right
  elif ((board[1][0] and board[1][1] != ' ') or (board[2][0] and board[2][2] != ' ')) and (board[1][2] == ' '):
    r = 1
    c = 2
  #middle
  elif ((board[0][0] and board[2][2] != ' ') or (board[2][0] and board[0][2] != ' ') or (board[1][0] and board[1][2] != ' ')) and (board[1][1] == ' '):
    r = 1
    c = 1
  #bottom left
  elif ((board[0][0] and board[1][0] != ' ') or (board[1][1] and board[0][2] != ' ')) and (board[2][0] == ' '):
    r = 2
    c = 0
  #bottom right
  elif ((board[2][0] and board[2][1] != ' ') or (board[1][2] and board[0][2] != ' ') or (board[0][0] and [1][1] != " ")) and (board[2][2] == ' '):
    r = 2
    c = 2
  #bottom mid
  elif ((board[2][0] and board[2][2] != ' ') or (board[0][1] and board[1][1] != ' ')) and (board[2][1] == ' '):
    r = 2
    c = 1

  #checking for wins
    #top left
  elif ((board[0][1] and board[0][2] == player) or (board[2][0] and board[1][0] == player) or (board[1][1] and board[2][2] == player)) and (board[0][0] == ' '):
    r = 0
    c = 0
  #top middle
  elif ((board[0][0] and board[0][2] == player) or (board[2][1] and board[1][1] == player)) and (board[0][1] == ' '):
    r = 0
    c = 1
  #top right
  elif ((board[0][0] and board[0][1] == player) or (board[2][0] and board[1][1] == player) or (board[2][2] and board[1][2] == player) or (board[0][1] and board[2][1] == player)) and (board[0][2] == ' '):
    r = 0
    c = 2
  #middle left
  elif ((board[1][1] and board[1][2] == player) or (board[0][0] and board[2][0] == player)) and (board[1][0] == ' '):
    r = 1
    c = 0
  #middle right
  elif ((board[1][0] and board[1][1] == player) or (board[2][0] and board[2][2] == player)) and (board[1][2] == ' '):
    r = 1
    c = 2
  #middle
  elif ((board[0][0] and board[2][2] == player) or (board[2][0] and board[0][2] == player) or (board[1][0] and board[1][2] == player)) and (board[1][1] == ' '):
    r = 1
    c = 1
  #bottom left
  elif ((board[0][0] and board[1][0] == player) or (board[1][1] and board[0][2] == player )) and (board[2][0] == ' '):
    r = 2
    c = 0
  #bottom right
  elif ((board[2][0] and board[2][1] == player) or (board[1][2] and board[0][2] == player) or (board[0][0] and [1][1] == player)) and (board[2][2] == ' '):
    r = 2
    c = 2
  #bottom mid
  elif ((board[2][0] and board[2][2] == player) or (board[0][1] and board[1][1] == player)) and (board[2][1] == ' '):
    r = 2
    c = 1

    #moves list
  elif board[1][1] == ' ':
    r = 1
    c = 1
  elif board[2][1] == ' ':
    r = 2
    c = 1
  elif board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][0] == ' ':
    r = 2
    c = 1
  elif board[0][0] == ' ':
    r = 0
    c = 0
  elif board[2][2] == ' ':
    r = 2
    c = 2
  elif board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][2] == ' ':
    r = 1
    c = 2
  return r, c