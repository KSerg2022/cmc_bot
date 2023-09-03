FROM python:3.10


RUN apt-get update && apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /cmc_bot
WORKDIR /cmc_bot

EXPOSE 8081

RUN pip install -r /cmc_bot/requirements.txt

CMD python bot.py

#RUN adduser --disabled-password cmc-user
#
#USER cmc-user
