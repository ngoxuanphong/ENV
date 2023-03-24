# Game-Phỏm
## :dart: Báo cáo Game Phỏm
1.   `Tốc độ chạy`
      - **1000000 Game**: 10 phút 
2. `Chuẩn form`: **Đã test**
3. `Đúng luật`: **Đã check**
4. `Không bị loop vô hạn`: **Đã test** với 1000000 ván
5. `Số ván check_vic > victory_thật`:**Đã test** 10000 ván thì có(thắng thật:1754, check_victory:1798)
6. `Giá trị state, action:`

## :globe_with_meridians: ENV_state
*   [0:52] **các con bài**
*   #5,6,7,8 lá bài rác của từng người 
    #9,10,11,12 lá bài đã ăn  và các lá phỏm đã hạ 
*   [52] **player turn**
*   [53] **player phase** 
*   [54] **lá bài rác vừa hạ** 
*   [55:55+52] **các lá còn lại để hạ**
*   [55+52:55+52+52] **các lá còn lại  của từng player sau khi hạ**
*   #0,1,2,3 các lá còn lại  của từng player 



## :bust_in_silhouette: P_state
*   [0:51] **Lá bài của bản thân**
*   [52:104]] **lá bài của người tiếp theo đánh cho mình**
*   [104:104+52]] **Lá bài rác của người tiếp theo**
*   [104+52:104+52+52]:   **lá bài rác của 2 người khác và bản thân**
*   [104+52+52:104+52+52+52]]:   **lá phỏm của bản thân**
*   [104+52x3:104+526]:   **lá phỏm của 3 người khác**
*   [416:420]:   **lví trí của bản thân**
*   [423:423+52+52+52+52]:   **lá bài trên tay  người chơi  khi hạ phỏm**
*   [631] Check xem có ù 3 phỏm rồi kết thúc game 
*   [632] Check cả làng có móm khong
* **Note** : tất cả các index đều chỉ có giá trị 1/0



## :video_game: Action
* [0]   **action  ăn bài**
* [1]     **action không ăn bài**
* [2:54] **action đánh bài**
## Quy định lá bài
   - index_card // 4
  => quyết định lá bài và điểm của lá bài
- index_card % 4
  => quyết định chất
  ( 0 = Bích , 1 là tép ,2 = rô , 3 = cơ )
  ( 1 = lá A ,2 = lá 2 , 3 = lá 3 ..., 11 = lá j , 12
= lá q , 13 = lá k)
