import importlib.util
from setup import SHOT_PATH
import sys

import warnings

warnings.filterwarnings("ignore")
from numba.core.errors import (
    NumbaDeprecationWarning,
    NumbaPendingDeprecationWarning,
    NumbaExperimentalFeatureWarning,
    NumbaWarning,
)

warnings.simplefilter("ignore", category=NumbaDeprecationWarning)
warnings.simplefilter("ignore", category=NumbaPendingDeprecationWarning)
warnings.simplefilter("ignore", category=NumbaExperimentalFeatureWarning)
warnings.simplefilter("ignore", category=NumbaWarning)

COUNT_TEST = 1000


# check hết hệ thống
def CheckAllFunc(Agent, BOOL_CHECK_ENV, msg):
    for func in ["DataAgent", "Train", "Test"]:
        try:
            getattr(Agent, func)
        except:
            msg.append(f"Không có hàm: {func}")
            BOOL_CHECK_ENV = False
    return BOOL_CHECK_ENV, msg


def setup_game(game_name):
    try:
        spec = importlib.util.spec_from_file_location(
            "env", f"{SHOT_PATH}base/{game_name}/env.py"
        )
    except:
        spec = importlib.util.spec_from_file_location("env", f"base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def CheckRunGame(Agent, BOOL_CHECK_ENV, msg):
    for game_name in [
        "Splendor_v2",
        "Splendor_v3",
        "MachiKoro",
        "SushiGo",
        "TLMN",
        "TLMN_v2",
    ]:
        env = setup_game(game_name)
        try:
            per = Agent.DataAgent()
            win, per = env.numba_main_2(Agent.Train, COUNT_TEST, per, 0)
        except:
            msg.append(f"Train đang bị lỗi {game_name}")
            BOOL_CHECK_ENV = False
            break

        try:
            per = Agent.DataAgent()
            win, per = env.numba_main_2(Agent.Test, COUNT_TEST, per, 0)
        except:
            msg.append(f"Test đang bị lỗi {game_name}")
            BOOL_CHECK_ENV = False
            break

    return BOOL_CHECK_ENV, msg


def check_agent(Agent):
    BOOL_CHECK_ENV = True
    msg = []
    BOOL_CHECK_ENV, msg = CheckAllFunc(Agent, BOOL_CHECK_ENV, msg)
    BOOL_CHECK_ENV, msg = CheckRunGame(Agent, BOOL_CHECK_ENV, msg)
    return BOOL_CHECK_ENV, msg
