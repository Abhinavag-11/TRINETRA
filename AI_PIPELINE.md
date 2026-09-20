# TRINETRA — AI & Neuromorphic Vision Pipeline Specification

**Architecture:** Video Vision Transformer (ViViT) + Spiking Neural Network (SpikingJelly LIF)  
**Input:** 16-Frame Rolling Temporal Buffer  
**Hardware Target:** CPU-First Standard Terminals (CUDA Auto-Detect)

---

## 1. Rolling 16-Frame Temporal Analysis

Unlike traditional object detectors that evaluate isolated static images, surveillance intrusion detection requires spatial-temporal dynamics (distinguishing between normal walking, creeping, fence scaling, and aggressive rushing).

TRINETRA uses a rolling 16-frame buffer:
$$\mathcal{B}_t = \{ F_{t-15}, F_{t-14}, \dots, F_t \}, \quad F_i \in \mathbb{R}^{H \times W \times 3}$$
As new frames arrive, the oldest frame is dequeued:
$$\mathcal{B}_{t+1} = \{ F_{t-14}, \dots, F_{t+1} \}$$

Each sequence of 16 frames is normalized using standard ImageNet coefficients and resized to $224 \times 224$:
$$X_{\text{norm}} \in \mathbb{R}^{1 \times 16 \times 3 \times 224 \times 224}$$

---

## 2. ViViT Spatial Patch Embedding Extractor

Each frame in the 16-frame sequence is divided into non-overlapping spatial patches of size $P \times P$ ($16 \times 16$):
$$N = \left( \frac{H}{P} \right) \left( \frac{W}{P} \right) = \left( \frac{224}{16} \right)^2 = 14 \times 14 = 196 \text{ patches}$$

The flattened patch vectors $x_p \in \mathbb{R}^{P^2 \cdot C} = \mathbb{R}^{768}$ are linearly projected into an embedding dimension $D = 192$:
$$z_0 = [x_{\text{class}}; x_p^1 E; x_p^2 E; \dots; x_p^N E] + E_{\text{pos}}$$
where:
- $E \in \mathbb{R}^{(P^2 \cdot C) \times D}$ is the learnable patch projection matrix.
- $x_{\text{class}} \in \mathbb{R}^{1 \times D}$ is the learnable spatial `[CLS]` token.
- $E_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}$ represents 2D spatial positional embeddings.

The sequence of patches is passed through 4 Transformer encoder layers utilizing Multihead Self-Attention (MSA) and Multilayer Perceptrons (MLP):
$$z'_\ell = \text{MSA}(\text{LayerNorm}(z_{\ell-1})) + z_{\ell-1}$$
$$z_\ell = \text{MLP}(\text{LayerNorm}(z'_\ell)) + z'_\ell$$

The spatial representation of each frame is extracted via the spatial `[CLS]` token:
$$\mathbf{f}_t = z_L^0[t] \in \mathbb{R}^{192}$$
Yielding a temporal sequence of feature vectors across the 16 frames:
$$\mathbf{F} \in \mathbb{R}^{1 \times 16 \times 192}$$

---

## 3. Spiking Neural Network (SpikingJelly LIF)

The 16-frame feature embeddings are fed into a neuromorphic Spiking Neural Network implemented with **SpikingJelly**. Temporal dynamics are modeled via multi-step **Leaky Integrate-and-Fire (LIF)** neurons.

### Continuous Membrane Dynamics:
$$\tau \frac{dV(t)}{dt} = -(V(t) - V_{\text{rest}}) + I(t)$$

### Discrete Multi-Step Simulation:
At each discrete timestep $t \in \{1, 2, \dots, 16\}$:
$$H[t] = V[t-1] + \frac{1}{\tau} \left( -(V[t-1] - V_{\text{rest}}) + W \cdot \mathbf{f}_t \right)$$

### Spike Generation:
When the membrane potential $H[t]$ crosses the firing threshold $V_{\text{th}} = 1.0$, the neuron fires a discrete binary spike:
$$S[t] = \Theta(H[t] - V_{\text{th}}) = \begin{cases} 1 & \text{if } H[t] \ge V_{\text{th}} \\ 0 & \text{otherwise} \end{cases}$$

### Membrane Reset:
$$V[t] = H[t] \cdot (1 - S[t]) + V_{\text{reset}} \cdot S[t]$$
where $V_{\text{reset}} = 0$.

### Mean Firing Rate Accumulation:
The output threat classification is determined by computing the average firing rate across all $T = 16$ simulation timesteps:
$$\bar{R}_c = \frac{1}{T} \sum_{t=1}^{T} S_c[t], \quad c \in \{1, \dots, 8\}$$

The class with the highest firing rate represents the predicted action category:
$$\hat{y} = \arg\max_c (\bar{R}_c)$$

---

## 4. Multi-Factor Risk Scoring Engine

TRINETRA determines incident risk through a multi-factor formula rather than raw model confidence alone:

$$\text{RiskScore} = \text{BaseWeight}(\text{Threat}) \times \text{Confidence} \times \text{SectorSensitivity} \times \text{CameraTrust}$$

### Base Threat Taxonomy Weights ($0 - 100$):
- `NORMAL`: 5.0
- `LOITERING`: 40.0
- `UNUSUAL MOVEMENT`: 50.0
- `GROUP MOVEMENT`: 70.0
- `BOUNDARY CROSSING`: 80.0
- `VEHICLE INTRUSION`: 85.0
- `RESTRICTED AREA ACTIVITY`: 90.0
- `HUMAN INTRUSION`: 95.0

### Categorical Risk Mapping:
- **CRITICAL**: $\text{RiskScore} \ge 80.0$ or threat is `HUMAN INTRUSION` / `RESTRICTED AREA ACTIVITY`
- **HIGH**: $60.0 \le \text{RiskScore} < 80.0$
- **MEDIUM**: $35.0 \le \text{RiskScore} < 60.0$
- **LOW**: $\text{RiskScore} < 35.0$
