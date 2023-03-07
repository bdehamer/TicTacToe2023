import random

team_name = 'mendoza'
strategy_name = 'try not to lose strategy'
strategy_description = 'trying not to lose'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  #print_board(board)
  if (player == "X"):
    if (board[0][0] == ' '):
      c = 0
      r = 0
    elif (board[0][1] == ' ' and board[0][2] == ' '):
      r = 0
      c = 2
    elif (board[0][1] == ' '):
      r = 0
      c = 1
    elif (board[0][1] != player and board[1][1] != player):
      r = 2
      c = 1
    elif (board[0][1] != player and board[1][1] == ' '):
      r=1
      c=1
    elif (board[1][1] != player and board[1][0] != player):
      r = 1
      c = 2
    elif (board[1][1] != player and board[1][2] != player):
      r = 1
      c = 0
    elif (board[1][1] == player and board[0][0] == player and board[2][2] == ' '):
      r = 2
      c=2
    elif (board[1][1] == player and board[0][2] == player and board[2][0] == ' '):
      r=2
      c=0
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
  
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  if (player == "O"):
    if (board[1][1] == ' '):   
      c = 1
      r = 1
    elif (board[0][2] == ' ' and board[2][0] == ' '):
      r=0
      c=2
    elif (board[0][2] == player and board[2][0] == ' '):
      r=2
      c=0
    elif (board[0][2] == player and board[2][0] != player and board[0][0] == ' '):
      r=0
      c=0
    elif (board[0][2] == player and board[2][0] != player and board[2][2] == ' '):
      r=2
      c=2
    elif (board[0][2] == player and board[2][2] == player and board[1][2] == ' '):
      r=1
      c=2
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  return r, c