import random

team_name = 'davila'
strategy_name = 'davila strats'
strategy_description = 'Play the next open spot.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


    
def move(player, board, score):
  """
  print ("new turn begun")
  """
  if board[1][1] == ' ':
    """
    print("took middle")
    """
    r = 1
    c = 1
    return r, c
  """
  print (player)
  print_board(board)
  """
  r = 0
  c = 0
  opp = 0
  own = 0
  os = 0

  
  while c <= 2 and r <= 2:
    if c < 3 and board[r][c] == player:
      c = c + 1
      own += 1
      """
      print("saw player")
      """
    elif c < 3 and board[r][c] != ' ':
      c = c + 1
      opp += 1
      """
      print("saw opponent")
      """
    if c < 3 and board[r][c] == ' ':
      c = c + 1
      os += 1
      """
      print("saw nothing")
      """
    if c > 2:
      """
      print ("c is too high")
      """
      if own == 2 and opp != 1:
        c = 0
        if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
        while board[r][c] != ' ':
          c += 1
          if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
      elif opp == 2 and own != 1:
        c = 0 
        if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
        while board[r][c] != ' ':
          c += 1
          if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
      else:
        """
        print("new row")
        """
        c = 0
        r += 1
        own = 0
        opp = 0
        
  c = 0
  r = 0
  own = 0
  opp = 0
  """
  print ("searching verticals")
  """
  while c <=2 and r <=2:
    if r < 3 and board[r][c] == player:
      r = r + 1
      own += 1
      """
      print("saw player")
      """
 
    elif r < 3 and board[r][c] != ' ':
      r = r + 1
      opp += 1
      """
      print("saw opponent")
      """
   
    if r < 3 and board[r][c] == ' ':
      r = r + 1
      os += 1
      """
      print("saw nothing")
      """
   
    if r > 2:
      """
      print ("r is too high")
      """
  
      if own == 2 and opp != 1:
        r = 0
        if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
        while board[r][c] != ' ':
          r += 1
          if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
      elif opp == 2 and own != 1:
        r = 0 
        if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
        while board[r][c] != ' ':
          r += 1
          if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
      else:
        """
        print("new row")
        """
        r = 0
        c += 1
        own = 0
        opp = 0
  c = 0
  r = 0
  own = 0
  opp = 0
  """
  print("searching diagonals")
  """
  while c <=2 and r <=2:
    if r < 3 and board[r][c] == player:
      r = r + 1
      c = c + 1
      own += 1
      """
      print("saw player")
      """

    elif r < 3 and board[r][c] != ' ':
      r = r + 1
      c = c + 1
      opp += 1
      """
      print("saw opponent")
      """
   
    if r < 3 and board[r][c] == ' ':
      r = r + 1
      c = c + 1
      os += 1
      """
      print("saw nothing")
      """
 
    if r > 2:
      """
      print ("r is too high")
      """

      if own == 2 and opp != 1:
        r = 0
        c = 0
        if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
        while board[r][c] != ' ':
          r += 1
          c += 1
          if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
      elif opp == 2 and own != 1:
        r = 0
        c = 0
        if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
        while board[r][c] != ' ':
          r += 1
          c += 1
          if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
      else:
        """
        print("new diagonal")
        """
        r = 2
        c += 1
        own = 0
        opp = 0
  r = 2
  c = 0
  own = 0
  opp = 0
  while c <=2 and r >= 0:
    if r >= 0 and board[r][c] == player:
      r = r - 1
      c = c + 1
      own += 1
      """
      print("saw player")
      """

    elif r >=0 and board[r][c] != ' ':
      r = r - 1
      c = c + 1
      opp += 1
      """
      print("saw opponent")
      """

    if r >= 0 and board[r][c] == ' ':
      r = r - 1
      c = c + 1
      os += 1
      """
      print("saw nothing")
      """

    if r <= -1:
      """
      print ("r is too high")
      """
      if own == 2 and opp != 1:
        """
        print ("looking for win")
        """
        r = 2
        c = 0
        if board[r][c] == ' ':
            """
            print("ran victory")
            """
          
        while board[r][c] != ' ':
          r = r - 1
          c = c + 1
          if board[r][c] == ' ':
            """
            print("ran victory")
            """
            return r, c
      elif opp == 2 and own != 1:
        """
        print ("looking for counter here")
        """
        r = 2
        c = 0
        if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
        while board[r][c] != ' ':
          r = r - 1
          c = c + 1
          if board[r][c] == ' ':
            """
            print("ran counter")
            """
            return r, c
  if r > 2 or c > 2:
    c = 0
    r = 0
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
      """
      print("ran random")
      """
    return r, c




"""
  if board [1][1] != player and board[1][1] != ' ':
    print ("checking diagonals")
    if board[0][0] or board[2][2] != player and board[0][0] or board[2][2] != ' ':
      print("found in 1st")
      if board[0][0] == ' ':
        r = 0
        c = 0
        return r,c
      if board[2][2] == ' ':
        r = 2
        c = 2
        return r,c
    if board[2][0] or board[0][2] != player and board[2][0] or board[0][2] != ' ':
      print("found in 2nd")
      if board[2][0] == ' ':
        r = 2
        c = 0
        return r,c
      if board[0][2] == ' ':
        r = 0
        c = 2
        return r,c
      
  if r > 2 or c > 2:
    print ("made it")
    c = 0
    r = 0
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
      print("ran random")
    return r, c
"""
  
  
    
  


  
  