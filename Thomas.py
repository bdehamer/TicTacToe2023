team_name = 'Thomas'
strategy_name = 'Counter'
strategy_description = 'Play the next open spot.'
import random as rand


def move(player, board, score, filled):
  r = 0
  c = 0
  count()
  corners=[0,2]
  if (player == 'x') and (filled == 0):
    r = rand(corners)
    c = rand(corners)
  return r, c


def count(board, filled):
  r=0
  c=0
  filled = 0
  chckpnt =0
  while (chckpnt < 9):
    if board[r][c] == 'player':
      filled += 1
    c += 1
    if c > 2:
      c = 0
      r = r + 1
    chckpnt += 1