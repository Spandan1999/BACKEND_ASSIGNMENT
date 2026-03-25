# Backend Data Pipeline (Docker Assignment)

## Overview

This project implements a containerized data pipeline with three services:

* **Flask Mock Server** – Provides customer data from JSON
* **FastAPI Pipeline Service** – Ingests data and stores in PostgreSQL
* **PostgreSQL** – Database for customer records

**Flow:**
Flask API → FastAPI ingestion → PostgreSQL → API response

---

## Tech Stack

* Python 3.13.2
* Flask
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker & Docker Compose

---

## How to Run

### Start services

```bash
docker compose up --build
```

### Test endpoints

Test mock server:

```bash
curl "http://localhost:5000/api/customers?page=1&limit=5"
```

Run ingestion:

```bash
curl -X POST http://localhost:8000/api/ingest
```

Test pipeline API:

```bash
curl "http://localhost:8000/api/customers?page=1&limit=5"
```

---

## Services

| Service           | Port | Description           |
| ----------------- | ---- | --------------------- |
| Flask Mock Server | 5000 | Customer data API     |
| FastAPI Pipeline  | 8000 | Ingestion & query API |
| PostgreSQL        | 5432 | Database              |

---

## Key Features

* Dockerized microservice architecture
* Data ingestion pipeline
* PostgreSQL persistence
* Pagination support
* Upsert logic
* Offline dependency installation for reliable builds

---

## Stop Services

```bash
docker compose down
```

---

## Author

**Spandan Satapathy**
Backend Developer | Node.js | Python | PostgreSQL | Docker
Experience building secure and scalable backend systems in government and fintech domains.
