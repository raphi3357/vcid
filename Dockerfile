FROM python:slim

RUN useradd monitoring

WORKDIR /home/monitoring

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY monitoring.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP monitoring.py

RUN chown -R monitoring:monitoring ./
USER monitoring

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]