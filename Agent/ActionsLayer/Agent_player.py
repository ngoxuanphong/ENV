import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHOT_PATH
import importlib.util
game_name = sys.argv[1]

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHOT_PATH}base/{game_name}/env.py")
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


from numba.typed import List

def convert_to_save(perData):
    return perData
def convert_to_test(perData):
    return list(perData)
    
@njit()
def DataAgent():
    return [np.zeros((1, getActionSize())), np.random.rand(getActionSize(), getActionSize()), np.zeros((getActionSize(),getActionSize()))]

@njit()
def Train(state,per):
    actions = getValidActions(state)
    weight = per[0][0]

    output = actions*weight + actions
    c = np.where(output == np.max(output))[0]
    action = np.random.choice(c)

    per[0] += per[1][action]
    win = getReward(state)

    if win != -1:
        per[0] = np.zeros((1, getActionSize()))
        if win == 1:
            per[2] += per[1]
        else:
            per[1] = np.random.rand(getActionSize(), getActionSize())
        
    if actions[action] != 1:
        print(action, output, weight, actions)
    return action, per

@njit()
def Test(state,per):
    actions = getValidActions(state)
    weight = per[0][0]

    output = actions*weight + actions
    c = np.where(output == np.max(output))[0]
    action = np.random.choice(c)
    per[0] += np.argsort(np.argsort(per[2][action]))
    win = getReward(state)
    if win != -1:
        per[0] = np.zeros((1, getActionSize()))
    return action, per