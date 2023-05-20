import importlib.util
import os
import sys

import numpy as np
from numba import njit
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


def DataAgent():
    return List([np.zeros((1, 1))])


@njit()
def Test(state, per):
    ValidActions = getValidActions(state)
    ValidActions = np.where(ValidActions == 1)[0]

    if state[12] <= 9 and 1 in ValidActions:
        return 1, per
    if state[13] >= 4 and 0 in ValidActions:
        return 0, per

    for i in range(3, 15):
        if i in ValidActions:
            return i, per

    action = ValidActions[np.random.randint(len(ValidActions))]
    return action, per
