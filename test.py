# Check hệ thống

import Base.Sheriff.env as env
from CheckEnv import check_env
print(check_env(env))


# env = make('MachiKoro')
# getActionSize = env.getActionSize
# getStateSize = env.getStateSize
# getAgentSize = env.getAgentSize

# getValidActions = env.getValidActions
# getReward = env.getReward
# numba_main_2 = env.numba_main_2


# import numpy as np
# from numba import njit, jit
# from setup import make
# @njit()
# def bot_lv0(state, perData):
#     validActions = getValidActions(state)
#     arr_action = np.where(validActions==1)[0]
#     idx = np.random.randint(0, arr_action.shape[0])
#     return arr_action[idx], perData

# win1, per = numba_main_2(bot_lv0, 1000, np.array([0]), 0)
# win2, per = numba_main_2(bot_lv0, 1000, np.array([0]), 1)
# print(win1, win2)