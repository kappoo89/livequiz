import webbrowser
import vocabolario
import cv2
import os
import pytesseract

import pyscreenshot as ImageGrab
from PIL import Image


def takeScreenShot():
    im = ImageGrab.grab(bbox=(0, 25, 495, 900))
    im.save('./screenshots/screen.png')
    # im.show()
    return


def preprocessImage():
    image = cv2.imread('./screenshots/screen.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    filename = './screenshots/gray.png'
    # filename = './screenshots/{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    return


def imageToText():
    tessdata_dir_config = r'--tessdata-dir "/usr/local/Cellar/tesseract/3.05.02/share/tessdata"'
    text = pytesseract.image_to_string(
        Image.open('./screenshots/gray.png'),
        lang='ita',
        config=tessdata_dir_config)
    print(text)

    # return text


# def removeArticloli(params):
#     articoli = vocabolario.articoli
#     return [x for x in params if x not in articoli]
#
#
# def removepPreposizioni(params):
#     preposizioni = vocabolario.preposizioni
#     return [x for x in params if x not in preposizioni]
#
#
# def removeAvverbi(params):
#     avverbi = vocabolario.avverbi
#     return [x for x in params if x not in avverbi]
#
#
def openChrome(url):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    return
