import os


def check_graphics(game_name):
    BOOL_CHECK_GRAPHICS = True
    msg = []
    if os.path.exists(f'Base/{game_name}/_render_func.py') == 0:
        BOOL_CHECK_GRAPHICS = False
        msg.append('Không tồn tại file _render_func.py')
    
    return BOOL_CHECK_GRAPHICS, msg