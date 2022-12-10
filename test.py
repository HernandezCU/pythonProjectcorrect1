import time 
size = 0
g_mode = 'grow'

def set_mode(size):
    global g_mode
    if size >= 170:
        mode = 'shrink'
        g_mode = mode
        print("change mode to shrink")
        return g_mode
    elif size <= 0:
        mode = 'grow'
        g_mode = mode
        print("change mode to grow")
        return g_mode
    elif size > 0 and size < 170:
        print("mode is still", g_mode)
        return g_mode


for i in range(0, 171):
    s_size = i
    s_mode = set_mode(s_size)
    print(size, s_mode)
    time.sleep(1)
