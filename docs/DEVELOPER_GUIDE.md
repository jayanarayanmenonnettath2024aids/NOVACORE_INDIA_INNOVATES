# PALLAVI AI - Developer Documentation

## 🏗️ Architecture Overview
The PALLAVI platform follows an **Enterprise Service Pattern** with a modular AI orchestration layer.

### Core Modules
1. **AI Engine**: Transformer-based intent classification and language detection.
2. **Telephony Bridge**: Simulation layer for Twilio/Vonage integration.
3. **Service Layer**: Department-specific logic (Water, Power, Roads, etc.).
4. **Data Layer**: SQLAlchemy + PostgreSQL core with Redis caching.

## 🛠️ Service Logic
Each department is isolated into its own service class to ensure horizontal scalability.

### [Water Service](file:///c:/PROJECTS/India%20Innovates/backend/services/departments/water_service.py)
Handles hydrodynamic simulations and field team dispatch for pipeline bursts.

### [Electricity Service](file:///c:/PROJECTS/India%20Innovates/backend/services/departments/electricity_service.py)
Interfaces with grid telemetry and manages power outage restitution workflows.

## 🔒 Security
The platform implements a simulated JWT-based authentication system with RBAC.
- **Admin**: Full access to analytics and system controls.
- **Operator**: Access to ticket management and citizen lookup.
- **Auditor**: Read-only access to audit logs and performance metrics.

---
*Created for Project PALLAVI AI by Sri Eshwar College of Engineering Team NovaCore.*
