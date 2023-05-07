import numpy as np
from numba import njit
from numba.typed import List
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


def DataAgent():
    return np.array([0])


@njit()
def valueOf(action, master, nLeftCards):
    if action == 52:
        if nLeftCards > 0:
            return 3
        return 1
    if action // 13 == master:
        return 2
    return 20 - action % 13


@njit()
def Test(state, per):
    validActions = getValidActions(state)
    validActions = np.where(validActions == 1)[0]
    master = np.where(state[158:162] == 1)[0][0]

    valueOfActions = np.zeros_like(validActions)
    for i in range(len(validActions)):
        valueOfActions[i] = valueOf(validActions[i], master, state[162])
    action = validActions[np.argmax(valueOfActions)]
    return action, per
