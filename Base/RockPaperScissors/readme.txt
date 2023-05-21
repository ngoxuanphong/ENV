Actions:[0: 3] Kéo, búa, bao
Env:
    [0: 2] loại người chơi đưa ra -1 0, 1, 2
    [2]: turn
    [3]: người đang chơi 0, 1,
        0 là người chơi 1
        1 là người chơi 2
    [4]: phase
        0 người chơi đưa ra
        1 người chơi xác nhận
    [5]: Người chiến thắng -1   0, 1
    [6]: end game?

State:
    [0: 3]: Loại mình đưa ra
    [3: 6]: Loại player khác đưa ra
    [6]: Phase 
    [7]: End game chưa?
  *Nếu state == full 0: người chơi đưa ra action < 3

getValidActions:
    phase0: [0: 3] = 1
    phase1: [3] = 1--- xác nhận kết quả

stepEnv(env, action):
    player = env[4]
    if action < 3:
        Lưu lại
        env[4] = (env[4] + 1)%2
        if env[4] == 0:
            So sánh--> kết quả
            env[5] += 1

    if action = 3:
        env[4] += 1: đến lượt người chơi khác xác nhận
        if env[4] % 2 == 0:
            if env[6]: env[7] = 1 game kết thúc
            else: env[5] = 0
        
         


