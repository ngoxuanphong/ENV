# ENV - Environment for Reinforcement Learning
ENV is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API
##  Installation
We are support Python 3.7, 3.8, 3.9, 3.10 on Linux and Windows
To install the base ENV library, use:
- Using pip:
    ```
    Update later
    ```

- Directly from source (recommended):
    ```
    git clone https://github.com/ngoxuanphong/ENV.git
    cd ma-gym
    pip install -r requirements.txt
    ```

##  API
```
from setup import make
from numba import njit
import numpy as np

@njit()
def Agent(state, agent_data):
    validActions = env.getValidActions(state)
    actions = np.where(validActions==1)[0]
    action = np.random.choice(actions)
    return arr_action[idx], agent_data

count_win, agent_data = env.numba_main_2(Agent, count_game_train, agent_data, level)
```

Please refer to [Wiki](https://github.com/ngoxuanphong/ENV/wiki/Using) for complete usage details

##  Environment
ENV includes 20 games:
* [Catan](https://github.com/ngoxuanphong/ENV/tree/main/Base/Catan/)
* [CatanNoExchange](https://github.com/ngoxuanphong/ENV/tree/main/Base/CatanNoExchange/)
* [Century](https://github.com/ngoxuanphong/ENV/tree/main/Base/Century/)
* [Durak](https://github.com/ngoxuanphong/ENV/tree/main/Base/Durak/)
* [Exploding_Kitten](https://github.com/ngoxuanphong/ENV/tree/main/Base/Exploding_Kitten/)
* [Imploding_Kitten](https://github.com/ngoxuanphong/ENV/tree/main/Base/Imploding_Kitten/)
* [MachiKoro](https://github.com/ngoxuanphong/ENV/tree/main/Base/MachiKoro/)
* [Poker](https://github.com/ngoxuanphong/ENV/tree/main/Base/Poker/)
* [Sheriff](https://github.com/ngoxuanphong/ENV/tree/main/Base/Sheriff/)
* [Splendor](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor/)
* [Splendor_v2](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor_v2/)
* [Splendor_v3](https://github.com/ngoxuanphong/ENV/tree/main/Base/Splendor_v3/)
* [StoneAge](https://github.com/ngoxuanphong/ENV/tree/main/Base/StoneAge/)
* [SushiGo](https://github.com/ngoxuanphong/ENV/tree/main/Base/SushiGo/)
* [TicketToRide](https://github.com/ngoxuanphong/ENV/tree/main/Base/TicketToRide/)
* [TLMN](https://github.com/ngoxuanphong/ENV/tree/main/Base/TLMN/)

    Please refer to [Wiki](https://github.com/ngoxuanphong/ENV/wiki/Environments) for more details.
