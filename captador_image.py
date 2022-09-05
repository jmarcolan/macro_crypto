import cv2
import numpy as np
import pyautogui
# necessario para pegar toda a imagem
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import detectamdo_objetos as do
from matplotlib import pyplot as plt




def snapshot():
    img = pyautogui.screenshot()
    open_cv_image = np.array(img) 
    # Convert RGB to BGR 
    # open_cv_image = open_cv_image[:, :, ::-1].copy()
    im_rgb = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
    return im_rgb