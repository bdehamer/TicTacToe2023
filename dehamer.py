import random
team_name = 'dehamer'
strategy_name = 'dehamer-copilot'
strategy_description = 'copilot assisted'

def move(player, board, score):
    # Check for winning moves for the current player
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_win(board, player):
                    return (i, j)
                board[i][j] = ' '
    
    # Check for winning moves for the opponent
    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent
                if check_win(board, opponent):
                    return (i, j)
                board[i][j] = ' '
    
    # Capture a corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for i, j in corners:
        if board[i][j] == ' ':
            return (i, j)
    
    # Pick a random move
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == ' ':
            return (i, j)
        
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    
    # Check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    # No win found
    return False