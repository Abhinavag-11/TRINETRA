# TRINETRA — Blockchain & Immutable Ledger Architecture

**Module:** Blockchain Chain of Custody Adapter  
**Production Standard:** Hyperledger Fabric 2.5 LTS Architecture  
**Prototype / Offline Implementation:** LocalLedgerAdapter (Append-Only SHA-256 Block Chain)

---

## 1. On-Chain vs. Off-Chain Storage Architecture

A critical architectural rule of TRINETRA is:
> **RAW VIDEO EVIDENCE FILES ARE NEVER STORED ON THE BLOCKCHAIN.**

Storing massive multi-megabyte video files directly inside blockchain state causes ledger bloat, excessive latency, and scalability bottlenecks. TRINETRA utilizes a **hybrid on-chain/off-chain model**:

- **Off-Chain (Local Storage)**: High-resolution MP4 evidence clips are saved to local filesystem storage (`data/evidence/EVD-XXXXX.mp4`).
- **On-Chain (Blockchain Ledger)**: Only the cryptographic SHA-256 digest, Ed25519 digital signature, timestamp, threat taxonomy, camera identifier, and operator ID are committed to the blockchain block.

```
[MP4 Evidence Clip] ──► [SHA-256 Hasher] ──► 64-Hex Digest
                                                 │
                                                 ▼
               ┌──────────────────────────────────────────────────┐
               │              BLOCKCHAIN BLOCK #N                 │
               ├──────────────────────────────────────────────────┤
               │ Previous Hash:    096b5bdb3ce704d2e9...          │
               │ Block Hash:       f820c7a8b329184910...          │
               │ Timestamp:        2026-09-10T15:34:44Z           │
               │ Evidence ID:      EVD-20260910-26C3CB            │
               │ Evidence Hash:    11f578f77df3c3cc3e...          │
               │ Threat Type:      HUMAN INTRUSION                │
               │ Operator ID:      TRINETRA_OPERATOR              │
               │ Merkle Root:      11f578f77df3c3cc               │
               └──────────────────────────────────────────────────┘
```

---

## 2. LocalLedgerAdapter Mathematical Specification

For standalone evaluation, demonstration, and offline tactical deployment, TRINETRA provides the `LocalLedgerAdapter`. It implements a deterministic, append-only, SHA-256 hash-chained block storage engine.

### Genesis Block ($N = 0$):
$$\text{PrevHash}_0 = \text{0000000000000000000000000000000000000000000000000000000000000000}$$
$$H_0 = \text{SHA-256}(\text{PrevHash}_0 \,\|\, 0 \,\|\, T_0 \,\|\, \text{"GENESIS"} \,\|\, \text{"GENESIS"})$$

### Consecutive Blocks ($N \ge 1$):
$$\text{PrevHash}_N = H_{N-1}$$
$$H_N = \text{SHA-256}(\text{PrevHash}_N \,\|\, N \,\|\, T_N \,\|\, \text{EvidenceID}_N \,\|\, \text{EvidenceHash}_N)$$

### Mathematical Proof of Tamper-Evident Immutability:
If an attacker alters an earlier record $k < N$ (e.g. changing an evidence hash from $H_{\text{evd}}$ to $H'_{\text{evd}}$):
$$H'_k \ne H_k \implies \text{PrevHash}_{k+1} \ne H'_{k}$$
The entire chain of block hashes from $k$ to $N$ collapses and fails verification immediately.

---

## 3. Hyperledger Fabric 2.5 Enterprise Integration

TRINETRA's `FabricAdapter` is designed to connect to an enterprise Hyperledger Fabric network:
- **Channel:** `trinetrachannel`
- **Chaincode (Smart Contract):** `trinetra-evidence-cc`
- **Endorsement Policy:** Requires validation by multiple peer nodes (e.g., BOP Outpost + HQ Command Node).
- **Transactions Supported:**
  - `createIncident(incidentId, threatType, camera, timestamp)`
  - `registerEvidence(evidenceId, sha256Digest, signature, officerId)`
  - `verifyEvidence(evidenceId, currentSha256)`
  - `getAuditTrail(evidenceId)`

### Honest Status Labelling:
In compliance with SIH honesty requirements, whenever an active live Fabric peer is not configured, TRINETRA explicitly displays:
```
BLOCKCHAIN: DEMO / LOCAL LEDGER
```
Never claiming decentralization when operating in local hash-chain mode.
