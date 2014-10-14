def enforce(cur_callback, goal_callback, add_callback, remove_callback):
  converged = True
  cur = set(cur_callback())
  goal = set(goal_callback())
  missing = goal - cur
  for key in missing:
    add_callback(key)
    converged = False
  extra = cur - goal
  for key in extra:
    remove_callback(key)
    converged = False
  return converged

