# PALLAVI AI: Detailed Module Documentation

This document explains the technical depth and responsibilities of the various modules in the PALLAVI AI Calling Agent project.

## 1. Backend Services (`/backend/services`)

### 1.1 `ai_service.py`
The AI service orchestrates the high-level intelligence. It combines keyword-based heuristics with placeholders for LLM-based categorization. It handles:
-   **Language Mapping**: Translating raw transcripts to standard ISO codes.
-   **Intent Extraction**: Determining if the citizen is reporting a new issue, checking status, or giving feedback.
-   **Priority Matrix**: Assigning urgency based on safety and infrastructure metrics.

### 1.2 `telephony_service.py`
Acts as the bridge between raw telephony events (Webhooks) and internal business logic.
-   **Inbound Flow**: Handshake with STT -> Identification with `citizen_service` -> Ticket creation with `ticket_service`.
-   **Outbound Flow**: Logic for timing and retry strategies for automated citizen callbacks.

### 1.3 `sla_service.py`
A vital background worker logic that:
-   Calculates the "Deadline" for every ticket based on its priority at creation.
-   Periodically sweeps the database for breaches.
-   Triggers escalations which are then handled by the `escalation_service.py`.

## 2. Telephony Layer (`/backend/telephony`)

### 2.1 `voice_processing.py`
Simulates the computational heavy lifting of speech processing.
-   **Noise Floor Simulation**: Logic to handle "Confidence Scores" below 0.5.
-   **Multilingual Dictionaries**: Massive datasets for English, Hindi, and Tamil to ensure simulation variety.

## 3. Frontend Dashboard (`/frontend/dashboard`)

### 3.1 Component Architecture
The dashboard is built for high-performance data viewing:
-   **Recharts Integration**: Custom wrappers for city-health bar charts and urgency pies.
-   **context/AppStateContext.jsx**: Centralized state to prevent "prop-drilling" across the complex admin interface.
-   **Leaflet Mapping**: Simulated spatial layer for identifies geographical grievance hotspots.

---

### Developed by Team NOVACORE
Part of India Innovates 2026
"Every voice deserves to be heard."
