# Architecture Overview

## Overview

The OWASP Smoke Testing Framework is a lightweight Python-based defensive security testing framework designed to perform automated smoke tests against web applications.

The framework focuses on identifying common OWASP Top 10 security weaknesses through modular testing components.

---

# High-Level Workflow

1. Load YAML configuration
2. Execute security modules
3. Collect findings
4. Generate JSON security report

---

# Core Components

## main.py

Coordinates:
- configuration loading
- scanner execution
- report generation

---

## SQL Injection Module

File:
- `sql_injection.py`

Purpose:
- tests URL parameters using common SQL injection payloads
- detects basic database error signatures

---

## SSRF Validation Module

File:
- `ssrf.py`

Purpose:
- tests for potential Server-Side Request Forgery behavior
- validates handling of internal/private URLs

---

## HTTP Header Audit Module

File:
- `header_audit.py`

Purpose:
- checks for recommended HTTP security headers
- identifies missing hardening controls

---

## CORS Validation Module

File:
- `cors_checker.py`

Purpose:
- detects insecure Cross-Origin Resource Sharing configurations

---

## Report Generator

File:
- `report_generator.py`

Purpose:
- generates structured JSON security reports

---

# Security Design Principles

- defensive security testing only
- minimal attack surface
- modular architecture
- CI/CD compatible
- lightweight dependency footprint

---

# Future Architecture Improvements

Planned future enhancements include:

- plugin-based scanner engine
- asynchronous scanning
- Docker containerization
- SIEM integration
- GitHub Actions CI integration
- Prometheus metrics support