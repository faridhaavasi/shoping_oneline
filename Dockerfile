FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD {"python", "manage.py","runserver","8000"}

EXPOSE 8000
