# 🧠 RadStack: Unsupervised Risk-Adaptive Access Control for OpenStack

> **IEEE Transactions on Cloud Computing, 2025**

![Architecture](proposed-architecture.png)

![F1 Score](https://img.shields.io/badge/F1--Score-0.992-4CAF50?style=for-the-badge)
![AUC](https://img.shields.io/badge/ROC--AUC-0.9993-2196F3?style=for-the-badge)
![Latency](https://img.shields.io/badge/Latency%20Overhead-11.6%25-FFB300?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-blue?style=for-the-badge)

---

## 📘 Overview

**RadStack** is an **unsupervised, explainable, and risk-adaptive access control (RAdAC) framework** for **OpenStack Keystone**.  
It autonomously detects anomalous identity behaviors **without labeled data**, fusing geometric, density, and boundary-based anomaly detectors to dynamically enforce graded access policies.

Built atop the **Risk-Adaptive DevStack Dataset (RAdA)** — a self-collected dataset of **over 222,000 events and 31 engineered features** — RadStack achieves near-perfect accuracy and interpretability while keeping **latency overhead under 12%**.

---

## 🧩 Repository Structure

```plaintext
RadStack/
│
├── 📁 RAdA-dataset/             # Risk-Adaptive DevStack Dataset
│   ├── RAdA_parsed_struct.rar
│   ├── parser_v1.py
│  
│
├── 📁 Codes/
│   ├── 1-RadStack-visualization.ipynb
│   └── 2-RadStack-ablation-studies.ipynb
│
├── 📁 Results/
│   ├── 📁 metrics/        # Tables III–XVI results
│   ├── 📁 plots/          # Visuals (SHAP, ablations, scalability)
│   └── 📁 models/         # Saved IF, LOF, OCSVM ensembles
│
└── README.md
```

---

## 🚀 Framework Summary

| 🧩 Stage | 📝 Description |
|:--------|:---------------|
| 🧮 **Feature Engineering** | 31 attributes grouped into 5 domains — Behavioral, System-level, Semantic, Temporal, and Outcome |
| ⚙️ **Core Models** | Isolation Forest (IF), Local Outlier Factor (LOF), One-Class SVM (OCSVM) |
| 🧠 **Fusion Layer** | Rank-based + Weighted ensemble (0.5 : 0.2 : 0.3) |
| 🔐 **Policy Mapping** | Risk-adaptive tri-level decision: *Allow*, *Step-up*, *Deny* |
| 🔍 **Explainability** | SHAP & permutation importance for transparency |
| ⚡ **Performance** | **ROC-AUC = 0.999 · F1 = 0.992 · Overhead < 12%** |

---

## 🧬 Dataset: RAdA

RAdA is an **instrumented DevStack dataset** capturing **authentication, policy, and token logs** under reproducible conditions.  
Each record aggregates user and system-level indicators across five analytic perspectives:

| Domain | Example Features |
|:--------|:----------------|
| 🧠 **Behavioral (B)** | request_rate, failure_ratio |
| ⚙️ **System (S)** | processing_time_ms, core_switches |
| 🗂️ **Semantic (M)** | endpoint_class, HTTP method |
| ⏰ **Temporal (T)** | hour_of_day, off_hour_flag |
| ✅ **Outcome (O)** | status_code, success_flag |

> RAdA forms a reproducible benchmark for **unsupervised cloud identity analytics**.

---

## 📈 Experimental Results

### 🔹 Baseline Performance

| 🧪 Model | 🎯 ACC | 🧮 F1 | 📈 ROC-AUC | ⏱️ Inference (s) |
|:------|:----:|:--:|:--------:|:-------------:|
| Isolation Forest | 0.88 | 0.88 | 0.95 | 0.10 |
| Local Outlier Factor | 🟩 **0.99** | 🟩 **0.99** | 🟦 **0.996** | 1.47 |
| One-Class SVM | 🟩 **0.997** | 🟩 **0.997** | 🟦 **0.9999** | 2.05 |

---

### 🔹 Ensemble Fusion

| ⚙️ Model | 🧮 F1 | 📈 ROC-AUC | 📊 PR-AUC | ⚡ Overhead |
|:------|:--:|:--------:|:-------:|:----------:|
| Unweighted Ensemble (ENS) | 🟩 **0.9925 ± 0.002** | 🟦 0.9993 | 🟦 0.9993 | 🟨 +11.6 % |
| Weighted Ensemble (W-ENS) | 0.9920 | 0.9986 | 0.9977 | +11.6 % |

---

### 🔹 Policy Distribution

| Decision | % Requests | Expected Cost |
|:----------|:-----------:|:--------------:|
| ✅ Allow | 87 % | 1.7 × 10⁵ |
| ⚠️ Step-Up | 8 % | 2.0 × 10⁵ |
| ⛔ Deny | 5 % | 4.4 × 10⁵ |

---

### 🔹 Sensitivity & Scaling

| Test | Result |
|:-----|:--------|
| Contamination 0.03–0.12 | ROC-AUC > 🟩 **0.9995** |
| Gaussian noise (2× var) | < 4 % degradation |
| Temporal drift (5 folds) | AUC > 🟩 **0.96** |
| Scaling effect | Min-Max normalization optimal (AUC = 0.995) |
| Runtime (222k samples) | Fit ≈ 4.6 s  · Infer ≈ 5 s |

---

## 🔍 Explainability

**Top SHAP & Permutation Features:**  
📦 `response_size_bytes` · 🕒 `processing_time_ms` · 🧩 `num_headers` · ✅ `status_code`  

> These features explain **> 50 % of anomaly variance**, ensuring transparent IAM decisions.

| SHAP Summary | Permutation Importance |
|:--------------|:----------------------|
| ![SHAP](Results/plots/A17_shap_summary_IF.png) | ![Perm](Results/plots/A12_perm_importance_top20.png) |

---

## ⚖️ Comparative Evaluation

| Reference | Domain | Interpret. | F1 | AUC | Latency (%) |
|:-----------|:--------|:-----------:|:--:|:--:|:--:|
| Gutierrez et al. (2024) | IDS | Low | 0.951 | 0.962 | 21.3 |
| Mahmud & Lendák (2024) | Synthetic | Mid | 0.958 | 0.975 | 18.6 |
| Asgarov et al. (2024) | Endpoints | Low | 0.950 | 0.963 | 16.8 |
| Ding et al. (2025) | Time-Series | High | 0.987 | 0.989 | 38.4 |
| Wang et al. (2025) | Graph | High | 0.988 | 0.993 | 34.1 |
| 🧠 **RadStack (ours)** | IAM (OpenStack) | 🟩 **High** | 🟩 **0.992** | 🟦 **0.995** | 🟨 **11.7** |

---

## 🧪 Ablation Insights

| Ablation | Removed | Observation |
|:----------|:--------|:-------------|
| A2 | Behavioral | ↓ Precision –5 % |
| A3 | System | ↓ Recall –11 % |
| A4 | Semantic | Minor change |
| A5 | Temporal | Negligible impact |
| A13 | Noise & Missing | < 4 % degradation |
| A20 | Bootstrap | Significant improvement *(p = 0.0005)* |

---

## ⚙️ Reproducibility

```bash
# Clone and install
git clone https://github.com/mishaurooj/RadStack.git
cd RadStack
pip install -r requirements.txt

# Run notebooks
jupyter notebook Codes/1-RadStack-visualization.ipynb
jupyter notebook Codes/2-RadStack-ablation-studies.ipynb
```

---

## 🧾 Citation

```bibtex
@article{radstack2025,
  title={RadStack: An Unsupervised Risk-Adaptive Access Control Framework for OpenStack},
  author={Muhammad Afaq and Misha Urooj Khan and Ahmad Suleman},
  journal={IEEE Transactions on Cloud Computing},
  year={2025},
  note={Dataset: Risk-Adaptive DevStack Dataset (RAdA)}
}
```

---

## 🪪 License

**CC BY-NC-SA 4.0** — for academic and non-commercial use with attribution.

---

## 🌐 Summary

RadStack merges **unsupervised anomaly detection** and **risk-adaptive authorization** into a reproducible and explainable pipeline.  
It provides a **transparent, scalable, and high-precision** model for modern **cloud identity analytics**.

> “RadStack bridges the interpretability gap between classical UAD and modern XAI — enabling measurable trust in cloud identity systems.” — *IEEE TCC 2025*
