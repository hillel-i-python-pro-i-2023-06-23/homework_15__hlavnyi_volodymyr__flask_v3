FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV AM_I_IN_A_DOCKER_CONTAINER True

ARG USER=user

RUN useradd --system ${USER}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./app.py app.py
COPY --chown=${USER} ./application application

USER ${USER}

ENTRYPOINT ["flask", "run"]