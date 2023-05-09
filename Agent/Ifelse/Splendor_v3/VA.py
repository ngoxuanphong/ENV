import numpy as np
import random as rd
from numba import njit, jit
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
    return np.array([])


@njit()
def valueOf(card, pGemTokens, pGoldTokens, pDevCards, adjust=0):
    if np.sum(card) == 0:
        return -1
    cost = card[-5:]
    score = card[0]
    needs = cost - pDevCards - pGemTokens
    needs[needs < 0] = 0
    needs[needs > 0] = 1
    if adjust == 1:
        return 1 / ((score + 1) * (np.sum(needs) + 1))
    return (score + 1) / (np.sum(needs) + 1)


@njit()
def Test(state, per):
    pGemTokens = state[6:11]
    pGoldTokens = state[11]
    pDevCards = state[12:17]

    adjust = 0
    if state[17] <= 8:
        adjust = 1

    faceupCards = state[18:150]
    facedownCards = state[175:208]
    cards = np.append(faceupCards, facedownCards).reshape(15, -1)
    valueOfCards = np.array(
        [valueOf(card, pGemTokens, pGoldTokens, pDevCards, adjust) for card in cards]
    )
    mostValuableCards = (-valueOfCards).argsort()[:1]
    action = mostValuableCards[np.random.randint(len(mostValuableCards))]
    return action, per
