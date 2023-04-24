import numpy as np

NUMBER_PLAYER = 4
NUMBER_PHASE = 7
ATTRIBUTE_PLAYER = 20       #(Coin, số lượng mỗi loại thẻ (12 thẻ thường, 3 thẻ special, 4 thẻ target (22-16-10-4)))
NUMBER_TYPE_NORMAL_CARD = 12
NUMBER_TYPE_SPECIAL_CARD = 3
NUMBER_TARGET_CARD = 4
NUMBER_PER_NORMAL_CARD = 6


INDEX = 0
#thông tin 4 người chơi
ENV_PLAYER_IN4 = INDEX
INDEX += NUMBER_PLAYER * ATTRIBUTE_PLAYER

#số lượng mỗi loại thẻ trên bàn chơi
ENV_NORMAL_CARD = INDEX
INDEX += NUMBER_TYPE_NORMAL_CARD

#thẻ người chơi đã mua trong turn
ENV_CARD_BUY_IN_TURN = INDEX
INDEX += NUMBER_TYPE_NORMAL_CARD

#các thông tin khác
# ENV_OTHER_IN4 = INDEX

#thẻ người chơi đổi đi
ENV_CARD_SELL = INDEX
INDEX += 1

#người chơi được đổ xúc sắc tiếp hay không
ENV_PLAYER_CONTINUE = INDEX
INDEX += 1

#Giá trị xúc sắc gần nhất
ENV_LAST_DICE = INDEX
INDEX += 1

#Người chơi bị chọn
ENV_PICKED_PLAYER = INDEX
INDEX += 1

#Người chơi hành động
ENV_ID_ACTION = INDEX
INDEX += 1

#Phase
ENV_PHASE = INDEX
INDEX += 1

#Check_end_game
ENV_CHECK_END = INDEX
INDEX += 1

ENV_LENGTH = INDEX


P_INDEX = 0

#thông tin 4 người chơi
P_PLAYER_IN4 = P_INDEX
P_INDEX += NUMBER_PLAYER * ATTRIBUTE_PLAYER

#số lượng mỗi loại thẻ trên bàn chơi
P_NORMAL_CARD = P_INDEX
P_INDEX += NUMBER_TYPE_NORMAL_CARD

#thẻ người chơi đã mua trong turn
P_CARD_BUY_IN_TURN = P_INDEX
P_INDEX += NUMBER_TYPE_NORMAL_CARD

#các thông tin khác
#thẻ người chơi đổi đi
P_CARD_SELL = P_INDEX
P_INDEX += NUMBER_TYPE_NORMAL_CARD

#người chơi được đổ xúc sắc tiếp hay không
P_PLAYER_CONTINUE = P_INDEX
P_INDEX += 1

#Giá trị xúc sắc gần nhất
P_LAST_DICE = P_INDEX
P_INDEX += 1

#Người chơi bị chọn
P_PICKED_PLAYER = P_INDEX
P_INDEX += NUMBER_PLAYER


#Phase
P_PHASE = P_INDEX
P_INDEX += NUMBER_PHASE

#Check end
P_CHECK_END = P_INDEX
P_INDEX += 1

P_LENGTH = P_INDEX


ALL_CARD_FEE =  np.array([1, 1, 1, 2, 2, 3, 5, 3, 6, 3, 3, 2, 6, 7, 8, 22, 16, 10, 4])























































