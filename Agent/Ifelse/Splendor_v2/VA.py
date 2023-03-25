import numpy as np
import random as rd
from numba import njit, jit
from numba.typed import List
import sys, os
from setup import SHORT_PATH
import importlib.util
game_name = sys.argv[1]

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHORT_PATH}Base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

env = setup_game(game_name)

getActionSize = env.getActionSize
getStateSize = env.getStateSize
getAgentSize = env.getAgentSize

getValidActions = env.getValidActions
getReward = env.getReward


@njit
def DataAgent():
  per = []
  per.append(np.zeros(5))
  per.append(np.zeros(5))
  return per

njit()
def Test(state, per):
    validActions = getValidActions(state)
    validActions = np.where(validActions == 1)[0]

    purchaseCardActions = validActions[(validActions>=1) & (validActions<13)]
    if len(purchaseCardActions) > 0:
        action = purchaseCardActions[0]
        for purchaseCardAction in purchaseCardActions:
            if state[18 + 11*(purchaseCardAction-1)] > state[18 + 11*(action-1)]:
                action = purchaseCardAction
        return action, per
    
    reverseFacedownCardActions = validActions[(validActions>=13) & (validActions<16)]
    if len(reverseFacedownCardActions) > 0:
        action = reverseFacedownCardActions[np.random.randint(len(reverseFacedownCardActions))]
        return action, per

    faceupCards = state[18:150].reshape(12,-1)
    faceupCards_l0_l1 = faceupCards[:8]
    faceupCards_l2 = faceupCards[8:]
    totalCostFaceUpCards_l0_l1 = np.sum(faceupCards_l0_l1, axis=1)[-5:]
    totalCostFaceUpCards_l2 = np.sum(faceupCards_l2, axis=1)[-5:]
    if np.sum(totalCostFaceUpCards_l0_l1) > 0:
        mostThreeTokens = (-totalCostFaceUpCards_l0_l1).argsort()[:3] + 31
    else:
        mostThreeTokens = (-totalCostFaceUpCards_l2).argsort()[:3] + 31
    takeTokenActions = validActions[(validActions>=31) & (validActions<36)]
    mostAvalableThreeTokens = np.intersect1d(mostThreeTokens, takeTokenActions)
    takeTokenActions = np.concatenate((
        takeTokenActions, 
        takeTokenActions,
        takeTokenActions,
        mostAvalableThreeTokens
    ))
    if len(takeTokenActions) > 0:
        action = takeTokenActions[np.random.randint(len(takeTokenActions))]
        return action, per 
        
    action = validActions[np.random.randint(len(validActions))]
    return action, per