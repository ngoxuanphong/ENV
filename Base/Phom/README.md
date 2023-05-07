##  :video_game: Action
    * [0]   action  ăn bài
    * [1]    action không ăn bài
    * [2:54] action đánh bài


##  Quy định lá bài
    - index_card // 4
      => quyết định lá bài và điểm của lá bài
    - index_card % 4
      => quyết định chất
      ( 0 = Bích,  1 là tép, 2 = rô,  3 = cơ )
      ( 1 = lá A, 2 = lá 2,  3 = lá 3 ..., 11 = lá j,  12
    = lá q,  13 = lá k)

##  :bust_in_silhouette: Player_state
    -   [0:51] Lá bài của bản thân
    -   [52:104] Lá bài của người tiếp theo đánh cho mình
    -   [104:104+52] Lá bài rác của người tiếp theo
    -   [104+52:104+52+52]   Lá bài rác của 2 người khác và bản thân
    -   [104+52+52:104+52+52+52]   Lá phỏm của bản thân
    -   [104+52x3:104+52x6]  Lá phỏm của 3 người tiếp theo lượt
    -   Trong đó :
    -   ([104+52x3:104+52x4], [104+52x4:104+52x5], [104+52x5:104+52x6] là lá bài trên tay 3 người tiếp theo lượt) 
    -   [416:420]   Ví trí của bản thân
    -   [420:423]   Phase
        -   Phase 1 là index 420,  Phase 2 là index 421,  Phase 0 là index 422
        -   Phase 0 là phase bắt đầu game (luôn bằng 0 )
        -   Phase 1 là phase lựa chọn bốc bài hay ăn bài đối thủ 
        -   Phase 2 là phase lựa chọn bài để đánh 
    -   [423:631]  Lá bài trên tay  người chơi  khi hạ phỏm
        -   [423:423+52:] là lá bài của bản thân 
        -   ([423+52:423+52+52], [423+52+52:423+52+52+52], [423+52+52+52:631] là lá bài trên tay 3 người tiếp theo lượt)
    -   [631] Kiểm tra xem kết thúc game chưa
        -   Kết thúc là giá trị 1 còn chưa kết thúc là 0
    -   [632] Kiểm tra người chơi  thắng hay thua
        -   Thắng là giá trị 1 còn thua là 0
    * Note : tất cả các index đều chỉ có giá trị 1/0


##  :globe_with_meridians: ENV_state
    -   [0:52] các con bài
    -   #5,6,7,8 lá bài rác của từng người 
        #9,10,11,12 lá bài đã ăn  và các lá phỏm đã hạ 
    -   [52] player turn
    -   [53] player phase 
    -   [54] lá bài rác vừa hạ 
    -   [55:55+52] các lá còn lại để hạ
    -   [55+52:55+52+52] các lá còn lại  của từng player sau khi hạ
    -   #0,1,2,3 các lá còn lại  của từng player 






