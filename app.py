from flask import Flask,render_template, request, redirect    # сперва подключим модуль
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,FileField,IntegerField,DateField
from wtforms.validators import InputRequired, Email
import re
import pandas as pd
import requests
import openpyxl
import numpy as np
from datetime import timedelta


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






with app.app_context():
  data_all = pd.read_excel('Mondi.xlsx', index_col=None, header=0)
  result = {'number': np.arange(len(data_all['cloud'])*24)}
  result = pd.DataFrame(result)
  names_array = ['Tmean','Tmax','Tmin','humidity','v','Precipitation','cloud']

  a = np.empty(24)
  array_24 = []
  one_array = data_all['date_to_model'].to_numpy()
  for i in range(len(one_array)):
    date_hour = [str(data_all['date_to_model'][i] + timedelta(hours=k)) for k in range(len(a))]
    array_24 = np.append(array_24,date_hour)


  result['date_to_model'] = array_24

  a = np.empty(24)
  array_24 = []

  for j in names_array:
    a = np.empty(24)
    array_24 = []
    one_array = data_all[j].to_numpy()
    for i in range(len(one_array)):
      if one_array[i]!= '?*':
        a.fill(one_array[i])
        array_24 = np.append(array_24,a)
      else:
        a.fill(10)
        array_24 = np.append(array_24,a)

    result[j] = array_24


  print(result)





app.run(port=5000)    # запустим сервер на 8000 порту!