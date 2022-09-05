import detectamdo_objetos as do
import captador_image as cp
from matplotlib import pyplot as plt
import cv2
import json
import mouse_driver as md


def r_detecta_bomber(img, bomber):
    template = cv2.imread(bomber["img"]) 
    saida = do.detecta_multiplos_objetos(img,template, bomber["limiar"])
    if saida[2] == True:
        return True, saida
    else:
        return False, ()
    
def find_bomb(img, ls_bomber_av):  
    for i, bomber in enumerate(ls_bomber_av):
#         print("---------------")
#         print(bomber)
        encontrou, saida = r_detecta_bomber(img, bomber)
        if encontrou:
            bomber_encontrado = ls_bomber_av.pop(i)
            return True, bomber_encontrado, saida
    
    
    
    print("nao encontrado nenhum bomber")
    return False, {}, ()


def findo_box_heros(img, ls_bomber_disponiveis):
    l = do.get_heros_from_image(img)
    print(len(l))
    for image in l:
        img = image[0]
        b = find_bomb(img, ls_bomber_disponiveis)
        yield b
    return False, {}, ()
            
def get_next_bomber(ls_b):
    im_rgb = cp.snapshot()
    for b in findo_box_heros(im_rgb, ls_b):
        yield b

    saida = do.get_local_click(im_rgb)
    for i in md.scrola_mouse_house(saida,True):
        im_rgb = cp.snapshot()
        for b in findo_box_heros(im_rgb, ls_b):
            yield b
            
    return False, {}, ()
    