import numpy as np
from numba import njit
from numba.typed import List


__ACTIONS__ = np.array([[0,-1],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15],[1,16],[1,17],[1,18],[1,19],[1,20],[1,21],[1,22],[1,23],[1,24],[1,25],[1,26],[1,27],[1,28],[1,29],[1,30],[1,31],[1,32],[1,33],[1,34],[1,35],[1,36],[1,37],[1,38],[1,39],[1,40],[1,41],[1,42],[1,43],[1,44],[1,45],[1,46],[1,47],[1,48],[1,49],[1,50],[1,51],[2,1],[2,2],[2,3],[2,5],[2,6],[2,7],[2,9],[2,10],[2,11],[2,13],[2,14],[2,15],[2,17],[2,18],[2,19],[2,21],[2,22],[2,23],[2,25],[2,26],[2,27],[2,29],[2,30],[2,31],[2,33],[2,34],[2,35],[2,37],[2,38],[2,39],[2,41],[2,42],[2,43],[2,45],[2,46],[2,47],[2,49],[2,50],[2,51],[3,2],[3,3],[3,6],[3,7],[3,10],[3,11],[3,14],[3,15],[3,18],[3,19],[3,22],[3,23],[3,26],[3,27],[3,30],[3,31],[3,34],[3,35],[3,38],[3,39],[3,42],[3,43],[3,46],[3,47],[3,50],[3,51],[4,3],[4,7],[4,11],[4,15],[4,19],[4,23],[4,27],[4,31],[4,35],[4,39],[4,43],[4,47],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[5,14],[5,15],[5,16],[5,17],[5,18],[5,19],[5,20],[5,21],[5,22],[5,23],[5,24],[5,25],[5,26],[5,27],[5,28],[5,29],[5,30],[5,31],[5,32],[5,33],[5,34],[5,35],[5,36],[5,37],[5,38],[5,39],[5,40],[5,41],[5,42],[5,43],[5,44],[5,45],[5,46],[5,47],[6,12],[6,13],[6,14],[6,15],[6,16],[6,17],[6,18],[6,19],[6,20],[6,21],[6,22],[6,23],[6,24],[6,25],[6,26],[6,27],[6,28],[6,29],[6,30],[6,31],[6,32],[6,33],[6,34],[6,35],[6,36],[6,37],[6,38],[6,39],[6,40],[6,41],[6,42],[6,43],[6,44],[6,45],[6,46],[6,47],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[7,33],[7,34],[7,35],[7,36],[7,37],[7,38],[7,39],[7,40],[7,41],[7,42],[7,43],[7,44],[7,45],[7,46],[7,47],[8,20],[8,21],[8,22],[8,23],[8,24],[8,25],[8,26],[8,27],[8,28],[8,29],[8,30],[8,31],[8,32],[8,33],[8,34],[8,35],[8,36],[8,37],[8,38],[8,39],[8,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[9,24],[9,25],[9,26],[9,27],[9,28],[9,29],[9,30],[9,31],[9,32],[9,33],[9,34],[9,35],[9,36],[9,37],[9,38],[9,39],[9,40],[9,41],[9,42],[9,43],[9,44],[9,45],[9,46],[9,47],[10,28],[10,29],[10,30],[10,31],[10,32],[10,33],[10,34],[10,35],[10,36],[10,37],[10,38],[10,39],[10,40],[10,41],[10,42],[10,43],[10,44],[10,45],[10,46],[10,47],[11,32],[11,33],[11,34],[11,35],[11,36],[11,37],[11,38],[11,39],[11,40],[11,41],[11,42],[11,43],[11,44],[11,45],[11,46],[11,47],[12,36],[12,37],[12,38],[12,39],[12,40],[12,41],[12,42],[12,43],[12,44],[12,45],[12,46],[12,47],[13,40],[13,41],[13,42],[13,43],[13,44],[13,45],[13,46],[13,47],[14,9],[14,10],[14,11],[14,13],[14,14],[14,15],[14,17],[14,18],[14,19],[14,21],[14,22],[14,23],[14,25],[14,26],[14,27],[14,29],[14,30],[14,31],[14,33],[14,34],[14,35],[14,37],[14,38],[14,39],[14,41],[14,42],[14,43],[14,45],[14,46],[14,47],[15,13],[15,14],[15,15],[15,17],[15,18],[15,19],[15,21],[15,22],[15,23],[15,25],[15,26],[15,27],[15,29],[15,30],[15,31],[15,33],[15,34],[15,35],[15,37],[15,38],[15,39],[15,41],[15,42],[15,43],[15,45],[15,46],[15,47]], dtype=np.int64)


__ENV_SIZE__ = 60
@njit()
def initEnv():
    env = np.full(__ENV_SIZE__, 0, dtype=np.int64)

    # [0:52] Th??ng tin 52 l?? b??i: 0 1 2 3 l?? tr??n tay ng?????i ch??i, -1 l?? ???? ????nh tr??n b??n
    # Quy ?????nh c??c l?? b??i: M???i index th??? hi???n tr???ng th??i c???a 1 l?? b??i. ??? index k:
        # m = k // 4: ????? l???n l?? b??i (m = 0 l?? l?? 3, m = 1 l?? l?? 4, . . ., m = 12 l?? l?? 2)
        # n = k % 4: Ch???t c???a l?? b??i (n = 0; 1; 2; 3 l???n l?????t t????ng ???ng B??ch, T??p, R??, C??)
    temp = np.arange(52, dtype=np.int64)
    np.random.shuffle(temp)
    for i in range(4):
        env[temp[13*i:13*(i+1)]] = i

    # Index ng?????i ch??i ??ang action
    # env[52] = 0

    # T??nh tr???ng ng?????i ch??i (b??? l?????t hay ch??a, 1 l?? ch??a b??? l?????t)
    env[53:57] = 1

    # Index ng?????i ch??i ????nh b??? b??i tr??n b??n (ho???c l?? ng?????i ch??i kh???i ?????u v??ng m???i)
    # env[57] = 0

    # Ki???u b??? b??i ???????c ????nh tr??n b??n v?? l?? cao nh???t c???a b??? ????
    # env[58:60] = 0

    #
    return env


__STATE_SIZE__ = 165
@njit()
def getAgentState(env, cards_in_pre_hand):
    state = np.zeros(__STATE_SIZE__, dtype=np.float64)
    cards_state = env[0:52]
    p_idx = env[52]
    players_state = env[53:57]
    own_cur_hand = env[57]

    # [0:52]: B??i tr??n tay b???n th??n
    state[np.where(cards_state==p_idx)[0]] = 1

    # [52:104]: B??i m?? c??c ng?????i kh??c ???? ????nh ra
    state[52 + np.where(cards_state==-1)[0]] = 1

    # 104, 105, 106: T??nh tr???ng b??? l?????t c???a nh???ng ng?????i ch??i kh??c theo th??? t???
    # 107, 108, 109: S??? l?? b??i c??n l???i c???a nh???ng ng?????i ch??i kh??c
    for i in range(1, 4):
        other_idx = (p_idx + i) % 4
        state[103+i] = players_state[other_idx]
        state[106+i] = np.count_nonzero(cards_state==other_idx)

    if own_cur_hand != p_idx:
        # 110, 111, 112: Ng?????i v???a ????nh ra b??? b??i tr??n b??n
        state_own_idx = (own_cur_hand - p_idx) % 4
        state[109+state_own_idx] = 1

        # [113:165]: C??c l?? b??i n???m trong b??? hi???n ??ang tr??n b??n
        state[113+cards_in_pre_hand] = 1

    return state


@njit()
def continuous_subsequence(arr, k):
    list_return = List([np.int64(0) for _ in range(0)])
    n = arr.shape[0]
    if n >= k:
        for i in range(0, n-k+1):
            sub_arr = arr[i:i+k]
            if np.max(sub_arr) - np.min(sub_arr) == k-1:
                list_return.append(sub_arr[k-1])

    return list_return


@njit()
def get_pos_hands(arr_card, h_type, pos_hand_types, pos_hand_score):
    pos_hands = List([np.array([0, 0], dtype=np.int64) for _ in range(0)])

    for hand_type in pos_hand_types:
        if hand_type == 0:
            pos_hands.append(np.array([0, -1], dtype=np.int64))
        elif hand_type == 1:
            for i in arr_card:
                if i >= pos_hand_score:
                    pos_hands.append(np.array([1, i], dtype=np.int64))
        elif hand_type >= 2 and hand_type <= 4:
            for i in range(13):
                if i != 12 or hand_type != 4:
                    temp = arr_card[arr_card//4 == i]
                    if temp.shape[0] >= hand_type:
                        for j in temp[hand_type-1:]:
                            if hand_type != h_type or j >= pos_hand_score:
                                pos_hands.append(np.array([hand_type, j], dtype=np.int64))
        elif hand_type >= 5 and hand_type <= 13:
            temp = np.unique(arr_card//4)
            arr_score = temp[temp < 12]
            list_subsequence = continuous_subsequence(arr_score, hand_type-2)
            for i in list_subsequence:
                temp = arr_card[arr_card//4==i]
                for j in temp:
                    if j >= pos_hand_score:
                        pos_hands.append(np.array([hand_type, j], dtype=np.int64))
        elif hand_type >= 14:
            arr_score = [np.int64(0) for _ in range(0)]
            for i in range(12):
                temp = arr_card[arr_card//4 == i]
                if temp.shape[0] >= 2:
                    arr_score.append(i)

            list_subsequence = continuous_subsequence(np.array(arr_score, dtype=np.int64), hand_type-11)
            for i in list_subsequence:
                temp = arr_card[arr_card//4 == i]
                for j in temp[1:]:
                    if hand_type != h_type or j >= pos_hand_score:
                        pos_hands.append(np.array([hand_type, j], dtype=np.int64))

    return pos_hands


@njit()
def get_hand_type(cards_in_pre_hand):
    n = cards_in_pre_hand.shape[0]
    if n == 0: # R???ng
        return -1
    # n >= 1

    if n == 1: # L?? ????n
        return 1
    # n >= 2

    arr_score = np.unique(cards_in_pre_hand//4)
    if arr_score.shape[0] == 1: # Check ????i tam t???
        return n
    # arr_score.shape[0] >= 2

    if np.max(arr_score) == 12:
        return -1
    # Kh??ng ch???a l?? 2

    if arr_score.shape[0] == n: # C?? th??? l?? b??? d??y
        if n < 3:
            return -1
        # n >= 3

        check = True
        for i in range(arr_score.min()+1, arr_score.max()):
            if i not in arr_score:
                check = False
                break

        if check:
            return n + 2

        return -1
    # Kh??ng l?? b??? d??y

    if arr_score.shape[0] * 2 == n: # C?? th??? l?? b??? d??y ????i th??ng
        if n < 6 or n > 8:
            return -1
        # n >= 6 v?? n <= 8

        check = True
        for i in range(arr_score.min(), arr_score.max()+1):
            if i not in arr_score:
                check = False
                break

            temp = cards_in_pre_hand[cards_in_pre_hand//4 == i]
            if temp.shape[0] < 2:
                check = False
                break

        if check:
            return arr_score.shape[0] + 11

        return -1

    return -1


__ACTION_SIZE__ = 403
@njit()
def getValidActions(state):
    validActions = np.zeros(__ACTION_SIZE__, dtype=np.float64)
    arr_card = np.where(state[0:52] == 1)[0]
    cards_in_pre_hand = np.where(state[113:165] == 1)[0]
    own_cur_hand = state[110:113]
    if (own_cur_hand==0).all():
        hand_type = 0
        hand_score = 0
    else:
        hand_type = get_hand_type(cards_in_pre_hand)
        if cards_in_pre_hand.shape[0] != 0:
            hand_score = np.max(cards_in_pre_hand) + 1
        else:
            hand_score = 0

    if arr_card.shape[0] == 0 or hand_type == -1:
        validActions[0] = 1
    else:
        if hand_type == 0: # B???t ?????u v??ng m???i
            pos_hand_types = np.arange(1, 16, dtype=np.int64) # ???????c ????nh t???t c??? c??c b???, kh??ng ???????c b??? l?????t
            pos_hand_score = 0
        else: # Ph???i ch???n b??? b??i c???a ng?????i tr?????c
            pos_hand_score = hand_score
            if (hand_type>=1 and hand_type<=3) or (hand_type>=5 and hand_type<=13): # ????n, ????i, tam ho???c d??y
                if hand_score <= 48: # C??c b??? ????n ????i tam kh??ng ch???a l?? 2 v?? d??y
                    pos_hand_types = np.array([0, hand_type], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng b??? c??ng ki???u m???nh h??n
                else: # C??c b??? ????n ????i tam c?? ch???a l?? 2
                    if hand_type == 1: # L?? 2 ????n
                        pos_hand_types = np.array([0, 1, 4, 14, 15], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng l?? 2 m???nh h??n, t??? qu??, 3 ????i th??ng, 4 ????i th??ng
                    elif hand_type == 2: # ????i 2
                        pos_hand_types = np.array([0, 2, 4, 15], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng ????i 2 m???nh h??n, t??? qu??, 4 ????i th??ng
                    else: # Tam 2
                        pos_hand_types = np.array([0], dtype=np.int64) # Ch??? c?? th??? b??? l?????t
            elif hand_type == 14: # 3 ????i th??ng
                pos_hand_types = np.array([0, 4, 14, 15], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng t??? qu??, 3 ????i th??ng m???nh h??n, 4 ????i th??ng
            elif hand_type == 4: # T??? qu??
                pos_hand_types = np.array([0, 4, 15], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng t??? qu?? m???nh h??n, 4 ????i th??ng
            else: # 4 ????i th??ng
                pos_hand_types = np.array([0, 15], dtype=np.int64) # B??? l?????t ho???c ch???n b???ng 4 ????i th??ng m???nh h??n

        pos_hands = get_pos_hands(arr_card, hand_type, pos_hand_types, pos_hand_score)
        for hand in pos_hands:
            if hand[0] == 0:
                validActions[0] = 1
            elif hand[0] >= 1 and hand[0] <= 4:
                validActions[13*np.sum(np.arange(4,5-hand[0],-1)) + hand[1] - (hand[0]-1)*(hand[1]//4) - hand[0] + 2] = 1
            elif hand[0] >= 5 and hand[0] <= 13:
                validActions[4*np.sum(np.arange(10,15-hand[0],-1)) + hand[1] - 4*hand[0] + 142] = 1
            else:
                validActions[27*hand[0] + hand[1] - (hand[1]//4) - 39] = 1

    return validActions


@njit()
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData


@njit()
def checkEnded(env):
    for i in range(4):
        if np.count_nonzero(env[0:52] == i) == 0:
            return i

    return -1


@njit()
def get_cards_in_hand(arr_card, hand):
    cards_in_hand = [np.int64(0) for _ in range(0)]
    if hand[0] == 0:
        pass
    elif hand[0] >= 1 and hand[0] <= 4:
        temp = arr_card[arr_card//4 == hand[1]//4]
        for j in temp[0:hand[0]-1]:
            cards_in_hand.append(j)
        else:
            cards_in_hand.append(hand[1])
    elif hand[0] >= 5 and hand[0] <= 13:
        last = hand[1]//4
        hand_length = hand[0] - 2
        for i in range(last-hand_length+1, last):
            temp = arr_card[arr_card//4 == i]
            cards_in_hand.append(temp[0])
        else:
            cards_in_hand.append(hand[1])
    else:
        last = hand[1]//4
        hand_length = hand[0] - 11
        for i in range(last-hand_length+1, last):
            temp = arr_card[arr_card//4 == i]
            for j in temp[0:2]:
                cards_in_hand.append(j)
        else:
            temp = arr_card[arr_card//4 == last]
            cards_in_hand.append(temp[0])
            cards_in_hand.append(hand[1])

    return np.array(cards_in_hand, dtype=np.int64)


@njit()
def stepEnv(action, env):
    hand = __ACTIONS__[action]
    arr_card = np.where(env[0:52] == env[52])[0]
    cards_in_hand = get_cards_in_hand(arr_card, hand)
    env[cards_in_hand] = -1

    if hand[0] == 0:
        env[53+env[52]] = 0
    else:
        env[57] = env[52]
        env[58:60] = hand

        if hand[1] >= 48 or hand[0] == 4 or hand[0] == 14 or hand[0] == 15 or np.sum(env[53:57]) == 1:
            env[53:57] = 1

    for i in range(1,4):
        next_idx = (env[52]+i) % 4
        if env[53+next_idx] == 1:
            env[52] = next_idx
            break

    return cards_in_hand


@njit()
def check_player_hand(env):
    for i in range(4):
        arr_card = np.where(env[0:52] == i)[0]

        temp = arr_card[arr_card//4 == 12]
        if temp.shape[0] == 4:
            return False

        temp = np.unique(arr_card//4)
        arr_score = temp[temp < 12]
        if arr_score.shape[0] == 12:
            return False

        arr_score = [np.int64(0) for _ in range(0)]
        for i in range(12):
            temp = arr_card[arr_card//4 == i]
            if temp.shape[0] >= 2:
                arr_score.append(i)

        list_subsequence = continuous_subsequence(np.array(arr_score, dtype=np.int64), 5)
        if len(list_subsequence) > 0:
            return False

    return True


@njit()
def getAgentSize():
    return 4


@njit()
def getStateSize():
    return __STATE_SIZE__


@njit()
def getActionSize():
    return __ACTION_SIZE__


@njit()
def getReward(state):
    a = np.count_nonzero(state[0:52]==1)
    b = np.min(state[107:110])
    if a*b == 0:
        if a == 0:
            return 1
        else:
            return 0
    else:
        return -1


@njit()
def one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env = initEnv()
    while not check_player_hand(env):
        env = initEnv()

    cards_in_hand = np.full(0, 0, dtype=np.int64)
    while True:
        p_idx = env[52]
        state = getAgentState(env, cards_in_hand)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
            validActions = getValidActions(state)
            if validActions[action] != 1:
                raise Exception('Action kh??ng h???p l???')
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(state, per3)
        else:
            raise Exception('Sai list_other.')

        if action != 0:
            cards_in_hand = stepEnv(action, env)
        else:
            stepEnv(action, env)

        winner = checkEnded(env)
        if winner != -1:
            break

    p0_idx = np.where(list_other==-1)[0][0]
    cards_in_hand = np.full(0, 0, dtype=np.int64)
    for p_idx in range(4):
        env[52] = p_idx
        env[57] = p_idx
        state = getAgentState(env, cards_in_hand)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(state, per3)
        else:
            raise Exception('Sai list_other.')

    if p0_idx == winner: result = 1
    else: result = 0
    return result, per_player


@njit()
def n_games_numba(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3):
    win = 0
    for _ in range(num_game):
        np.random.shuffle(list_other)
        winner, per_player = one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3)
        win += winner

    return win, per_player


def one_game_normal(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env = initEnv()
    while not check_player_hand(env):
        env = initEnv()

    cards_in_hand = np.full(0, 0, dtype=np.int64)
    while True:
        p_idx = env[52]
        state = getAgentState(env, cards_in_hand)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
            validActions = getValidActions(state)
            if validActions[action] != 1:
                raise Exception('Action kh??ng h???p l???')
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(state, per3)
        else:
            raise Exception('Sai list_other.')

        if action != 0:
            cards_in_hand = stepEnv(action, env)
        else:
            stepEnv(action, env)

        winner = checkEnded(env)
        if winner != -1:
            break

    p0_idx = np.where(list_other==-1)[0][0]
    cards_in_hand = np.full(0, 0, dtype=np.int64)
    for p_idx in range(4):
        env[52] = p_idx
        env[57] = p_idx
        state = getAgentState(env, cards_in_hand)
        if list_other[p_idx] == -1:
            action, per_player = p0(state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(state, per3)
        else:
            raise Exception('Sai list_other.')

    if p0_idx == winner: result = 1
    else: result = 0
    return result, per_player


def n_games_normal(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3):
    win = 0
    for _ in range(num_game):
        np.random.shuffle(list_other)
        winner, per_player = one_game_normal(p0, list_other, per_player, per1, per2, per3, p1, p2, p3)
        win += winner

    return win, per_player


import importlib.util, json, sys
try:
    from setup import SHORT_PATH
except:
    pass


def load_module_player(player):
    spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/{player}/Agent_player.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@njit()
def check_run_under_njit(agent, perData):
    return True


def numba_main_2(p0, num_game, per_player, level, *args):
    num_bot = getAgentSize() - 1
    list_other = np.array([-1] + [i+1 for i in range(num_bot)])
    try: check_njit = check_run_under_njit(p0, per_player)
    except: check_njit = False

    if "_level_" not in globals():
        global _level_
        _level_ = level
        init = True
    else:
        if _level_ != level:
            _level_ = level
            init = True
        else:
            init = False

    if init:
        global _list_per_level_
        global _list_bot_level_
        _list_per_level_ = []
        _list_bot_level_ = []

        if _level_ == 0:
            _list_per_level_ = [np.array([[0.]], dtype=np.float64) for _ in range(num_bot)]
            _list_bot_level_ = [bot_lv0 for _ in range(num_bot)]
        else:
            env_name = sys.argv[1]
            if len(args) > 0:
                dict_level = json.load(open(f'{SHORT_PATH}Log/check_system_about_level.json'))
            else:
                dict_level = json.load(open(f'{SHORT_PATH}Log/level_game.json'))

            if str(_level_) not in dict_level[env_name]:
                raise Exception('Hi???n t???i kh??ng c?? level n??y')

            lst_agent_level = dict_level[env_name][str(level)][2]
            lst_module_level = [load_module_player(lst_agent_level[i]) for i in range(num_bot)]
            for i in range(num_bot):
                data_agent_level = np.load(f'{SHORT_PATH}Agent/{lst_agent_level[i]}/Data/{env_name}_{level}/Train.npy',allow_pickle=True)
                _list_per_level_.append(lst_module_level[i].convert_to_test(data_agent_level))
                _list_bot_level_.append(lst_module_level[i].Test)

    if check_njit:
        return n_games_numba(p0, num_game, per_player, list_other,
                                _list_per_level_[0], _list_per_level_[1], _list_per_level_[2],
                                _list_bot_level_[0], _list_bot_level_[1], _list_bot_level_[2])
    else:
        return n_games_normal(p0, num_game, per_player, list_other,
                                _list_per_level_[0], _list_per_level_[1], _list_per_level_[2],
                                _list_bot_level_[0], _list_bot_level_[1], _list_bot_level_[2])
