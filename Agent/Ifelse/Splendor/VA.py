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


def DataAgent():
    per = np.array([0])
    return per


from Base.Splendor.env import __NORMAL_CARD__


@njit()
def valueOf(cardId, pDevCards, pTokens):
    infoCard = __NORMAL_CARD__[cardId - 5]
    score = infoCard[0]
    cost = infoCard[6:]
    needs = cost - pDevCards - pTokens
    needs[needs < 0] = 0
    needs[needs > 0] = 1
    return (score + 1) / (np.sum(needs) + 1)


@njit()
def Test(state, per):
    validActions = getValidActions(state)
    validActions = np.where(validActions == 1)[0]

    pInfo = state[201:213]
    pTokens = pInfo[1:6]
    pDevCards = pInfo[6:11]

    purchaseCardActions = validActions[(validActions >= 5) & (validActions < 95)]
    if len(purchaseCardActions) > 0:
        valueOfCards = np.zeros_like(purchaseCardActions) - 1
        for i in range(len(purchaseCardActions)):
            valueOfCards[i] = valueOf(purchaseCardActions[i], pDevCards, pTokens)
        action = purchaseCardActions[0]
        for i in range(len(purchaseCardActions)):
            if valueOfCards[i] > valueOf(action, pDevCards, pTokens):
                action = purchaseCardActions[i]
        return action, per

    takeTokenActions = validActions[(validActions >= 0) & (validActions < 5)]
    if len(takeTokenActions) > 0:
        action = takeTokenActions[np.random.randint(len(takeTokenActions))]
        return action, per

    action = validActions[np.random.randint(len(validActions))]
    return action, per
