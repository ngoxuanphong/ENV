import numpy as np
import random as rd
from numba import njit, jit
from numba.typed import List
import sys, os
from setup import SHORT_PATH
import importlib.util
game_name = sys.argv[1]

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHORT_PATH}Base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

env = setup_game(game_name)

getActionSize = env.getActionSize
getStateSize = env.getStateSize
getAgentSize = env.getAgentSize

getValidActions = env.getValidActions
getReward = env.getReward

@njit
def DataAgent():
  return [np.zeros((1,1))]

__ACTIONS__ = np.array([[0,-1],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15],[1,16],[1,17],[1,18],[1,19],[1,20],[1,21],[1,22],[1,23],[1,24],[1,25],[1,26],[1,27],[1,28],[1,29],[1,30],[1,31],[1,32],[1,33],[1,34],[1,35],[1,36],[1,37],[1,38],[1,39],[1,40],[1,41],[1,42],[1,43],[1,44],[1,45],[1,46],[1,47],[1,48],[1,49],[1,50],[1,51],[2,1],[2,2],[2,3],[2,5],[2,6],[2,7],[2,9],[2,10],[2,11],[2,13],[2,14],[2,15],[2,17],[2,18],[2,19],[2,21],[2,22],[2,23],[2,25],[2,26],[2,27],[2,29],[2,30],[2,31],[2,33],[2,34],[2,35],[2,37],[2,38],[2,39],[2,41],[2,42],[2,43],[2,45],[2,46],[2,47],[2,49],[2,50],[2,51],[3,2],[3,3],[3,6],[3,7],[3,10],[3,11],[3,14],[3,15],[3,18],[3,19],[3,22],[3,23],[3,26],[3,27],[3,30],[3,31],[3,34],[3,35],[3,38],[3,39],[3,42],[3,43],[3,46],[3,47],[3,50],[3,51],[4,3],[4,7],[4,11],[4,15],[4,19],[4,23],[4,27],[4,31],[4,35],[4,39],[4,43],[4,47],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[5,14],[5,15],[5,16],[5,17],[5,18],[5,19],[5,20],[5,21],[5,22],[5,23],[5,24],[5,25],[5,26],[5,27],[5,28],[5,29],[5,30],[5,31],[5,32],[5,33],[5,34],[5,35],[5,36],[5,37],[5,38],[5,39],[5,40],[5,41],[5,42],[5,43],[5,44],[5,45],[5,46],[5,47],[6,12],[6,13],[6,14],[6,15],[6,16],[6,17],[6,18],[6,19],[6,20],[6,21],[6,22],[6,23],[6,24],[6,25],[6,26],[6,27],[6,28],[6,29],[6,30],[6,31],[6,32],[6,33],[6,34],[6,35],[6,36],[6,37],[6,38],[6,39],[6,40],[6,41],[6,42],[6,43],[6,44],[6,45],[6,46],[6,47],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[7,33],[7,34],[7,35],[7,36],[7,37],[7,38],[7,39],[7,40],[7,41],[7,42],[7,43],[7,44],[7,45],[7,46],[7,47],[8,20],[8,21],[8,22],[8,23],[8,24],[8,25],[8,26],[8,27],[8,28],[8,29],[8,30],[8,31],[8,32],[8,33],[8,34],[8,35],[8,36],[8,37],[8,38],[8,39],[8,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[9,24],[9,25],[9,26],[9,27],[9,28],[9,29],[9,30],[9,31],[9,32],[9,33],[9,34],[9,35],[9,36],[9,37],[9,38],[9,39],[9,40],[9,41],[9,42],[9,43],[9,44],[9,45],[9,46],[9,47],[10,28],[10,29],[10,30],[10,31],[10,32],[10,33],[10,34],[10,35],[10,36],[10,37],[10,38],[10,39],[10,40],[10,41],[10,42],[10,43],[10,44],[10,45],[10,46],[10,47],[11,32],[11,33],[11,34],[11,35],[11,36],[11,37],[11,38],[11,39],[11,40],[11,41],[11,42],[11,43],[11,44],[11,45],[11,46],[11,47],[12,36],[12,37],[12,38],[12,39],[12,40],[12,41],[12,42],[12,43],[12,44],[12,45],[12,46],[12,47],[13,40],[13,41],[13,42],[13,43],[13,44],[13,45],[13,46],[13,47],[14,9],[14,10],[14,11],[14,13],[14,14],[14,15],[14,17],[14,18],[14,19],[14,21],[14,22],[14,23],[14,25],[14,26],[14,27],[14,29],[14,30],[14,31],[14,33],[14,34],[14,35],[14,37],[14,38],[14,39],[14,41],[14,42],[14,43],[14,45],[14,46],[14,47],[15,13],[15,14],[15,15],[15,17],[15,18],[15,19],[15,21],[15,22],[15,23],[15,25],[15,26],[15,27],[15,29],[15,30],[15,31],[15,33],[15,34],[15,35],[15,37],[15,38],[15,39],[15,41],[15,42],[15,43],[15,45],[15,46],[15,47]], dtype=np.int64)
#---------------------------------------------------------------------------------------------------------
@njit()
def getCardOnHand(state):
    card_on_hand = state[0:52]
    return np.where(card_on_hand == 1)[0]
def getMode(state):
    another_cards_numb = state[107:110]
    if len(np.where(another_cards_numb < 8 )[0]) > 2:
     return 1    
    else:
       return 0
def checkArrInArr(arr1,arr2):
  # print('arr1,arr2',arr1,arr2)
  arr_return = []
  for i in range(len(arr1)):
    if arr1[i] in arr2:
      arr_return.append(i)
  return arr_return
@njit()
def getSpecialCard(state):
    p_cards = state[0:52]
    p_cards = np.where(p_cards == 1)[0]
    p_cards_value = p_cards//4
    policy = np.zeros(52)
    for i in range(52):
        arr_copy = np.copy(p_cards)
        arr_temp = np.where(arr_copy // 4 == i)[0] 
    # check day
    arr_day = []
    arr_unique = np.unique(p_cards_value)
    for i in range(1,len(arr_unique)):
        if arr_unique[i] == arr_unique[i-1] + 1 :

            arr_day.append(arr_unique[i])
        elif p_cards_value[i] != p_cards_value[i-1] - 1:
            if len(arr_day) >= 3:
                arr_id = checkArrInArr(p_cards_value,arr_day)
                # print('arr_id',arr_id)
                arr_id = p_cards[arr_id]
                policy[arr_id] = 1
            arr_day = []
    return np.where(policy == 1)[0]
@njit()
def getBoDay(state):
    p_cards = state[0:52]
    p_cards = np.where(p_cards == 1)[0]
    p_cards_value = p_cards//4
    policy = np.zeros(52)
    for i in range(52):
        arr_copy = np.copy(p_cards)
        arr_temp = np.where(arr_copy // 4 == i)[0] 
    # check day
    arr_day = []
    arr_unique = np.unique(p_cards_value)
    for i in range(1,len(arr_unique)):
        if arr_unique[i] == arr_unique[i-1] + 1 :
            arr_day.append(arr_unique[i])
        elif arr_unique[i] != arr_unique[i-1] - 1:
            if len(arr_day) >= 3:
                arr_id = checkArrInArr(p_cards_value,arr_day)

                arr_id = p_cards[arr_id]
                policy[arr_id] = 1
            arr_day = []
    return np.where(policy == 1)[0]
@njit()
def getHighestCard(action):
  return __ACTIONS__[action][1]

def getTypeAction(action):
  return __ACTIONS__[action][0]
def getValueActions(action):
  return __ACTIONS__[action][1]
def getLowestValueOfChain(action):
    type_ = getTypeAction(action) - 3
    highestValue = getValueActions(action)
    return highestValue//4 - type_ 
def countCardInChain(state,cardValue):
   cards_on_hand = state[0:52]
   cards_on_hand = np.where(cards_on_hand == 1)[0]
   count = 0
   for card_value_ in cards_on_hand:
     if  card_value_ // 4 == cardValue // 4 and card_value_ != cardValue:
       count += 1
   return count
def getAction(state,actions):
    boDay = getBoDay(state)//4
    for action in actions:
        type_ = getTypeAction(action)
        value_ = getValueActions(action)
        if value_//4 not in boDay and value_//4 != 12:
          # print('value_//4',value_//4)
          return action
        else:
          count_chain = countCardInChain(state,getValueActions(action))
          if count_chain > 2:
            # print('count_chain',count_chain)
            return action
    return -1  
def getActionLaDon(state,actions):
    boDay = getBoDay(state)//4
    # check xem co trong bo day va bo doi hay k
    for action in actions:
        type_ = getTypeAction(action)
        value_ = getValueActions(action)
        specialCard = getSpecialCard(state)
        if value_ //4 == 12:
          return action
        if value_//4 not in specialCard//4:
          # print('value_//4',value_//4)
          #  count_chain = countCardInChain(state,getValueActions(action))
          #  if count_chain == 0 or  value_ == 12:
          #   # print('count_chain',count_chain)
            return action
        
# check xem co trong bo doi hay khong
    return -1  
#----------------------------------------------------------------------------------------------------
def Test(state,per):
  cards_on_hand = state[0:52]
  cards_on_hand = np.where(cards_on_hand == 1)[0]
  actions = getValidActions(state)
  specialCards = getSpecialCard(state)

  if np.min(state[107:110]) >=8: 
    if actions[0] == 1 :
        return 0,per
  actions = np.where(actions == 1)[0]
  boDay = getBoDay(state)//4
  type_action = [getTypeAction(action) for action in actions]
  id = np.argmax(type_action)
# Xu ly danh la 2 ------------------------
  if getTypeAction(actions[id]) == 2 and getValueActions(actions[id])//4 in specialCards//4:
     action_ = getAction(state,actions)
     if action_ != -1:
       return action_,per
      #  print('actions[0]',actions[0])
     elif np.min(state[107:110]) > 8:
        return actions[0],per
     else :
       return actions[1],per
# Xu ly danh la 1 ----------------------
  if getTypeAction(actions[id]) == 1 and getValueActions(actions[id])//4 in specialCards//4:
      action_ = getActionLaDon(state,actions[id:])
      if action_ != -1 :
        return action_,per
      elif np.min(state[107:110]) > 8:
        return actions[0],per
      else:
        return actions[1],per
  valueCard = __ACTIONS__[actions[id]][1] // 4
  cardsOnHand = (len(cards_on_hand) + np.sum(state[107:110]))/4
  if valueCard > 13/cardsOnHand * 3.33 + 6:
      return actions[0],per
  return actions[id],per