team_name = 'Thomas'
strategy_name = 'logik'
strategy_description = 'counteracts conventional logic plays.'
import random as rand

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  checkpoint = 0 
  arbscore = 0
  x= 0
  print_board(board)
  while checkpoint < 9:
    if board[r][c] == 'X':
      arbscore += (1*(10^x))
    if board[r][c] == '0':
      arbscore += (2*(10^x))
    c = c + 1
    checkpoint += 1
    x += 1
    print(arbscore)
    if c > 2:
      c = 0
      r = r + 1
  r=0
  c=0
  if (arbscore == 000000000):
    r = rand.randint(0,2)
    c = rand.randint(0,2)
  if (arbscore == 1000000 or 1 or 100 or 100000000):
    r = 1
    c = 1
  if (arbscore == 20001):
    r=2
    c=2
  if (arbscore == 20100):
    r=2
    c=0
  if (arbscore == 100020000):
    r=0
    c=0
  if (arbscore == 1020000):
    r=0
    c=2
  if (arbscore == 102020001):
    r=0
    c=2
  if (arbscore == 100020201):
    r=2
    c=0
  if (arbscore == 1020102):
    r=2
    c=2
  if (arbscore == 201020100):
    r=0
    c=0
  if (arbscore == 100020021 or 1020120):
    r=2
    c=1
  if (arbscore == 100220001 or 1220100):
    r=1
    c=0
  if (arbscore == 120020001 or 21020100):
    r=0
    c=1
  if (arbscore == 100022001 or 1022100):
    r=1
    c=2
  if (arbscore == 102220101 or 122020101 or 102022101 or 201022101 or 201220101 or 221020101):
    r=0
    c=1
  if (arbscore == 102020121 or 122020101 or 102022101 or 101022102 or 101020122 or 121020102):
    r=1
    c=2
  if (arbscore == 121020201 or 101220201 or 101020221 or 201020121 or 201220101 or 22102010111):
    r=1
    c=0
  if (arbscore == 101020221 or 101022201 or 101220201 or 101022102 or 101020122 or 101220102):
    r=2
    c=1
  if (arbscore == 112020021 or 102221001 ):
    r=0
    c=2
  if (arbscore == 120020211 or 100122201 ):
    r=2
    c=0
  if (arbscore == 211020120 or 201122100 ):
    r=0
    c=0
  if (arbscore == 1221102 or 21020112 ):
    r=2
    c=2
  else:
    while board[r][c] != ' ':
      c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  return r,c



  
  