import random

team_name = 'pyle'
strategy_name = 'Skynet'
strategy_description = 'Skynet begins to learn rapidly and eventually becomes self-aware.'

# settings
file_name = 'pyle_untrained.csv'
rounds_to_save = 33
save_to_file = False

#globals
old_score = 0
round = -1
board_states = []
weights_list = []
current_game_moves = []
current_game_boards = []

def load_lists():
  weights_file = open(file_name, 'r')
  states = []
  weights = []
  for line in weights_file:
    line_split = line.split(',')
    line_split[9] = line_split[9][:-1]
    states.append(line_split[0])
    weights.append([float(i) for i in line_split[1:]])
  weights_file.close()
  return states, weights


def save_lists(board_states, weights):
  weights_file = open(file_name, 'w')
  for i in range(len(board_states)):
    weights_file.write(board_states[i])
    for j in range(9):
      weights_file.write(','+str(weights[i][j]))
    weights_file.write('\n')
  weights_file.close()

def normalize_weights(weights):
  for n in range(9):
    if weights[n] < 0:
      weights[n] = 0.
    elif weights[n] > 1:
      weights[n] = 1.
  m = 1./sum(weights)
  for n in range(9):
    weights[n] = weights[n] * m
  return weights


def move(player, board, score):
  global old_score, board_states, weights_list, current_game_boards, current_game_moves, round

  # load states and weights if they are not loaded
  if board_states == []:
    board_states, weights_list = load_lists()

  # place the board state into a handy string
  board_state = player + board[0][0] + board[0][1] + board[0][2] +\
                board[1][0] + board[1][1] + board[1][2] +\
                board[2][0] + board[2][1] + board[2][2]

  # detect a new round
  if board_state[1:] == '         ':
    round += 1
    
    # weightings for loss/win/cats
    if score < old_score:
      m = -0.05
    elif score > old_score:
      m = 0.05
    else:
      m = 0.03

    # find the board states that match the ones from the last game and weight their probability
    for x in range(len(current_game_boards)):
      i = board_states.index(current_game_boards[x])
      weights_list[i][current_game_moves[x]] += m
      weights_list[i] = normalize_weights(weights_list[i])

    # reset current game board and moves
    current_game_boards = []
    current_game_moves = []

    # save to file if selected
    if save_to_file and round % rounds_to_save == 0 and round > 0:
      print('saving...', end='')
      save_lists(board_states, weights_list)
      print('complete')
  
  # save the current score
  old_score = score

  # retrieve the index of the current boardstate
  i = board_states.index(board_state)
  current_game_boards.append(board_state)

  # randomly select move based on weights
  roll = random.random()
  if roll < weights_list[i][0]:
    r, c = (0, 0)
    current_game_moves.append(0)
  elif roll < sum(weights_list[i][:2]):
    r, c = (0, 1)
    current_game_moves.append(1)
  elif roll < sum(weights_list[i][:3]):
    r, c = (0, 2)
    current_game_moves.append(2)
  elif roll < sum(weights_list[i][:4]):
    r, c = (1, 0)
    current_game_moves.append(3)
  elif roll < sum(weights_list[i][:5]):
    r, c = (1, 1)
    current_game_moves.append(4)
  elif roll < sum(weights_list[i][:6]):
    r, c = (1, 2)
    current_game_moves.append(5)
  elif roll < sum(weights_list[i][:7]):
    r, c = (2, 0)
    current_game_moves.append(6)
  elif roll < sum(weights_list[i][:8]):
    r, c = (2, 1)
    current_game_moves.append(7)
  else:
    r, c = (2, 2)
    current_game_moves.append(8)

  # return the move
  return r, c