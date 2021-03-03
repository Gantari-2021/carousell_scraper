import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/photography-6/')
soup = BeautifulSoup(html_doc.text, 'html.parser')

kamera_populer = soup.find(attrs={'class':'D_J'})
#print(kamera_populer)

titles = kamera_populer.findAll(attrs={'class':'D_oS'})
#print(titles)
#images = kamera_populer.findAll(attrs={'class':'D_jQ'})

for title in titles:
    #print(title.text)
    print(title.find('p',attrs={'class':'D_cp M_bJ D_cy M_bS D_cA M_bV D_cE M_bY D_cG M_ca D_cJ M_ce D_cM M_ch D_cP'}).text)

    #image
    print(title.find('div',attrs={'class':'D_pb'}).find('img'))

    #harga
    print(title.find('p',attrs={'class':'D_cp M_bJ D_cy M_bS D_cA M_bV D_cE M_bY D_cG M_ca D_cJ M_ce D_cL M_cg D_cO'}).text)


