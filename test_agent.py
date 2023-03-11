import sys
import os
import time
from setup import SHORT_PATH
import importlib.util, sys
import numpy as np
list_game = os.listdir("Base/")
agent_name = 'MultiDimensionAlgorithm'
print(agent_name)
level = 0
N = 100
for game_name in list_game:
    print("-------------------------")
    # game_name = 'TLMN'
    # print(game_name, agent_name)

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

    def load_module_player(player):
        spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/{player}/Agent_player.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module

    def setup_game(game_name):
        spec = importlib.util.spec_from_file_location('env', f"base/{game_name}/env.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module 
        spec.loader.exec_module(module)
        return module


    add_game_to_syspath(game_name)
    path_save = CreateFolder(agent_name, game_name, level)
    _p1_ = load_module_player(agent_name)
    _env_ = setup_game(game_name)
    # print(path_save)


    try:
        per_agent = _p1_.convert_to_test(np.load(path_save+"Train.npy", allow_pickle=True))
        # print("Đã đọc được file data.")
    except:
        per_agent = _p1_.DataAgent()
        per_agent = _p1_.convert_to_save(per_agent)
        print("Đã khởi tạo data.")


    win, per_agent = _env_.numba_main_2(_p1_.Test, 10, per_agent, level)
    # print("Thắng", win, "trận.")

    start = time.time()
    win, per_agent = _env_.numba_main_2(_p1_.Test, N, per_agent, level)
    end = time.time()
    print(game_name, ". Thắng", win, "trận, thời gian", end - start)