FROM python:3.13.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
COPY packages ./packages

RUN pip install --upgrade pip

RUN pip install \
    --no-cache-dir \
    --timeout 5 \
    --retries 0 \
    -r requirements.txt \
    || (echo "PyPI unreachable → installing from local packages" && \
        pip install --no-cache-dir --no-index --find-links=packages -r requirements.txt)

COPY . .

EXPOSE 5000

CMD ["python","app.py"]