# state based
# small NN deep
import numpy as np
import random as rd
from numba import njit, jit
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


from numba.typed import List

def DataAgent():
    per = List([np.zeros((100,getStateSize(),getActionSize())), #[0][value][idS] khi mở đầu game
           np.zeros((100,getStateSize(),getActionSize())), #[1][value][ids] lưu lại cuối cùng
           np.zeros((1,1,1)) #[2][0][0][0] vừa thắng hay thua
           ])
    return per

@njit()
def Train(state,per):
    actions = getValidActions(state)
    weights = np.zeros(getActionSize())
    if per[2][0][0][0] == 0:
        temp = np.arange(getActionSize(), dtype=np.float64)
        np.random.shuffle(temp)
        weights += temp
        for ids in range(getStateSize()):
            if state[ids] < 100:
                per[0][int(state[ids])][ids] += temp/np.max(temp)
    else:
        for ids in range(getStateSize()):
            if state[ids] < 100:
                weights += np.argsort(np.argsort(per[0][int(state[ids])][ids]))/getActionSize()
    output = weights * actions + actions
    action = np.argmax(output)
    win = getReward(state)
    if win != -1:
        if win == 1:
            # print("đây")
            per[1] += per[0]
            per[2][0][0][0] = 1
        else:
            per[0][:, :, :] = 0.0
            per[2][0][0][0] = 0
    return action, per

@njit
def Test(state, per):
    state_int = state.astype(np.int64)
    stateSize = getStateSize()
    actionSize = getActionSize()
    where_ = np.where((state_int < per[stateSize][0]) & (state_int >= 0))[0]
    weight = np.zeros(actionSize)
    for i in where_:
        weight += per[i][state_int[i]]

    actions = getValidActions(state)
    output = (weight + 1) * actions
    action = np.argmax(output)

    return action, per

def convert_to_save(perData):
    if len(perData) == getStateSize() + 1:
        raise Exception("Data này đã được convert rồi.")
    data = List()
    arr = np.zeros(getStateSize(), int)
    for i in range(getStateSize()):
        for j in range(100):
            if (perData[1][j, i] == 0).all():
                check = True
                for k in range(j, 100):
                    if (perData[1][k, i] != 0).any():
                        check = False
                        break
                if check:
                    arr[i] = j
                    break
        else:
            arr[i] = 100
    
    for i in range(getStateSize()):
        data.append(perData[1][:arr[i], i])
        for j in range(data[i].shape[0]):
            data[i][j] = np.argsort(np.argsort(data[i][j]))/float(getActionSize())
    
    data.append(np.array([arr], float))
    return data

def convert_to_test(perData):
    return List(perData)