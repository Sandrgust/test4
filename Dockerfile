FROM python:3.9
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py
RUN pip install --upgrade pip
COPY . ./home/
WORKDIR /home/
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
CMD [ "bash", "flask", "run"]
