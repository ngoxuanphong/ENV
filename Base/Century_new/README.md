##   Thông tin quan trọng:
      - cách xác định loại thẻ action dựa trên mã thẻ: mã thẻ có 9 số, 4 số đầu là số tài nguyên người chơi cần bỏ ra khi dùng thẻ, 4 số kế tiếp là số tài nguyên người chơi nhận được khi dùng thẻ, số cuối cùng là số lần dùng nâng cấp token của thẻ.
      Quy ước phase: 
            * phase1: chọn mua thẻ (6 thẻ top và 5 thẻ point) hay đánh thẻ (thẻ trên tay) hay nghỉ ngơi (11 action mua, 45 action đánh, 1 action nghỉ)
            * phase2: nếu mua thẻ top, chọn token để vào các thẻ trước thẻ mình mua (4 action)
            * phase3: nếu đánh thẻ, chọn xem có thực hiện action của thẻ tiếp ko (2action, 1 cái là ko, 1 cái trùng vs action dùng thẻ)
            * phase4: trả token dư thừa (4 action) (trùng phase 2)
            * phase5: chọn loại tài nguyên để nâng cấp    

##  :video_game: Action
      0 | Nghỉ ngơi
      1 | mua thẻ thường 1
      2 | mua thẻ thường 2
      3 | mua thẻ thường 3
      4 | mua thẻ thường 4
      5 | mua thẻ thường 5
      6 | mua thẻ thường 6
      7 | mua thẻ điểm 1
      8 | mua thẻ điểm 2
      9 | mua thẻ điểm 3
      10 | mua thẻ điểm 4
      11 | mua thẻ điểm 5
      12 | dùng thẻ 000020000
      13 | dùng thẻ 000030000
      14 | dùng thẻ 000040000
      15 | dùng thẻ 000011000
      16 | dùng thẻ 000000100
      17 | dùng thẻ 000021000
      18 | dùng thẻ 000002000
      19 | dùng thẻ 000010100
      20 | dùng thẻ 000000010
      21 | dùng thẻ 200002000
      22 | dùng thẻ 200000100
      23 | dùng thẻ 300000010
      24 | dùng thẻ 300003000
      25 | dùng thẻ 300001100
      26 | dùng thẻ 400000200
      27 | dùng thẻ 400000110
      28 | dùng thẻ 500000020
      29 | dùng thẻ 500000300
      30 | dùng thẻ 010030000
      31 | dùng thẻ 020000200
      32 | dùng thẻ 020030100
      33 | dùng thẻ 020020010
      34 | dùng thẻ 030000300
      35 | dùng thẻ 030000020
      36 | dùng thẻ 030010110
      37 | dùng thẻ 030020200
      38 | dùng thẻ 001041000
      39 | dùng thẻ 001012000
      40 | dùng thẻ 001002000
      41 | dùng thẻ 002021010
      42 | dùng thẻ 002000020
      43 | dùng thẻ 002023000
      44 | dùng thẻ 002002010
      45 | dùng thẻ 003000030
      46 | dùng thẻ 000100200
      47 | dùng thẻ 000130100
      48 | dùng thẻ 000103000
      49 | dùng thẻ 000122000
      50 | dùng thẻ 000111100
      51 | dùng thẻ 000211300
      52 | dùng thẻ 000203200
      53 | dùng thẻ 110000010
      54 | dùng thẻ 201000020
      55 | dùng thẻ 000000002
      56 | dùng thẻ 000000003
      57 | bỏ token vàng
      58 | bỏ token đỏ
      59 | bỏ token xanh
      60 | bỏ token nâu
      61 | không dùng tiếp thẻ action
      62 | nâng cấp vàng lên đỏ
      63 | nâng cấp đỏ lên xanh
      64 | nâng cấp xanh lên nâu

##  :bust_in_silhouette: P_state
      [0:480] Thông tin người chơi: gồm 5 người chơi với thông tin từng người là (điểm, số thẻ đã mua, 4 vị trí thể hiện số lượng 4 loại token,45 vị trí cho 45 loại thẻ hành động down, 45 vị trí cho 45 loại thẻ hành động up)
      [480:534] Thông tin 6 thẻ action lật trên bàn: mỗi thẻ gồm 9 thuộc tính ((số lượng tài nguyên bỏ ra(4 vị trí), số lượng tài nguyên nhận(4 vị trí), số lần nâng cấp (1 vị trí)))
      [534:554] Thông tin token free có sẵn ở các thẻ lật trên bàn, chỉ xét 5 thẻ đầu
      
      [554:579] thông tin  5 thẻ điểm lật trên bàn: mỗi thẻ gồm 5 thuộc tính (số lượng tài nguyên bỏ ra(4 vị trí), điểm (1 vị trí))
      [579]: Số đồng bạc còn trên bàn
      [580]: Số đồng vàng còn trên bàn
      [581:587]: vị trí thẻ action người chơi mua (dùng khi người chơi mua thẻ cần đặt token)
      [587:632]: vị trí thẻ người chơi dùng gần nhất (dùng khi nâng cấp hoặc thẻ dùng được nhiều lần)
      [632]: trạng thái game kết thúc hay chưa
      [633:638]: phase của game, phase nào ứng với vị trí tương ứng có giá trị là 1
      [638:643]: Thứ tự bắt đầu game
      [643:679]: Các action cards có thể còn trong chồng action card
      [679:724]: Các thẻ điểm còn có thể còn trong chồng thẻ điểm
      [724:729]: Vị trí người chơi thực hiện tại so với người quan sát. Nếu là bản thân đang hành động thì giá trị tại 724 là 1
      [729]: số lượng token cần phải bỏ đi
      [730]: số lần upgrade còn lại

      Total length player_state: 731



#  :globe_with_meridians: Env_State
      [0:255] Thông tin người chơi: gồm 5 người chơi với thông tin từng người là (điểm, số thẻ đã mua, 4 vị trí thể hiện số lượng 4 loại token, 45 vị trí cho 45 loại thẻ hành động (giá trị 1 là sở hữu, -1 là đã dùng cần chờ nghỉ ngơi, 0 là không sở hữu))
      [255:309] Thông tin 6 thẻ action lật trên bàn, mỗi thẻ gồm 9 thuộc tính (#(số lượng tài nguyên bỏ ra(4 vị trí), số lượng tài nguyên nhận(4 vị trí), số lần nâng cấp (1 vị trí)))
      [309:329] Thông tin token free có sẵn ở các thẻ lật trên bàn, chỉ xét 5 thẻ đầu
      [329:354] thông tin  5 thẻ điểm lật trên bàn mỗi thẻ có 5 vị trí, 4 vị trí đầu là chi phí mua, vị trí sau cùng là điểm
      [354:397] chuỗi lưu trữ thứ tự các thẻ action sau khi xáo 
      [397:433] CHuỗi lưu trữ thứ tự các thẻ điểm sau khi xáo 
      [433] số lần người chơi đã nâng cấp khi dùng thẻ nâng cấp 
      [434] Thẻ người chơi định mua hoặc là thẻ người chơi vừa dùng
      [435]   Số token người chơi cần phải bỏ ra
      [436]  Số đồng bạc còn trên bàn chơi
      [437]   Số đồng vàng còn trên bàn chơi
      [438]   Action mà người chơi vừa thực hiện khi dùng action card
      [439]   Phase của game 
      [440]   Trạng thái game kết thúc hay chưa
      [441]   ID Người chơi được hành động
      [442:447]   Điểm khi bắt đầu của người chơi

## :station: Chức năng của các hàm
      * getActionSize() :trả ra tổng số lượng action của game
      * getAgentSize() : trả ra tổng số lượng người chơi trong một ván
      * getStateSize() : lấy độ dài của mảng thông tin mà người chơi được nhận mỗi lượt (state)
      * initEnv() : khởi tạo môi trường ván chơi (env_state)
      * getAgentState(env_state) : nhận vào thông tin môi trường, chuyển đổi thành thông tin của người chơi ở góc nhìn của người chơi (state)
      * getValidActions(player_state_origin) : nhận vào thông tin người chơi thấy được, trả ra các hành động người chơi được phép làm.
      * stepEnv(env_state, action): nhận vào thông tin môi trường và hành động của người chơi, trả ra môi trường mới sau khi người chơi hành động (env_state)
      * system_check_end(env_state) : nhận vào thông tin môi trường, kiểm tra xem ván chơi đã đến thời điểm kết thúc chưa
      * getReward(player_state) : nhận vào thông tin người chơi nhận được, trả ra giá trị có thể là -1, 0, 1 ứng với game chưa kết thúc, người chơi thua, người chơi thắng
      * check_winner(env_state) : nhận vào thông tin môi trường, trả ra vị trí của người chiến thắng trong danh sách người chơi
      * one_game_numba(p0, list_other, per_player, per1, per2, per3, p1, p2, p3): nhận vào các hàm chương trình chơi (người chơi) và dữ liệu tương ứng của từng chương trình. Thực hiện hết 1 ván chơi với các chương trình được truyền vào, trả ra ID của chương trình chiến thắng và biến dữ liệu của nó. Hàm này dùng khi các chương trình chạy được trong môi trường numba
      * n_games_numba(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2, p3): Hàm này dùng để chạy nhiều lần hàm one_game_numba, trả ra số lần thắng của chương trình cần kiểm tra và dữ liệu tương ứng của chương trình.
      * one_game_normal, n_games_normal tương tự với one_game_numba, n_games_numba nhưng các chương trình có thể hoạt động không nhất thiết phải là trong môi trường numba
      * getPredictState(state, action): nhận vào một state và một action có thể thực hiện được tương ứng với state đó, trả ra một mảng các state có thể nhận được và mảng xác suất tương ứng của từng state đó
      * get_Prob_State(arr_all_predict_state): Hàm này dùng bên trong hàm getPredictState, dùng để lọc trùng, tính xác suất xuất hiện của các state



