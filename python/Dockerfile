FROM library/python:3.6-stretch

WORKDIR /app

COPY requirements.txt  .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "main.py"]