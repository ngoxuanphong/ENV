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


@njit
def DataAgent():
    return np.array([0])


@njit
def Test(state, per):
    actions = np.where(getValidActions(state) == 1)[0]
    value = np.array(
        [
            1,
            12,
            13,
            27,
            39,
            51,
            60,
            14,
            26,
            37,
            20,
            30,
            45,
            15,
            41,
            40,
            55,
            29,
            61,
            64,
            63,
            34,
            35,
            10,
            11,
            53,
            33,
            54,
            58,
            7,
            59,
            43,
            5,
            19,
            8,
            42,
            38,
            2,
            31,
            56,
            50,
            66,
            57,
            44,
            32,
            46,
            48,
            6,
            47,
            36,
            4,
            49,
            62,
            52,
            9,
            23,
            3,
            24,
            65,
            16,
            17,
            67,
            25,
            18,
            21,
            0,
            22,
            28,
        ]
    )
    for a in value:
        if a in actions:
            return a, per
