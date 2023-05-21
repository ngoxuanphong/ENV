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


@njit()
def DataAgent():
    return np.array([0.0])


@njit()
def Test(state, per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0]
    if state[12] > 8:
        if 0 in actions:
            return 0, per
    if 1 in actions:
        return 1, per
    if 2 in actions:
        return 2, per
    for action in actions:
        if action in range(15, 19):
            return action, per
    return np.random.choice(actions), per
