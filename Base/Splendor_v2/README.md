##  Thông tin quan trọng:
     -    17: Điểm của bản thân
     -    213, 214, 215: Điểm của 3 người chơi còn lại
     
## :video_game: Action
    -  [0]   : Là action bỏ lượt
    -  [1:13]  lấy 12 thẻ trên bàn
    -  [13:16] Là mở 3 thẻ đang úp
    -  [16:28] Úp 12 thẻ trên bàn
    -  [28:31] Úp 3 thẻ ẩn
    -  [31:36] Lấy 5 nguyên liêu
    -  [36:42] Trả 6 nguyên liệu

## :bust_in_silhouette: P_state
     - Thông tin nguyên liệu theo thứ tự: red, blue, green, black, white, yellow
     -   [:6]            là Số lượng nguyên liệu đang có trên bàn
     -   [6: 18]         thông tin của người chơi, gồm có  6 nguyên liệu đang có, 5 nguyên liệu mặc định và điểm
     -   [18:150]:       12 thẻ bình thường trên bàn, mỗi thẻ có 11 state gồm: [điểm, 5 state loại thẻ, 5 nguyên liệu mua]
     -   [150: 175]:     5 thẻ Noble trên bàn, mỗi thẻ có 5 state gồm: [5 loại nguyên liệu cần]
     -   [175:208]:      3 thẻ úp trên tay, mỗi thẻ có 11 state gồm: [điểm, 5 state loại thẻ, 5 nguyên liệu mua]
     -   [208: 213]:     5 nguyên liệu đã lấy trong phase lấy nguyên liệu
     -   [213:216]:      điểm của 3 người chơi còn lại
     -   [216:219]:      Có thể úp được thẻ ẩn không, (1, 0). Gồm có 3 thẻ ẩn của 3 loại
     -   [219]:          Số thẻ có thể úp trên bàn
     -   [220]:          Đã hết game hay chưa(1, 0)


## :globe_with_meridians: ENV_state
    -    [0:90]     các thẻ trên bàn: 5 là đang ở trên bàn, -(p_id) là đang úp, p_id là người chơi đã mua được
    -    [100]      Turn
    -    [101:107]  Nguyên liệu trên bàn, gồm có 6 nguyên liệu
    -    [107 + 12 * p_id:119 + 12 * p_id] thông tin của người chơi, gồm có  6 nguyên liệu đang có, 5 nguyên liệu mặc định và điểm
    -    [155:160] 5 Nguyên liệu mà người đó đã lấy trong turn
    -    [161:164] 3 thẻ ẩn có thể úp cấp 1, 2, 3


