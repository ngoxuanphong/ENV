# ở turn nào thì dùng bộ nào
# time-lapse
# không gian n chiều
# small NN deep
import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHORT_PATH
import importlib.util
game_name = sys.argv[1]
from numba.typed import List

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHORT_PATH}base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module 
    spec.loader.exec_module(module)
    return module

env = setup_game(game_name)
def convert_to_save(perData):
    return perData
def convert_to_test(perData):
    return List(perData)
getActionSize = env.getActionSize
getStateSize = env.getStateSize
getAgentSize = env.getAgentSize

getValidActions = env.getValidActions
getReward = env.getReward


def DataAgent():
    per = List([np.zeros((1,1)), #[0][0][0] turn hiện tại
            np.zeros((10000,getActionSize())), #[1][turn] lưu bộ đã dùng trong game
            np.zeros((10000,getActionSize())) #[2][turn] lưu kết quả khi thắng
           ])
    return per

@njit()
def Train(state,per):
    actions = getValidActions(state)
    turn = int(per[0][0][0])
    if np.sum(per[1][turn]) == 0:
        weights = np.argsort(np.argsort(np.random.rand(getActionSize()))) * 1.0
        per[1][turn] = weights
    else:
        weights = per[1][turn]
    output = actions * weights + actions
    action = np.argmax(output)
    win = getReward(state)
    per[0] += 1
    if win != -1:
        if win == 1:
            per[2] += per[1]
        if win == 0:
            per[1] = np.zeros((10000,getActionSize()))
        per[0] = np.zeros((1,1))
    return action, per

@njit()
def Test(state,per):
    actions = getValidActions(state)
    turn = int(per[0][0][0])
    if len(per[2]) > turn:
        weights = per[2][turn]/np.max(per[2][turn])
        output = actions * weights + actions
        action = np.argmax(output)
    else:
        action = np.random.choice(np.where(actions == 1)[0])
    win = getReward(state)
    per[0] += 1
    if win != -1:
        per[0] = np.zeros((1,1))
    if actions[action] != 1:
        action = np.random.choice(np.where(actions == 1)[0])
    return action, per