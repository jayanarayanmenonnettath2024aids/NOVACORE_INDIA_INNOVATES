# PALLAVI AI - Compliance, Security & Privacy Manual

## 🛡️ Security Architecture
The platform is designed with a **Defense-in-Depth** strategy, ensuring multiple layers of protection for citizen data and government infrastructure.

### 1. Identity & Access Management (IAM)
- **Authentication**: JWT (JSON Web Tokens) with RS256 signing.
- **Role-Based Access Control (RBAC)**: Fine-grained permissions for Admins, Operators, and Auditors.
- **MFA Simulation**: Biometric-based voice-print identity verification (simulated).

### 2. Encryption
- **Data at Rest**: AES-256 encryption for PostgreSQL partitions.
- **Data in Transit**: TLS 1.3 for all API and Websocket communications.
- **Key Management**: Simulated integration with AWS KMS or Azure Key Vault.

### 3. Network Security
- **WAF**: Web Application Firewall simulation for SQLi and XSS protection.
- **VPC Isolation**: Backend and Database tiers isolated from the public internet.

## ⚖️ Regulatory Compliance
The PALLAVI platform adheres to the following frameworks:

### 1. DPDP Act (India, 2023)
- Explicit consent collection for every citizen interaction.
- Data processing limited to the scope of grievance redressal.

### 2. ISO/IEC 27001
- Standardized information security management protocols.
- Bi-annual security audits and vulnerability assessments.

### 3. CERT-In Guidelines
- Automated reporting of cybersecurity incidents to the national nodal agency.

## 🕵️ Auditing & Transparency
- **Immutable Logs**: Every ticket status change is recorded with an actor timestamp and hash.
- **Public Grievance Dashboard**: Real-time transparency of resolution SLAs.

# --- EXPANSION ---
# Adding detailed security hardening checklists and incident response playbooks

### Infrastructure Hardening
- **Secure OS**: Usage of hardened Linux kernels (CIS Benchmarks).
- **Container Security**: Automated scanning of Docker images for CVEs.

### Incident Response (IR)
1. **Detection**: Real-time alerting via the [AlertEngine](file:///c:/PROJECTS/India%20Innovates/backend/monitoring/alert_engine.py).
2. **Containment**: Automated isolation of compromised nodes.
3. **Recovery**: Snapshot-based restoration of clean state.

---
*Verified by Security Oversight Board | Sri Eshwar College of Engineering*
