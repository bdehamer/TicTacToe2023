import random 

team_name = 'desrosiers'
strategy_name = 'Blitzkrieg'
strategy_description = 'Defense!! oorah!'

# x always plays first 
## defense strategy -
## if player goes middle, take one corner 
## if player goes anywhere on sides, go middle 

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

# and board[][] != player
def move(player, board, score):
  condition = True
  # useful for if opponent is in space 
  opponent = not(player or ' ')
  # random just in case
  r = 0
  c = 0
  # answers "which player am i this game?"
  # return r,c 
  # takes care of vertical 3
  if(board[0][0] == opponent and board[1][0] == opponent and board[2][0] == ' '):
    if(board[2][0] == ' '): 
      r = 2 
      c = 0
  elif(board[0][0] == opponent and board[2][0] == opponent and board[1][1] == opponent and board[1][2] == opponent and board[1][0] == ' '):
    r = 1 
    c = 0
  elif(board[0][1] == opponent and board[1][1] == opponent and board[2][1] == ' '):
    if(board[2][1] == ' '):
      r = 2 
      c = 1
  elif(board[0][0] == opponent and board[1][1] == opponent and board[2][0] == opponent):
    r = 1
    c = 0
  elif(board[0][2] == opponent and board[1][2] == opponent and board[2][2] == ' '):
    if(board[2][2] == ' '):
      r = 2 
      c = 2
  elif(board[1][0] == opponent and board[2][0] == opponent and board[0][0] == ' '):
    if(board[0][0] == ' '):
      r = 0 
      c = 0
  elif(board[1][1] == opponent and board[2][1] == opponent and board[0][1] == ' '):
    if(board[0][1] == ' '):
      r = 0 
      c = 1
  elif(board[1][2] == opponent and board[2][2] == opponent and board[0][2] == ' '):
    if(board[0][2] == ' '):
      r = 0 
      c = 2
  # takes care of horizontal 3 
  elif(board[0][0] == opponent and board[0][1] == opponent and board[0][2] == ' '):
    if(board[0][2] == ' '):
      r = 0 
      c = 2
  elif(board[1][0] == opponent and board[1][1] == opponent and board[1][2] == ' '):
    if(board[1][2] == ' '):
      r = 1 
      c = 2
  elif(board[2][0] == opponent and board[2][1] == opponent and board[2][2] == ' '):
    if(board[2][2] == ' '):
      r = 2 
      c = 2
  elif(board[0][1] == opponent and board[0][2] == opponent and board[0][0] == ' '):
    if(board[0][0] == ' '):
      r = 0 
      c = 0
  elif(board[1][1] == opponent and board[1][2] == opponent and board[1][0] == ' '):
    if(board[1][0] == ' '):  
      r = 1 
      c = 0
  elif(board[2][1] == opponent and board[2][2] == opponent and board[2][0] == ' '):
    if(board[2][0] == ' '):
      r = 2 
      c = 0
  # L --> R diagonal win 
  elif(board[2][0] == opponent and board[1][1] == opponent and board[0][2] == ' '):
    if(board[0][2] == ' '):
      r = 0 
      c = 2 
  elif(board[0][0] == opponent and board[1][1] == opponent and board[2][2] == ' '):
    r = 2 
    c = 2 
  # R --> L diagonal win 
  elif(board[2][2] == opponent and board[1][1] == opponent and board[0][0] == ' '):
    if(board[0][0] == ' '):
      r = 0
      c = 0
  elif(board[0][2] == opponent and board[1][1] == opponent and board[2][0] == ' '):
    if(board[2][0] == ' '):
      r = 2 
      c = 0
  # horizontal gap win  
  elif(board[0][0] == opponent and board[0][2] == opponent and board[0][1] == ' '):
    if(board[0][1] == ' '):
      r = 0
      c = 1 
  elif(board[1][0] == opponent and board[1][2] == opponent and board[1][1] == ' '):
    if(board[1][1] == ' '):
      r = 1
      c = 1
  elif(board[2][0] == opponent and board[2][2] == opponent and board[2][1] == ' '):
    if(board[2][1] == ' '):
      r = 2
      c = 1
  # vertical gap win 
  elif(board[0][0] == opponent and board[2][0] == opponent and board[1][0] == ' '):
    if(board[1][0] == ' '):
      r = 1 
      c = 0
  elif(board[0][1] == opponent and board[2][1] == opponent and board[1][1] == ' '):
    if(board[1][1] == ' '):
      r = 1 
      c = 1
  elif(board[0][2] == opponent and board[2][2] == opponent and board[1][2] == ' '):
    if(board[1][2] == ' '):
      r = 1 
      c = 2
  # take top right if open
  elif(board[0][2] == ' '): 
    r = 0 
    c = 2 
  elif(board[2][2] == ' '):
    r = 2 
    c = 2 
  elif(board[2][1] == ' '):
    r = 2 
    c = 1
  elif(board[1][2] == ' '): 
    r = 1 
    c = 2 
  elif(board[2][0] == ' '):
    r = 2 
    c = 0
  # take middle if top right is taken 
  elif(board[0][2] == opponent): 
    r = 1 
    c = 1 
  else:
    while(condition):
      for row in range(3):
        for col in range(3):
          if(board[row][col] == ' '):
            r = row
            c = col 
            condition = False 
  return r, c