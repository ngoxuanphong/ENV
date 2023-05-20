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
    policy = np.array(
        [
            0,
            1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            10,
            10,
            10,
            10,
            10,
            10,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            15,
            -1,
            0,
        ]
    ).astype(np.int64)
    return policy


@njit()
def getLuaMi(state):
    return state[1]


@njit()
def getNongTrai(state):
    return state[2]


@njit()
def getTiemBanh(state):
    return state[3]


@njit()
def getQuanCaPhe(state):
    return state[4]


@njit()
def getCuaHangTienLoi(state):
    return state[5]


@njit()
def getRung(state):
    return state[6]


@njit()
def getQuanAnGiaDinh(state):
    return state[10]


@njit()
def getChoTraiCay(state):
    return state[12]


def getTrungTamThuongMai(state):
    return state[15]


@njit()
def get22dCard(state):
    return state[16]


@njit()
def get16dCard(state):
    return state[17]


@njit()
def get10dCard(state):
    return state[18]


@njit()
def get4dCard(state):
    return state[19]


@njit()
def Test(state, per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0].astype(np.int64)
    phase = state[122:129]
    phase = np.where(phase == 1)[0]
    dice = state[117]

    if get10dCard(state) > 0:
        per[49] = 10
    if get22dCard(state) > 0:
        per[50] = 10
    if get16dCard(state) > 0:
        per[52] = 10
    if phase == 1:
        if dice != 4 and dice != 2:
            return 1, per
        elif dice == 4 or dice == 2:
            return 0, per
    if state[18] == 1 and getQuanAnGiaDinh(state) < 1 and 43 in actions:
        return 43, per
    if getQuanCaPhe(state) > 1:
        per[37] = -1
    if getReward(state) == 0 or getReward(state) == 1:
        per = np.array(
            [
                0,
                1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                10,
                10,
                10,
                10,
                10,
                10,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                15,
                -1,
                0,
            ]
        ).astype(np.int64)
    point_actions = per[actions]
    idx = np.argmax(point_actions)
    action = actions[idx]
    return action, per
