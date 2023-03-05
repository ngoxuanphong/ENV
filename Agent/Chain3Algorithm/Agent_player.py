import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHORT_PATH
# from setup import SHOT_PATH
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
# chain of action
def DataAgent():
    per = List([np.zeros((1,1,2)) - 1, # [0] lưu 2 action gần nhất [0][0] = action 2 turn trước, [0][1] = action 1 turn trước
           np.zeros((1,1,getActionSize())) + np.argsort(np.argsort(np.random.rand(getActionSize()))), # [1] nháp 1
           np.zeros((1,1,getActionSize())), # [2] lưu 1
           np.zeros((1,getActionSize(),getActionSize())) + np.argsort(np.argsort(np.random.rand(getActionSize(),getActionSize()),axis = 1),axis = 1), # [3] nháp 2
           np.zeros((1,getActionSize(),getActionSize())), # [4] lưu 2
           np.zeros((getActionSize(),getActionSize(),getActionSize())) + np.argsort(np.argsort(np.random.rand(getActionSize(),getActionSize(),getActionSize()),axis = 2),axis = 2), # [5] nháp 3
           np.zeros((getActionSize(),getActionSize(),getActionSize())) # [6] lưu 3
    ])
    return per

@njit()
def create2(arr):
    # x = np.zeros((1,getActionSize(),getActionSize()))
    # for id in range(getActionSize()):
    #     x[0][id] = np.argsort(np.argsort(np.random.rand(getActionSize())))
    # return x
    for id in range(getActionSize()):
        np.random.shuffle(arr[0][id])
@njit()
def create3(arr):
    # x = np.zeros((getActionSize(),getActionSize(),getActionSize()))
    # for id1 in range(getActionSize()):
    #     for id2 in range(getActionSize()):
    #         x[id1][id2] = np.argsort(np.argsort(np.random.rand(getActionSize())))
    # return x
    for id1 in range(getActionSize()):
        for id2 in range(getActionSize()):
            np.random.shuffle(arr[id1][id2])

@njit()
def Train(state,per):
    actions = getValidActions(state)
    last1act = int(per[0][0][0][1])
    last2act = int(per[0][0][0][0])
    if last2act == -1:
        # khi chưa action nào được đưa ra
        if last1act == -1:
            output = per[1][0][0] * actions + actions
        else:
            # khi đã có 1 action trước đó
            output = per[3][0][last1act] * actions + actions
    else:
        output = per[5][last2act][last1act] * actions + actions
    action = np.argmax(output)
    preact = np.zeros((1,1,2)) - 1
    preact[0][0][1] = action
    preact[0][0][0] = last1act
    per[0] = preact
    win = getReward(state)
    if win != -1:
        if win == 1:
            per[2] += per[1]
            per[4] += per[3]
            per[6] += per[5]
        if win == 0:
            per[1] = np.zeros((1,1,getActionSize())) + np.argsort(np.argsort(np.random.rand(getActionSize())))
            create2(per[3])
            create3(per[5])
        per[0] = np.zeros((1,1,2))
    return action, per

@njit()
def Test(state,per):
    actions = getValidActions(state)
    last1act = int(per[0][0][0][1])
    last2act = int(per[0][0][0][0])
    if last2act == -1:
        # khi chưa action nào được đưa ra
        if last1act == -1:
            output = per[2][0][0] * actions + actions
        else:
            # khi đã có 1 action trước đó
            output = per[4][0][last1act] * actions + actions
    else:
        output = per[6][last2act][last1act] * actions + actions
    action = np.argmax(output)
    preact = np.zeros((1,1,2)) - 1
    preact[0][0][1] = action
    preact[0][0][0] = last1act
    per[0] = preact
    return action,per


def convert_to_save(perData):
    return perData
def convert_to_test(perData):
    return List(perData)