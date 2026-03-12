# PALLAVI AI: API & Middleware Integration Manual

## Overview
This document provides an exhaustive technical specification of the PALLAVI AI platform's API layer and its sophisticated middleware architecture. Designed for 10,000+ LOC enterprise environments, this system ensures high availability, strict security, and seamless multilingual processing.

---

## 1. API Architecture

### 1.1 Core Principles
- **Asynchronous First**: All endpoints are built using FastAPI's `async def` to handle thousands of concurrent voice streams.
- **Strict Validation**: Every request is validated against complex Pydantic models with cross-field constraints.
- **Linguistic Contextualization**: Headers determine the localization context for AI responses and UI strings.

### 1.2 Resource Hierarchy
```mermaid
graph TD
    A[API Gateway] --> B[/v1/citizens]
    A --> C[/v1/tickets]
    A --> D[/v1/ai]
    A --> E[/v1/telephony]
    A --> F[/v1/admin]
    
    B --> B1[GET /profile]
    B --> B2[POST /register]
    
    C --> C1[POST /create]
    C --> C2[GET /track/{id}]
    C --> C3[PATCH /update]
    
    D --> D1[POST /classify]
    D --> D2[POST /sentiment]
    D --> D3[POST /translate]
```

---

## 2. Middleware Stack

The platform utilizes a multi-layered middleware architecture to intercept and process requests before they reach the controller logic.

### 2.1 Security & Authentication Middleware
- **JWT Provider**: Validates RSA-256 signed tokens from the Central Identity Provider (CIDH).
- **RBAC Engine**: Enforces Role-Based Access Control at the middleware level.
- **WAF Simulation**: Detects and logs suspicious patterns like SQL injection or rapid-fire requests.

### 2.2 Observability & Telemetry Middleware
- **Correlation IDs**: Every request is assigned a unique X-Request-ID for distributed tracing.
- **Latency Tracking**: Records TTFB (Time To First Byte) and full resolution time.
- **Prometheus Exporter**: Surfaces metrics on `/metrics` for Grafana dashboards.

### 2.3 Localization & Regionalization Middleware
- **Accept-Language Parsing**: Automatically detects citizen language preference from headers.
- **Regional Context Injection**: Injects ward and district metadata into the request state based on citizen credentials.

---

## 3. Detailed Endpoint Specification

### 3.1 Ticket Management (`/v1/tickets`)

#### `POST /create`
Creates a new grievance ticket. Initiates the AI classification pipeline.

**Request Payload:**
```json
{
  "citizen_id": "CIT-99238",
  "complaint_text": "Severe water leakage near the central park entrance.",
  "location": {
    "lat": 12.9716,
    "lng": 77.5946,
    "address": "MG Road, Block 4"
  },
  "media_attachments": ["audio_ref_001", "img_ref_002"]
}
```

**Internal Logic:**
1. **Schema Validation**: Validates geospatial coordinates and citizen existence.
2. **AI Classification**: Calls `AIEngine.classify_intent` to determine the department.
3. **Priority Assessment**: Calls `AIEngine.calculate_priority` based on sentiment and keywords.
4. **Persistence**: Commits to PostgreSQL via SQLAlchemy.
5. **Notification**: Dispatches events to the `NotificationService` for SMS/WhatsApp alerts.

---

## 4. Advanced Integration Patterns

### 4.1 Voice Stream Processing
The telephony middleware handles binary audio streams, performing real-time chunking for the Transcriber service.

```python
async def process_audio_chunk(chunk: bytes, session_id: str):
    # Core logic for handling incoming audio chunks from telephony provider
    # 1. Reassemble chunks
    # 2. Perform silence detection
    # 3. Stream to ASR (Automatic Speech Recognition)
    pass
```

### 4.2 Webhook Integration
External departmental systems (e.g., BESCOM for Electricity) receive updates via high-reliability webhooks.

- **Retries**: Exponential backoff (1s, 10s, 60s, 10m).
- **Payload Signing**: HMAC-SHA256 signature for verification.
- **Dead Letter Queues**: Failed deliveries are stored in Redis for manual audit.

---

## 5. Error Handling & Resilience

### 5.1 Standardized Error Codes
| Code | Category | Description |
|------|----------|-------------|
| P100 | Validation | Missing mandatory field |
| P200 | Auth | Token expired or invalid signature |
| P300 | AI | Context window exceeded or model timeout |
| P400 | Data | Database connection pool exhausted |

### 5.2 Circuit Breaking
Middleware automatically trips the circuit for the `AI_CLASSIFIER` service if latencies exceed 500ms for more than 5% of requests.

---

## 6. Development & Testing
- **Mock Handlers**: Use `?mock=true` to simulate external service responses.
- **Sandbox Mode**: Isolated environment for testing integration with dummy regional data.

---
*Last Updated: 2026-03-12 | Version 2.0.0-enterprise*
