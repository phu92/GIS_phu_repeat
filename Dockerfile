FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/phu92/GIS_phu_repeat.git
WORKDIR /home/GIS_phu_repeat
RUN echo "SECRET_KEY=django-insecure-nlz1_pthlx#p%x&bh-_j2g@jh$2rx5$=v@ja(o7$@1%_!t85$_" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]