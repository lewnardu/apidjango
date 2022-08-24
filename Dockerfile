# image base
FROM python:3.7.3

# enviar  saída para o terminal sem buffer
ENV PYTHONUNBUFFERED 1

# criando pasta de trabalho no contêiner
# copiando o conteúdo do diretório atual para o diretório de trabalho
RUN mkdir /app
WORKDIR /app
ADD . /app

# instalação de pacotes necessários
RUN apt-get update -y \
    && apt-get install -y default-libmysqlclient-dev build-essential \
    && apt-get install -y nano \
    && apt-get install -y git

# instalação de requirements
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VITUAL_ENV/bin:$PATH"
#instalação do python
RUN python3 -m venv /opt/venv
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install --trusted-host pypi.python.org -r requirements.txt

#inicializar o env
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt install -y libpangocairo-1.0-0 \
    && apt install -y libcairo2-dev