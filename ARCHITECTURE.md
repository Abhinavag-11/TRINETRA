# TRINETRA — Architecture & Technical Design Document

**System:** TRINETRA — AI-Based Video Surveillance Analytics & Evidence Management Platform  
**Target:** Windows Desktop Application (PySide6 / Qt 6)  
**SIH Problem Statement ID:** SIH26187

---

## 1. Architectural Philosophy

TRINETRA is built upon three non-negotiable architectural principles:

1. **Local-First Resilience**: All core capabilities—video decoding, 16-frame temporal buffering, ViViT + SNN inference, evidence extraction, cryptographic hashing, digital signing, and SQLite logging—execute 100% locally on standard CPU endpoints. If network access fails, TRINETRA transitions seamlessly to **OFFLINE FAIL-SAFE MODE** without losing a single frame or alert.
2. **Deterministic Chain of Custody**: Evidence is never merely saved as arbitrary files on disk. Every clip is carved to a deterministic temporal window ($[T-3\text{s}] \to \text{Event} \to [T+3\text{s}]$), hashed via chunked SHA-256, signed with an asymmetric Ed25519 digital key, and anchored to an append-only block ledger.
3. **Freeze-Free Asynchronous UI**: Expensive operations (video decoding, tensor attention, clip writing, hashing, and PDF generation) never execute on the Qt main GUI thread. They are isolated in dedicated `QThread` workers communicating strictly via typed Qt signals.

---

## 2. Component Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TRINETRA DESKTOP GUI                            │
│                       (PySide6 / Qt 6 QMainWindow)                     │
│                                                                        │
│  [Dashboard]  [Live Surveillance]  [Video Analysis]  [Incident Center] │
│  [Evidence Vault]  [Blockchain Explorer]  [Cyber SOC]  [PDF Reports]  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Qt Signals / Slots
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     BACKGROUND WORKER LAYER (QThreads)                 │
│                                                                        │
│   VideoAnalysisWorker         ReportWorker          LiveStreamWorker   │
└─────────┬───────────────────────────────┬──────────────────────────────┘
          │                               │
          ▼                               ▼
┌──────────────────────────────┐  ┌──────────────────────────────────────┐
│       AI & CV PIPELINE       │  │        SECURITY & CRYPTO ENGINE      │
│                              │  │                                      │
│  • VideoPreprocessor         │  │  • EvidenceHasher (SHA-256)          │
│  • Rolling 16-Frame Buffer   │  │  • DigitalSigner (Ed25519)           │
│  • ViViT Feature Extractor   │  │  • Zero-Trust Auth & MFA             │
│  • SpikingJelly LIF (SNN)    │  │  • Role-Based Access Control (RBAC)  │
│  • Multi-Factor Risk Engine  │  │  • SecurityMonitor & Tamper Demo     │
└─────────┬────────────────────┘  └───────────────┬──────────────────────┘
          │                                       │
          ▼                                       ▼
┌──────────────────────────────┐  ┌──────────────────────────────────────┐
│     EVIDENCE & VIDEO LAYER   │  │        BLOCKCHAIN LEDGER LAYER       │
│                              │  │                                      │
│  • VideoFileSource           │  │  • BlockchainAdapter Interface       │
│  • EvidenceClipExtractor     │  │  • LocalLedgerAdapter (Hash Chain)   │
│  • Overlapping Window Merge  │  │  • FabricAdapter (Hyperledger Stub)  │
└─────────┬────────────────────┘  └───────────────┬──────────────────────┘
          │                                       │
          └───────────────────┬───────────────────┘
                              ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       LOCAL DATA & REPOSITORY LAYER                    │
│                                                                        │
│   • SQLite Database (trinetra.db)                                      │
│   • Local Storage: /videos, /evidence, /thumbnails, /reports, /logs   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Data Flow & Transaction Lifecycle

When a surveillance video is processed, the system executes the following deterministic sequence:

1. **Ingestion & Validation**: `VideoFileSource.inspect()` verifies video format, FPS, resolution, duration, and frame count.
2. **Temporal Frame Buffering**: Frames are progressively decoded and added to `TemporalFrameBuffer(capacity=16)`.
3. **Neuromorphic AI Inference**:
   - Every 5th frame, the 16-frame window is converted into a normalized tensor: $[1, 16, 3, 224, 224]$.
   - `ViViTFeatureExtractor` divides each frame into $16 \times 16$ patches and runs spatial self-attention, generating spatial embeddings: $[1, 16, 192]$.
   - `SpikingThreatClassifier` feeds embeddings into SpikingJelly Leaky Integrate-and-Fire (LIF) neurons over 16 timesteps, computing mean spike firing rates.
   - `RiskEngine` calculates risk score based on threat category, confidence, and sector sensitivity.
4. **Window Aggregation & Merging**: If threats are detected, `EvidenceClipExtractor.merge_overlapping_intervals()` combines overlapping intervals (e.g. 40s and 42s detections merge into $[37\text{s}, 45\text{s}]$).
5. **Evidence Carving**: High-resolution video clip is carved from the source file and saved to `data/evidence/EVD-XXXXX.mp4`.
6. **Cryptographic Hashing**: `EvidenceHasher.calculate_sha256()` computes the file's SHA-256 digest.
7. **Digital Signature**: `DigitalSigner.sign_evidence()` signs the payload using an asymmetric Ed25519 private key.
8. **Blockchain Commitment**: `LocalLedgerAdapter.register_evidence()` creates block $N$ with $H_N = \text{SHA256}(H_{N-1} + N + T + \text{ID} + \text{Digest})$.
9. **Persistence & UI Dispatch**: Incident and evidence records are committed to SQLite; UI tables, timeline markers, and KPI metrics update asynchronously.
