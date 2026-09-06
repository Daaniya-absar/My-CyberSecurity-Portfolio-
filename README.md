# 🔐 Cybersecurity Portfolio — Daaniya Absar

**Penetration Testing | Red Teaming | Vulnerability Assessment & Penetration Testing (VAPT)**  
*Documenting my journey, projects, and continuous learning in offensive security.*

---

## 👋 About Me

I am an aspiring cybersecurity professional with a strong passion for **Penetration Testing**, **Red Teaming**, and **Vulnerability Assessment**. My journey began with structured learning through platforms like Hack The Box Academy and TryHackMe, where I develop practical skills through hands-on lab environments.

I am committed to building a solid foundation in offensive security, understanding adversarial tactics, and developing the ability to identify, exploit, and remediate vulnerabilities. This portfolio serves as a living document of my learning journey, projects, and the skills I am acquiring.

---

## 🎯 Key Areas of Focus

| Area | Description |
|------|-------------|
| **Penetration Testing** | Systematic exploitation of vulnerabilities in networks, systems, and applications. |
| **Red Teaming** | Simulating advanced persistent threats to test organizational defenses. |
| **VAPT** | Comprehensive vulnerability assessment and penetration testing methodologies. |
| **Linux/Windows Security** | Privilege escalation, misconfiguration exploitation, and system hardening. |
| **Web Application Security** | OWASP Top 10, API security, and secure coding practices. |
| **Network Security** | Reconnaissance, scanning, enumeration, and exploitation of network services. |

---

## 🛠️ Projects & Practical Work

### 🧪 Linux Privilege Escalation — Hands-on Lab
*A complete chain of privilege escalation from low-privileged user to root access.*

**Objective:** Gain root access on a Linux target through systematic enumeration and exploitation.

**Approach:**
- Initial access via SSH with provided credentials.
- Identification of sudo misconfigurations allowing lateral movement.
- Comprehensive system enumeration (SUID binaries, cron jobs, writable files, kernel version).
- Discovery and exploitation of a known vulnerability in sudo (CVE-2021-3156).
- Successful root access and flag retrieval.

**Key Learnings:**
- The importance of thorough system enumeration.
- How misconfigured permissions can lead to complete compromise.
- Real-world application of publicly disclosed vulnerabilities.

📄 *Writeup available in the `writeups/htb-labs/` directory.*

---

### 🔍 HTTP Traffic Interception & IDOR Scanner
*A custom Python toolkit for identifying Insecure Direct Object References.*

**Objective:** Build a lightweight tool to intercept HTTP traffic and detect IDOR vulnerabilities.

**Approach:**
- Developed a modular Python proxy to log and analyze requests/responses.
- Implemented passive scanning for anomalies (sequential IDs, missing access controls).
- Built an active testing module to exploit potential IDOR vulnerabilities.

**Key Learnings:**
- Understanding HTTP request/response structures.
- Common patterns leading to IDOR vulnerabilities.
- Building practical automation tools for security testing.

📄 *Code and documentation available in the `projects/` directory.*

---

### 🌐 Vulnerability Exploitation — Web Application Security
*Exploiting known vulnerabilities in web applications to understand attack vectors.*

**Objective:** Exploit an unauthenticated file-read vulnerability in a web application.

**Approach:**
- Vulnerability research and CVE analysis.
- Using exploitation frameworks (Metasploit) for rapid exploitation.
- Retrieving sensitive files from the target server.

**Key Learnings:**
- The risks of running outdated software and plugins.
- Using automated tools for efficient vulnerability exploitation.
- Importance of vulnerability research and threat intelligence.

📄 *Writeup available in the `writeups/htb-labs/` directory.*

---

### 🔄 Currently Learning
- Active Directory security and enumeration
- Windows privilege escalation techniques
- Buffer overflow exploitation
- Advanced web application security

### 🎯 Future Goals
- eJPT Certification
- OSCP Certification
- Advanced red teaming tactics
- Cloud security (AWS/Azure)
- API security testing

---

## 🧠 Skills & Competencies

| Category | Skills |
|----------|--------|
| **Offensive Security** | Enumeration, Vulnerability Identification, Exploitation, Post-Exploitation |
| **Web Security** | OWASP Top 10, IDOR, SQL Injection, XSS, Authentication Bypasses |
| **Network Security** | Nmap, Wireshark, tcpdump, Netcat, Network Protocols |
| **Privilege Escalation** | Linux SUID/SGID, Cron Jobs, Sudo Misconfigurations, Kernel Exploits |
| **Tools** | Burp Suite, Metasploit, Kali Linux, Python, Bash, PowerShell |
| **Reporting** | LaTeX, Markdown, Technical Documentation, Professional Report Writing |

---

## 🏆 Certifications & Training

| Course/Certification | Status |
|----------------------|--------|
| HTB Academy: Penetration Tester Job Role Path | In Progress |
| eJPT (eLearnSecurity Junior Penetration Tester) | Planned |
| OSCP (Offensive Security Certified Professional) | Long-term Goal |

---

## 📈 Professional Development Goals

1. **Master the Fundamentals:** Build a solid understanding of networking, operating systems, and web technologies.
2. **Develop Practical Skills:** Gain hands-on experience through CTFs, labs, and real-world projects.
3. **Specialize:** Deepen expertise in web application security and Active Directory exploitation.
4. **Certifications:** Validate skills through industry-recognized certifications.
5. **Community Contribution:** Share knowledge through writeups, blogs, and open-source contributions.

---

## 💡 Why This Portfolio?

This portfolio is a reflection of my **dedication to continuous learning** and my passion for offensive security. It serves multiple purposes:

- **Learning Journal:** Documenting my progress, challenges, and breakthroughs.
- **Skill Demonstration:** Showcasing practical skills and knowledge acquisition.
- **Professional Growth:** Building a portfolio that demonstrates my abilities and commitment to the field.
- **Knowledge Sharing:** Contributing to the cybersecurity community by sharing my writeups and research.

---

## 📫 Connect With Me

I am always open to connecting with fellow security enthusiasts, professionals, and potential employers.

- **LinkedIn:** www.linkedin.com/in/daaniyaabsar
- **Email:** diyasultanxv.engr@gmail.com

---

## 📝 Disclaimer

All projects and writeups in this portfolio are for **educational purposes only**. The tools and techniques described are intended to be used in controlled lab environments or with explicit authorization. I do not condone or support any illegal or unethical activities.

---

*"Security is not a product, but a process."* — Bruce Schneier

---

**📅 Last Updated:** September 2026
