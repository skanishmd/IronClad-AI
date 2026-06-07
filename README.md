# 🛡️ IronClad AI: The Secure Agent Infrastructure

> **Build the future of Biology without leaking your Intellectual Property.**

IronClad AI is a security-first framework designed for researchers, founders, and developers using local AI agents (like Gemini CLI). It provides a hardened environment to manage your career trajectory and proprietary research secrets without risking data exposure to the cloud.

---

## 🚀 The Methodology: "Surgical Strike"

This infrastructure separates your data into three distinct security tiers:
1.  **Context (Public/Shared):** High-level goals stored in `GEMINI.md`.
2.  **Intellectual Property (Air-Gapped):** Sensitive scaffolds and algorithms in `SECRET_IP.md`.
3.  **Local Shield:** Encryption and folder-hiding scripts to protect from unauthorized local access.

---

## 🛠️ Installation & Setup

### 1. Clone the Shell
```bash
git clone <your-repo-url>
cd IronClad-AI-Template
```

### 2. Personalize your Context
Rename `GEMINI_TEMPLATE.md` to `GEMINI.md` and fill in your background. 
**Note:** `GEMINI.md` and `SECRET_IP.md` are automatically ignored by Git—they will NEVER be pushed to the public web.

---

## 🔒 Security CLI Instructions

### For Windows Users (PowerShell)
To hide and encrypt your environment:
```powershell
.\SecureMemory.ps1 -Action Lock
```
To reveal your environment for editing:
```powershell
.\SecureMemory.ps1 -Action Unlock
```

### For Mac/Linux Users (Bash)
To hide and restrict permissions:
```bash
chmod +x secure_memory.sh
./secure_memory.sh lock
```
To restore visibility:
```bash
./secure_memory.sh unlock
```

---

## ⚠️ The Iron-Clad Warning
The `.gitignore` in this repo is your primary shield. **Do not modify it** unless you fully understand how to air-gap local data. Always verify that your `SECRET_IP.md` remains untracked before performing a git push.

---
*Architected by a Computational Oncology Researcher & AI-Bio Founder.*
