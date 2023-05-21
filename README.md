# ENV - Environment for Reinforcement Learning
ENV is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API

![Python package](https://github.com/ngoxuanphong/ENV/workflows/Python%20package/badge.svg) 
<!-- ![Upload Python Package](https://github.com/ngoxuanphong/ENV/workflows/Upload%20Python%20Package/badge.svg) -->
<!-- [![Downloads](https://pepy.tech/badge/ma-gym)](https://pepy.tech/project/ma-gym) -->
[![Wiki Docs](https://img.shields.io/badge/-Wiki%20Docs-informational?style=flat)](https://github.com/ngoxuanphong/ENV/wiki)

##  Installation
We are support Python 3.7, 3.8, 3.9, 3.10 on Linux and Windows
To install the base ENV library, use:
- Using pip:
    ```python
    Update later
    ```

- Directly from source (recommended):
    ```python
    git clone https://github.com/ngoxuanphong/ENV.git
    cd ENV
    pip install -r requirements.txt
    ```

##  API
```python
from setup import make
from numba import njit
import numpy as np

@njit()
def Agent(state, agent_data):
    validActions = env.getValidActions(state)
    actions = np.where(validActions==1)[0]
    action = np.random.choice(actions)
    return action, agent_data
    
env = make('SushiGo')
env.numba_main_2(Agent, 1000, [0], 0)
# count_win, agent_data = env.numba_main_2(Agent, count_game_train, agent_data, level)
```
[Example](https://github.com/ngoxuanphong/ENV/blob/main/Log/Example.ipynb)

Please refer to [Wiki](https://github.com/ngoxuanphong/ENV/wiki/Using) for complete usage details

##  Environment
ENV includes 20 games:

|Game        |Win lv0       |win lv1        |win lv1        |Time lv0       |Time lv1       |Time lv1       |
|:-----------|:-----------  |:-----------   |:-----------   |:-----------   |:-----------   |:-----------   |
|Catan     |2535| 211| 13      |307| 224| 324|
|CatanNoExchange     |2464| 339| False      |190| 673| False|
|Century     |1932| 12| 1      |48| 51| 52|
|Durak     |2561| 447| False      |15| 18| False|
|Exploding_Kitten     |2002| 1631| False      |18| 16| False|
|Fantan     |2413| 117| False      |27| 63| False|
|GoFish     |2536| 2499| False      |10| 12| False|
|Imploding_Kitten     |1659| 1316| False      |37| 39| False|
|MachiKoro     |2542| 53| 7      |13| 14| 18|
|Phom     |2444| 500| False      |31| 33| False|
|Poker     |1109| 1155| False      |71| 59| False|
|Sheriff     |2510| 3| 362      |28| 30| 33|
|Splendor     |2449| 28| 1      |114| 154| 90|
|Splendor_v2     |2621| 15| 1      |48| 51| 50|
|Splendor_v3     |2615| 677| 29      |29| 26| 36|
|StoneAge     |2467| 36| 0      |92| 217| 133|
|SushiGo     |2010| 141| 154      |11| 14| 14|
|TicketToRide     |2041| 0| False      |60| 913| False|
|TLMN     |2456| 772| 262      |16| 17| 26|
|WelcomeToTheDungeon_v1     |2530| 833| 796      |3| 12| 15|
|WelcomeToTheDungeon_v2     |2481| 914| 464      |4| 15| 14|

Please refer to [Wiki](https://github.com/ngoxuanphong/ENV/wiki/Environments) for more details.
