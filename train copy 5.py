import sys
import os
import time
from setup import SHORT_PATH
import importlib.util, sys
import numpy as np

agent_name = 'MultiDimensionAlgorithm'
game_name = 'Phom'
training_time = 12*60*60
level = 0
mode = "train"
print(game_name, agent_name)

def add_game_to_syspath(game_name):
    if len(sys.argv) >= 2:
        sys.argv = [sys.argv[0]]
    sys.argv.append(game_name)

def CreateFolder(player, game_name, level): #Tên folder của người chơi
    path_data = f'Agent/{player}/Data'
    if not os.path.exists(path_data):
        os.mkdir(path_data)
    path_save_player = f'Agent/{player}/Data/{game_name}_{level}/'
    if not os.path.exists(path_save_player):
        os.mkdir(path_save_player)
    return path_save_player

def load_module_player(player, game_name = None):
    if game_name == None:
        spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/{player}/Agent_player.py")
    else:
        spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/ifelse/{game_name}/{player}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"Base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module 
    spec.loader.exec_module(module)
    return module

add_game_to_syspath(game_name)
path_save = CreateFolder(agent_name, game_name, level)
_p1_ = load_module_player(agent_name)
_env_ = setup_game(game_name)
print(path_save)

try:
    raise
    per_agent = _p1_.convert_to_test(np.load(path_save+"Train.npy", allow_pickle=True))
    print("Đã đọc được file data.")
except:
    per_agent = _p1_.DataAgent()
    print("Đã khởi tạo data.")


if mode == "train":
    start = time.time()
    N = 10000
    count = N
    while True:
        win, per_agent = _env_.numba_main_2(_p1_.Train, N, per_agent, level)
        count_time = time.time() - start
        print("Xong", count, "trận sau", count_time)
        count += N
        if count_time >= training_time:
            break
    
    np.save(path_save+"Train.npy", _p1_.convert_to_save(per_agent))
    print("Đã train xong:", time.time()-start)

    per_test = _p1_.convert_to_test(np.load(path_save+"Train.npy", allow_pickle=True))

    win, per_agent = _env_.numba_main_2(_p1_.Test, 1000, per_test, level)
    print("Thắng", win, "trận.")
# else:
#     win, per_agent = _env_.numba_main_2(_p1_.Test, 1000, per_agent, level)
#     print("Thắng", win, "trận.")