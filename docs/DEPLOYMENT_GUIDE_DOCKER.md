# PALLAVI AI: Deployment Guide (Docker & Containerization)

## 1. Containerization Overview
PALLAVI AI is designed to run in a highly resilient, containerized environment using Docker and Kubernetes. This ensures environment parity across Development, Staging, and Production.

---

## 2. Prerequisites
- **Docker Engine**: v24.0+
- **Docker Compose**: v2.20+
- **System Memory**: 8GB RAM minimum
- **Disk Space**: 20GB for data volumes

---

## 3. Deployment Steps

### 3.1 Environment Configuration
Create a `.env` file in the root directory:
```bash
POSTGRES_USER=pallavi_admin
POSTGRES_PASSWORD=secure_governance_pwd
POSTGRES_DB=india_innovates
REDIS_URL=redis://redis:6379/0
AI_ENGINE_VERSION=v2.5-enterprise
```

### 3.2 Build and Launch
Run the following command to build the images and start the services:
```bash
docker-compose up --build -d
```

### 3.3 Database Migrations
Initialize the regional metadata and seed the corpus:
```bash
docker-compose exec backend python scripts/seed_massive_corpus.py
docker-compose exec backend python backend/utils/regional_metadata_gen.py
```

---

## 4. Service Health Checks
- **Backend API**: `http://localhost:8000/health`
- **Dashboard UI**: `http://localhost:3000`
- **Metrics (Prometheus)**: `http://localhost:9090`
- **Audit Logs**: `http://localhost:8000/v1/admin/audit`

---

## 5. Scaling in Production
For nation-scale deployment, the `docker-compose.yml` should be translated into Kubernetes manifests:
- **Deployment**: Use `ReplicaSets` of 10+ backend pods.
- **Service**: Expose via an `ALB` (Application Load Balancer) with SSL termination.
- **Persistence**: Utilize `RDS` (Relational Database Service) for multi-AZ PostgreSQL.

---
*Document Version: 2.0.0-Docker | Maintained by: Platform Eng*
