import math

def terminal(board):
  """
  Returns true if the game has ended(Win Lose or draw)
  """
  pass

def utility(board):
  """
  Returns:
    -1: The minimizing player wins
     1: The maximizing player wins
     0: Otherwise
  """
  pass

def actions(board):
  """
  Given the board as input returns all the available actions
  """
  pass

# alpha: max & beta: min
def max_value(board, alpha, beta):
    """
    function MAX-VALUE(state):
      if TERMINAL(state):
        return UTILITY(state)
      v = -∞
      for action in ACTIONS(state):
        v = MAX(v, MIN-VALUE(RESULT(state, action)))
      return v
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        # alpha-beta pruning
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v


def min_value(board, alpha, beta):
    """
    function MAX-VALUE(state):
      if TERMINAL(state):
        return UTILITY(state)
      v = +∞
      for action in ACTIONS(state):
        v = MIN(v, MAX-VALUE(RESULT(state, action)))
      return v
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        # alpha-beta pruning
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v
