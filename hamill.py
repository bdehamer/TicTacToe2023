import random

team_name = 'hamill'
strategy_name = 'Corner'
strategy_description = 'Tries to get three or for corners and then gets three in a row in anyway that is possible'

game = 0
old_score = 0
old_player = ' '
last_player = ' '
history = []
old_board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  if board[0][2] == ' ':
    r = 0
    c = 2
  elif board[0][0] == ' ' and board[2][0] == ' ':
    r = 2
    c = 0
  elif board[2][0] == player and board[1][1] == ' ':
    r = 1
    c = 1
  elif board[2][2] == ' ' and board[1][0] == ' ':
    r = 2
    c = 2
  elif board[2][2] == player and board[1][2] == ' ':
    r = 1
    c = 2
  elif board[1][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  #print_board(board)
  return r, c
  
  '''
  if old_score != score:
    old_player = last_player
    if score < old_score:
      print("Loss as", old_player)
    elif score > old_score:
      print("Win as", old_player)
    else:
      print("Cats as", old_player)
    print_board(old_board)
    game = game + 1
    print("new game", game)
   '''
  