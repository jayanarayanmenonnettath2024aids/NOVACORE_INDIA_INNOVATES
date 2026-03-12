# PALLAVI AI - API Reference Guide

## 📡 Base URL
`http://localhost:8000/api/v1`

## 🎟️ Tickets API
### GET `/tickets/`
Returns a list of all grievances. Supports pagination and filtering.

### POST `/tickets/`
Creates a new grievance ticket.

## 📞 Telephony API
### POST `/telephony/inbound`
The main entry point for citizen voice calls. Expects `phone_number` and `speech_text`.

## 📊 Analytics API
### GET `/analytics/summary`
Returns the aggregated dashboard metrics.

## 🛡️ Monitoring API
### GET `/monitoring/health`
Returns system heartbeat and hardware usage statistics.

---
*For full Swagger documentation, visit /docs when the server is running.*
