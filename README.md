# Mini Traffic Interception & IDOR Scanner

A custom-built Python security toolkit that intercepts HTTP(S) traffic, passively scans it for common misconfigurations, and actively tests for Insecure Direct Object Reference (IDOR) vulnerabilities.

## What it does

- **`interceptor.py`** — A `mitmproxy` script that logs every intercepted request/response to a SQLite database, and passively flags:
  - Missing security headers (CSP, X-Frame-Options, HSTS)
  - Possible leaked secrets (JWTs, AWS keys) in response bodies

- **`hunt.py`** — An authenticated active-testing script that takes a URL containing a numeric resource ID, tests adjacent IDs while attaching a session token, and reports status codes + response sizes for comparison — used to detect broken object-level authorization (IDOR).

## Real finding

Using this tool against a local instance of [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), I identified and confirmed a real IDOR vulnerability in the basket endpoint (`/rest/basket/:id`), allowing an authenticated user to view other users' private basket contents by simply changing the ID in the URL. Full writeup with evidence in `report.pdf`.

## Stack

Python, mitmproxy, SQLite, requests

## Disclaimer

Built and tested exclusively against a locally-hosted, intentionally vulnerable practice application (OWASP Juice Shop) for educational purposes. No third-party or production systems were tested.# My-CyberSecurity-Portfolio-
