from numba import njit, jit
import numpy as np
#Building Card
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning,NumbaExperimentalFeatureWarning, NumbaWarning
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaExperimentalFeatureWarning)
warnings.simplefilter('ignore', category=NumbaWarning)
BUILDING_CARDS = np.array([[10,  2,  1,  0,  0,  0,  0,  0],
                            [11,  1,  2,  0,  0,  0,  0,  0],
                            [11,  2,  0,  1,  0,  0,  0,  0],
                            [12,  1,  1,  1,  0,  0,  0,  0],
                            [12,  1,  1,  1,  0,  0,  0,  0],
                            [12,  2,  0,  0,  1,  0,  0,  0],
                            [13,  1,  1,  0,  1,  0,  0,  0],
                            [13,  1,  1,  0,  1,  0,  0,  0],
                            [13,  1,  0,  2,  0,  0,  0,  0],
                            [13,  0,  2,  1,  0,  0,  0,  0],
                            [14,  1,  0,  1,  1,  0,  0,  0],
                            [14,  1,  0,  1,  1,  0,  0,  0],
                            [14,  0,  2,  0,  1,  0,  0,  0],
                            [14,  0,  1,  2,  0,  0,  0,  0],
                            [15,  0,  1,  1,  1,  0,  0,  0],
                            [15,  0,  1,  1,  1,  0,  0,  0],
                            [16,  0,  0,  2,  1,  0,  0,  0],
                            [ 0,  0,  0,  0,  0,  7,  0,  0],
                            [ 0,  0,  0,  0,  0,  7,  0,  0],
                            [ 0,  0,  0,  0,  0,  7,  0,  0],
                            [ 0,  0,  0,  0,  0,  0,  4,  1],
                            [ 0,  0,  0,  0,  0,  0,  4,  2],
                            [ 0,  0,  0,  0,  0,  0,  4,  3],
                            [ 0,  0,  0,  0,  0,  0,  4,  4],
                            [ 0,  0,  0,  0,  0,  0,  5,  1],
                            [ 0,  0,  0,  0,  0,  0,  5,  2],
                            [ 0,  0,  0,  0,  0,  0,  5,  3],
                            [ 0,  0,  0,  0,  0,  0,  5,  4]])

CIV_CARDS = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],     #X??c, ????
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],     #X??c, Xe
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],     #X??c, lu
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],     #X??c ?????ng h???
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #1Th???c, D???t
                    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #3Th???c, D???t
                    [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #5Th???c, C??y
                    [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],     #7Th???c, Lu
                    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #??i???m, s??o
                    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #??i???m, s??o
                    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],     #2B???c, xe
                    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #Roll, V??ng, ng?????i
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #C???, ng?????i
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],     #L??a, ?????ng h???
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #2NL, c??y
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],     #N??ng c???p, ????

                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],     #X??c, 1, l??a
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],     #X??c, 1, nh??
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0],     #X??c, 2, c??? 
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0],     #X??c, 2, c???
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],     #X??c, 2, l??a
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0],     #X??c, 2, nh??
                    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0],     #2Th???c, 2, nh??
                    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],     #3Th???c, 2, l??a
                    [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],     #4Th???c, 1, nh??
                    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0],     #??i???m, 3, nh??
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0],     #g???ch, 2, ng?????i
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],     #b???c, 1, l??a
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],     #b???c, 1, ng?????i
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],     #v??ng, 1, ng?????i
                    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0],     #2C???, 2, c???
                    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],     #3C???, 1, c???
                    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],     #4C???, 1, c???
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0],     #Roll, g???, 2, ng?????i
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],     #Roll, b???c, 1, ng?????i
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],])     #L??c, 1, lua


BUILD_4_2 = np.array([
    [0, 0, 1, 3],
    [0, 1, 0, 3],
    [2, 0, 0, 2],
    [0, 1, 3, 0],
    [2, 2, 0, 0],
    [0, 3, 1, 0],
    [3, 0, 1, 0],
    [0, 0, 3, 1],
    [0, 3, 0, 1],
    [3, 0, 0, 1],
    [3, 1, 0, 0],
    [0, 2, 2, 0],
    [1, 0, 3, 0],
    [1, 0, 0, 3],
    [1, 3, 0, 0],
    [0, 2, 0, 2],
    [0, 0, 2, 2],
    [2, 0, 2, 0]])

BUILD_4_3 = np.array([
    [0, 1, 1, 2],
    [1, 2, 0, 1],
    [0, 2, 1, 1],
    [0, 1, 2, 1],
    [2, 1, 0, 1],
    [1, 1, 2, 0],
    [1, 2, 1, 0],
    [2, 1, 1, 0],
    [1, 0, 2, 1],
    [2, 0, 1, 1],
    [1, 0, 1, 2],
    [1, 1, 0, 2]])

BUILD_4_4 =  np.array([[1, 1, 1, 1]])

BUILD_5_2 = np.array([
    [0, 3, 2, 0],
    [4, 0, 0, 1],
    [0, 0, 2, 3],
    [0, 0, 1, 4],
    [3, 0, 0, 2],
    [4, 1, 0, 0],
    [2, 0, 3, 0],
    [3, 2, 0, 0],
    [0, 2, 3, 0],
    [1, 0, 4, 0],
    [1, 4, 0, 0],
    [4, 0, 1, 0],
    [0, 0, 3, 2],
    [0, 0, 4, 1],
    [0, 4, 0, 1],
    [2, 3, 0, 0],
    [0, 1, 4, 0],
    [2, 0, 0, 3],
    [0, 2, 0, 3],
    [0, 3, 0, 2],
    [0, 4, 1, 0],
    [3, 0, 2, 0],
    [1, 0, 0, 4],
    [0, 1, 0, 4]])

BUILD_5_3 = np.array([
    [1, 2, 2, 0],
    [3, 1, 1, 0],
    [1, 3, 0, 1],
    [0, 2, 2, 1],
    [1, 1, 0, 3],
    [0, 1, 2, 2],
    [0, 1, 3, 1],
    [1, 0, 3, 1],
    [1, 3, 1, 0],
    [2, 2, 0, 1],
    [1, 2, 0, 2],
    [3, 0, 1, 1],
    [2, 1, 0, 2],
    [0, 1, 1, 3],
    [2, 2, 1, 0],
    [0, 3, 1, 1],
    [3, 1, 0, 1],
    [2, 0, 1, 2],
    [1, 1, 3, 0],
    [1, 0, 1, 3],
    [0, 2, 1, 2],
    [2, 0, 2, 1],
    [2, 1, 2, 0],
    [1, 0, 2, 2]])

BUILD_5_4 =  np.array([[1, 1, 2, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 1, 2]])


P_ID_PLAYER = 142
ID_START_PEOPLE = 318
ID_END_PEOPLE = 322
P_START_CIV = 322
P_END_CIV = 326
P_START_BUILD = 326
P_END_BUILD = 330
P_START_PUSH_RECENT = 354
P_END_PUSH_RECENT = 370
P_START_PULL_RECENT = 370
P_END_PULL_RECENT = 386
P_ALL_TOOL = 386
P_START_DICE_FOR_CIV = 387
P_END_DICE_FOR_CIV = 411
P_TOTAL_DICE = 411
P_PHASE = 412

E_ID_PLAYER = 211
TOTAL_INDEX_PLAYER = 44
TOTAL_CARD_STATE = 8
E_START_CIV = 387
E_END_CIV = 391
E_START_BUILD = 391
E_END_BUILD = 395
E_PUSH_RECENT = 395
E_PULL_RECENT = 396
E_ALL_TOOL = 397
E_START_DICE_FOR_CIV = 398
E_END_DICE_FOR_CIV = 402
E_TOTAL_DICE = 402
E_PHASE = 403


STATE_ENV_SIZE = E_PHASE + 11
STATE_PLAYER_SIZE = P_PHASE + 11
ALL_ACTION_SIZE = 68
@njit()
def initEnv(BUILDING_CARDS, CIV_CARDS):
    all_build_card = np.zeros((4, 7))
    all_build_card[:, 0] = 1
    all_build_card = all_build_card.flatten()

    all_civ_card = np.zeros(36)
    all_civ_card[:4] = 1

    env = np.zeros(STATE_ENV_SIZE)
    env[0] = 1 #Ng?????i ch??i ?????u ti??n
    build_card = np.arange(28)
    np.random.shuffle(build_card)
    civ_card = np.arange(36)
    np.random.shuffle(civ_card)

    env[5:41] = civ_card
    env[41:69] = build_card
    env[69:73] = [100, 100, 100, 100]
    env[73:77] = 7
    env[83:179] = CIV_CARDS[civ_card[np.where(all_civ_card == 1)[0]]].flatten()
    env[179:211] = BUILDING_CARDS[build_card[np.where(all_build_card == 1)[0]]].flatten()

    for i in range(4):
        p_id_env = 211+TOTAL_INDEX_PLAYER*i
        env[p_id_env + 3] = 12
        env[p_id_env + 2] = 5
        env[p_id_env] = 400
    env[E_START_CIV:E_END_BUILD] = -1
    env[E_PHASE] = 1
    return env, all_build_card.reshape((4,7)), all_civ_card

@njit()
def getAgentState(env):
    p_state = np.zeros(STATE_PLAYER_SIZE)
    p_state[:P_ID_PLAYER] = env[69:E_ID_PLAYER] #C??c th??ng tin ??? tr??n b??n

    p_state[ID_START_PEOPLE:ID_END_PEOPLE] = env[0:4] #?????n ng?????i n??o ??ang ch??i
    p_idx = np.where(env[0:4] == 1)[0][0]

    infor_card_env = env[E_START_CIV:E_END_BUILD] #Ng?????i ??ang ch??i l?? 0, ng?????i kh??c l???n l?????t l?? 1, 2, 3
    
    s_ = E_ID_PLAYER + TOTAL_INDEX_PLAYER*p_idx
    p_state[P_ID_PLAYER:P_ID_PLAYER+TOTAL_INDEX_PLAYER] = env[s_:s_+TOTAL_INDEX_PLAYER] #Th??ng tin c???a ng?????i ??ang ch??i
    p_state[P_START_CIV + np.where(infor_card_env == p_idx)[0]] = 1 #Th??ng tin th??? c???a ng?????i ??ang ch??i ???? ?????t, ho???c ???? l???y
    # print('Trong ng?????i ch??i', np.where(infor_card_env == p_idx)[0], p_state[P_START_CIV:P_END_BUILD])

    for i in range(1, 4):
        p_other_idx = (p_idx + i)%4
        s_o = E_ID_PLAYER + TOTAL_INDEX_PLAYER*p_other_idx
        p_state[P_ID_PLAYER + TOTAL_INDEX_PLAYER*i: P_ID_PLAYER + TOTAL_INDEX_PLAYER*(i+1)] = env[s_o:s_o+TOTAL_INDEX_PLAYER]

        p_state[P_START_CIV + TOTAL_CARD_STATE*i + np.where(infor_card_env == p_other_idx)[0]] =  1
    
    p_state[P_START_PUSH_RECENT + int(env[E_PUSH_RECENT])] = 1
    p_state[P_START_PULL_RECENT + int(env[E_PULL_RECENT])] = 1
    p_state[P_ALL_TOOL] = env[E_ALL_TOOL]
    for i in range(4):
        if env[E_START_DICE_FOR_CIV + i] > 0:
            p_state[P_START_DICE_FOR_CIV + i*6 + int(env[E_START_DICE_FOR_CIV + i]) - 1] = 1

    p_state[P_TOTAL_DICE] = env[E_TOTAL_DICE]
    p_state[P_PHASE:] = env[E_PHASE:]

    return p_state.astype(np.float64)
    
@njit()
def RollDice(count_dice):
    total_of_dice = 0
    for i in range(count_dice):
        total_of_dice += np.random.randint(1, 7)
    return total_of_dice

@njit()
def RollDiceUseTool(env, e_idp):
    id_warehouse = int(env[E_PULL_RECENT])
    # env[e_idp + 9:e_idp + 12] = np.abs(env[e_idp + 9:e_idp + 12]) #Tr??? l???i c??ng c??? nh?? b??nh th?????ng
    env[e_idp + 31 + id_warehouse] = 0
    env[e_idp + 15 + np.where(env[e_idp + 9:e_idp + 12] > 0)[0]] = 1
    if id_warehouse != 7:
        count_source_take = (env[E_TOTAL_DICE] + env[E_ALL_TOOL])//id_warehouse
        env[e_idp+5+id_warehouse - 3] += count_source_take
        env[69+id_warehouse - 3] -= count_source_take
    else:
        count_source_take = (env[E_TOTAL_DICE] + env[E_ALL_TOOL])//2
        env[e_idp+3] += count_source_take
   ##print('T???ng s??? c??ng c???', env[E_ALL_TOOL], 'x??c x???c', env[E_TOTAL_DICE], 'T???ng', env[E_TOTAL_DICE] + env[E_ALL_TOOL])
   ##print('Nguy??n li???u l???y', id_warehouse - 3, '---L???y---:', count_source_take)
    env[E_TOTAL_DICE] = 0
    env[E_ALL_TOOL] = 0
    
    env[E_PHASE:] = 0  #?????i phase
    env[E_PHASE + 2] = 1
    return env

@njit()
def RollDiceGetRes(count_dice, env, id_warehouse, e_idp):
    total_of_dice = 0
    for i in range(count_dice):
        total_of_dice += np.random.randint(1, 7)
    if id_warehouse != 7: #G???, g???ch, b???c, v??ng
        count_source_take = (total_of_dice)//id_warehouse
        env[e_idp+5+id_warehouse - 3] += count_source_take
        env[69+id_warehouse - 3] -= count_source_take
    else:
        count_source_take = (total_of_dice)//2
        env[e_idp+3] += count_source_take
   ##print('Kh??ng c?? c??ng c???, T???ng s??? dice', total_of_dice, 'Nguy??n li???u l???y', id_warehouse - 3, '---L???y---:', count_source_take)
    return env

@njit()
def GetScoreEndGame(env):
    for id_score in range(4):
        e_o_idp = int(E_ID_PLAYER + TOTAL_INDEX_PLAYER*id_score)
        score_civ_yellow = env[e_o_idp + 42]*env[e_o_idp + 1] + env[e_o_idp + 39]*env[e_o_idp + 4] + env[e_o_idp + 40]*np.sum(env[e_o_idp + 9:e_o_idp + 12]) + env[e_o_idp + 41]*env[e_o_idp + 2]
        civ_player = env[e_o_idp + 22:e_o_idp + 30]
        count_civ_player = civ_player[civ_player > 0]
        score_civ_green =  len(count_civ_player)*len(count_civ_player)
        env[e_o_idp] += (score_civ_yellow + score_civ_green)
        env[e_o_idp] += np.sum(env[e_o_idp + 5:e_o_idp + 9])
    return env

@njit()
def getAgentSize():
    return 4

@njit()
def getActionSize():
    return 68

@njit()
def getStateSize():
    return STATE_PLAYER_SIZE

@njit()
def checkEnded(env):
    if env[82] == 0:
        return np.array([-1])
    else:
        arr_score = env[np.array([211, 255, 299, 343])]
        return np.where(arr_score == np.max(arr_score))[0]


@njit()
def getValidActions(p_state):
    p_state = p_state.astype(np.int64)
    list_action = np.zeros(ALL_ACTION_SIZE)
    lst_phase = np.where(p_state[P_PHASE:] == 1)[0]
    if len(lst_phase) == 0:
        return list_action.astype(np.float64)
    if p_state[13] == 1:
        list_action[0] = 1
        return list_action.astype(np.float64)
    phase = lst_phase[0]
    s_ = P_ID_PLAYER

    p_push_recent = np.where(p_state[P_START_PUSH_RECENT : P_END_PUSH_RECENT] == 1)[0]
    p_pull_recent = np.where(p_state[P_START_PULL_RECENT : P_END_PULL_RECENT] == 1)[0]

    card_state = np.zeros(TOTAL_CARD_STATE)
    for i in range(4):
        card_state += p_state[P_START_CIV + TOTAL_CARD_STATE*i:P_START_CIV + TOTAL_CARD_STATE*(i+1)]
        # print(p_state[P_START_CIV + TOTAL_CARD_STATE*i:P_START_CIV + TOTAL_CARD_STATE*(i+1)])
        
    if phase == 0: #Ch???n ?? ?????t ng?????i
        so_nguoi_co_the_dat = p_state[s_ + 2] - np.sum(p_state[s_ + 31:s_ + 39]) - len(np.where(p_state[P_START_CIV:P_END_BUILD] == 1)[0])
        # print(card_state, p_state[s_ + 31:s_ + 39])
        civ_can_get = np.where(card_state[:4] == 0)[0]
        build_can_get = np.where(card_state[4:] == 0)[0]

        if so_nguoi_co_the_dat > 0:
            list_action[19+civ_can_get] = 1
            list_action[23+build_can_get] = 1

        people_in_warehouse = np.zeros(8)
        for i in range(4):
            people_in_warehouse +=  p_state[173 + TOTAL_INDEX_PLAYER*i:181 + TOTAL_INDEX_PLAYER*i] #S??? ng?????i ??? m???i ??

        list_action[11:13] = (people_in_warehouse[0:2] == 0) #L??a, c???

        if so_nguoi_co_the_dat >= 2 and p_state[142 + 2] < 10:
            list_action[13] = (people_in_warehouse[2] == 0) #Sinh s???n

        for id_res, res in  enumerate(p_state[s_ + 34:s_ + 38]):
            if res == 0:
                list_action[14 + id_res] = (people_in_warehouse[3 + id_res] < 7) #G???, b???c, g???ch, v??ng
        list_action[18] = 1 #L????ng th???c


    if phase == 1: #?????t s??? ng?????i
        so_nguoi_da_dat = np.sum(p_state[s_ + 31:s_ + 39]) + len(np.where(p_state[P_START_CIV:P_END_BUILD] == 1)[0])
        if len(p_push_recent) > 0:
            if p_push_recent[0] != 7: #G??? g???ch b???c v??ng
                people_in_warehouse = np.zeros(8)
                for i in range(4):
                    people_in_warehouse +=  p_state[s_ + 31 + TOTAL_INDEX_PLAYER*i:s_ + 39 + TOTAL_INDEX_PLAYER*i]
                count_people_can_push = np.minimum(7 - people_in_warehouse, (p_state[s_ + 2]) - so_nguoi_da_dat)[int(p_push_recent[0])]
                ##print('S??? ng?????i t???i ??a c?? th??? ?????t', count_people_can_push, np.sum(p_state[173:181]), 't???ng s??? ng?????i', p_state[s_ + 2], '?? v???a ?????t', p_state[P_PUSH_RECENT])
                list_action[1:int(count_people_can_push+1)] = 1 
            else: #L????ng th???c
                so_nguoi_co_the_dat = p_state[s_ + 2] - so_nguoi_da_dat
                list_action[1:int(so_nguoi_co_the_dat + 1)] = 1 
        

    if phase == 2: #L???y ng?????i t??? c??c ??
        ##print(p_state[s_ + 31:s_ + 39], p_state[P_START_CIV:P_END_BUILD])
        list_action[29 + np.where(p_state[s_ + 31:s_ + 39] > 0)[0]] = 1 #C??c ?? nguy??n li???u
        list_action[48 + np.where(p_state[P_START_CIV:P_END_CIV] == 1)[0]] = 1 #Ng?????i ??ang c?? ??? ?? civ
        list_action[52 + np.where(p_state[P_START_BUILD:P_END_BUILD] == 1)[0]] = 1  #Ng?????i ??ang c?? ??? ?? build
        if p_state[s_ + 30] != 0:
            list_action[63] = 1

    if phase == 3: #Tr??? nguy??n li???u mua th??? civ
        list_action[40:44] = (p_state[s_ + 5:s_ + 9] > 0)

    if phase == 4: #D??ng c??ng c???(end ho???c h???t th?? qua roll x??c x???c)
        list_action[37:40] = (p_state[s_ + 15:s_ + 18] > 0)
        list_action[44:47] = (p_state[s_ + 12:s_ + 15] > 0)
        list_action[0] = 1

    if phase == 5: #tr??? nguy??n li???u khi mua th??? build 1 -> 7
        list_action[40:44] = (p_state[s_ + 5:s_ + 9] > 0)

    if phase == 6: #Ch???n tr??? nguy??n li???u ho???c tr??? ??i???m khi kh??ng ????? th???c ??n
        list_action[27] = 1
        list_action[28] = 1
        
    if phase == 7: #Ch???n gi?? tr??? x??c x???c khi d??ng th??? civ x??c x???c
        # dice_after = p_state[P_START_DICE_FOR_CIV:P_END_DICE_FOR_CIV].astype(np.int64)
        for i in range(4):
            dice_after = np.where(p_state[P_START_DICE_FOR_CIV + i*6: P_START_DICE_FOR_CIV + (i+1)*6] == 1)[0]
            if len(dice_after) > 0:
                # print(p_state[P_START_DICE_FOR_CIV + i*6: P_START_DICE_FOR_CIV + (i+1)*6], int(dice_after[0]))
                list_action[56 + int(dice_after[0]) + 1] = 1
    
    if phase == 8: #L???y nguy??n li???u t??? ng??n h??ng khi d??ng th??? civ l???y 2 nguy??n li???u b???t k???
        list_action[64:68] = (p_state[4:8] > 0)
    
    if phase == 9: #tr??? nguy??n li???u khi mua th??? civ c?? s??? l?????ng m???c ?????nh
        if len(p_pull_recent) > 0:
            id_build_card = int(p_pull_recent[0] - 12)
            all_infor_build_card = p_state[110:142].reshape((4, 8))
            build_card_take = all_infor_build_card[id_build_card]
            p_stock = p_state[s_ + 5:s_ + 9]
            ##print('Th??ng tin th??? build', build_card_take, 'res ???? l???y', p_state[8:12], p_stock)

            card_civ_need = np.zeros(4)

            if build_card_take[6] == 4 and build_card_take[7] == 2:
                for case_card in BUILD_4_2:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])

            elif build_card_take[6] == 4 and build_card_take[7] == 3:
                for case_card in BUILD_4_3:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])

            elif build_card_take[6] == 4 and build_card_take[7] == 4:
                for case_card in BUILD_4_4:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])

            elif build_card_take[6] == 5 and build_card_take[7] == 2:
                for case_card in BUILD_5_2:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])

            elif build_card_take[6] == 5 and build_card_take[7] == 3:
                for case_card in BUILD_5_3:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])

            elif build_card_take[6] == 5 and build_card_take[7] == 4:
                for case_card in BUILD_5_4:
                    if ((p_stock + p_state[8:12]) >= case_card).all() and (case_card >= p_state[8:12]).all():
                        card_civ_need += (case_card-p_state[8:12])
                        
            list_action[40:44] = (card_civ_need > 0)


    if phase == 10: #tr??? nguy??n li???u n???u kh??ng ????? th???c ??n
        list_action[40:44] = (p_state[s_ + 5:s_ + 9] > 0)
    
    return list_action.astype(np.float64)

@njit()
def stepEnv(action, env, all_build_card, all_civ_card):
    action = int(action)
    phase = np.where(env[E_PHASE:] == 1)[0][0]
    idp = np.where(env[0:4] == 1)[0][0]
    e_idp = int(E_ID_PLAYER + TOTAL_INDEX_PLAYER*idp)

    check_end_pull_people = True
    if phase == 0: #?????t ng?????i
        # print('action ??? step', action)
        id_warehouse = action - 11
        if action in np.arange(14, 19):
            ##print('V??o action c???n ph???i ?????t s??? ng?????i')
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 1] = 1

            env[E_PUSH_RECENT] = id_warehouse 

        else:
            if action == 13:
                env[e_idp + 31 + id_warehouse] += 2
            if action in [11, 12]:
                env[e_idp + 31 + id_warehouse] += 1
            if action in np.arange(19, 27):
                # print('?????t ng?????i l???i')
                env[E_START_CIV + action - 19] = idp

            env[0:4] = 0 #?????i ng?????i ch??i
            check_people = True
            for i in range(1, 5):
                o_idp = (idp+i)%4
                e_o_idp = int(211 + TOTAL_INDEX_PLAYER*o_idp)
                so_nguoi_da_dat = np.sum(env[e_o_idp + 31:e_o_idp + 39]) + len(np.where(env[E_START_CIV:E_END_BUILD] == o_idp)[0])
                # print('Ng?????i ch??i', o_idp, '???? ?????t', 'S??? ng?????i ???? ?????t', so_nguoi_da_dat, env[e_o_idp + 31:e_o_idp + 39], env[E_START_CIV:E_END_BUILD])
                if so_nguoi_da_dat < env[e_o_idp + 2]:
                    env[o_idp] = 1
                    ##print('?????i sang ng?????i ch??i', np.where(env[0:4] == 1)[0])
                    check_people = False
                    break
            if check_people == True:
                env[E_PHASE:] = 0  #?????i phase
                env[E_PHASE + 2] = 1
                env[int(env[4])%4] = 1

    elif phase == 1: #?????t s??? ng?????i
        id_warehouse = int(env[E_PUSH_RECENT])
        env[e_idp + 31 + id_warehouse] += action
        ##print('?????t', action, 'ng?????i')
        env[0:4] = 0 #?????i ng?????i ch??i
        check_people = True
        for i in range(1, 5):
            o_idp = (idp+i)%4
            e_o_idp = int(211 + TOTAL_INDEX_PLAYER*o_idp)
            so_nguoi_da_dat = np.sum(env[e_o_idp + 31:e_o_idp + 39]) + len(np.where(env[E_START_CIV:E_END_BUILD] == o_idp)[0])
            ##print('Ng?????i ch??i', o_idp, '???? ?????t', 'S??? ng?????i ???? ?????t', so_nguoi_da_dat, env[e_o_idp + 31:e_o_idp + 39], env[E_START_CIV:E_END_BUILD])
            if so_nguoi_da_dat < env[e_o_idp + 2]:
                env[o_idp] = 1
                ##print('?????i sang ng?????i ch??i', np.where(env[0:4] == 1)[0][0])
                check_people = False
                break
        env[E_PHASE:] = 0  #?????i phase
        if check_people == True:
            env[E_PHASE + 2] = 1
            env[int(env[4])%4] = 1
        else:
            env[E_PHASE] = 1

    elif phase == 2: #L???y ng?????i t??? c??c ??

        if action in np.arange(29, 37):
            id_warehouse = action - 29

        elif action in np.arange(48, 56):
            id_warehouse = action - 48 + 8

        elif action == 63:
            id_warehouse = -1 #action l???y 2 nguy??n li???u t??? th??? civ v?? sang phase tr??? nguy??n li???u
        
        

        if id_warehouse in [0, 1, 2]:
            env[e_idp + 31 + id_warehouse] = 0 

        if id_warehouse in [8, 9, 10, 11, 12, 13, 14, 15]:
            env[E_START_CIV + id_warehouse-8] = -1
        
        if id_warehouse == -1: #Chuy???n sang l???y 2 nguy??n li???u b???t k??? tr??n b??n
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 8] = 1
    
        if id_warehouse == 0: #Th??m l??a
            env[e_idp+1] += 1

        elif id_warehouse == 1: #Th??m c??ng c??? v??o ?? c?? s??? l?????ng c??ng c??? b?? nh???t
            id_min = np.argmin(env[e_idp+9:e_idp+12]) 
            env[e_idp + 9 + id_min] += 1
            env[e_idp + 15 + np.where(env[e_idp + 9:e_idp + 12] > 0)[0]] = 1
        elif id_warehouse == 2: #Th??m s??? ng?????i
            env[e_idp+2] += 1
        

        elif id_warehouse in [3, 4, 5, 6, 7]: #L???y t??i nguy??n
            env[E_PULL_RECENT] = id_warehouse
            if np.sum(env[e_idp+12:e_idp+15]) > 0 or (env[e_idp+15:e_idp+18] > 0).any(): #N???u c??n th??? c??ng c??? ????? d??ng
                count_dice = int(env[e_idp+31+id_warehouse])
                env[E_TOTAL_DICE] = RollDice(count_dice)
                env[E_PHASE:] = 0  #?????i phase
                env[E_PHASE + 4] = 1
            else: #Kh??ng c?? c??ng c??? th?? roll lu??n
                count_dice = int(env[e_idp+31+id_warehouse])
                env[e_idp + 31 + id_warehouse] = 0 
                env = RollDiceGetRes(count_dice, env, id_warehouse, e_idp)

        elif id_warehouse in [8,9,10,11]: #L???y th??? civ
            env[E_PULL_RECENT] = id_warehouse
            if np.sum(env[e_idp+5:e_idp+9]) >= (id_warehouse - 7):
                env[E_PHASE:] = 0  #?????i phase
                env[E_PHASE + 3] = 1

                check_end_pull_people = False
            
        elif id_warehouse in [12, 13, 14, 15]: #L???y th??? build

            env[E_PULL_RECENT] = id_warehouse
            
            id_build_card = id_warehouse - 12
            all_infor_build_card = env[179:211].reshape((4, 8))
            build_card_take = all_infor_build_card[id_build_card]
            ##print('Th??ng tin th??? build', build_card_take)

            if build_card_take[0] > 0: #????y l?? card l???y ??i???m, tr??? nguy??n li???u v?? c???ng ??i???m lu??n
                if (env[e_idp+5:e_idp+9] >= build_card_take[1:5]).all(): #N???u th???a nguy??n li???u
                    env[e_idp+5:e_idp+9] -= build_card_take[1:5] #Tr??? nguy??n li???u c???a b???n th??n
                    env[69:73] += build_card_take[1:5] #C???ng nguy??n li???u cho ng??n h??ng
                    env[e_idp] +=  build_card_take[0] #C???ng ??i???m
                    env[e_idp + 4] += 1 #C???ng th??m s??? nh??
                    
                    env[E_START_CIV + int(env[E_PULL_RECENT])-8] = -2 #????nh d???u l?? ???? l???y


            else: #????y l?? card ?????i nguy??n li???u l???y th??? build

                if build_card_take[5] == 7: #N???u l?? th??? tr??? 1-> nguy??n li???u 
                    if np.sum(env[e_idp+5:e_idp+9]) > 0:
                        env[E_PHASE:] = 0  #?????i phase
                        env[E_PHASE + 5] = 1

                        check_end_pull_people = False
                
                if build_card_take[6] > 0: #N???u l?? th??? tr??? s??? l?????ng nguy??n li???u c??? ?????nh
                    if np.sum(env[e_idp+5:e_idp+9]) >= build_card_take[6]: #T???ng s??? l?????ng nguy??n li???u ph???i l???n h??n th??? c???n
                        check_phase = False
                        if build_card_take[6] == 4 and build_card_take[7] == 2:
                            for case_card in BUILD_4_2:
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        elif build_card_take[6] == 4 and build_card_take[7] == 3:
                            for case_card in BUILD_4_3:
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        elif build_card_take[6] == 4 and build_card_take[7] == 4:
                            for case_card in BUILD_4_4:                                                             
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        elif build_card_take[6] == 5 and build_card_take[7] == 2:
                            for case_card in BUILD_5_2:
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        elif build_card_take[6] == 5 and build_card_take[7] == 3:
                            for case_card in BUILD_5_3:
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        elif build_card_take[6] == 5 and build_card_take[7] == 4:
                            for case_card in BUILD_5_4:
                                if (env[e_idp + 5:e_idp + 9] >= case_card).all():
                                    check_phase = True
                                    break

                        if check_phase == True:
                            env[E_PHASE:] = 0  #?????i phase
                            env[E_PHASE + 9] = 1

                            check_end_pull_people = False


    elif phase == 3: #Tr??? nguy??n li???u mua th??? civ
        count_res_give = int(env[E_PULL_RECENT] - 7)
        id_card_civ = count_res_give-1
        card_civ_id = 83 + 24*id_card_civ

        res_giv = int(action - 40)
        env[77 + res_giv] += 1 #C??c nguy??n li???u ???? tr??? trong turn tr??? nguy??n li???u
        env[e_idp + 5 + res_giv]  -= 1 #Tr??? nguy??n li???u c???a b???n th??n
        env[69 + res_giv] += 1 # C???ng nguy??n li???u cho ng??n h??ng
        ##print('C??c nguy??n li???u ???? tr???', env[77:81], 'c???n tr???', count_res_give, env[e_idp + 5:e_idp + 9])
        check_end_pull_people = False
        ##print('trong phase 3', check_end_pull_people)
        if np.sum(env[77:81]) == count_res_give: #Khi ????? nguy??n li???u th?? m??? th??? civ m???i, l???y th??? cho ng?????i ch??i, sang ng?????i ch??i kh??c

            #print('Civ card l???y', env[5:41][np.where(all_civ_card == 1)[0][id_card_civ]])
            env[77:81] = 0 #C??c nguy??n li???u ???? l???y g??n l???i b???ng 0

            env[E_START_CIV + id_card_civ] = -2 #????nh d???u l?? ???? l???y

            env[E_PHASE:] = 0  #?????i phase v??? phase 2
            env[E_PHASE + 2] = 1
            ##print('V???n tr??? ???????c')
            check_end_pull_people = True

            env[e_idp + 22:e_idp + 30] += env[card_civ_id + 11: card_civ_id + 19] #Th??m th??? v??n minh
            env[e_idp + 39:e_idp + 43] += (env[card_civ_id + 19])*env[card_civ_id + 20: card_civ_id + 24] #Th??m th??? s??? ng?????i t??nh ??i???m cu???i game
            
            env[e_idp + 1] += env[card_civ_id + 8] #Th??m l??a
            env[e_idp + 3] += env[card_civ_id + 2] #Th??? c?? th??m th???c ??n(1,2 ,3 ,4, 5, 6, 7)

            if env[card_civ_id] == 0:
                if env[card_civ_id + 5] > 0:
                    env[e_idp + 5 + 2] += env[card_civ_id + 5] #Th??m nguy??n li???u b???c
                    env[69 + 2] -= env[card_civ_id + 5]
                if env[card_civ_id + 6] > 0:
                    env[e_idp + 5 + 3] += env[card_civ_id + 6] #Th??m nguy??n li???u v??ng
                    env[69 + 3] -= env[card_civ_id + 6]

                if env[card_civ_id] == 0:
                    if env[card_civ_id + 4] > 0:
                        env[e_idp + 5 + 1] += env[card_civ_id + 4] #Th??m nguy??n li???u g???ch
                        env[69 + 1] -= env[card_civ_id + 4]
                    
            env[e_idp] += env[card_civ_id + 3] #Th??m ??i???m

            if env[card_civ_id + 7] == 1: #Th??m c??ng c???
                id_min = np.argmin(env[e_idp+9:e_idp+12]) 
                env[e_idp + 9 + id_min] += 1
                env[e_idp + 15 + np.where(env[e_idp + 9:e_idp + 12] > 0)[0]] = 1
            
            if env[card_civ_id + 7] > 1: #Th??m 2, 3, 4 c??ng c??? d??ng sau
               ##print('Th??? c?? th??m c??ng c???', env[card_civ_id:card_civ_id+25])
                id_civ_tool_1_use = int(env[card_civ_id + 7]) - 2
                env[e_idp + 12 + id_civ_tool_1_use] = 1
            
            if env[card_civ_id] > 0: #Th??? roll 2 x??c x???c ????? l???y t??i nguy??n
                if env[card_civ_id + 4] > 0: #G???
                    res_take = 3
                elif env[card_civ_id + 5] > 0: #V??ng
                    res_take = 5
                elif env[card_civ_id + 6] > 0: #G???ch
                    res_take = 6

                if np.sum(env[e_idp+12:e_idp+15]) > 0 or (env[e_idp+9:e_idp+12] > 0).any(): #N???u c??n th??? c??ng c??? ????? d??ng
                    env[E_TOTAL_DICE] = RollDice(2)
                    env[E_PULL_RECENT] = res_take
                    env[E_PHASE:] = 0  #?????i phase
                    env[E_PHASE + 4] = 1
                    check_end_pull_people = False
                else: #Kh??ng c?? c??ng c??? th?? roll lu??n
                    env = RollDiceGetRes(2, env, res_take, e_idp)


            if env[card_civ_id + 9] == 2: #th??? l???y th??m 2 nguy??n li???u
                check_end_pull_people = False
                env[e_idp+30] = 2

            if env[card_civ_id + 1] == 1:
                check_end_pull_people = False
                for dice in range(4):
                    env[E_START_DICE_FOR_CIV + dice] = np.random.randint(1, 7)
                env[E_PHASE:] = 0  #?????i phase
                env[E_PHASE + 7] = 1

            if env[card_civ_id + 10] == 1: #Th??? ch???n th??m 1 th??? civ m???i t??? ch???ng b??i ??p
               ##print('Th??? l???y 1 th??? m???i t??? ?? v??n minh')
                card_has_not_been_collected = np.where(all_civ_card == 0)[0] 
                if len(card_has_not_been_collected) > 0:
                    id_card_top_most_close = int(card_has_not_been_collected[0]) 
                   ##print('Civ card l???y th??m', env[5:41][id_card_top_most_close])
                    all_civ_card[id_card_top_most_close] = -1
                
                    id_card_in_deck = int(env[5:41][id_card_top_most_close])
                    infor_card_top_most_close = CIV_CARDS[id_card_in_deck] #L???y th??ng tin th??? s??? m??? th??m

                    env[e_idp + 22:e_idp + 30] += infor_card_top_most_close[11:19] #Th??m th??? v??n minh
                    env[e_idp + 39:e_idp + 43] += (infor_card_top_most_close[19])*infor_card_top_most_close[20:24] #Th??m th??? s??? ng?????i t??nh ??i???m cu???i game


    elif phase == 4: #D??ng c??ng c???(end ho???c h???t th?? qua roll x??c x???c)
        check_use_tool = False
        check_end_pull_people = False
        if action == 0:
            env = RollDiceUseTool(env, e_idp)
            check_end_pull_people = True

            ###N???u c??n c?? th??? l???y ng?????i th?? l???y, kh??ng th?? sang ng?????i ch??i kh??c
        else:
            if action in [37, 38, 39]:
                id_action = action - 37
                env[E_ALL_TOOL] += env[e_idp + 9 + id_action]
                # env[e_idp + 9 + id_action] = - env[e_idp + 9 + id_action]
                env[e_idp + 15 + id_action] = 0
                ###N???u c??n c?? th??? l???y c??ng c??? th?? l???y c??ng c???
                if np.sum(env[e_idp+12:e_idp+15]) > 0 or (env[e_idp+15:e_idp+18] > 0).any():
                    check_use_tool = True

            elif action in [44, 45, 46]:
                id_action = action - 44
                env[E_ALL_TOOL] += (id_action + 2)
                env[e_idp + 12 + id_action] = 0
                if np.sum(env[e_idp+12:e_idp+15]) > 0 or (env[e_idp+15:e_idp+18] > 0).any():
                    check_use_tool = True
                
            if check_use_tool == False:
                env = RollDiceUseTool(env, e_idp)
                check_end_pull_people = True

            
    elif phase == 5: #tr??? nguy??n li???u khi mua th??? build tr??? nguy??n li???u b???t k??? t??? 1 -> 7

        res_giv = int(action - 40)
        env[77 + res_giv] += 1 #C??c nguy??n li???u ???? tr??? trong turn tr??? nguy??n li???u
        env[e_idp + 5 + res_giv]  -= 1 #Tr??? nguy??n li???u c???a b???n th??n
        env[69 + res_giv] += 1 # C???ng nguy??n li???u cho ng??n h??ng

        check_end_pull_people = False
        if np.sum(env[77:81]) == 7 or action == 47 or np.sum(env[e_idp+5:e_idp+9]) == 0:
            env[E_START_CIV + int(env[E_PULL_RECENT])-8] = -2 #????nh d???u l?? ???? l???y

            score_add = env[77:81] *(np.array([3, 4, 5, 6]))
            env[e_idp] += np.sum(score_add) #C???ng th??m ??i???m
            env[e_idp + 4] += 1 #C???ng th??m s??? nh??

            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1

            check_end_pull_people = True

            env[77:81] = 0 #reset l???i nguy??n li???u ???? tr???


    elif phase == 6: #Ch???n tr??? nguy??n li???u ho???c tr??? ??i???m khi kh??ng ????? th???c ??n
        check_end_pull_people = False
        if action == 28: #Ch???n tr??? ??i???m, sang ng?????i ch??i kh??c
            check_end_pull_people = True
            env[e_idp] -= 10
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1
            env[e_idp + 21] = 1 #????nh d???u ???? tr??? nguy??n li???u

            #?????i l???i ng?????i ch??i cu???i c??ng

            main_player = int(env[4])%4
            # env[0:4] = 0 #?????i ng?????i ch??i
            id_move = int((main_player+3)%4)
           ##print('?????i ng?????i ch????i ??? phase 6', 'main_player', main_player, 'chuy???n sang', int((main_player+3)%4))

        if action == 27: #Ch???n tr??? nguy??n li???u, sang phase 10
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 10] = 1

    elif phase == 7: #Ch???n gi?? tr??? x??c x???c khi d??ng th??? civ x??c x???c
        ##print('gi?? tr??? x??c x???c', env[E_START_DICE_FOR_CIV:E_END_DICE_FOR_CIV], 'Ng?????i ch??i ti???p theo', idp)
        dice = action - 56
        # print('dice', dice, env[E_START_DICE_FOR_CIV:E_END_DICE_FOR_CIV])
        if dice == 6: env[e_idp+1] += 1 #Th??m l??a
        if dice == 1: 
            env[e_idp+5] += 1 #Th??m g???
            env[69] -= 1
        if dice == 2: 
            env[e_idp+6] += 1 #Th??m g???ch
            env[69+1] -= 1
        if dice == 3: 
            env[e_idp+7] += 1 #Th??m b???c
            env[69+2] -= 1
        if dice == 4: 
            env[e_idp+8] += 1 #Th??m v??ng
            env[69+3] -= 1
        if dice == 5:
            id_min = np.argmin(env[e_idp+9:e_idp+12])
            env[e_idp + 15 + np.where(env[e_idp + 9:e_idp + 12] > 0)[0]] = 1
            env[e_idp + 9 + id_min] += 1

        id_dice = np.where(env[E_START_DICE_FOR_CIV:E_END_DICE_FOR_CIV] == dice)[0][0]
        env[E_START_DICE_FOR_CIV + id_dice] = 0

        env[0:4] = 0 #?????i ng?????i ch??i
        o_idp = (idp+1)%4
        idp = o_idp
        env[o_idp] = 1
        e_idp = int(E_ID_PLAYER + TOTAL_INDEX_PLAYER*idp)

        check_end_pull_people = False
        if (env[E_START_DICE_FOR_CIV:E_END_DICE_FOR_CIV] == 0).all():
            check_end_pull_people = True
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1

    
    elif phase == 8: #L???y nguy??n li???u t??? ng??n h??ng khi d??ng th??? civ l???y 2 nguy??n li???u b???t k???
        env[e_idp + 30] -= 1
        id_res = action - 64
        env[e_idp + 5 + id_res] += 1 #th??m nguy??n li???u cho ng?????i ch??i
        env[69 + id_res] -= 1 #Tr??? nguy??n li???u ??? ng??n h??ng

        if env[e_idp + 30] == 0:
            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1

    elif phase == 9: #tr??? nguy??n li???u khi mua th??? build c?? s??? l?????ng m???c ?????nh
        check_end_pull_people = False
        res_giv = int(action - 40)
        env[77 + res_giv] += 1 #C??c nguy??n li???u ???? tr??? trong turn tr??? nguy??n li???u
        env[e_idp + 5 + res_giv]  -= 1 #Tr??? nguy??n li???u c???a b???n th??n
        env[69 + res_giv] += 1 # C???ng nguy??n li???u cho ng??n h??ng

        id_build_card = int(env[E_PULL_RECENT] - 12)
        all_infor_build_card = env[179:211].reshape((4, 8))
        build_card_take = all_infor_build_card[id_build_card]

        check_get_card = False
        if build_card_take[6] == 4 and build_card_take[7] == 2:
            for case_card in BUILD_4_2:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        elif build_card_take[6] == 4 and build_card_take[7] == 3:
            for case_card in BUILD_4_3:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        elif build_card_take[6] == 4 and build_card_take[7] == 4:
            for case_card in BUILD_4_4:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        elif build_card_take[6] == 5 and build_card_take[7] == 2:
            for case_card in BUILD_5_2:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        elif build_card_take[6] == 5 and build_card_take[7] == 3:
            for case_card in BUILD_5_3:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        elif build_card_take[6] == 5 and build_card_take[7] == 4:
            for case_card in BUILD_5_4:
                if (env[77:81] == case_card).all(): #L???y th??? 
                    check_get_card = True
                    break

        if check_get_card == True:
            check_end_pull_people = True

            score_add = env[77:81] *(np.array([3, 4, 5, 6]))
            env[e_idp] += np.sum(score_add) #C???ng th??m ??i???m
            env[e_idp + 4] += 1 #C???ng th??m s??? nh??

            env[E_START_CIV + int(env[E_PULL_RECENT])-8] = -2 #????nh d???u l?? ???? l???y

            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1

            env[77:81] = 0

    elif phase == 10: #tr??? nguy??n li???u n???u kh??ng ????? th???c ??n
        check_end_pull_people = False
        res_giv = int(action - 40)
        env[77 + res_giv] += 1 #C??c nguy??n li???u ???? tr??? trong turn tr??? nguy??n li???u
        env[e_idp + 5 + res_giv]  -= 1 #Tr??? nguy??n li???u c???a b???n th??n
        env[69 + res_giv] += 1 # C???ng nguy??n li???u cho ng??n h??ng
       ##print('S??? l?????ng nguy??n li???u c???n ph???i tr???', env[81])
        if np.sum(env[77:81]) == env[81]:
            check_end_pull_people = True
            env[77:81] = 0

            env[E_PHASE:] = 0  #?????i phase
            env[E_PHASE + 2] = 1

            env[e_idp + 21] = 1 #????nh d???u ???? tr??? nguy??n li???u
            #?????i l???i ng?????i ch??i cu???i c??ng

            main_player = int(env[4])%4
            # env[0:4] = 0 #?????i ng?????i ch??i
            # env[int((main_player+3)%4)] = 1
            id_move = int((main_player+3)%4)
            env[81] = 0
           ##print('?????i ng?????i ch????i ??? phase 10', 'main_player', main_player, 'chuy???n sang', int((main_player+3)%4))


    # N???u h???t ng?????i th?? chuy???n sang ng?????i ch??i kh??c, kh??ng th?? v???n gi??? ng?????i ch??i d??
    # N???u t???t c??? m???i ng?????i h???t ng?????i th?? c???ng th??m turn, turn n??y c??ng ch??nh l?? ng?????i ch??i ch??nh
    so_nguoi_da_dat = np.sum(env[e_idp + 31:e_idp + 39]) + len(np.where(env[E_START_CIV:E_END_BUILD] == idp)[0])

   ##print('S??? ng?????i ???? ?????t', so_nguoi_da_dat)
    if check_end_pull_people == True:
        # print(env[e_idp + 31:e_idp + 39], np.where(env[E_START_CIV:E_END_BUILD] == idp)[0], idp, env[E_START_CIV:E_END_BUILD])
        if so_nguoi_da_dat == 0 and phase != 1 and phase != 0:
            main_player = int(env[4])%4
            env[0:4] = 0 #?????i ng?????i ch??i
            if env[e_idp + 21] == 1:
                idp = id_move
           ##print('T???i l??c tr??? nguy??n li???u',  'main_player', main_player, 'chuy???n sang', idp)
            if (idp+1)%4 == main_player: 
               ##print('Xong 1 v??ng')
                #N???u l?? ng?????i cu???i c??ng l???y h???t ng?????i th?? tr??? th???c ??n
                #Kh??ng ????? th???c ??n th?? ch???n tr??? nguy??n li???u ho???c tr??? 10 ??i???m
                #Kh??ng ????? nguy??n li???u th?? auto ch???n tr??? ??i???m
                check_tra_thuc_an = True
                for id_return in range(4):
                    e_id_return = int(E_ID_PLAYER + TOTAL_INDEX_PLAYER*id_return)
                    if env[e_id_return + 21] == 0: #Ch??a tr??? th???c ??n
                        if (env[e_id_return + 3] + env[e_id_return + 1]) >= env[e_id_return + 2]:
                            if (env[e_id_return + 2] - env[e_id_return + 1]) > 0:
                                env[e_id_return + 3] -= (env[e_id_return + 2] - env[e_id_return + 1])
                                env[e_id_return + 21] = 1
                        elif (np.sum(env[e_id_return + 5: e_id_return + 9]) + env[e_id_return + 3] + env[e_id_return + 1]) < env[e_id_return + 2]:
                            env[e_id_return] -= 10 #Tr??? ??i???m
                            env[e_id_return + 3] = 0
                            env[e_id_return + 21] = 1 
                        else:
                            env[81] = env[e_id_return + 2] - env[e_id_return + 3] - env[e_id_return + 1]
                            env[e_id_return + 3] = 0
                            check_tra_thuc_an = False

                            #?????i ng?????i ch??i
                            env[0:4] = 0
                            env[id_return] = 1

                            #?????i phase
                            env[E_PHASE:] = 0 
                            env[E_PHASE + 6] = 1
                            break
                
                if check_tra_thuc_an == True: #???? tr??? th???c ??n h???t cho mn, sang v??ng m???i, m??? th??? m???i
                   ##print('Sang turn m???i')
                    
                    for id_return in range(4): #Tr??? l???i tr???ng th??i th??nh ch??a tr??? th???c ??n
                        e_id_return = int(E_ID_PLAYER + TOTAL_INDEX_PLAYER*id_return)
                        env[e_id_return + 21] = 0

                    env[4] += 1 #Sang v??ng ch??i ti???p theo

                    env[int(env[4])%4] = 1 #Ng?????i ch??i ch??nh ti???p theo s??? b???t ?????u ?????t ng?????i

                    #?????i phase
                    env[E_PHASE:] = 0
                    env[E_PHASE] = 1

                    all_card_civ_open =  np.where(all_civ_card == 1)[0]
                    id_da_lay = np.where(env[E_START_CIV:E_END_CIV] == -2)[0]
                   ##print('th??? c??', all_card_civ_open, 'ID d?? l???y', id_da_lay)
                    all_civ_card[all_card_civ_open[id_da_lay]] = -1 #???? c?? ng?????i l???y
                   ##print(all_civ_card)

                    so_luong_can_mo_them = len(id_da_lay)
                    card_co_the_mo = np.where(all_civ_card == 0)[0]
                    if len(card_co_the_mo) < so_luong_can_mo_them:
                        env[82] = 1
                        env = GetScoreEndGame(env)

                    else:
                        all_civ_card[card_co_the_mo[:so_luong_can_mo_them]] = 1
                        civ_card = env[5:41]
                        ##print(np.where(all_civ_card == 1)[0])
                        id_civ_card_open = civ_card[np.where(all_civ_card == 1)[0]].astype(np.int64)
                        env[E_START_CIV:E_END_CIV] = -1
                        env[83:179] = CIV_CARDS[id_civ_card_open].flatten()
                   ##print('all civ card', all_civ_card)
                    id_da_lay = np.where(env[E_START_BUILD:E_END_BUILD] == -2)[0]
                    if len(id_da_lay) > 0:
                        # print('L???y th??? build', id_da_lay, all_build_card)
                        for id_deck_card in range(4):
                            if id_deck_card in id_da_lay:
                                id_card_open = np.where(all_build_card[id_deck_card] == 1)[0]
                                if id_card_open == 6:
                                    env[82] = 1
                                    env = GetScoreEndGame(env)
                                    break
                                else:
                                    all_build_card[id_deck_card][id_card_open] = -1
                                    all_build_card[id_deck_card][id_card_open + 1] = 1
                                    all_build_card = all_build_card.flatten()
                                    build_card = env[41:69]
                                    id_build_card_open = build_card[np.where(all_build_card == 1)[0]].astype(np.int64)
                                    env[179:211] = BUILDING_CARDS[id_build_card_open].flatten()
                                    all_build_card = all_build_card.reshape((4,7))
                        # print(all_build_card)
                        id_build_desk, id_card_in_desk = np.where(all_build_card == 1)
                        env[73 + id_build_desk] = 7 - id_card_in_desk

                        env[E_START_BUILD:E_END_BUILD] = -1

            else:
               ##print('?????i ng?????i ch??i kh??c l???y ng?????i', env[E_START_CIV:E_END_BUILD], env[77:81])
                env[(idp+1)%4] = 1

                env[E_PHASE:] = 0 
                env[E_PHASE + 2] = 1

    return env, all_build_card, all_civ_card


@njit()
def getReward(p_state):
    p_state = p_state.astype(np.int64)
    if p_state[13] == 0:
        return -1
    else:
        if p_state[P_ID_PLAYER] == np.max(p_state[np.array([142, 186, 230, 274])]):
            return 1
        else:
            return 0

@njit()
def one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env, all_build_card, all_civ_card = initEnv(BUILDING_CARDS, CIV_CARDS)
    _cc = 0
    while _cc <= 1000:
        idx = np.where(env[0:4] == 1)[0][0]
        player_state = getAgentState(env)
        
        if list_other[idx] == -1:
            action, per_player = p0(player_state,per_player)
            list_action = getValidActions(player_state)
            if list_action[action] != 1:
                raise Exception('Action kh??ng h???p l???')
        elif list_other[idx] == 1:
            action, per1 = p1(player_state,per1)
        elif list_other[idx] == 2:
            action, per2 = p2(player_state,per2)
        elif list_other[idx] == 3:
            action, per3 = p3(player_state,per3) 


        env, all_build_card, all_civ_card = stepEnv(action, env, all_build_card, all_civ_card)
        if checkEnded(env)[0] != -1:
            break
        
        _cc += 1

    env[82] = 1 #G??n cho bi???n k???t th??c game
    for p_idx in range(4):
        env[83] = p_idx
        env[0:4] = 0
        env[p_idx] = 1
        p_state = getAgentState(env)
        if list_other[p_idx] == -1:
            act, per_player = p0(p_state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(p_state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(p_state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(p_state, per3)
        else:
            raise Exception('Sai list_other.')

    winner = False

    if np.where(list_other == -1)[0][0] in checkEnded(env):
        winner = True
    else: winner = False

    return winner,  per_player

@njit()
def n_games_numba(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3):
    win = 0
    for _ in range(num_game):
        np.random.shuffle(list_other)
        winner, per_player = one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3)
        win += winner

    return win, per_player

def one_game_normal(p0, list_other, per_player, per1, per2, per3, p1, p2, p3):
    env, all_build_card, all_civ_card = initEnv(BUILDING_CARDS, CIV_CARDS)
    _cc = 0
    while _cc <= 1000:
        idx = np.where(env[0:4] == 1)[0][0]
        player_state = getAgentState(env)
        
        if list_other[idx] == -1:
            action, per_player = p0(player_state,per_player)
            list_action = getValidActions(player_state)
            if list_action[action] != 1:
                raise Exception('Action kh??ng h???p l???')
        elif list_other[idx] == 1:
            action, per1 = p1(player_state,per1)
        elif list_other[idx] == 2:
            action, per2 = p2(player_state,per2)
        elif list_other[idx] == 3:
            action, per3 = p3(player_state,per3) 


        env, all_build_card, all_civ_card = stepEnv(action, env, all_build_card, all_civ_card)
        if checkEnded(env)[0] != -1:
            break
        
        _cc += 1

    env[82] = 1 #G??n cho bi???n k???t th??c game
    for p_idx in range(4):
        env[83] = p_idx
        env[0:4] = 0
        env[p_idx] = 1
        p_state = getAgentState(env)
        if list_other[p_idx] == -1:
            act, per_player = p0(p_state, per_player)
        elif list_other[p_idx] == 1:
            action, per1 = p1(p_state, per1)
        elif list_other[p_idx] == 2:
            action, per2 = p2(p_state, per2)
        elif list_other[p_idx] == 3:
            action, per3 = p3(p_state, per3)
        else:
            raise Exception('Sai list_other.')

    winner = False

    if np.where(list_other == -1)[0][0] in checkEnded(env):
        winner = True
    else: winner = False

    return winner,  per_player

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
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData

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