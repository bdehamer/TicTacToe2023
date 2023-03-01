import random
import os.path
import importlib

import example0
import example1
import example2

modules = [example0, example1, example2]

test_board = [['O', 'X', 'O'],
              ['X', 'X', 'O'],
              ['X', 'O', 'X']]

for module in modules:
  importlib.reload(module)
  print ('reloaded',module)
  for required_variable in ['team_name', 'strategy_name', 'strategy_description']:
    if not hasattr(module, required_variable):
      setattr(module, required_variable, 'missing assignment')

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def check_winner(board):
  for r in range(3):
    if board[r][0] != ' ' and board[r][0] == board[r][1] and board[r][0] == board[r][2]:
      return board[r][0]
  for c in range(3):
    if board[0][c] != ' ' and board[0][c] == board[1][c] and board[0][c] == board[2][c]:
      return board[0][c]  
  if board[0][0] != ' ' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    return board[0][0]
  if board[0][2] != ' ' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
    return board[0][2] 
  else:
    for r in range(3):
      for c in range(3):
        if board[r][c] == ' ':
          return ' '
    return 'C'

def main_play(modules):
    '''main_play plays a tournament and outputs results to screen and file.
    This function is called once when this file is executed.
    modules: a list of modules such as [team1, team2]    
    
    Returns:
        scores:
        moves:
        sections: a list of [str, str, str, list of str]    
            '''
    scores = play_tournament(modules)
    section0, section1, section2 = make_reports(modules, scores)
    code = make_code_string(modules)
    # On screen, include the first three out of four sections of the report.
    print(section0+section1+section2)
    # To file output, store all teams' code and all teams' section 3 reports.
    post_to_file(section0+section1+section2 + code)
    return scores, [section0, section1, section2]

def play_tournament(modules):
  zeros_list = [0]*len(modules)
  scores = [zeros_list[:] for module in modules] # Copy it or it's only 1 list
  for first_team_index in range(len(modules)):
    for second_team_index in range(first_team_index):
      # choose X and O
      player1 = modules[first_team_index]
      player2 = modules[second_team_index]
      score1, score2 = play_iterative_rounds(player1, player2) 
      scores[first_team_index][second_team_index] = score1
      # Redundant, but record this for the other player, from their perspective
      scores[second_team_index][first_team_index] = score2
  return scores
  
def play_iterative_rounds(player1, player2):
  number_of_rounds = 100
  score1 = 0
  score2 = 0
  for round in range(number_of_rounds):
    winner = play_round(player1, player2, score1, score2)
    if winner == '1':
      score1 = score1 + 1
      score2 = score2 - 1
    if winner == '2':
      score1 = score1 - 1
      score2 = score2 + 1
  return score1, score2

def play_round(player1, player2, score1, score2):
  '''if random.randint(0,1) == 0:
    playerX = modules[first_team_index]
    playerO = modules[second_team_index]
  else:
    playerO = modules[first_team_index]
    playerX = modules[second_team_index]'''
  board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]
  
  if random.randint(0,1) == 0:
    #player1 is X
    turns = 0
    while turns < 18:
      r, c = player1.move('X', board[:], score1)
      if r >=0 and r <= 2 and c >= 0 and c <= 2:
        if board[r][c] == ' ':
          board[r][c] = 'X'
      if check_winner(board) == 'X':
        return '1'
      if check_winner(board) == 'C':
        return 'C'
      r, c = player2.move('O', board[:], score2)
      if r >=0 and r <= 2 and c >= 0 and c <= 2:
        if board[r][c] == ' ':
          board[r][c] = 'O'
      if check_winner(board) == 'O':
        return '2'
      if check_winner(board) == 'C':
        return 'C'
    return 'C'
  else:
    #player2 is X
    turns = 0
    while turns < 18:
      r, c = player2.move('X', board[:], score2)
      if r >=0 and r <= 2 and c >= 0 and c <= 2:
        if board[r][c] == ' ':
          board[r][c] = 'X'
      if check_winner(board) == 'X':
        return '2'
      if check_winner(board) == 'C':
        return 'C'
      r, c = player1.move('O', board[:], score1)
      if r >=0 and r <= 2 and c >= 0 and c <= 2:
        if board[r][c] == ' ':
          board[r][c] = 'O'
      if check_winner(board) == 'O':
        return '1'
      if check_winner(board) == 'C':
        return 'C'
    return 'C'

def make_reports(modules, scores):
    section0 = make_section0(modules, scores)
    section1 = make_section1(modules, scores)
    section2 = make_section2(modules, scores)

    return section0, section1, section2
        
def make_section0(modules, scores):
    '''
    Produce the following string:
    ----------------------------------------------------------------------------
    Section 0 - Line up
    ----------------------------------------------------------------------------
    Player 0 (P0): Team name 0, Strategy name 0,
         Strategy 0 description
    Player 1 (P1): Team name 1, Strategy name 1, 
         Strategy 1 description
    ''' 
    section0 = '-'*80+'\n'
    section0 += 'Section 0 - Line up\n'
    section0 += '-'*80+'\n'
    for index in range(len(modules)):
        section0 += 'Player ' + str(index) + ' (P' + str(index) + '): '
        section0 += str(modules[index].team_name) + ', ' + str(modules[index].strategy_name) + '\n'
        strategy_description = str(modules[index].strategy_description)
        # Format with 8 space indent 80 char wide
        while len(strategy_description) > 1:
            newline = strategy_description[:72].find('\n')
            if newline> -1:
                section0 += ' '*8 + strategy_description[:newline+1]
                strategy_description = strategy_description[newline+1:]
            else:
                section0 += ' '*8 + strategy_description[:72] + '\n'
                strategy_description = strategy_description[72:]
    return section0
    
def make_section1(modules, scores):
    '''
    ----------------------------------------------------------------------------
    Section 1 - Player vs. Player
    ----------------------------------------------------------------------------
    A column shows pts/round earned against each other player:      
    '''
    # First line
    section1 = '-'*80+'\nSection 1 - Player vs. Player\n'+'-'*80+'\n'
    section1 += 'Each column shows pts/round earned against each other player:\n'
    # Second line
    section1 += '        '
    for i in range(len(modules)):
          section1 += '{:>7}'.format('P'+str(i))
    section1 += '\n'
    # Add one line per team
    for index in range(len(modules)):
        section1 += 'vs. P' + str(index) + ' :'
        for i in range(len(modules)):
            section1 += '{:>7}'.format(int(scores[i][index]))
        section1 += '\n'

    # Last line
    section1 += 'TOTAL  :'
    for index in range(len(modules)):
        section1 += '{:>7}'.format(int(sum(scores[index])))     
    return section1+'\n'
    
def make_section2(modules, scores):
    '''
    ----------------------------------------------------------------------------
    Section 2 - Leaderboard
    ----------------------------------------------------------------------------
    Average points per round:
    Team name (P#):  Score       with strategy name
    Champ10nz (P0):   100 points with Loyal
    Rockettes (P1):  -500 points with Backstabber
    ''' 
    section2 = '-'*80+'\nSection 2 - Leaderboard\n'+'-'*80+'\n'
    section2 += 'Average points per round:\n'
    section2 += 'Team name (P#):  Score      with strategy name\n'
    
    # Make a list of teams' 4-tuples
    section2_list = []
    for index in range(len(modules)):
        section2_list.append((modules[index].team_name,
                              'P'+str(index),
                              str(sum(scores[index])/len(modules)),
                              str(modules[index].strategy_name)))
    section2_list.sort(key=lambda x: int(float(x[2])), reverse=True)
    
    # Generate one string per team
    # Rockettes (P1):  -500 points with Backstabber
    for team in section2_list:
        team_name, Pn, n_points, strategy_name = team
        section2 += '{:<10}({}): {:>10} points with {:<40}\n'.format(team_name[:10], Pn, int(float(n_points)), strategy_name[:40])                       
    return section2                                              
   
def make_code_string(modules):
    '''Returns a string of the code from each file.
    '''
    code = '-'*80 + '\n'
    code += 'Code of each player\'s algorithm\n'
    code = '-'*80 + '\n'
    for index in range(len(modules)):
        players_code_filename = str(modules[index]).split(' ')[1].replace('\'','')
        directory = os.path.dirname(os.path.abspath(__file__))  
        filename = os.path.join(directory, players_code_filename)
        players_code_file = open(filename+'.py', 'r')
        code += '-'*80 + '\n'
        code += players_code_filename
        code +='-'*80 + '\n'
        code += ''.join(players_code_file.readlines())
    return code

def copy_template():
    '''Transfer code in team0.py to team1.py though team14.py
    '''
    directory = os.path.dirname(os.path.abspath(__file__))  
    with open(os.path.join(directory, 'team0.py'), 'r') as sourcefile:
        source = sourcefile.readlines()
    for i in range(1, 15):
        target = 'team'+str(i)+'.py'
        filename = os.path.join(directory, target)
        with open(filename, 'w') as target_file:
            target_file.write(''.join(source))                                   
                     
def post_to_api():
    pass

def post_to_local_html():
    pass
    
def post_to_file(string, filename='tournament.txt', directory=''):
    '''Write output in a txt file.
    '''
    # Use the same directory as the python script
    if directory=='':
        directory = os.path.dirname(os.path.abspath(__file__))  
    # Name the file tournament.txt
    filename = os.path.join(directory, filename)
    # Create the file for the round-by-round results
    filehandle = open(filename,'w')
    filehandle.write(string) 
    
#play_tournament(modules)
#print_board(test_board)
#print(check_winner(test_board))

### Call main_play() if this file is executed
if __name__ == '__main__':
    scores, reports = main_play(modules)   
    section0, section1, section2 = reports