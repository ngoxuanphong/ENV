# import Base.MachiKoro.env as env
# from CheckEnv import check_env
# print(check_env(env))

import os
for agent in os.listdir('Agent'):
    if os.path.exists(f'Agent/{agent}/Data'):
        for env_name in os.listdir(f'Agent/{agent}/Data'):
            path_old =f'Agent/{agent}/Data/{env_name}' 
            print(path_old.replace('0', '1'))
            os.rename(path_old, path_old.replace('0', '1'))
