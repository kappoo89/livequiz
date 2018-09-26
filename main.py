#modules
import modules

modules.takeScreenShot()
modules.imageToText()

# str = 'come si chiama Un gruppo di pesci'
str = modules.imageToText().encode('utf-8')
str = str.replace('\n', ' ')
str = str.lower()

params = str.split(' ')

params = modules.removeArticloli(params)
params = modules.removepPreposizioni(params)
params = modules.removeAvverbi(params)

base_url = 'https://www.google.it/search?q='
params = '%20'.join(params)
url = base_url + params

modules.openChrome(url)
print url
