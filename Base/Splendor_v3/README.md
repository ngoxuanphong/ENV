##  Thông tin quan trọng:
     -    17: Điểm của bản thân
     -    213, 214, 215: Điểm của 3 người chơi còn lại
     
## :video_game: Action
     -   [0:12]: Chọn 12 thẻ trên bàn
     -   [12:15]: Chọn 3 thẻ úp trên tay

## Thứ tự ưu tiên các action
     - Thẻ taget

     - 1. -> Lấy thẻ
     - 2. Nếu số nguyên liệu đang có <=7 và lấy được và có nguyên liệu để mua thẻ taget -> Lấy 3 nguyên liệu
     - 3. Nếu thẻ taget ở trên bàn và úp được -> úp thẻ
     - 4. Nếu trên bàn có thể lấy được thẻ có nguyên liệu mặc định cần cho thẻ taget -> Lấy thẻ đó với số lượng nguyên liệu bỏ ra ít nhất
     - 5. Nếu có nguyên liệu cần để mua thẻ taget thì sẽ lấy nguyên liệu đó -> Lấy nguyên liệu
     - 6. Nếu có thẻ miễn phí trên bàn -> Lấy thẻ miễn phí
     - 7. Nếu có nguyên liệu cho thẻ taget và trên bàn nguyên liệu đó có >= 4 nguyên liệu  -> lấy 2 nguyên liệu đó
     - 8. Nếu tổng số nguyên liệu <= 8, và có thể lấy 2 nguyên liệu bất kỳ trên bàn -> Lấy 2 nguyên liệu
     - 9. Nếu mua được nguyên liệu nào trên bàn thì lấy nguyên liệu đó
     - 10. Lấy thẻ bất kỳ trên bàn với số lượng nguyên liệu bỏ ra ít nhất

## :bust_in_silhouette: P_state
     - Thông tin nguyên liệu theo thứ tự: red, blue, green, black, white, yellow
     -   [:6]            là Số lượng nguyên liệu đang có trên bàn
     -   [6: 18]         thông tin của người chơi, gồm có  6 nguyên liệu đang có, 5 nguyên liệu mặc định và điểm
     -   [18:150]:       12 thẻ bình thường trên bàn, mỗi thẻ có 11 state gồm: [điểm, 5 state loại thẻ, 5 nguyên liệu mua]
     -   [150: 175]:     5 thẻ Noble trên bàn, mỗi thẻ có 5 state gồm: [5 loại nguyên liệu cần]
     -   [175:208]:      3 thẻ úp trên tay, mỗi thẻ có 11 state gồm: [điểm, 5 state loại thẻ, 5 nguyên liệu mua]
     -   [208: 213]:     5 nguyên liệu đã lấy trong phase lấy nguyên liệu (Không có ý nghĩa trong game này)
     -   [213:216]:      điểm của 3 người chơi còn lại
     -   [216:219]:      Có thể úp được thẻ ẩn không, (1, 0). Gồm có 3 thẻ ẩn của 3 loại
     -   [219]:          Số thẻ có thể úp trên bàn
     -   [220]:          Đã hết game hay chưa(1, 0)


     
## :globe_with_meridians: ENV_state
    -   [0:90] các thẻ trên bàn: 5 là đang ở trên bàn, -(p_id) là đang úp, p_id là người chơi đã mua được
    -   [100] Turn
    -   [101:107] Nguyên liệu trên bàn, gồm có 6 nguyên liệu
    -   [107 + 12 * p_id:119 + 12 * p_id] thông tin của người chơi, gồm có  6 nguyên liệu đang có, 5 nguyên liệu mặc định và điểm
    -   [155:160] 5 Nguyên liệu mà người đó đã lấy trong turn
    -   [161:164] 3 thẻ ẩn có thể úp cấp 1, 2, 3
