@njit
def initPer():
  per = []
  per.append(np.zeros(1))
  return per

@njit
def agentSheriff(state, per):
  validActions = getValidActions(state)
  validActions = np.where( validActions)[0]
  if 61 in validActions:
    return 61, per
  if 77 in validActions:
    return 77, per
  if 78 in validActions:
    return 78, per
  action = np.random.choice(validActions)
  return action, per
