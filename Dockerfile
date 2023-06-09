FROM python:3

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./app/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app/main.py" ]
