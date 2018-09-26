#modules
import modules

str = 'come si chiama Un gruppo di pesci'
str = str.lower()

# modules.takeScreenShot()

params = str.split(' ')
params = modules.removeArticloli(params)
params = modules.removepPreposizioni(params)
params = modules.removeAvverbi(params)

print params

#
base_url = 'https://www.google.it/search?q='
params = '%20'.join(params)
url = base_url + params

# modules.openChrome(url)
# print url
