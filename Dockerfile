FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/luwbe1/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=qvvz!^@_2!)rn0giae(im-m@ggz5)ksa88q*dt-xqfglvzq$e#" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

