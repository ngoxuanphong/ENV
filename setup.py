
DRIVE_FOLDER = "G:/My Drive/AutomaticColab/"
SHORT_PATH = ""
import importlib.util
import sys


def make(game_name: str = 'RockPaperScissors'):
    '''
    This function is used to setup the game environment.
    It is used to import the game environment from the game folder.
    '''
    global _game_name
    _game_name = game_name
    def add_game_to_syspath(game_name):
        if len(sys.argv) >= 2:
            sys.argv = [sys.argv[0]]
        sys.argv.append(game_name)

    def setup_game():
        spec = importlib.util.spec_from_file_location(
            "env", f"{SHORT_PATH}src/env.py"
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module

    add_game_to_syspath(game_name)
    env = setup_game()

    return env

def setup_game(game_name):
    global _game_name
    _game_name = game_name
    # print(game_name)
    spec = importlib.util.spec_from_file_location(
        "env", f"{SHORT_PATH}src/env.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
