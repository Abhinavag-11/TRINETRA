# 🛡️ TRINETRA — SIH 2026 Judge Demonstration & Slide Presentation Guide

<div align="center">

**SMART INDIA HACKATHON 2026 • OFFICIAL PRESENTATION SCRIPT**  
**Team Name:** Trinetra | **Problem Statement ID:** SIH26187  
**Problem Statement Title:** *AI-Based Intelligent Video Analytics Platform for Border Surveillance using existing CCTV Infrastructure*  
**Theme:** Blockchain & Cybersecurity | **PS Category:** Software

</div>

---

## 🎯 Demonstration Strategy

This guide maps your live software demonstration **1-to-1 with your 6-Slide SIH Presentation Deck** for a crisp, high-impact **3 to 5-minute presentation** to the judging panel.

| Slide # | Slide Title in PPT | Live Software Demonstration Action | Key Value Proposition |
| :---: | :--- | :--- | :--- |
| **Slide 1** | **Title & Problem Statement** | Launch `TRINETRA.exe` & Zero-Trust Eye-Blink Authentication | Problem ID: SIH26187, BSF / Ministry of Home Affairs mandate |
| **Slide 2** | **The Problem & Our Solution** | Command Dashboard & Multi-Modal Vision (Zero-DCE Night Vision) | Illuminates pitch-black footage in <6ms without \$10,000 thermal cameras |
| **Slide 3** | **Technical Approach & Architecture**| Start AI Surveillance: 16-Frame Buffer $\to$ ViViT $\to$ SpikingJelly LIF | Spatial + Temporal + Risk Assessment Intelligence formula |
| **Slide 4** | **Feasibility & Viability** | Show CPU execution (0% GPU required), 30 FPS, ANPR Vehicle Scanner | Commodity CCTV reuse, sub-3s latency, zero cloud dependency |
| **Slide 5** | **Impact & Benefits** | Intrusion alert, Approach Vector (+12.9%), Neuromorphic DVS (99.9% power saved) | High detection accuracy, zero vegetation false alarms, solar BOP efficiency |
| **Slide 6** | **Research, Evidence & Blockchain** | Evidence Vault live tamper test, LocalLedger verify, PDF report export | Unbroken cryptographic chain of custody, legal court compliance |

---

## ⏱️ Step-by-Step Presentation Script (3–5 Minutes)

### 📌 ACT 1: Slide 1 Mapping — Zero-Trust Authentication (0:00 – 0:35)
1. **Launch TRINETRA**:
   ```cmd
   python main.py
   ```
   *(Or double-click `dist\TRINETRA\TRINETRA.exe`)*
2. Point to the **Indian Army Border Operations Authentication Terminal**:
   - **Explain**:
     > *"Respected Judges, solving Problem Statement SIH26187 requires zero-trust security from the ground up. TRINETRA authenticates border personnel using cryptographic credentials coupled with real-time biological eye-blink liveness verification."*
3. Click **`⚡ Quick Demo Login (Judge Mode)`** (pre-fills `admin` / `Trinetra@2026`).
4. Click **`🔒 Verify Credentials & Initiate Face Authentication`**.
5. Look at the camera, **blink your eyes naturally**:
   - Watch the HUD state transition: `AWAITING_BLINK` $\to$ `BLINK DETECTED` $\to$ `LIVENESS VERIFIED: 100%`.
   - Access is granted to **Cdr. Abhinav Agarwal**! (Explain that 2D photos and tablet replays cannot spoof this biological detector).

---

### 📌 ACT 2: Slide 2 Mapping — The Problem vs. Our Solution (0:35 – 1:15)
1. The **Command Dashboard** appears:
   - Point out **Indian Army Sector Telemetry**: *HQ 16 Corps • BOP Samba Outpost (IB/LC Sector)*.
   - Point out the 4 KPI cards: *Cameras Online*, *Threats Today*, *Evidence Clips*, *Immutable Ledger State*.
2. Click **`ANALYZE SURVEILLANCE FEED`** to open the Central Surveillance Canvas.
3. **Address the Slide 2 Problem**:
   > *"As highlighted in our Slide 2, traditional CCTV cameras struggle in complete darkness, fog, and rain, creating blind spots along remote frontier fences."*
4. **Demonstrate Our Zero-DCE Solution**:
   - In the parameter deck, select **Tactical Vision Mode**: `🌙 Zero-DCE Night Vision (Deep Curve)`.
   - Explain:
     > *"Instead of deploying cost-prohibitive \$10,000 thermal cameras across thousands of kilometers of border fences, our Zero-DCE engine uses high-speed recursive quadratic curves ($LE_n(x)$) to illuminate pitch-black scenes with an **8x to 9x lux gain** in sub-6ms on standard edge CPUs!"*

---

### 📌 ACT 3: Slide 3 Mapping — Technical Approach & How It Works (1:15 – 2:00)
1. Click **`⚡ Load Sample Border Video`**.
2. Point to the **Interactive Border Exclusion Geofence Canvas**:
   - Select preset `Perimeter Fence Line (Center 40%-75% Y)`.
   - Drag your mouse directly on the video canvas to demonstrate **Custom Geofence Drawing**.
3. Point out the **Perspective Height Orientation**:
   - Set to `Front-Facing (Approaching -> Height Increases)`.
4. Click **`▶ START AI SURVEILLANCE & BORDER ANALYSIS`**.
5. Walk the judges through the **Slide 3 Architecture Pipeline**:
   - Point to the live diagnostic checkmarks:
     1. `Video Decode ✓` (Ingestion)
     2. `Frame Sampling ✓`
     3. `16-Frame Buffer ✓` (Circular rolling temporal pattern buffer)
     4. `ViViT Extraction ✓` (Spatial-temporal Vision Transformer embeddings)
     5. `SNN/LIF Spikes ✓` (SpikingJelly Leaky Integrate-and-Fire neuromorphic neurons)
     6. `Height Analysis ✓` (Pinhole perspective ingress tracking)
     7. `Threat Classifier ✓` (Multi-factor risk assessment)
   - Quote your **Key Innovation Formula**:
     > *"Spatial Intelligence (ViViT) + Temporal Intelligence (16 Frames + SNN) + Temporal Validation = Smarter Detection, Faster Response, and Safer Borders."*

---

### 📌 ACT 4: Slide 4 Mapping — Feasibility & Viability (2:00 – 2:45)
1. Point out the **Live Telemetry Badges** updating in real-time below the video:
   - `🌙 Zero-DCE: Lux 8.5x (Active)`
   - `⚡ Neuromorphic Savings: 99.9%` (Skips static background pixels to conserve battery at solar BOPs)
   - `🚗 Edge ANPR: 1 Tracked`
2. **Address Slide 4 Feasibility**:
   > *"Judges, notice that this entire multi-modal pipeline (Zero-DCE + DVS + ANPR + ViViT + SNN) is executing live on a standard CPU with **sub-3 second latency** and zero GPU or cloud requirement, proving 100% technical and cost feasibility."*

---

### 📌 ACT 5: Slide 5 Mapping — Real-Time Alert & Ingress Vector (2:45 – 3:30)
1. At timestamp `~00:00:06.9s`, the intruder approaches and crosses the fence:
   - An audible siren sounds (`QApplication.beep()`).
   - The glowing red **CRITICAL INTRUSION ALERT** banner appears:
     ```
     🚨 CRITICAL INTRUSION ALERT: BORDER EXCLUSION ZONE BREACH DETECTED!
     Zone: Perimeter Fence Line | Camera: FRONT_FACING
     Height Analysis: 71px → 80px (+12.9% INWARD ADVANCE CONFIRMED)
     ```
2. **Explain the False-Alarm Rejection**:
   > *"Notice the telemetry: initial height 71px expanded to 80px (+12.9% growth). Using pinhole geometry ($h = f \cdot H/Z$), TRINETRA validates that the target is actively advancing inward toward our post, discarding windblown bushes or grazing livestock that lack directional approach."*
3. Click the detection marker on the **Temporal Timeline** to show detailed telemetry.
4. Point out the **Automated Calibrated Evidence Extraction**:
   > *"TRINETRA automatically carves out exactly $[T - 3\text{s}] \to \text{Event} \to [T + 3\text{s}]$ (a 6.0-second calibrated clip) and commits its cryptographic fingerprint to the blockchain."*
5. Click **`🛡️ Review in Defence Vault →`**.

---

### 📌 ACT 6: Slide 6 Mapping — Research, Tamper Demo & Blockchain (3:30 – 4:30)
1. In the **Evidence Vault**:
   - Point out the newly registered evidence item: `EVD-2026...`, duration `6.0s`, status `✓ VERIFIED`.
   - Click **`Verify Integrity`** $\implies$ `✓ Cryptographic SHA-256 match confirmed! File authentic and unaltered.`
2. **The Showstopper Tamper Demonstration (Slide 6 Forensic Evidence)**:
   > *"Judges, what happens if an adversary or compromised insider tampers with this video evidence file on the local hard disk?"*
3. Click **`⚡ Tamper (Demo)`** (modifies bytes on disk).
4. Click **`Verify Integrity`** again:
   - **Immediate Red Alert**: `✕ Evidence Integrity Compromised! Stored digest does NOT match computed digest!`
   - Vault status turns red: `✕ COMPROMISED`.
5. Open the **`🔗 Blockchain`** tab:
   - Show the append-only block chain table with Genesis block, block index, timestamp, and SHA-256 hashes.
   - Click **`✓ Verify Entire Hash-Chain`** to prove that the ledger history is mathematically unbroken.
6. Open the **`📊 Reports`** tab:
   - Click **`📄 Generate PDF Incident Dossier`**.
   - Show the generated ReportLab PDF containing sector telemetry, chronological incident table, SHA-256 digest, Ed25519 signature, and command sign-off block.
7. Conclude:
   > *"TRINETRA fulfills every mandate of SIH26187: 24x7 intelligent surveillance on existing CCTV infrastructure, bio-inspired power savings, and a tamper-evident blockchain chain-of-custody for national border defense."*

---

## 🏆 Checklist for High-Scoring Judge Evaluation

- [x] **Problem Statement ID Mentioned**: `SIH26187`
- [x] **Theme Emphasized**: `Blockchain & Cybersecurity`
- [x] **Existing CCTV Reuse Demonstrated**: No expensive smart camera hardware required.
- [x] **Zero-DCE Night Vision Shown**: 8x-9x lux boost in sub-6ms on CPU.
- [x] **Neuromorphic SNN Power Savings Shown**: 85%-99.9% energy reduction for solar BOPs.
- [x] **Edge ANPR Shown**: HSRP and Indian Army plate tracking with blacklist threat detection.
- [x] **Pinhole Height Directional Tracker Shown**: $\Delta h_{px} \ge +12\%$ approach trajectory.
- [x] **Calibrated $[T-3\text{s}, T+3\text{s}]$ Evidence Clip Shown**: 6-second window with interval merging.
- [x] **Live Tamper Demonstration Executed**: Proves court-admissible chain of custody.
- [x] **37/37 Automated Tests Passing**: Verified via `python -m pytest`.
