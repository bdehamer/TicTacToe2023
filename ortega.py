team_name = 'Ortega'
strategy_name = 'Too Many ifs'
strategy_description = 'Try not to lose'
import random

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2]+'\n')

def move(player, board, score):
  r = random.randint(0,2)
  c = random.randint(0,2)
  
  if player == 'X': #CHECKS FOR X WIN CONDITION ------------------
    if board[0][0] == 'X' and board[0][1] == board[0][0]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[0][0] == 'X' and board[1][0] == board[0][0]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[0][0] == 'X' and board[1][1] == board[0][0]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[0][2] == 'X' and board[0][1] == board[0][2]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[0][2] == 'X' and board[1][2] == board[0][2]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[0][2] == 'X' and board[1][1] == board[0][2]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[2][2] == 'X' and board[1][2] == board[2][2]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[2][2] == 'X' and board[2][1] == board[2][2]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[2][2] == 'X' and board[1][1] == board[2][2]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[2][0] == 'X' and board[1][0] == board[2][0]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[2][0] == 'X' and board[2][1] == board[2][0]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[2][0] == 'X' and board[1][1] == board[2][0]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[1][1] == 'X' and board[0][1] == board[1][1]:
      if board[2][1] == ' ':
        r = 2
        c = 1
    elif board[1][1] == 'X' and board[1][2] == board[1][1]:
      if board[1][0] == ' ':
        r = 1
        c = 0
    elif board[1][1] == 'X' and board[2][1] == board[1][1]:
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[1][1] == 'X' and board[1][0] == board[1][1]:
      if board[1][2] == ' ':
        r = 1
        c = 2
    elif board[0][0] == 'X' and board[2][2] == board[0][0]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[0][0] == 'X' and board[2][0] == board[0][0]:
      if board[1][0] == ' ':
        r = 1
        c = 0
    elif board[0][0] == 'X' and board[0][2] == board[0][0]:
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[2][2] == 'X' and board[0][2] == board[2][2]:
      if board[1][2] == ' ':
        r = 1
        c = 2
    elif board[2][2] == 'X' and board[2][0] == board[2][2]:
      if board[2][1] == ' ':
        r = 2
        c = 1
    elif board[0][2] == 'X' and board[2][0] == board[0][2]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[0][1] == 'X' and board[2][1] == board[0][1]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[1][0] == 'X' and board[1][2] == board[1][0]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    else: #CHECKS FOR O WIN CONDITION ------------------
      if board[0][0] == 'O' and board[0][1] == board[0][0]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[0][0] == 'O' and board[1][0] == board[0][0]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[0][0] == 'O' and board[1][1] == board[0][0]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[0][2] == 'O' and board[0][1] == board[0][2]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[0][2] == 'O' and board[1][2] == board[0][2]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[0][2] == 'O' and board[1][1] == board[0][2]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[2][2] == 'O' and board[1][2] == board[2][2]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[2][2] == 'O' and board[2][1] == board[2][2]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[2][2] == 'O' and board[1][1] == board[2][2]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[2][0] == 'O' and board[1][0] == board[2][0]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[2][0] == 'O' and board[2][1] == board[2][0]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[2][0] == 'O' and board[1][1] == board[2][0]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[1][1] == 'O' and board[0][1] == board[1][1]:
        if board[2][1] == ' ':
          r = 2
          c = 1
      elif board[1][1] == 'O' and board[1][2] == board[1][1]:
        if board[1][0] == ' ':
          r = 1
          c = 0
      elif board[1][1] == 'O' and board[2][1] == board[1][1]:
        if board[0][1] == ' ':
          r = 0
          c = 1
      elif board[1][1] == 'O' and board[1][0] == board[1][1]:
        if board[1][2] == ' ':
          r = 1
          c = 2
      elif board[0][0] == 'O' and board[2][2] == board[0][0]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[0][0] == 'O' and board[2][0] == board[0][0]:
        if board[1][0] == ' ':
          r = 1
          c = 0
      elif board[0][0] == 'O' and board[0][2] == board[0][0]:
        if board[0][1] == ' ':
          r = 0
          c = 1
      elif board[2][2] == 'O' and board[0][2] == board[2][2]:
        if board[1][2] == ' ':
          r = 1
          c = 2
      elif board[2][2] == 'O' and board[2][0] == board[2][2]:
        if board[2][1] == ' ':
          r = 2
          c = 1
      elif board[0][2] == 'O' and board[2][0] == board[0][2]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[0][1] == 'O' and board[2][1] == board[0][1]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[1][0] == 'O' and board[1][2] == board[1][0]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      else:
        if board[1][1] == ' ':
          r = 1
          c = 1
        else:
          while board[r][c] != ' ':
            r = random.randint(0,2)
            c = random.randint(0,2)

    
  elif player == 'O':
    if board[0][0] == 'O' and board[0][1] == board[0][0]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[0][0] == 'O' and board[1][0] == board[0][0]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[0][0] == 'O' and board[1][1] == board[0][0]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[0][2] == 'O' and board[0][1] == board[0][2]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[0][2] == 'O' and board[1][2] == board[0][2]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[0][2] == 'O' and board[1][1] == board[0][2]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[2][2] == 'O' and board[1][2] == board[2][2]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[2][2] == 'O' and board[2][1] == board[2][2]:
      if board[2][0] == ' ':
        r = 2
        c = 0
    elif board[2][2] == 'O' and board[1][1] == board[2][2]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[2][0] == 'O' and board[1][0] == board[2][0]:
      if board[0][0] == ' ':
        r = 0
        c = 0
    elif board[2][0] == 'O' and board[2][1] == board[2][0]:
      if board[2][2] == ' ':
        r = 2
        c = 2
    elif board[2][0] == 'O' and board[1][1] == board[2][0]:
      if board[0][2] == ' ':
        r = 0
        c = 2
    elif board[1][1] == 'O' and board[0][1] == board[1][1]:
      if board[2][1] == ' ':
        r = 2
        c = 1
    elif board[1][1] == 'O' and board[1][2] == board[1][1]:
      if board[1][0] == ' ':
        r = 1
        c = 0
    elif board[1][1] == 'O' and board[2][1] == board[1][1]:
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[1][1] == 'O' and board[1][0] == board[1][1]:
      if board[1][2] == ' ':
        r = 1
        c = 2
    elif board[0][0] == 'O' and board[2][2] == board[0][0]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[0][0] == 'O' and board[2][0] == board[0][0]:
      if board[1][0] == ' ':
        r = 1
        c = 0
    elif board[0][0] == 'O' and board[0][2] == board[0][0]:
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[2][2] == 'O' and board[0][2] == board[2][2]:
      if board[1][2] == ' ':
        r = 1
        c = 2
    elif board[2][2] == 'O' and board[2][0] == board[2][2]:
      if board[2][1] == ' ':
        r = 2
        c = 1
    elif board[0][2] == 'O' and board[2][0] == board[0][2]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[0][1] == 'O' and board[2][1] == board[0][1]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[1][0] == 'O' and board[1][2] == board[1][0]:
      if board[1][1] == ' ':
        r = 1
        c = 1
    else:
      if board[0][0] == 'X' and board[0][1] == board[0][0]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[0][0] == 'X' and board[1][0] == board[0][0]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[0][0] == 'X' and board[1][1] == board[0][0]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[0][2] == 'X' and board[0][1] == board[0][2]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[0][2] == 'X' and board[1][2] == board[0][2]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[0][2] == 'X' and board[1][1] == board[0][2]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[2][2] == 'X' and board[1][2] == board[2][2]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[2][2] == 'X' and board[2][1] == board[2][2]:
        if board[2][0] == ' ':
          r = 2
          c = 0
      elif board[2][2] == 'X' and board[1][1] == board[2][2]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[2][0] == 'X' and board[1][0] == board[2][0]:
        if board[0][0] == ' ':
          r = 0
          c = 0
      elif board[2][0] == 'X' and board[2][1] == board[2][0]:
        if board[2][2] == ' ':
          r = 2
          c = 2
      elif board[2][0] == 'X' and board[1][1] == board[2][0]:
        if board[0][2] == ' ':
          r = 0
          c = 2
      elif board[1][1] == 'X' and board[0][1] == board[1][1]:
        if board[2][1] == ' ':
          r = 2
          c = 1
      elif board[1][1] == 'X' and board[1][2] == board[1][1]:
        if board[1][0] == ' ':
          r = 1
          c = 0
      elif board[1][1] == 'X' and board[2][1] == board[1][1]:
        if board[0][1] == ' ':
          r = 0
          c = 1
      elif board[1][1] == 'X' and board[1][0] == board[1][1]:
        if board[1][2] == ' ':
          r = 1
          c = 2
      elif board[0][0] == 'X' and board[2][2] == board[0][0]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[0][0] == 'X' and board[2][0] == board[0][0]:
        if board[1][0] == ' ':
          r = 1
          c = 0
      elif board[0][0] == 'X' and board[0][2] == board[0][0]:
        if board[0][1] == ' ':
          r = 0
          c = 1
      elif board[2][2] == 'X' and board[0][2] == board[2][2]:
        if board[1][2] == ' ':
          r = 1
          c = 2
      elif board[2][2] == 'X' and board[2][0] == board[2][2]:
        if board[2][1] == ' ':
          r = 2
          c = 1
      elif board[0][2] == 'X' and board[2][0] == board[0][2]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[0][1] == 'X' and board[2][1] == board[0][1]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      elif board[1][0] == 'X' and board[1][2] == board[1][0]:
        if board[1][1] == ' ':
          r = 1
          c = 1
      else:
        if board[1][1] == ' ':
          r = 1
          c = 1
        else:
          while board[r][c] != ' ':
            r = random.randint(0,2)
            c = random.randint(0,2)
  return r, c