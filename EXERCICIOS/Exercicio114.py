'''
Crie um codigo em Python que teste se um site esta acessivel ou nao.
'''
import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print(f'Site Off-Line')
except:
    print('Site INACESSIVEL')
else:
    print('Site OnLine')
    print(site.read())   # comando para ler o HTML do site
