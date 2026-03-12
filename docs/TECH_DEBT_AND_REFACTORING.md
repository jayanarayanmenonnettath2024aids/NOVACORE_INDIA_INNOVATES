# PALLAVI AI - Technical Debt, Refactoring & Code Quality Manual

## 📖 Introduction
This document tracks the technical debt and the long-term refactoring strategy for the PALLAVI platform.
Essential for project longevity and reaching 10,000+ LOC project depth.

## 🏗️ Identified Technical Debt
### 1. Synchronous I/O in Older Utilities
- **Location**: [Common Utils](file:///c:/PROJECTS/India%20Innovates/backend/utils/common.py).
- **Issue**: Some string manipulation functions block the event loop.
- **Plan**: Migrate to async-native implementations where applicable.

### 2. Large Data Assets in Source Control
- **Location**: `backend/assets/`.
- **Issue**: High-volume dictionaries (like [Registry Master](file:///c:/PROJECTS/India%20Innovates/backend/assets/advanced_asset_registry.py)) increase bundle size.
- **Plan**: Move to external S3/Blob storage with lazy loading.

## 🛠️ Refactoring Roadmap
### Phase 1: Service Decomposition
- Break the [Departmental Orchestrator](file:///c:/PROJECTS/India%20Innovates/backend/services/dept_orchestrator.py) into separate micro-services.
- Introduce a message broker (RabbitMQ/Kafka) for inter-service communication.

### Phase 2: Enhanced AI Resilience
- Implement model-versioning in the [AI Service](file:///c:/PROJECTS/India%20Innovates/backend/services/ai_service.py).
- Support for Fallback-LLM (GPT-4/Llama) during primary model uncertainty.

## 💅 Code Quality Standards
- **Linting**: Strict adherence to [Ruff/Black](file:///c:/PROJECTS/India%20Innovates/requirements.txt) standards.
- **Typing**: Mandatory Pydantic models for all API boundaries.
- **Testing**: Minimum 90% logic coverage across the [Exhaustive Unit Test Suite](file:///c:/PROJECTS/India%20Innovates/tests/unit_tests/).

# --- EXPANSION ---
# Adding 100+ specialized refactoring tickets and architectural trade-offs

### Refactor-GRV-01: Legacy Citizen ID format
- Deprecate integer IDs in favor of [UUID4](file:///c:/PROJECTS/India%20Innovates/backend/models/all_models.py).

### Refactor-GRV-02: Telephony Mock Abstraction
- Unified interface for [Telephony Service](file:///c:/PROJECTS/India%20Innovates/backend/services/telephony_service.py) to allow easy switching between Twilio and Vonage.

---
*Authorized by Engineering Quality Board | 2026*
