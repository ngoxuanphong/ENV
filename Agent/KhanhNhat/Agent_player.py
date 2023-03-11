import numpy as np
from numba import njit
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


def DataAgent():
    perx_ = List()
    stateSize = getStateSize()
    actionSize = getActionSize()
    perx_.append(np.zeros((1000*stateSize, actionSize)))
    perx_.append(np.zeros((1000*stateSize, actionSize)))
    perx_.append(np.zeros((1,2)))

    temp = np.arange(actionSize, dtype=np.float64)
    perx_.append(np.array([temp]))
    return perx_


@njit
def Train(state, per):
    weight = per[3][0]
    np.random.shuffle(weight)
    actions = getValidActions(state)
    output = (weight + 1) * actions
    action = np.argmax(output)

    # Tìm các max value cho array bias
    if per[2][0][1] >= 9000:
        state_int = state.astype(np.int64)
        state_int[state_int >= 1000] = per[2][0][0] + 1
        where_ = np.where((state_int <= per[2][0][0]) & (state_int >= 0))[0]
        arr_idx = (where_ * 1000 + state_int[where_]).astype(np.int64)
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


def convert_to_save(per_data):
    if len(per_data) == getStateSize() + 1:
        raise Exception("Data này đã được convert rồi.")

    data = List()
    arr = np.zeros(getStateSize(), np.int64)
    for i in range(getStateSize()):
        for j in range(1000):
            if (per_data[0][1000*i+j]==0).all():
                check = True
                for k in range(j, 1000):
                    if (per_data[0][1000*i+k]!=0).any():
                        check = False
                        break
                if check:
                    arr[i] = j
                    break
        else:
            arr[i] = 1000

    for i in range(getStateSize()):
        data.append(per_data[0][1000*i:1000*i+arr[i]])

    data.append(np.array([arr.astype(float)]))
    for i in range(0, len(data)-1):
        for j in range(data[i].shape[0]):
            if np.max(data[i][j]) != 0.0:
                data[i][j] /= np.max(data[i][j])

    return data


def convert_to_test(per_data):
    return List(per_data)