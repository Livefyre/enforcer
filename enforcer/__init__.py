"""
cur_callback and goal_callback are invoked to detimine what actions should be taken
to reach convergence. Should return a dict where the keys are the set, and the values are a
context to use when adding or removing items.
"""
def enforce(cur_callback, goal_callback, add_callback, remove_callback):
  converged = True
  cur = cur_callback()
  goal = goal_callback()
  missing = set(goal.keys()) - set(cur.keys())
  for key in missing:
    add_callback(key, goal[key])
    converged = False
  extra = set(cur.keys()) - set(goal.keys())
  for key in extra:
    remove_callback(key, cur[key])
    converged = False
  return converged

