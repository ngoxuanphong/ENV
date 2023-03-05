import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHORT_PATH
import importlib.util

game_name = sys.argv[1]

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHORT_PATH}base/{game_name}/env.py")
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

def DataAgent():
    per = [np.random.choice(np.arange(getActionSize()),size=getActionSize(),replace=False) * 1.0,np.zeros(getActionSize())]
    return per
def convert_to_save(perData):
    return perData
def convert_to_test(perData):
    return List(perData)
@njit()
def Train(state,per):
    actions = getValidActions(state)
    output = actions * per[0] + actions
    action = np.argmax(output)
    win = getReward(state)
    if win == 1:
        per[1] += per[0]
    if win == 0:
        np.random.shuffle(per[0])
    return action,per

@njit()
def Test(state,per):
    actions = getValidActions(state)
    output = per[1] * actions + actions
    action = np.argmax(output)
    return action, per