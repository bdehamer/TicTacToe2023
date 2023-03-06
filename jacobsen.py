team_name = 'jacobsen'
strategy_name = 'Jacobsen Stratagem'
strategy_description = 'The Samuel Paul Jacobsen Approach'


def move(player, board, score):
  enemy = not (player or ' ')
  r = 0
  c = 0
  go = False

  while go == False:
    if board[1][1] == ' ':
      r = 1
      c = 1

    elif board[0][0] == ' ':
      r = 0
      c = 0

    elif board[0][2] == ' ':
      r = 0
      c = 2

    elif board[2][0] == ' ':
      r = 2
      c = 0

    elif board[2][2] == ' ':
      r = 2
      c = 2

    elif board[1][0] == ' ':
      r = 1
      c = 0

    elif board[0][1] == ' ':
      r = 0
      c = 1

    elif board[2][1] == ' ':
      r = 2
      c = 1

    elif board[1][2] == ' ':
      r = 1
      c = 2

    #########################
    if board[1][1] == enemy:
      if board[0][1] == enemy:
        if board[2][1] == ' ':
          r = 2
          c = 1
      if board[2][1] == enemy:
        if board[0][1] == ' ':
          r = 0
          c = 1
      if board[1][0] == enemy:
        if board[1][2] == ' ':
          r = 1
          c = 2
      if board[1][2] == enemy:
        if board[1][0] == ' ':
          r = 1
          c = 0
      if board[0][0] == enemy:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == enemy:
        if board[0][0] == ' ':
          r = 0
          c = 0
      if board[0][2] == enemy:
        if board[2][0] == ' ':
          r = 2
          c = 0
      if board[2][0] == enemy:
        if board[0][2] == ' ':
          r = 0
          c = 2
    if board[1][0] == enemy:
      if board[0][0] == enemy:
        if board[2][0] == ' ':
          r = 2
          c = 0
      if board[2][0] == enemy:
        if board[0][0] == ' ':
          r = 0
          c = 0

    if board[0][1] == enemy:
      if board[0][0] == enemy:
        if board[0][2] == ' ':
          r = 0
          c = 2
      if board[0][2] == enemy:
        if board[0][0] == ' ':
          r = 0
          c = 0
    if board[1][2] == enemy:
      if board[0][2] == enemy:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == enemy:
        if board[0][2] == ' ':
          r = 0
          c = 2

    if board[2][1] == enemy:
      if board[2][0] == enemy:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == enemy:
        if board[2][0] == ' ':
          r = 2
          c = 0

    if board[0][0] == enemy:
      if board[2][0] == enemy:
        if board[1][0] == ' ':
          r = 1
          c = 0
      if board[0][2] == enemy:
        if board[0][1] == ' ':
          r = 0
          c = 1
      if board[2][2] == enemy:
        if board[1][1] == ' ':
          r = 1
          c = 1
    if board[2][2] == enemy:
      if board[0][2] == enemy:
        if board[1][2] == ' ':
          r = 1
          c = 2
      if board[2][0] == enemy:
        if board[2][1] == ' ':
          r = 2
          c = 1
    ########################
    if board[1][1] == player:
      if board[0][1] == player:
        if board[2][1] == ' ':
          r = 2
          c = 1
      if board[2][1] == player:
        if board[0][1] == ' ':
          r = 0
          c = 1
      if board[1][0] == player:
        if board[1][2] == ' ':
          r = 1
          c = 2
      if board[1][2] == player:
        if board[1][0] == ' ':
          r = 1
          c = 0
      if board[0][0] == player:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == player:
        if board[0][0] == ' ':
          r = 0
          c = 0
      if board[0][2] == player:
        if board[2][0] == ' ':
          r = 2
          c = 0
      if board[2][0] == player:
        if board[0][2] == ' ':
          r = 0
          c = 2
    if board[1][0] == player:
      if board[0][0] == player:
        if board[2][0] == ' ':
          r = 2
          c = 0
      if board[2][0] == player:
        if board[0][0] == ' ':
          r = 0
          c = 0

    if board[0][1] == player:
      if board[0][0] == player:
        if board[0][2] == ' ':
          r = 0
          c = 2
      if board[0][2] == player:
        if board[0][0] == ' ':
          r = 0
          c = 0
    if board[1][2] == player:
      if board[0][2] == player:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == player:
        if board[0][2] == ' ':
          r = 0
          c = 2

    if board[2][1] == player:
      if board[2][0] == player:
        if board[2][2] == ' ':
          r = 2
          c = 2
      if board[2][2] == player:
        if board[2][0] == ' ':
          r = 2
          c = 0

    if board[0][0] == player:
      if board[2][0] == player:
        if board[1][0] == ' ':
          r = 1
          c = 0
      if board[0][2] == player:
        if board[0][1] == ' ':
          r = 0
          c = 1
      if board[2][2] == player:
        if board[1][1] == ' ':
          r = 1
          c = 1

    if board[2][2] == player:
      if board[0][2] == player:
        if board[1][2] == ' ':
          r = 1
          c = 2
      if board[2][0] == player:
        if board[2][1] == ' ':
          r = 2
          c = 1
    #########################
    go = True

  return r, c