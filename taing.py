import random
team_name = 'taing'
strategy_name = 'taing strategy'
strategy_description = 'Play the next open spot.'
    
def move(player, board, score):
  r = 0
  c = 0
  i = 0
  while i<3 and board[r][c] != ' ':
      if board[i][0] == player and board[i][1] == player and board[0][2] == ' ':
              r = i
              c = 2

      i + 1
    
  i = 0
  
  while i<3 and board[r][c] != ' ':
      if board[i][0] == player and board[i][1] == ' ' and board[0][2] == ' ':
              r = i
              c = 1

      i + 1
    
  i = 0
  
  while i<3 and board[r][c] != ' ':
      if board[i][0] == ' ' and board[i][1] == ' ' and board[0][2] == ' ':
              r = i
              c = 0

  i + 1
  
  while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
    
  return r, c