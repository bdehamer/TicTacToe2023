team_name = 'Barry'
strategy_name = 'Eye of the Tiger'
strategy_description = 'Attack the corners first. Then attack middle. Attack sides if needed.'


    
def move(player, board, score):
  if board[0][0] == ' ' and board[0][0] != player:
    r = 0
    c = 0
  elif board[0][2] == ' ' and board[0][2] != player:
    r = 0
    c = 2
  elif board[2][0] == ' ' and board[2][0] != player:
    r = 2
    c = 0
  elif board[2][2] == ' ' and board[2][2] != player:
    r = 2
    c = 2

  if board[1][1] == ' ' and board[1][1] != player:
    r = 1
    c = 1
# I want to loop the above code^^^
    
  if board[1][1] == ' ' and board[1][1] != player:
    r = 1
    c = 1 
  elif board[1][0] == ' ' and board[1][0] != player:
    r = 1
    c = 0
  elif board[1][2] == ' ' and board[1][2] != player:
    r = 1
    c = 2
  elif board[0][1] == ' ' and board[0][1] != player:
    r = 0
    c = 1
  elif board[2][1] == ' ' and board[2][1] != player:
    r = 2
    c = 1


  
  return r, c




  

#if board[0][0] != player and board[0][0] != ' ':