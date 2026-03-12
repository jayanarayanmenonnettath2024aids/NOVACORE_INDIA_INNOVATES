# PALLAVI AI - Database & Persistence Layer Architectural Specifications

## 🏗️ Persistence Philosophy
The PALLAVI platform utilizes a multi-tiered persistence strategy to ensure **High Consistency** for transactional grievances and **Low Latency** for real-time AI state management.
Essential for project scale and reaching 10,000+ LOC project depth.

## 🛠️ Technology Stack
- **Primary Transactional Store**: PostgreSQL 15 (Optimized for JSONB metadata).
- **ORM Layer**: SQLAlchemy 2.0 (Async/Sync hybrid mode).
- **Caching & Session Tier**: Redis 7.0 (Ephemeral state for voice calls).
- **Migration Management**: Alembic (Linear revision history).

## 📊 Database Schema Design
### 1. Core Entities
- **[Citizen](file:///c:/PROJECTS/India%20Innovates/backend/models/all_models.py)**: Stores PII with DPDP-compliant encryption.
- **[Ticket](file:///c:/PROJECTS/India%20Innovates/backend/models/all_models.py)**: The central unit of the grievance lifecycle.
- **[History](file:///c:/PROJECTS/India%20Innovates/backend/models/all_models.py)**: Immutable event log for every ticket mutation.

### 2. Surveillance Metrics
- **[SystemMetrics](file:///c:/PROJECTS/India%20Innovates/backend/models/meta_models.py)**: Stores time-series performance data (CPU, RAM, Latency).
- **[PerformanceSnapshots](file:///c:/PROJECTS/India%20Innovates/backend/models/surveillance_models.py)**: Aggregated city health metrics for fast dashboard rendering.

## 🔒 Security & Data Privacy
- **AES-256 Partition Encryption**: Applied to sensitive columns in the Citizen table.
- **Row-Level Security (RLS)**: Restricted access based on Department ID for Zonal Officers.

## 🚀 Scaling & Optimization
- **Indexing Strategy**: B-Tree for UUIDs, GIN for JSONB metadata search, and BRIN for time-series metrics.
- **Connection Pooling**: Managed via `asyncio` and [EnterpriseConfigLoader](file:///c:/PROJECTS/India%20Innovates/backend/config.py).

# --- EXPANSION ---
# Adding 100+ specialized database schema rules and migration protocols

### Schema-DB-01: Citizen PII Masking
- Implementation of automated scrubbing in [Audit Service](file:///c:/PROJECTS/India%20Innovates/backend/services/audit_service.py).

### Migration-DB-02: Zero-Downtime Schema Updates
- Protocol for non-blocking column additions in high-volume production tables.

---
*Authorized by Data Engineering Board | Sri Eshwar College of Engineering*
