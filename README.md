# Docker Security Scanner

A containerized Python security vulnerability scanner for quick web application assessments.

## Features
- Port scanning (common ports)
- HTTP security header analysis
- Containerized for portability
- Lightweight and fast

## Built With
- Python 3.9
- Docker
- Requests library
- Socket programming

## Quick Start

### Build
```bash
docker build -t security-scanner:v1 .
```

### Run
```bash
docker run security-scanner:v1 <target_domain>
```

### Example
```bash
docker run security-scanner:v1 scanme.nmap.org
```

## What It Checks
- Open ports (21, 22, 23, 25, 80, 443, 3306, 3389, 8080)
- HTTP security headers (X-Frame-Options, CSP, HSTS, etc.)

## Security Note
Only scan systems you have permission to test. Unauthorized scanning is illegal.

## Author
Eugene Uguomore - Certified Ethical Hacker (CEH)