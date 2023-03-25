
## :video_game: Action



## :bust_in_silhouette: P_state

        19 ô đất, 54 điểm đặt, 72 đường đường, 9 cảng
        Thứ tự tài nguyên: Cây, Gạch, Cừu, Lúa, Đá, Sa mạc
        Thứ tự thẻ dev: KNIGHT, BUILD ROAD, YEAR_OF_PLENTY, MONOPOLY, VICTORY_POINT
    -   [0:114] Tài nguyên trên các ô đất mỗi ô 6 index nguyên liệu (0, 1) (19*6)
    -   [114:133] Vị trí Robber 19 vị trí đặt (0, 1)
    -   [133:361]   Số trên các ô đất (0, 1) (2 -> 12)*19

    -   [361:415]   Các cảng (Cây, Gạch, Cừu, Lúa, Đá, 3:1) 9 cảng *6
    -   [415:420]   Tài nguyên ngân hàng Dạng 0, 1
    -   [420]   Thẻ dev bank Dạng 0, 1
    -   [421:629]  Thông tin cá nhân
        - [0:5]: Tài nguyên
        - [5:10]: Thẻ dev
        - [10]: Điểm của người chơi
        - [11:83]: Đường: 72 đường, (0, 1)
        - [83:137]: Nhà: 54 điểm đặt nhà (0, 1)
        - [137:191]: Thành phố: 54 điểm đặt(0, 1)
        - [191]: Số thẻ knight đã dùng (sl)
        - [192]: Con đường dài nhất (sl)
        - [193:208]: Tỉ lệ trao đổi với Bank(với mỗi nguyên liệu, lần lượt là tỉ lệ 2, 3, 4. có 5 nguyên liệu) (0, 1)

    * Thông tin người chơi khác: [629:814], [814:999], [999:1184]
        -  [0]: Tổng tài nguyên(sl)
        -  [1]: Tổng số thẻ dev(sl)
        -  [2]: Điểm (sl)
        -  [3:75]: Đường
        -  [75:129]: Nhà
        -  [129:183]: Thành phố
        -  [183]: Số thẻ knight đã dùng
        -  [184]: Con đường dài nhất

    -   [1184:1188]: Danh hiệu quân đội mạnh nhất (0, 1) (4 người, người đang chơi là index 0)
    -   [1188:1192]: Danh hiệu con đường dài nhất (0, 1) (4 người)
    -   [1192:1203]: Tổng xx (0, 1) (2 -> 12)
    -   [1203]: Nguyên liệu còn lại có thể lấy ở đầu game (sl)
    -   [1204:1258]: Điểm đặt thứ nhất
    -   [1258]: Số tài nguyên phải bỏ do bị chia
    -   [1259:1263]: Đang dùng thẻ dev gì
    -   [1263]: Số lần dùng thẻ dev
    -   [1264:1268]: Loại thẻ dev được sử dụng trong turn hiện tại
    -   [1268:1273]: Số nguyên liệu còn lại ở trong kho
    -   [1273:1278]: Số nguyên liệu còn lại ở trong kho người chơi
    -   [1278:1291]: Các phase, gồm 13 phase 0 -> 12, phase 12 là phase chọn lấy nguyên liệu từ kho
    -   [1291:1296]: Tài nguyên đưa ra trong trade offer để trade với bank
    -   [1296]: EndGame


## :globe_with_meridians: ENV_state

        -   [0:19] Tài nguyên trên các ô đất
        -   [19] Vị trí Robber
        -   [20:39]   Số trên các ô đất
        -   [39:48]   Các cảng
        -   [48:53]   Tài nguyên ngân hàng
        -   [53:58]   Thẻ dev bank
        -   [58:100]  Thông tin người chơi 0

            - [0:5] Tài nguyên
            - [5:10] Tài nguyên
            - [10] Điểm
            - [11:26] Tài nguyên
            - [26:31] Tài nguyên
            - [31:35] Tài nguyên
            - [35] Số thẻ Knight đã dùng
            - [36] Con đường dài nhất 
            - [37:42] Tỉ lệ trao đổi với bank

        -   [100:142] Thông tin người chơi 1
        -   [142:184] Thông tin người chơi 2
        -   [184:226] Thông tin người chơi 3

        -   [226] Danh hiệu quân đội mạnh nhất
        -   [227] Danh hiệu con đường dài nhất
        -   [228] Tổng xúc xắc
        -   [229] Phase
        -   [230] Turn
        -   [231] Điểm đặt thứ nhất
        -   [232] Số tài nguyên trả do bị chia
        -   [233] Đang dùng thẻ dev gì
        -   [234] Số lần sử dụng thẻ dev

        -   [235:239] Loại thẻ dev được sử dụng trong turn hiện tại
        -   [239:244] Lượng nguyên liệu còn lại khi bị chia đầu game
        -   [244] Người chơi đang action(không hẳn là người chơi chính)
        -   [245:249] Số nguyên liệu đã lấy trong turn đầu game
        -   [249:254] Tài nguyên đưa ra trong trade offer
        -   [254:259] Tài nguyên yêu cầu trong trade offer
        -   [254:274] Tài nguyên trong kho dự trữ của người chơi
        -   [184:226] Thông tin người chơi 3
        -   [280] End Game

# Thông tin khác
        KNIGHT: 14
        BUILD ROAD* 2
        YEAR_OF_PLENTY * 2
        MONOPOLY * 2
        VICTORY_POINT * 5
        DESERT: 1
        lumber* 4
        brick * 3
        sheep * 4
        grain * 4
        ore * 3