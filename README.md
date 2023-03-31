## Installation

In terminal: 
    - git clone https://github.com/ngoxuanphong/ENV.git

## API

```
from setup import make
from numba import njit, jit
import numpy as np

@njit()
def Agent(state, perData):
    validActions = env.getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData

perData = np.array([0])
level = 0
count_game_train = 1000
count_win, perData = numba_main_2(Agent, count_game_train, perData, level)
print(count_win)
```

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
