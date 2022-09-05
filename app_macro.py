import time
import cv2
import numpy as np
import pyautogui
from matplotlib import pyplot as plt
# necessario para pegar toda a imagem

import detectamdo_objetos as do
import captador_image as cp
import mouse_driver as md


from enum import Enum, auto

class Game_States(Enum):
    ERROR = auto()
    PAGE = auto()
    SALON = auto()
    HERO = auto()
    TREASURE = auto()


class Tresure_Stats(Enum):
    ERROR = auto()
    WORKING = auto()
    SLEPING = auto()
    END_MAP = auto()


class Treasure():
    def __init__(self) -> None:
        self.g_sate = Tresure_Stats.WORKING
    

    def _att_state(self, im_rgb):
        im_safe = im_rgb.copy()
        s = do.r_final_jogo(im_safe)
        s2 = do.qnt_sleping(im_safe)

        r_sleeping = len(s2[1]) >= 10
        r_end_game = s[2]
        r_working = not r_end_game and not r_sleeping


        if(r_working):
            self.g_sate = Tresure_Stats.WORKING

        if(r_end_game):
            self.g_sate = Tresure_Stats.END_MAP

        if(r_sleeping):
            self.g_sate = Tresure_Stats.SLEPING



    def run(self) -> None:
        r_looping = True
        while r_looping:
            im_rgb = cp.snapshot()
            self._att_state(im_rgb)

            if(self.g_sate == Tresure_Stats.WORKING ):
                print("WORKING")
                # Todo aleatorio volta para o treasure hunt;
                pass


            if(self.g_sate == Tresure_Stats.END_MAP ):
                # r_looping = False
                print("END MAP")

                self._press_next_map(im_rgb)


            if(self.g_sate == Tresure_Stats.SLEPING ):
                print("SLEEPING")
                r_looping = False

            time.sleep(5)
        
        self._press_return_button(im_rgb)
        print("return to lound")


    def _press_next_map(self, im_rgb):
        im_safe = im_rgb.copy()
        s = do.r_final_jogo(im_safe)
        posi_objeto = s[1][0]
        go_to_and_click(posi_objeto)
    
    def _press_return_button(self, img):
        s = do.get_retorno_dungeon(img)
        posi_objeto = s[1][0]
        go_to_and_click(posi_objeto)



class Salon_Stats(Enum):
    ERROR = auto()
    INITING = auto()
    WAITING = auto()
    HEROS = auto()

class Salon():
    def __init__(self) -> None:
        self.s_state = Salon_Stats.INITING 


    def run(self) -> None:
        pass


class Hero():
    def __init__(self) -> None:
        pass
    
    def run(self) -> None:
        pass




class Game():
    def __init__(self) -> None:
        self.g_state = Game_States.SALON

        self.treasure = Treasure()
        self.salon = Salon()
        self.hero = Hero()


    
    def _att_state(self, im_rgb):
        # print("salon", do.r_salon(im_rgb)[2])
        # print("hero page",do.r_hero_page(im_rgb)[2])
        # print("treasure hunte",do.r_treasure_hunt(im_rgb)[2] )
        if( do.r_salon(im_rgb)[2]):
            self.g_state =  Game_States.SALON
            return True

        if(do.r_treasure_hunt(im_rgb)[2]):
            self.g_state =  Game_States.TREASURE
            return True

        if( do.r_hero_page(im_rgb)[2]):
            self.g_state =  Game_States.HERO
            return True

        self.g_state = Game_States.ERROR 
        return False
        
        

    def run(self):
        im_rgb = cp.snapshot()
        ok = self._att_state(im_rgb)

        if(self.g_state == Game_States.ERROR ):
            pass

        if(self.g_state == Game_States.SALON ):
            self.salon.run()

        if(self.g_state == Game_States.HERO ):
            self.hero.run()

        if(self.g_state == Game_States.TREASURE ):
            self.treasure.run()





def get_parameter_for_bound_bov(y_i):
    y = y_i[0][1]
    h = y_i[1][1] - y_i[0][1]
    x = y_i[0][0]
    w = y_i[1][0] - y_i[0][0]
    return x,y,h,w  

def draw_rectangle_object_detect(im_rgb, ob_detected):
    s = get_parameter_for_bound_bov(ob_detected)
    cv2.rectangle(im_rgb, (s[0], s[1]),
                  (s[0] + s[3], s[1] + s[2]),
                  (255, 0, 0), 3)
    return im_rgb, ob_detected, s

    
def go_to_and_click(posi_objeto):
    curent_position = pyautogui.position()
    md.leva_mouse_meio_detecao(posi_objeto[0], posi_objeto[1])
    pyautogui.click()
    pyautogui.moveTo(curent_position[0],curent_position[1])

def go_novo_map(img):
    im_safe = img.copy()
    s = do.r_final_jogo(im_safe)
    r_encontrou_fim = s[2]
    curent_position = pyautogui.position()
    if r_encontrou_fim:
        posi_objeto = s[1][0]
        print(posi_objeto)
        md.leva_mouse_meio_detecao(posi_objeto[0], posi_objeto[1])
        pyautogui.click()
        pyautogui.moveTo(curent_position[0],curent_position[1])
        return True
    else:
        print("nao detectou fim")
        return False


if __name__ == "__main__":
    
    tr = Treasure()
    tr.run()
    # im_rgb = cp.snapshot()
    # go_novo_map(im_rgb)