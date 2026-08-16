import re
import sqlite3, json
from datetime import datetime

def setup_db():
    conn = sqlite3.connect("traffic.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY,
        method TEXT, url TEXT, req_headers TEXT, req_body TEXT,
        status INTEGER, resp_headers TEXT, resp_body TEXT, timestamp TEXT
    )""")
    conn.commit()
    return conn

conn = setup_db()

SECRET_PATTERNS = [
    (r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}', 'JWT'),
    (r'AKIA[0-9A-Z]{16}', 'AWS Key'),
]

def scan_passive(flow):
    findings = []
    headers = dict(flow.response.headers)
    for h in ['Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security']:
        if h not in headers:
            findings.append(f"Missing header: {h}")
    body = flow.response.get_text()[:5000]
    for pattern, label in SECRET_PATTERNS:
        if re.search(pattern, body):
            findings.append(f"Possible {label} leaked in response body")
    return findings

def response(flow):
    findings = scan_passive(flow)
    if findings:
        print(f"⚠️  {flow.request.url}")
        for f in findings:
            print(f"   - {f}")
    conn.execute("INSERT INTO requests (method, url, req_headers, req_body, status, resp_headers, resp_body, timestamp) VALUES (?,?,?,?,?,?,?,?)",
        (flow.request.method, flow.request.url,
         json.dumps(dict(flow.request.headers)), flow.request.get_text(),
         flow.response.status_code, json.dumps(dict(flow.response.headers)),
         flow.response.get_text()[:5000], datetime.now().isoformat()))
    conn.commit()
    print(f"Logged: {flow.request.method} {flow.request.url} -> {flow.response.status_code}")
