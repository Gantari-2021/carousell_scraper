import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def kamera_populer ():
    html_doc = requests.get( 'https://id.carousell.com/categories/photography-6/' )
    soup = BeautifulSoup( html_doc.text, 'html.parser' )

    kamera_populer = soup.find(attrs={'class':'D_J'})

    titles = kamera_populer.findAll(attrs={'class':'D_oS'})

    return render_template('index.html', titles=titles)



if __name__=='__main__':
    app.run(debug=True)

