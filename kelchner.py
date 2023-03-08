team_name = 'kelchner'
strategy_name = 'reverse step by step'
strategy_description = 'Starting from bottom right play the next open spot to the left.'


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
  else:
    r = 2
    c = 2
    while board[r][c] != ' ':
      c = c - 1
      if c < 0:
        c = 2
        r = r - 1
  return r, c