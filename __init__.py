#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template
import datetime
import requests
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)
@app.route("/DVB/<Ort>/<station>/")
def index(Ort,station): 
       url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort={0}&hst={1}".format(Ort,station)
       response = requests.get(url)
       HTL = json.loads(response.content)  
       linie = HTL[0]
       linie2 = HTL[1]
       linie3 = HTL[2]
       linie4 = HTL[3]
                                         
       return render_template('base.html',linie = linie,linie2 = linie2,linie3 = linie3,linie4 = linie4)
@app.route("/Air")
def Air():
       form_data = {"ctl00$Inhalt$StationList":"114", "ctl00$Inhalt$BtnAnzeigen": "Anzeigen"}
       url = "https://www.umwelt.sachsen.de/umwelt/infosysteme/luftonline/Uebersicht.aspx"
       csrf_ids = ["__VIEWSTATEGENERATOR", "__EVENTVALIDATION", "__VIEWSTATE"]

       client = requests.session()

       form = client.get(url)
       form_soup = BeautifulSoup(form.content, 'html.parser')
       for csrf_id in csrf_ids:
              value = form_soup.find("input", {"id": csrf_id }).get("value")
              form_data[csrf_id] = value

       table = client.post(url, data=form_data)
       table_soup = BeautifulSoup(table.content, 'html.parser')
       #print(table_soup.prettify())
       data = table_soup.find_all('tr')[1].get_text()

       print(data[21:])
                                         
       return render_template('base2.html',data = data)
if __name__ == "__main__":
   #app.run(host='localhost', port=80, debug=True)
   app.run()
# import os

# from flask import Flask
# import requests
# import json
# from flask import render_template

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
    
#     # a simple page that says hello
    
#     @app.route('/DVB/<string:Ort>/<string:Station>')
#     def hello(Ort,Station): 
#        url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort={0}&hst={1}".format(Ort,Station)
#        print(url)

#        response = requests.get(url)

#        HTL = json.loads(response.content)
 

#        linie = HTL[0]
#        linie2 = HTL[1]
#        linie3 = HTL[2]
#        linie4 = HTL[3]

#       # HTL = HTL['list'][0]['main']['humidity']

       

#     #weather_Temp.round(2)

#     #weather_Temp = math.ceil(weather_Temp)

    
#        return render_template('base.html', linie = linie,linie2 = linie2,linie3 = linie3,linie4 = linie4)

#     from . import db
#     db.init_app(app)
#     from . import auth
#     app.register_blueprint(auth.bp)
#     return app
