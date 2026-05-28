# Usage Guide

## Overview

The OWASP Smoke Testing Framework is a lightweight Python-based application security testing framework designed to perform defensive smoke testing against web applications.

The framework focuses on identifying common OWASP Top 10 security weaknesses through automated validation modules.

---

# Environment Setup

## Clone Repository

```bash
git clone <repository-url>
cd phase-1-owasp-smoke-testing-framework
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
phase-1-owasp-smoke-testing-framework/
│
├── config/
├── docs/
├── sample-output/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Configuration

Application configuration is stored in:

```text
config/config.yaml
```

Example configuration:

```yaml
target:
  base_url: "http://localhost:3000"
  test_parameter: "q"

report:
  output_file: "sample-output/security-report.json"
```

---

# Running the Framework

Run the framework from the project root:

```bash
python -m src.main
```

---

# Security Modules

## SQL Injection Testing

File:

* `src/sql_injection.py`

Purpose:

* validates common SQL injection indicators
* checks for database error signatures

---

## SSRF Validation

File:

* `src/ssrf.py`

Purpose:

* validates handling of internal/private URLs
* tests metadata endpoint exposure

---

## HTTP Header Auditing

File:

* `src/header_audit.py`

Purpose:

* checks for recommended HTTP security headers

Headers audited:

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy

---

## CORS Validation

File:

* `src/cors_checker.py`

Purpose:

* detects insecure CORS configurations
* validates wildcard origin behavior

---

# Report Generation

Reports are generated in JSON format.

Default output location:

```text
sample-output/security-report.json
```

---

# Running Tests

Execute unit tests:

```bash
pytest
```

---

# Security Notice

This framework is intended strictly for:

* educational purposes
* authorized security testing
* defensive validation
* lab environments

Do NOT scan systems without explicit authorization.

Unauthorized security testing may violate laws, policies, or terms of service.

---

# Troubleshooting

## Virtual Environment Issues

Verify the correct interpreter is selected:

```bash
which python
```

Expected output should reference:

```text
venv/bin/python
```

---

## Import Errors

Ensure:

* `src/__init__.py` exists
* the project root is opened in VS Code
* dependencies are installed

---

# Future Improvements

Planned future enhancements:

* plugin-based scanning engine
* CI/CD integration
* Docker support
* TLS validation
* authentication weakness testing
* Prometheus metrics
* SIEM integration
