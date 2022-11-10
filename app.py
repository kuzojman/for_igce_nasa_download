from flask import Flask,render_template, request, redirect    # сперва подключим модуль
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,FileField,IntegerField,DateField
from wtforms.validators import InputRequired, Email
import re
import pandas as pd
import requests
import openpyxl

class get_values_from_form(FlaskForm):
  long_grad = StringField("long_grad")
  long_min = StringField("long_min")
  lat_grad = StringField("lat_grad")
  lat_min = StringField("lat_min")
  variables = StringField("variables")
  date_begin = StringField("date_begin")
  date_end = StringField("date_end")




app = Flask(__name__)      # объявим экземпляр фласка
app.secret_key = "randomstring"


@app.route("/")
def template():
  return  render_template('main.html') # рендерим шаблон, передавая переменные


@app.route("/get_something", methods=["GET", "POST"])
def get_something():
  form = get_values_from_form()
  if request.method == "POST":
    long_grad = request.form.get("long_grad")
    long_min = request.form.get("long_min")
    lat_grad = request.form.get("lat_grad")
    lat_min = request.form.get("lat_min")
    variables = request.form.getlist("variables")
    date_begin = request.form.get("date_begin")
    date_end = request.form.get("date_end")

    url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?'
    parametres_all = {'parameters': (',').join(variables),
                      'community': 'SB',
                      'longitude': int(long_grad)+int(long_min)/60,
                      'latitude':int(lat_grad)+int(lat_min)/60,
                      'start':date_begin.replace('-', ''),
                      'end':date_end.replace('-', ''),
                      'format':'JSON',
                      'site-elevation':50}
    r = requests.get(url, params=parametres_all)

    data_json = r.json()
    try:
      records = data_json['properties']['parameter']

      df = pd.DataFrame.from_dict(records)
      df.to_excel("output.xlsx")
      return redirect('/')
    except:
      return data_json["messages"][0]
    #return redirect('/')





app.run(port=5000)    # запустим сервер на 8000 порту!