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

@njit()
def DataAgent():
    return np.array([0])

@njit()
def Test(state,per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0]
    index_1 = 14*(0 + 1)
    cards_on_hand = state[index_1+2:index_1+14]
    turn = state[1:2] % 7
    #  reset per
    if turn == 1:
        per = np.array([5,13,8,0,3,10,4,11,1,15,6,2,12,9])
    #--------------#--------------#--------------#--------------#--------------
    if  cards_on_hand[1] == 3:
        per[1] = 0
    if cards_on_hand[10] == 1:
        per[7] = 15    
    if cards_on_hand[9] == 3:
        per[9] = 0
    if turn > 4 and cards_on_hand[1] < 1:
        per[1] = 0
    actions_point = per[actions]
    return actions[np.argmax(actions_point)],per