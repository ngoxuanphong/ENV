import numpy as np
from numba import njit
from numba.typed import List
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


def DataAgent():
    perx_ = List()
    stateSize = getStateSize()
    actionSize = getActionSize()
    perx_.append(np.zeros((1000*stateSize, actionSize)))
    perx_.append(np.zeros((1000*stateSize, actionSize)))
    perx_.append(np.zeros((1,2)))

    temp = np.arange(actionSize, dtype=np.float64)
    perx_.append(np.array([temp]))
    
    perx_.append(np.zeros((1,1)))

    return perx_


@njit
def Train(state, per):
    if per[4][0][0] == 1:
        per[1][:,:] = 0.0
        per[4][0][0] = 0

    weight = per[3][0]
    np.random.shuffle(weight)
    actions = getValidActions(state)
    output = (weight + 1) * actions
    action = np.argmax(output)

    stateSize = getStateSize()
    # Tìm các max value cho array bias
    if per[2][0][1] >= 9000:
        state_int = state.astype(np.int64)
        state_int[state_int >= 1000] = 1000 - 1
        where_ = np.where((state_int <= per[2][0][0]) & (state_int >= 0))[0]
        arr_idx = (where_ * per[0].shape[0] / stateSize + state_int[where_]).astype(np.int64)
        arr_idx = arr_idx[arr_idx <= 1000*stateSize]
        per[1][arr_idx] += weight
    else:
        max_ = np.max(state)
        if max_ > np.int64(per[2][0][0]):
            per[2][0][0] = max_ + 1

    # Bắt đầu lưu array bias
    reward = getReward(state)
    if per[2][0][1] >= 9000:
        if reward == 1:
            per[0] += per[1]
            per[1][:,:] = 0.0
        elif reward == 0:
            per[1][:,:] = 0.0

    if reward != -1:
        per[2][0][1] += 1

    return action, per


@njit
def Test(state, per):
    if per[4][0][0] == 0:
        per[1] = per[0]
        for i in range(per[1].shape[0]):
            per[1][i] /= (np.max(per[1][i]) + 1e-6)
        
        per[4][0][0] = 1

    state_int = state.astype(np.int64)
    state_int[state_int >= 1000] = 1000 - 1
    stateSize = getStateSize()
    where_ = np.where((state_int <= per[2][0][0]) & (state_int >= 0))[0]
    arr_idx = (where_ * per[0].shape[0] / stateSize + state_int[where_]).astype(np.int64)
    weight = np.zeros(getActionSize())
    weight = np.sum(per[1][arr_idx], axis=0)

    actions = getValidActions(state)
    output = (weight + 1) * actions
    action = np.argmax(output)

    return action, per


def convert_to_save(per_data):
    return per_data


def convert_to_test(per_data):
    return List(per_data)