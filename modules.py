import webbrowser
import vocabolario
import pyscreenshot as ImageGrab


def takeScreenShot():
    im = ImageGrab.grab(bbox=(0, 0, 510, 510))
    im.save('./screenshots/test.png')
    return


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
