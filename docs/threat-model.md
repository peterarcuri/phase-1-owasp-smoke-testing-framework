# Threat Model

## Purpose

This project simulates lightweight application security smoke testing designed to identify common web application security weaknesses.

The framework is intended strictly for:
- educational purposes
- defensive validation
- authorized security testing
- lab environments

---

# Threat Categories

## SQL Injection

Risk:
- unauthorized database access
- data leakage
- authentication bypass

Detection:
- payload injection
- database error signature analysis

---

## Server-Side Request Forgery (SSRF)

Risk:
- internal network access
- cloud metadata exposure
- lateral movement

Detection:
- metadata endpoint testing
- localhost/internal URL validation

---

## Security Header Misconfiguration

Risk:
- clickjacking
- MIME sniffing
- XSS exposure
- downgrade attacks

Detection:
- missing HTTP security headers

---

## CORS Misconfiguration

Risk:
- unauthorized cross-origin access
- credential leakage

Detection:
- wildcard origin validation
- insecure origin reflection

---

# Assumptions

The framework assumes:
- testing is authorized
- targets are reachable
- defensive analysis only

---

# Limitations

This framework does NOT:
- exploit vulnerabilities
- perform authenticated attacks
- bypass protections
- perform destructive testing

---

# Future Threat Coverage

Planned future coverage:
- authentication weaknesses
- insecure TLS configurations
- rate limiting bypass
- API security validation
- OWASP API Top 10