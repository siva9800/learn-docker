FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

RUN useradd -ms /bin/bash appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
