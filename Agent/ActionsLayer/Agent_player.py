import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHORT_PATH
import importlib.util

game_name = sys.argv[1]


def setup_game(game_name):
    spec = importlib.util.spec_from_file_location(
        "env", f"{SHORT_PATH}Base/{game_name}/env.py"
    )
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
    if len(perData) == 2:
        raise Exception("Data này đã được convert rồi.")

    data = List()
    data.append(np.zeros((1, getActionSize())))
    temp = np.zeros((getActionSize(), getActionSize()))
    for i in range(temp.shape[0]):
        temp[i] = np.argsort(np.argsort(perData[2][i])) + 1e-6 * np.random.rand(
            getActionSize()
        )

    data.append(temp)
    return data


def convert_to_test(perData):
    return List(perData)


@njit()
def DataAgent():
    return List(
        [
            np.zeros((1, getActionSize())),
            np.random.rand(getActionSize(), getActionSize()),
            np.zeros((getActionSize(), getActionSize())),
        ]
    )


@njit()
def Train(state, per):
    actions = getValidActions(state)
    weight = per[0][0]

    output = actions * weight + actions
    c = np.where(output == np.max(output))[0]
    action = c[np.random.randint(0, c.shape[0])]

    per[0] += per[1][action]
    win = getReward(state)

    if win != -1:
        per[0][:, :] = 0.0
        if win == 1:
            per[2] += per[1]
        else:
            per[1] = np.random.rand(getActionSize(), getActionSize())

    return action, per


@njit()
def Test(state, per):
    actions = getValidActions(state)
    weight = per[0][0]

    output = actions * weight + actions
    action = np.argmax(output)

    weight[:] += per[1][action]
    win = getReward(state)
    if win != -1:
        per[0][:, :] = 0.0
    return action, per
