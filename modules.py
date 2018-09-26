import webbrowser
import vocabolario
import pyscreenshot as ImageGrab

from PIL import Image
from pytesseract import image_to_string


def takeScreenShot():
    im = ImageGrab.grab(bbox=(230, 200, 800, 400))
    im.save('./screenshots/screen.png')
    # im.show()
    return


def imageToText():
    text = image_to_string(Image.open('./screenshots/screen.png'))
    return text


def removeArticloli(params):
    articoli = vocabolario.articoli
    return [x for x in params if x not in articoli]


def removepPreposizioni(params):
    preposizioni = vocabolario.preposizioni
    return [x for x in params if x not in preposizioni]


def removeAvverbi(params):
    avverbi = vocabolario.avverbi
    return [x for x in params if x not in avverbi]


def openChrome(url):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    return
