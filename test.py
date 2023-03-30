# Check hệ thống
# import Base.TicketToRide.env as env
# from CheckEnv import check_env
# print(check_env(env))

from setup import make
import numpy as np
from numba import njit, jit
import time

env = make('StoneAge')
getActionSize = env.getActionSize
getStateSize = env.getStateSize
getAgentSize = env.getAgentSize

getValidActions = env.getValidActions
getReward = env.getReward
numba_main_2 = env.numba_main_2

@njit()
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData

win1, per = numba_main_2(bot_lv0, 1000, np.array([0]), 0)
print(win1)
# a = time.process_time()
# win2, per = numba_main_2(bot_lv0, 1000, np.array([0]), 1)
# b = time.process_time()
# print(win2, b-a)

a = time.process_time()
win3, per = numba_main_2(bot_lv0, 1000, np.array([0]), -1)
b = time.process_time()
print(win3, b-a)