import pyautogui, sys
import numpy as np 
import time 

def leva_mouse_meio_detecao(top_left, bottom_right):
    
    x_esquerda = -1920
    y_esquerda = 0 

    x_w = bottom_right[0] - top_left[0]
    s_x = np.random.uniform(low=top_left[0], high=(top_left[0] + x_w), size=(50,))

    x_h = bottom_right[1]- top_left[1]
    s_y = np.random.uniform(low=top_left[1], high=(top_left[1] + x_h), size=(50,))

    pyautogui.moveTo(s_x[0] + x_esquerda , s_y[0] + y_esquerda, 1, pyautogui.easeInBounce)

    # pyautogui.moveTo(top_left[0] - (top_left[0] - bottom_right[0])/2 + x_esquerda , 
    #                 top_left[1] - ( top_left[1] - bottom_right[1])/2 + y_esquerda)
    pyautogui.click()


    # pyautogui.moveTo(top_left[0] - (top_left[0] - bottom_right[0])/2 + x_esquerda , 
    #                 top_left[1] - ( top_left[1] - bottom_right[1])/2 + y_esquerda, 1.4, pyautogui.easeInBounce)
    # # pyautogui.click()


def click_scroll(top_left, bottom_right, qnt_scroll):
    x_esquerda = -1920
    y_esquerda = 0 

    x_w = bottom_right[0] - top_left[0]
    s_x = np.random.uniform(low=top_left[0], high=(top_left[0] + x_w), size=(50,))

    x_h = bottom_right[1]- top_left[1]
    s_y = np.random.uniform(low=top_left[1], high=(top_left[1] + x_h), size=(50,))

    x = s_x[0] + x_esquerda
    y = s_y[0] + y_esquerda + 150 
    pyautogui.moveTo(x ,y , 1, pyautogui.easeInBounce)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.scroll(qnt_scroll)

def add_scroll(qnt_scroll):
    pyautogui.scroll(qnt_scroll)


def scrola_mouse_house(saida, baixo):
    print(saida)
    
    sc_size = -350
    if not baixo:
        sc_size = 350
    
    if saida[2] == True:
        posi_objeto = saida[1]
        click_scroll(posi_objeto[0][0], posi_objeto[0][1], sc_size)
        curent_position = pyautogui.position()
        for i in range(7):
            time.sleep(0.6)
            for j in range(6):
                time.sleep(0.2)
                add_scroll(sc_size)
            
            curent_position = pyautogui.position()
            yield True

            pyautogui.moveTo(curent_position[0],curent_position[1] , 1, pyautogui.easeInBounce)
            pyautogui.click()

    else:
        print("n encontrou o objeto")