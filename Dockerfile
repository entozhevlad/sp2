FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -qy gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Создание пользователя и назначение прав на директории
RUN useradd -rms /bin/bash sp && \
    chmod 777 /opt /run

WORKDIR /sp

COPY --chown=sp:sp . .

RUN pip install -r requirements.txt

USER sp

CMD ["gunicorn", "-b", "0.0.0.0:8001", "sp.wsgi:application"]
