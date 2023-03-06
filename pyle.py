team_name = 'pyle'
strategy_name = 'pyle strategy'
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
  global old_score, game, old_board, old_player, last_player
  print(old_score, score, old_player, player)
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
  r = 0
  c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  old_board = board[:]
  old_board[r][c] = player
  old_score = score
  last_player = player
  return 3, c