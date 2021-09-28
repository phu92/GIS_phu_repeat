FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdaaaaafge'

RUN git clone -b test --single-branch https://github.com/phu92/GIS_phu_repeat

WORKDIR /home/GIS_phu_repeat
RUN echo "SECRET_KEY=django-insecure-nlz1_pthlx#p%x&bh-_j2g@jh$2rx5$=v@ja(o7$@1%_!t85$_" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=GIS_phu_repeat.settings.deploy && python manage.py migrate --settings=GIS_phu_repeat.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GIS_phu_repeat.settings.deploy GIS_phu_repeat.wsgi --bind 0.0.0.0:8000"]