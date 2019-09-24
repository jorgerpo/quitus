FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
  
USER 0

SHELL ["/bin/sh","-c"]

RUN mkdir -p /app && \
    addgroup --gid 1001 connectivity && \
    adduser --system --uid 1001 --gid 1001 connectivity 

COPY . /tmp/src

RUN mkdir -p $HOME/.config/pip && cp /tmp/src/install/pip.conf $HOME/.config/pip/ && \
    pip install --no-cache-dir -r /tmp/src/install/requirements.txt

USER 1001

EXPOSE 8000

COPY ./app /app

# RUN find /app -type d -name "__pycache__" -exec rm -rf {} \;

WORKDIR /app/

ENV PYTHONPATH=/app

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload