import pygame
import sys
import time

def is_pressed(key):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #print(pygame.key.get_pressed())
    # 获取键盘状态
    key_state = pygame.key.get_pressed()
    #+特殊处理
    if key == '+':
        return key_state[pygame.K_KP_PLUS] or key_state[pygame.K_EQUALS]
    # 检测目标按键是否被按下
    return key_state[key_mapping[key]]

pygame.init()
#pygame.display.set_mode((100,200))
import pygame

key_mapping = {
    '-': pygame.K_MINUS,
    'backspace': pygame.K_BACKSPACE,
    'up': pygame.K_UP,
    'UP': pygame.K_UP,
    'down': pygame.K_DOWN,
    'DOWN': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'LEFT': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'RIGHT': pygame.K_RIGHT,
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9,
    'a': pygame.K_a,
    'A': pygame.K_a,
    'b': pygame.K_b,
    'B': pygame.K_b,
    'c': pygame.K_c,
    'C': pygame.K_c,
    'd': pygame.K_d,
    'D': pygame.K_d,
    'e': pygame.K_e,
    'E': pygame.K_e,
    'f': pygame.K_f,
    'F': pygame.K_f,
    'g': pygame.K_g,
    'G': pygame.K_g,
    'h': pygame.K_h,
    'H': pygame.K_h,
    'i': pygame.K_i,
    'I': pygame.K_i,
    'j': pygame.K_j,
    'J': pygame.K_j,
    'k': pygame.K_k,
    'K': pygame.K_k,
    'l': pygame.K_l,
    'L': pygame.K_l,
    'm': pygame.K_m,
    'M': pygame.K_m,
    'n': pygame.K_n,
    'N': pygame.K_n,
    'o': pygame.K_o,
    'O': pygame.K_o,
    'p': pygame.K_p,
    'P': pygame.K_p,
    'q': pygame.K_q,
    'Q': pygame.K_q,
    'r': pygame.K_r,
    'R': pygame.K_r,
    's': pygame.K_s,
    'S': pygame.K_s,
    't': pygame.K_t,
    'T': pygame.K_t,
    'u': pygame.K_u,
    'U': pygame.K_u,
    'v': pygame.K_v,
    'V': pygame.K_v,
    'w': pygame.K_w,
    'W': pygame.K_w,
    'x': pygame.K_x,
    'X': pygame.K_x,
    'y': pygame.K_y,
    'Y': pygame.K_y,
    'z': pygame.K_z,
    'Z': pygame.K_z,
    'space': pygame.K_SPACE,
    'SPACE':pygame.K_SPACE,
    'enter': pygame.K_RETURN,
    'ENTER': pygame.K_RETURN,
    'escape': pygame.K_ESCAPE,
    'ESCAPE': pygame.K_ESCAPE,
    'tab': pygame.K_TAB,
    'TAB': pygame.K_TAB
}

#pygame.mouse.set_visible(False)

'''
while True:
    #pygame.event.set_grab(True)
    time.sleep(0.1)
    if is_pressed('left'):
        print('left')
    if is_pressed('LEFT'):
        print('LEFT')
    if is_pressed('right'):
        print('right')
    if is_pressed('up'):
        print('up')
    if is_pressed('down'):
        print('down')
    if is_pressed('+'):
        print('+')
    if is_pressed('-'):
        print('-')
'''