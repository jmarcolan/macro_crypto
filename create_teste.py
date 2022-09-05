import captador_image as cp
import detectamdo_objetos as do
import mouse_driver as md
import time
def teste_1():
    im_rgb = cp.snapshot()
    saida = do.get_local_click(im_rgb)
    md.scrola_mouse_house(saida, True)
    for i in md.scrola_mouse_house(saida,True):
        print("foi")
    
    print("foi")
    # saida = do.detecta_multiplos_objetos(img,template1, 0.90)


if __name__ == "__main__":
    teste_1()