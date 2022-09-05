import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_rectangle_heros(img):
#     img = cv2.imread('./teste/foto_heros_menu_croped.bmp')
    template = cv2.imread('./menu/lado_direito_normal.bmp')
    img, saida_d, _ = detecta_multiplos_objetos(img, template)
    template2 = cv2.imread('./menu/lado_esquerdo_normal.bmp')
    img, saida_s, _ = detecta_multiplos_objetos(img, template2, 0.94)
    def transforma_xyhw(y_i):
        y = y_i[1][0][1]
        h = y_i[1][1][1] - y_i[0][0][1]
        x = y_i[0][0][0]
        w = y_i[1][1][0] - y_i[0][0][0]
        return x,y,h,w    
    
    s = zip(saida_s,saida_d)
    ls = list(map(transforma_xyhw, s))
    
    # tem um template diferente
    template1 = cv2.imread('./menu/lado_direito.bmp')
    img, saida_d, _ = detecta_multiplos_objetos(img, template1, 0.94)
    template1 = cv2.imread('./menu/lado_esquerdo_selecionado.bmp')
    img, saida_s, _ = detecta_multiplos_objetos(img, template1, 0.94)
    s = zip(saida_s,saida_d)
    ls_s = list(map(transforma_xyhw, s))

    for l in ls_s:
        ls.append(l)

    return ls

def crop_image(img, x,y,h,w):
    clone = img.copy()
    return clone[ y:y+h, x:x+w]


def get_heros_from_image(img):
    h_ret = get_rectangle_heros(img)
    ls = []
    for r in h_ret:
        im_c = crop_image(img, r[0], r[1], r[2], r[3])
        ls.append((im_c,  (r[0], r[1], r[2], r[3])))
    return ls


def detectando_objeto(img, template):
    newImage = img.copy()
    h, w, chanels  = template.shape
    meth = "cv2.TM_CCORR_NORMED"
    method = eval(meth)
    res = cv2.matchTemplate(newImage,template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(newImage,top_left, bottom_right, 255, 2)
    
    
    return (newImage, top_left, bottom_right)


def detecta_multiplos_objetos(img, template, trheshold =0.9):
    saida = []
    (tH, tW) = template.shape[:2]
    imageGray = img # cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    templateGray = template #cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray,
                           cv2.TM_CCOEFF_NORMED)
    
#     trheshold = 0.9
    (yCoords, xCoords) = np.where(result >= trheshold)
    clone = img.copy()
    print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
    # loop over our starting (x, y)-coordinates
    for (x, y) in zip(xCoords, yCoords):
        # draw the bounding box on the image
        cv2.rectangle(clone, (x, y), (x + tW, y + tH),(255, 0, 0), 3)
        saida.append(((x,y), (x + tW, y + tH)))
        
    r_encontrado_algo = len(saida) != 0 

    return clone, saida, r_encontrado_algo



def get_retorno_dungeon(img):
    template2 = cv2.imread('./menu/back_image.bmp')
    saida = detecta_multiplos_objetos(img,template2, 0.80)
    return saida


def r_house_blocked(img):
    template2 = cv2.imread('./bomber_stats/bomb_home_hability_block.bmp')
    saida = detecta_multiplos_objetos(img,template2, 0.80)
    return saida

def r_using_house(img):
    template1 = cv2.imread('./bomber_stats/bomb_home_using.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.80)
    return saida

def r_house_not_full(img):
    template1 = cv2.imread('./bomber_stats/bomb_home_not_full.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.93)
    return saida



def r_rest_on(img):
    template1 = cv2.imread('./bomber_stats/bomb_rest_on.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def r_rest_off(img):
    template1 = cv2.imread('./bomber_stats/bomb_rest_off.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def r_work_on(img):
    template1 = cv2.imread('./bomber_stats/bomb_work_on.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.95)
    return saida

def r_work_off(img):
    template1 = cv2.imread('./bomber_stats/bomb_work_on.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.95)
    return saida


def r_final_jogo(img):
    template1 = cv2.imread('./menu/new_map.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def get_local_click(img):
    template1 = cv2.imread('./menu/hero_click.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

# Hunt STATE
def qnt_sleping(img):
    template1 = cv2.imread('./bomber_stats/bomber_finish.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.80)
    template1 = cv2.imread('./bomber_stats/bomber_finish_1.bmp')
    saida1 = detecta_multiplos_objetos(saida[0],template1, 0.85)
    template1 = cv2.imread('./bomber_stats/bomber_finish_2.bmp')
    saida2 = detecta_multiplos_objetos(saida1[0],template1, 0.85)
    template1 = cv2.imread('./bomber_stats/bomber_finish_3.bmp')
    saida3 = detecta_multiplos_objetos(saida1[0],template1, 0.85)
    
    ls =[]
    for l in saida[1]:
        ls.append(l)
        
    for l in saida1[1]:
        ls.append(l)
        
    for l in saida2[1]:
        ls.append(l)
        
    for l in saida3[1]:
        ls.append(l) 
            
    r_encontrou = len(ls) != 0
    return saida2[0], ls, r_encontrou


# Get game state
def r_salon(img):
    template1 = cv2.imread('./menu/star_fase.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def r_hero_page(img):
    template1 = cv2.imread('./menu/hero_page.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def r_treasure_hunt(img):
    template1 = cv2.imread('./menu/bomb_working.bmp')
    saida = detecta_multiplos_objetos(img,template1, 0.90)
    return saida

def test_4():
    pass
    # im_rgb = cp.snapshot()
    # print("salon", r_salon(im_rgb)[2])
    # print("hero page",r_hero_page(im_rgb)[2])
    # print("treasure hunte", r_treasure_hunt(im_rgb)[2] )



def detect_id(img, img_id):
    saida = detecta_multiplos_objetos(img, img_id, 0.95)
    return saida

def test_3():
    template1 = cv2.imread('hero_common_houseBlocked_restON_workOFF.jpg')
    print("house block", r_house_blocked(template1)[2])
    print("house using", r_using_house(template1)[2])
    print("house not full", r_house_not_full(template1)[2])
    print("rest on" , r_rest_on(template1)[2])
    print("rest off", r_rest_off(template1)[2])
    print("work on" ,r_work_on(template1)[2])
    print("work off" ,r_work_off(template1)[2])

    cv2.imshow("Before NMS", template1)
    cv2.waitKey(0)

    template2 = cv2.imread('hero_legend_houseON_restOFF_workOFF.jpg')
    print("legend")
    print("house block", r_house_blocked(template2)[2])
    print("house using", r_using_house(template2)[2])
    print("house not full", r_house_not_full(template2)[2])
    print("rest on" , r_rest_on(template2)[2])
    print("rest off", r_rest_off(template2)[2])
    print("work on" ,r_work_on(template2)[2])
    print("work off" ,r_work_off(template2)[2])

    # # saida[2/]
    # print(saida[2])
    cv2.imshow("Before NMS", template2)
    cv2.waitKey(0)



def teste_1():
    img = cv2.imread('./teste/foto_imagem_inicial.bmp')
    template = cv2.imread('./menu/bomb_menu.bmp')

    img, top, bot = detectando_objeto(img, template)

    cv2.imwrite("detectando_heros_menu.jpg", img)

def teste_2():
    img = cv2.imread('./teste/foto_heros_menu.bmp')
    template = cv2.imread('./bomber_stats/bomb_work_on.bmp')

    img, saida = detecta_multiplos_objetos(img, template)
    cv2.imshow("Before NMS", img)
    cv2.waitKey(0)

def teste_4():
    pass

if __name__ == "__main__":
    test_3()

# x:-1140 y:561
# x:-1140 y409