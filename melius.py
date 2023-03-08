import random

team_name = 'melius'
strategy_name = 'no survivors'
strategy_description = 'Play the next open spot.'

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
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif board[2][1] == ' ':
    r = 2
    c = 1
  elif board[0][1] == ' ':
    r = 0
    c = 1
  elif board[1][0] == ' ':
    r = 1
    c = 0
  elif board[1][2] == ' ':
    r = 1
    c = 2
  else:
    r = random.randint(0,2)
    c = random.randint(0,2)

    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)


  return r,c


    
  
