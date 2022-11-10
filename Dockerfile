FROM education_web_cite:25_08_2022

# install libs
#RUN apt-get update && apt-get install -y python3-dev build-essential

# RUN apt-get install -y texlive-full

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./ /app

CMD ["python", "bot.py"]