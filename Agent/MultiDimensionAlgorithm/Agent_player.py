# không gian n chiều
# small NN deep
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
    per = [np.random.rand(getActionSize(),getStateSize()), #[0]
           np.zeros((getActionSize(),getStateSize())), #[1]
           np.zeros((1,1)), #[2]
           np.random.rand(getActionSize(),getStateSize()) * 10, #[3]
           np.zeros((getActionSize(),getStateSize())) #[4]
           ]
    return per

def convert_to_save(perData):
    return perData
def convert_to_test(perData):
    return List(perData)
    
@njit()
def findOut(state,geo):
    return np.sum((geo * state) ** 2,axis = 1)

@njit()
def Train(state,per):
    actions = getValidActions(state)
    nState = state - 1
    nState = state - per[3]
    output = np.sum((per[0] * nState) ** 2,axis = 1)
    output = actions * output + actions
    action = np.argmax(output)
    win = getReward(state)
    if win == 1:
        per[1] += per[0]
        per[4] += per[3]
        per[2][0] += 1
    if win == 0:
        per[0] = np.random.rand(getActionSize(),getStateSize())
        per[3] = np.random.rand(getActionSize(),getStateSize()) * 10
    return action,per

@njit()
def Test(state,per):
    actions = getValidActions(state)
    nState = state - 1
    nState = state - per[4]/per[2][0]
    output = np.sum((per[1]/per[2][0] * nState) ** 2,axis = 1)
    output = actions * output + actions
    action = np.argmax(output)
    return action, per