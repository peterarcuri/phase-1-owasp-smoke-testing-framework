# Testing Strategy

## Overview

The OWASP Smoke Testing Framework uses lightweight defensive security testing designed for:

* CI/CD pipelines
* development environments
* lab validation
* AppSec learning environments

The framework emphasizes:

* rapid validation
* modular testing
* low operational overhead
* defensive analysis

---

# Testing Objectives

Primary testing goals include:

* identifying common OWASP Top 10 weaknesses
* validating basic security hardening
* automating defensive smoke testing
* improving AppSec awareness

---

# Current Test Coverage

## SQL Injection Smoke Testing

Module:

* `sql_injection.py`

Validation Includes:

* common SQL injection payloads
* database error signatures
* basic input handling weaknesses

Example Payloads:

* `' OR 1=1 --`
* `"; DROP TABLE users; --`

Detection Focus:

* SQL syntax errors
* database exception leakage
* insecure query behavior

---

## SSRF Validation

Module:

* `ssrf.py`

Validation Includes:

* localhost access attempts
* cloud metadata endpoint exposure
* internal URL handling

Example Targets:

* `http://169.254.169.254`
* `http://127.0.0.1`
* `http://localhost`

Detection Focus:

* server-side URL processing
* internal request exposure

---

## HTTP Security Header Auditing

Module:

* `header_audit.py`

Headers Validated:

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy

Detection Focus:

* missing hardening controls
* insecure HTTP response configuration

---

## CORS Misconfiguration Detection

Module:

* `cors_checker.py`

Validation Includes:

* wildcard origin policies
* reflected origins
* credential exposure risks

Detection Focus:

* insecure cross-origin access
* overly permissive CORS policies

---

# Unit Testing

Framework uses:

```text
pytest
```

Current unit testing goals:

* validate module outputs
* validate report generation
* validate scanner responses
* validate JSON formatting

---

# Manual Validation

Recommended manual validation:

* run against intentionally vulnerable lab applications
* test against local Docker labs
* validate behavior using OWASP Juice Shop
* verify report accuracy

---

# CI/CD Testing Goals

Future pipeline integration will support:

* automated smoke testing during deployments
* pull request security validation
* GitHub Actions integration
* container security validation

---

# Security Constraints

This framework intentionally avoids:

* destructive exploitation
* denial-of-service behavior
* credential attacks
* privilege escalation attempts

The project is designed strictly for defensive security validation.

---

# Future Testing Enhancements

Planned improvements include:

* authenticated testing support
* API security validation
* TLS analysis
* plugin-based scanner loading
* asynchronous scanning
* Dockerized testing labs
* SAST integration
* DAST pipeline integration

---

# Long-Term DevSecOps Vision

The testing framework is intended to evolve into a lightweight DevSecOps security validation platform capable of integrating with:

* CI/CD pipelines
* Docker environments
* Kubernetes deployments
* Infrastructure-as-Code workflows
* monitoring and observability stacks
