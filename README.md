# 🧠 RadStack: Unsupervised Risk‑Adaptive Access Control for OpenStack  
### *(Updated & Professional GitHub‑Style README — 17 Feature Sections)*

![F1 Score](https://img.shields.io/badge/F1--Score-0.992-4CAF50?style=for-the-badge)
![AUC](https://img.shields.io/badge/ROC--AUC-0.9993-2196F3?style=for-the-badge)
![Latency](https://img.shields.io/badge/Latency%20Overhead-11.6%25-FFB300?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-blue?style=for-the-badge)

---

## 1️⃣ Overview  
RadStack is an **unsupervised, risk‑adaptive identity analytics framework** for **OpenStack Keystone**, offering high‑precision anomaly detection and transparent IAM decisions.

---

## 2️⃣ Key Features (17 Total)
1. **Unsupervised ensemble detection** (IF, LOF, OCSVM)  
2. **Formal risk‑score function R(x)**  
3. **Tri‑level policy engine (Allow / Step‑Up / Deny)**  
4. **31 engineered cloud‑IAM features**  
5. **High‑fidelity RAdA DevStack dataset (222k events)**  
6. **Rank‑based weighted fusion model**  
7. **SHAP + permutation explainability**  
8. **Noise‑robust and drift‑aware detection**  
9. **Bootstrap‑enhanced variance reduction**  
10. **Scalable to large Keystone deployments**  
11. **<12% latency overhead in production**  
12. **Reproducible Jupyter pipelines**  
13. **Full ablation suite (A1–A20)**  
14. **Cost‑aware risk distribution analysis**  
15. **Comparative evaluation with 2024–2025 literature**  
16. **Metrics, plots, and saved models included**  
17. **Open, extendable modular codebase**

---

## 3️⃣ Architecture  
```
User Request → Feature Engine → UAD Ensemble → Risk Score → Policy Mapper → Access Decision
```

---

## 4️⃣ Repository Structure  
```
RadStack/
├── RAdA-dataset/
├── Codes/
├── Results/
└── README.md
```

---

## 5️⃣ Dataset (RAdA)  
A reproducible DevStack dataset with 31 features across 5 domains.

| Domain | Example |
|-------|---------|
| Behavioral | request_rate, failure_ratio |
| System | latency_ms, switch_depth |
| Semantic | endpoint_class |
| Temporal | hour_of_day |
| Outcome | success_flag |

---

## 6️⃣ Feature Engineering  
- Normalization: Min‑Max  
- Temporal tagging  
- Semantic mapping  
- Request aggregation  

---

## 7️⃣ Core Models  
- **Isolation Forest**  
- **Local Outlier Factor**  
- **One‑Class SVM**

---

## 8️⃣ Fusion Strategy  
Weighted: **0.5 : 0.2 : 0.3**  
Also supports rank and unweighted ensembles.

---

## 9️⃣ Policy Mapping  
**Risk → Decision**  
- R < T1 → Allow  
- T1 ≤ R < T2 → Step‑Up  
- R ≥ T2 → Deny  

---

## 🔟 Performance Summary  
- **F1 = 0.992**  
- **ROC‑AUC = 0.9993**  
- **Overhead ≈ 11.6%**  
- Robust across contamination 0.03–0.12.

---

## 1️⃣1️⃣ Sensitivity & Robustness  
- Gaussian noise → <4% degradation  
- Drift folds → AUC > 0.96  
- Bootstrap → statistically significant gain  

---

## 1️⃣2️⃣ Explainability  
Top SHAP features:  
- response_size_bytes  
- processing_time_ms  
- num_headers  
- status_code  

---

## 1️⃣3️⃣ Ablation Studies  
A2: Behavioral removed → Precision –5%  
A3: System removed → Recall –11%  
A4–A5 minimal impact  
A20: Bootstrap → major stability gain  

---

## 1️⃣4️⃣ Comparative Study  
RadStack surpasses 2024–2025 anomaly detection baselines in F1, AUC, and latency.

---

## 1️⃣5️⃣ Reproducibility  
```bash
git clone https://github.com/mishaurooj/RadStack.git
cd RadStack
pip install -r requirements.txt
```

---

## 1️⃣6️⃣ Citation  
```bibtex
@article{radstack2025,
  title={RadStack: An Unsupervised Risk-Adaptive Access Control Framework for OpenStack},
  author={Muhammad Afaq and Misha Urooj Khan and Ahmad Suleman},
  journal={IEEE Transactions on Cloud Computing},
  year={2025}
}
```

---

## 1️⃣7️⃣ License  
CC BY‑NC‑SA 4.0  
For academic & non‑commercial use only.

---

## ⭐ Final Note  
RadStack integrates **trust**, **speed**, and **robustness** for next‑gen cloud IAM analytics.  
