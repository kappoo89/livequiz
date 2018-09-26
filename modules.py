import webbrowser
import vocabolario


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
