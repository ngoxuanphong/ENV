import importlib.util
import os
import random as rd
import sys

import numpy as np
from numba import jit, njit
from numba.typed import List

from setup import SHORT_PATH

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


@njit()
def DataAgent():
    return np.array([0])


@njit()
def Test(state, per):
    validActions = getValidActions(state)
    validActions = np.where(validActions == 1)[0]

    if 9 in validActions:
        return 9, per

    if 7 in validActions:
        return 7, per

    if 1 in validActions:
        return 1, per

    if 12 in validActions:
        return 12, per

    if 5 in validActions:
        return 5, per

    if 6 in validActions:
        return 6, per

    if 10 in validActions:
        return 10, per

    if 2 in validActions:
        return 2, per

    if 0 in validActions:
        return 0, per

    if 8 in validActions:
        return 8, per

    if 4 in validActions:
        return 4, per

    if 3 in validActions:
        return 3, per

    if 11 in validActions:
        return 11, per

    action = validActions[np.random.randint(len(validActions))]
    return action, per
