FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -qy gcc libjpeg-dev libxslt-dev libpq-dev \
    libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -rms /bin/bash sp && \
    mkdir -p /sp /var/log/sp /var/run/sp && \
    chown -R sp:sp /sp /var/log/sp /var/run/sp && \
    chmod 777 /opt /run

WORKDIR /sp

COPY --chown=sp:sp . .

RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

USER sp

CMD ["gunicorn", "-b", "0.0.0.0:8001", "sp.wsgi:application"]
