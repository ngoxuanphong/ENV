## Installation
**In terminal**
    ```
    git clone https://github.com/ngoxuanphong/ENV.git
    ```

## API
```
from setup import make
from numba import njit, jit
import numpy as np

@njit()
def Agent(state, perData):
    validActions = env.getValidActions(state)
    actions = np.where(validActions==1)[0]
    action = np.random.choice(actions)
    return arr_action[idx], perData

perData = np.array([0])
level = 0
count_game_train = 1000
count_win, perData = env.numba_main_2(Agent, count_game_train, perData, level)
print(count_win)
```

## FUNCTION
    * Agent(state, perData):
        input: state, data
        output: action(int), data
    * getValidActions(state): 
        input: state(np.float64)
        output: np.array valid action in turn of Environment
    * getReward(state):
        input: state(np.float64)
        output: -1, 0, 1
    * getActionSize():
        input: None
        output: int, count of array action size of Env
    * getStateSize():
        input: None
        output: int, count of array state size of Env

## Environment
* [Catan](https://github.com/ngoxuanphong/ENV/tree/main/Base/Catan/)
* [CatanNoExchange](https://github.com/ngoxuanphong/ENV/tree/main/Base/CatanNoExchange/)
* [Century](https://github.com/ngoxuanphong/ENV/tree/main/Base/Century/)
* [Durak](https://github.com/ngoxuanphong/ENV/tree/main/Base/Durak/)
* [Exploding_Kitten](https://github.com/ngoxuanphong/ENV/tree/main/Base/Exploding_Kitten/)
* [Imploding_Kitten](https://github.com/ngoxuanphong/ENV/tree/main/Base/Imploding_Kitten/)
* [MachiKoro](https://github.com/ngoxuanphong/ENV/tree/main/Base/MachiKoro/)
* [Phom](https://github.com/ngoxuanphong/ENV/tree/main/Base/Phom/)
* [Poker](https://github.com/ngoxuanphong/ENV/tree/main/Base/Poker/)
* [Sheriff](https://github.com/ngoxuanphong/ENV/tree/main/Base/Sheriff/)
* [Splendor](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor/)
* [Splendor_v2](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor_v2/)
* [Splendor_v3](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor_v3/)
* [StoneAge](https://github.com/ngoxuanphong/ENV/tree/main/Base/StoneAge/)
* [SushiGo](https://github.com/ngoxuanphong/ENV/tree/main/Base/SushiGo/)
* [TicketToRide](https://github.com/ngoxuanphong/ENV/tree/main/Base/TicketToRide/)
* [TLMN](https://github.com/ngoxuanphong/ENV/tree/main/Base/TLMN/)

## Make Environment
    * [Manual](https://docs.google.com/document/d/1I2Fquk4aEHwC-v_ROxmONNlOXUtiNQWWS6eiYBQUEeM/edit)
    
## Check Environment
    ```
    from CheckEnv import check_env
    import your_env as env #path to your env
    print(check_env(env))
    ```

## Check Agent
    ```
    from CheckPlayer import check_player
    import your_agent as agent #path to your env
    print(check_player(env))
    ```