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
    return np.array([0])

@njit()
def Test(state, per):
    validActions = getValidActions(state)
    validActions = np.where(validActions == 1)[0]

    if state[12]<5:
        if 0 in validActions:
            return 0, per
    if 11 in validActions:
        return 11, per
    if state[61] == 1:# Mage is choosen
        for i in (2, 3, 4, 5, 6, 7):
            if i in validActions:
                return i, per
        if np.sum(state[63:69]) == 0:
            if 0 in validActions:
                return 0, per
    if state[53] == 1: #Barbarian is choosen
        for i in (3, 4, 5, 6, 7, 2):
            if i in validActions:
                return i, per
        if np.sum(state[55:61]) == 0:
            if 0 in validActions:
                return 0, per
    action = np.random.choice(validActions)
    return action, per

