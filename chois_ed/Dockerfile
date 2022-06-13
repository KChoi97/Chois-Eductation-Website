FROM python:3.9-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY chois_ed ./chois_ed

EXPOSE 8000

FROM prodcution as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .