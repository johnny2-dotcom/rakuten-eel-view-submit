import eel
import desktop
import api

app_name="html"
end_point="index.html"
size=(2000,700)

@ eel.expose
def search_item(keyword):
    api.search_item(keyword)

@ eel.expose
def max_min_price(keyword_b):
    api.max_min_price(keyword_b)

@ eel.expose
def ranking_item(genreId):
    api.ranking_item(genreId)

    
desktop.start(app_name,end_point,size)