# TRINETRA — Defensive Cybersecurity & Zero-Trust Architecture

**Application:** TRINETRA Surveillance & Evidence Vault  
**Security Model:** Zero-Trust ("Never Trust, Always Verify")  
**Compliance Target:** Defensive Border Surveillance & Tamper-Evident Chain of Custody

---

## 1. Zero-Trust Security Tenets

TRINETRA operates on the principle that no user, device, network, or file is trusted by default. Every action requires continuous cryptographic verification.

1. **Explicit Identity Verification**: Every operator interaction is bound to an authenticated session, enforced with Multi-Factor Authentication (MFA).
2. **Least Privilege Enforcement**: Role-Based Access Control (RBAC) restricts capabilities strictly to designated responsibilities. Permissions are enforced in core application logic, not merely UI button visibility.
3. **Continuous Cryptographic Integrity**: Video evidence files are hashed via SHA-256 immediately upon generation, digitally signed via asymmetric Ed25519 keys, and committed to an append-only block ledger. Any alteration on disk immediately triggers a **CRITICAL SOC INTEGRITY ALERT**.
4. **Immutable Audit Trail**: All authentication events, video uploads, inference passes, evidence extractions, and verification checks are logged to an append-only SQLite audit repository.

---

## 2. Authentication & Credential Security

- **Password Hashing**: Passwords are never stored in plaintext. They are hashed using **PBKDF2-HMAC-SHA256** with **600,000 iterations** and a unique 16-byte cryptographically random salt (`secrets.token_hex(16)`).
- **Brute-Force Protection**: Accounts are automatically locked for 5 minutes after 5 consecutive failed login attempts, logging an `AUTH_LOCKOUT` security event.
- **Session Tokens**: Active sessions utilize a cryptographically secure 24-byte random hex token (`secrets.token_hex(24)`).
- **MFA Enforcement**: Time-based and numeric 6-digit MFA verification codes must be provided to complete authentication.

---

## 3. Role-Based Access Control (RBAC) Matrix

| Resource / Action | Administrator | Security Officer | Analyst | Viewer |
| :--- | :---: | :---: | :---: | :---: |
| **Command Dashboard** | ✓ | ✓ | ✓ | ✓ (Read-only) |
| **Live Surveillance Feeds** | ✓ | ✓ | — | ✓ (Read-only) |
| **Video File Analysis** | ✓ | ✓ | ✓ | — |
| **Incident Management** | ✓ | ✓ | — | — |
| **Evidence Vault (Playback & Verify)** | ✓ | ✓ | ✓ | ✓ (Read-only) |
| **Blockchain Explorer** | ✓ | ✓ | — | — |
| **Cyber SOC & Audit Trail** | ✓ | ✓ | — | — |
| **PDF Dossier Generation** | ✓ | ✓ | ✓ | — |
| **System Settings** | ✓ | — | — | — |
| **Simulate Tamper (Judge Demo)** | ✓ | ✓ | — | — |

---

## 4. Evidence Protection & Tamper Detection

1. **Chunked SHA-256 Hashing**:
   - Evidence files are processed in 64 KB binary chunks, computing a deterministic 256-bit hexadecimal digest:
     $$\text{Digest} = \text{SHA-256}(\text{Bytes}_{\text{clip}})$$
2. **Ed25519 Digital Signatures**:
   - Asymmetric digital signatures are generated using an Ed25519 private key generated via OpenSSL / Python `cryptography`:
     $$\text{Signature} = \text{Sign}_{\text{priv}}(\text{EvidenceID} \,\|\, \text{SHA-256} \,\|\, \text{Timestamp})$$
   - Public keys are exported in standard PEM format (`data/keys/ed25519_public.pem`).
3. **Live Tamper Verification**:
   - The *Verify Integrity* action recomputes the SHA-256 digest of the file on disk and compares it byte-for-byte against the initial database and blockchain records.
   - If a file is modified (even by a single bit), verification fails immediately, turning status to **`✕ COMPROMISED`** and raising an alert in the Cyber SOC.

---

## 5. Security Boundary & Ethical Declarations
- **Defensive Focus**: TRINETRA contains **zero offensive cyber tools**, malware, or credential harvesting mechanisms.
- **Data Protection**: Secrets, private keys, passwords, and MFA tokens are excluded from all logs.
