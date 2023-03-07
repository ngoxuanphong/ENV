Đã dùng 83% bộ nhớ … Bạn có thể giải phóng bộ nhớ hoặc mua thêm bộ nhớ cho Drive, Gmail và Google Photos.
## :dart: Báo cáo MachiKoro
1.   `Tốc độ chạy`
      - **1000 Game**: 
      - **1000 Game full numba**: 
      - **10000 Game**: 

2. `Chuẩn form`: **Đã test**
3. `Đúng luật`: **Đã check**
4. `Không bị loop vô hạn`: **Đã test** với 1000000 ván
5. `Tốc độ chạy các hàm con mà người chơi dùng`: 1000game: 
6. `Số ván check_vic > victory_thật`: chạy 10000 ván thì check_victory = check_winner = 
7. `Giá trị state, action`:
9. `Tối thiểu số lần truyền vào player`: 

## :globe_with_meridians: ENV_state
*   [0:396] **Thông tin các người chơi (coin, số lượng thẻ mỗi loại)**: (coin, is_police, typy_bag(4),    coin_bribe, number_smuggle_card, number_bribe_card_in_bag) => 9; 15*6: thẻ hối lộ done, thẻ done, thẻ hối lộ trong túi, thẻ trong túi, thẻ bỏ đi, thẻ trên tay => 90 => tổng mỗi người chơi 99 thông tin
*   [396:582] **thẻ bài ở chồng bài úp, có giá trị từ 0 - 15, trong đó 0 đại điện cho ko có thẻ, còn các thẻ còn lại có giá trị như dưới**
NORMAL_CARD = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
                        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                        6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                        7, 8, 8, 8, 8, 8])

ROYAL_CARD = np.array([ 9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15])

*   [582:707] **thẻ bài ở chồng bài lật bên trái, có giá trị từ 0 - 15, trong đó 0 đại điện cho ko có thẻ**
*   [707:832] **thẻ bài ở chồng bài lật bên phải, có giá trị từ 0 - 15, trong đó 0 đại điện cho ko có thẻ**

*   [832:892] **thẻ mà người chơi bỏ đi trong lượt ( được đặt ở trong chồng bài lật trái và lật phải)**
*   [892:896] **4 vị trí, thể hiện người chơi nào đang bị kiểm tra**
*   [896] **id người chơi đang action**
*   [897] **số lần đổi cảnh sát trưởng**
*   [898] **số người đã bị sherrif kiểm tra trong lượt**
*   [899] **check end**
*   [900] **phase game**





**Total env_state length: 901**
## :bust_in_silhouette: P_state
*   [0:99]: **Thông tin của người chơi chính**:
        0: player coin  : số coin đang có
        1: is_police    : có phải sheriff hay ko
        [2 : 6]: type_in_bag    : loại tài nguyên được khai báo trong túi khi đi chợ
        6: coin_bride           : số coin người chơi hối lộ sheriff
        7: number_smuggle       : số thẻ buôn lậu thành công của người chơi
        8: number_card_bride_bag:  số thẻ trong túi đi chợ người chơi mang ra hối lộ
        -90:-75: card_done_bride: thẻ người chơi đã buôn thành công đem ra hối lộ
        -75:60: card_done       : thẻ người chơi đã buôn thành công
        -60:-45: card_in_bag_bride: thẻ trong túi đi chợ người chơi dùng để hối lộ
        -45:-30: card_in_bag    : thẻ trong túi đi chợ của người chơi
        -30:-15: card_bag_drop  : thẻ trong túi của người chơi bị sheriff tịch thu và đem bỏ
        -15: card_hand          : thẻ trên tay người chơi
                        
*   [99:183] **Thông tin 3 người chơi còn lại**
    #(coin, is_police, typy_bag(4), coin_bribe, number_smuggle_card, number_bribe_card_in_bag) => 9 vị trí
    #thẻ done hối lộ: 15 vị trí, thẻ done chính ngạch của người chơi: 4 vị trí => 19 vị trí
    => 28*3 = 84 vị trí

*   [183:273]:   **Thông tin 6 thẻ đầu tiên ở chồng bài lật trái, cứ 15 vị trí sẽ có 1 vị trí là 1 nếu còn thẻ, nếu ko có thẻ tương ứng thì cả 15 giá trị là 0**:
ví dụ: chồng bài lật còn 2 thẻ thì chỉ có 2 vị trí là 1 lần lượt ở đoạn 183-198 và 198-213
*   [273:363]:   **Thông tin 6 thẻ đầu tiên ở chồng bài lật phải, cứ 15 vị trí sẽ có 1 vị trí là 1 nếu còn thẻ, nếu ko có thẻ tương ứng thì cả 15 giá trị là 0**:

*   [363:408]:   **số lượng các loại thẻ mà các người chơi còn lại đã bỏ ra trong lượt (các thẻ bị bỏ vào chồng bài lật**:
*   [408]:  **số lần đổi cảnh sát trưởng**
*   [409]:  **check end**

      

*   [410:421]:   **mảng biểu diễn phase của game**:
*   [421:466]:   **Các thẻ người chơi khác buôn thành công trong game**: Chỉ khác 0 khi game kết thúc, còn lại luôn bằng 0


**Total: player state length = 466 **

## :video_game: ALL_ACTION
Action	Mean
0	bỏ thẻ apple
1	bỏ thẻ cheese
2	bỏ thẻ bread
3	bỏ thẻ chicken
4	bỏ thẻ peper
5	bỏ thẻ mead
6	bỏ thẻ silk
7	bỏ thẻ crossbow
8	bỏ thẻ green_apple
9	bỏ thẻ gouda_cheese
10	bỏ thẻ rye_bread
11	bỏ thẻ royal_rooster
12	bỏ thẻ golden_apple
13	bỏ thẻ bleu_cheese
14	bỏ thẻ pump_bread
15	Không bỏ thẻ nữa
16	Lấy thẻ chồng bài rút
17	Lấy thẻ chồng bài lật trái
18	Lấy thẻ chồng bài lật phải
19	Trả thẻ vào chồng bài lật trái
20	Trả thẻ vào chồng bài lật phải
21	bỏ thẻ apple vào túi
22	bỏ thẻ cheese vào túi
23	bỏ thẻ bread vào túi
24	bỏ thẻ chicken vào túi
25	bỏ thẻ peper vào túi
26	bỏ thẻ mead vào túi
27	bỏ thẻ silk vào túi
28	bỏ thẻ crossbow vào túi
29	bỏ thẻ green_apple vào túi
30	bỏ thẻ gouda_cheese vào túi
31	bỏ thẻ rye_bread vào túi
32	bỏ thẻ royal_rooster vào túi
33	bỏ thẻ golden_apple vào túi
34	bỏ thẻ bleu_cheese vào túi
35	bỏ thẻ pump_bread vào túi
36	Không bỏ thẻ vào túi nữa
37	Khai báo hàng là apple
38	Khai báo hàng là cheese
39	Khai báo hàng là bread
40	Khai báo hàng là chicken
41	Kiểm tra người đầu tiên cạnh mình
42	Kiểm tra người thứ 2 cạnh mình
43	Kiểm tra người thứ 3 cạnh mình
44	Không hối lộ coin nữa
45	Hối lộ thêm 1 coin
46	hối lộ thẻ apple done
47	hối lộ thẻ cheese done
48	hối lộ thẻ bread done
49	hối lộ thẻ chicken done
50	hối lộ thẻ peper done
51	hối lộ thẻ mead done
52	hối lộ thẻ silk done
53	hối lộ thẻ crossbow done
54	hối lộ thẻ green_apple done
55	hối lộ thẻ gouda_cheese done
56	hối lộ thẻ rye_bread done
57	hối lộ thẻ royal_rooster done
58	hối lộ thẻ golden_apple done
59	hối lộ thẻ bleu_cheese done
60	hối lộ thẻ pump_bread done
61	Không hối lộ thẻ done nữa
62	hối lộ thẻ apple trong túi
63	hối lộ thẻ cheese trong túi
64	hối lộ thẻ bread trong túi
65	hối lộ thẻ chicken trong túi
66	hối lộ thẻ peper trong túi
67	hối lộ thẻ mead trong túi
68	hối lộ thẻ silk trong túi
69	hối lộ thẻ crossbow trong túi
70	hối lộ thẻ green_apple trong túi
71	hối lộ thẻ gouda_cheese trong túi
72	hối lộ thẻ rye_bread trong túi
73	hối lộ thẻ royal_rooster trong túi
74	hối lộ thẻ golden_apple trong túi
75	hối lộ thẻ bleu_cheese trong túi
76	hối lộ thẻ pump_bread trong túi
77	Không hối lộ thẻ trong túi nữa
78	Kiểm tra hàng
79	Cho qua
80	Bỏ thẻ tịch thu vào bên trái
81	Bỏ thẻ tịch thu vào bên phải