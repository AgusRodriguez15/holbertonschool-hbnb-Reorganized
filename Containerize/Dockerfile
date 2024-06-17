FROM Python 3.12.3

WORKDIR /Containerize

COPY requirements.txt requirements.txt

COPY . .

RUN pip install --no-cahce-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]