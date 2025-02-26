FROM python:3.12

WORKDIR /task

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirement.txt /task/requirement.txt
#キャッシュを無効
RUN pip install --no-cache-dir -r requirement.txt

COPY ./api /task

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]