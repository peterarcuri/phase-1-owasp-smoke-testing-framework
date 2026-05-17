# Phase 1 — OWASP Smoke Testing Framework

A lightweight Python-based web application security testing framework focused on identifying common OWASP Top 10 vulnerabilities through automated smoke testing.

---

# Objectives

This project is designed to strengthen practical DevSecOps and Application Security (AppSec) skills in:

- OWASP Top 10 awareness
- Security automation
- HTTP security analysis
- Secure coding practices
- Vulnerability validation
- Defensive security testing

---

# Features

## Current Features

- SQL Injection smoke testing
- SSRF validation checks
- HTTP security header auditing
- CORS misconfiguration detection
- JSON security reporting

---

## Planned Features

- Authentication weakness detection
- TLS inspection
- Rate limiting protection
- Plugin-based testing engine
- CI/CD integration support
- Docker container support

---

# Project Structure

```text
phase-1-owasp-smoke-testing-framework/
│
├── src/
├── tests/
├── docs/
├── config/
├── sample-output/
└── screenshots/
```

---

# Security Modules

| Module | Purpose |
|---|---|
| sql_injection.py | Detects basic SQL injection indicators |
| ssrf.py | Validates potential SSRF exposure |
| header_audit.py | Audits HTTP security headers |
| cors_checker.py | Detects insecure CORS configurations |

---

# Security Considerations

This framework is intended strictly for:

- educational purposes
- defensive security validation
- authorized security assessments
- lab environments

Do NOT scan systems without explicit authorization.

---

# Future Improvements

- SAST integration
- DAST pipeline support
- SIEM export capability
- Prometheus metrics
- Dockerized deployment
- GitHub Actions CI integration

---

# Example Security Checks

- Missing `Content-Security-Policy`
- Missing `Strict-Transport-Security`
- Weak CORS configuration
- Potential SQL injection behavior
- SSRF metadata endpoint exposure

---

# Long-Term DevSecOps Goals

This project will eventually integrate with:

- CI/CD pipelines
- Docker containers
- Terraform infrastructure
- Kubernetes deployments
- Monitoring stacks

to simulate real-world DevSecOps workflows.