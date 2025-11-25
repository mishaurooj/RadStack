# 🧠 RadStack: Unsupervised Risk‑Adaptive Access Control for OpenStack  
---

## 📌 Overview  
RadStack is an **unsupervised, risk‑adaptive access‑control framework** for **OpenStack Keystone**, combining anomaly detection, explainability, and risk‑based decisioning.  
This README includes **fully integrated figures** from the `Results/plots/` directory for a publication‑grade GitHub presentation.

---

## 📁 Repository Architecture  
```
RadStack/
 ├── RAdA-dataset/
 ├── Codes/
 ├── Results/
 │    └── plots/
 └── README.md
```

---

# 📊 Embedded Visualizations (From `Results/plots/`)

Below are all integrated figures:

## 1. A12 – Permutation Importance (Top 20)
![A12_perm_importance_top20](Results/plots/A12_perm_importance_top20.png)

## 2. A15 – Scalability
![A15_scalability](Results/plots/A15_scalability.png)

## 3. A17 – SHAP Summary (Isolation Forest)
![A17_shap_summary_IF](Results/plots/A17_shap_summary_IF.png)

## 4. A6 – Sensitivity Heatmap
![A6_sensitivity_heatmap](Results/plots/A6_sensitivity_heatmap.png)

## 5. Communication (V2)
![CommunicationV2](Results/plots/CommunicationV2.png)

## 6. Ensemble Structure, Component Quality, Stability
![Ensemble](Results/plots/Ensemble%20Structure,%20Component%20Quality,%20and%20Stability.png)

## 7. High Level Overview
![HighLevel](Results/plots/HighLevel.jpeg)

## 8. Policy Behavior & Middleware Overhead
![Policy Behavior](Results/plots/Policy%20Behavior,%20Enforcement%20Efficiency%20and%20Middleware%20Overhead.png)

## 9. Resilience to Noise, Attack, Temporal Drift
![Resilience](Results/plots/Resilience%20to%20Noise,%20Attack,%20and%20Temporal%20Drift.png)

## 10. Scalability & Preprocessing Sensitivity
![Scalability Preprocessing](Results/plots/Scalability%20and%20Preprocessing%20Sensitivity.png)

## 11. Dataset Visualization (1)
![Dataset1](Results/plots/dataset%20(1).png)

## 12. Dataset Visualization (2)
![Dataset2](Results/plots/dataset%20(2).png)

## 13. Feature Ablation
![feature-ablation](Results/plots/feature-ablation.png)

## 14. Processing Time Histogram
![hist_processing](Results/plots/hist_processing_time_ms.png)

## 15. Hyperparameter Sensitivity
![hypersens](Results/plots/hyperparameterSensitivty.png)

## 16. Policy Cost (Top 20)
![policy_cost](Results/plots/policy_top20_cost.png)

## 17. Scaling Methods
![scaling_methods](Results/plots/scalingmethods.png)

---

# 📘 Model Summary  
- **Ensemble:** Isolation Forest, LOF, OCSVM  
- **Fusion:** Rank + weighted ensemble (0.5 : 0.2 : 0.3)  
- **Dataset:** 222k events, 31 engineered features  
- **Performance:**  
  - F1 ≈ 0.992  
  - ROC‑AUC ≈ 0.9993  
  - Overhead ≈ 11.6%

---

# 🧩 Reproducibility  
```bash
git clone https://github.com/mishaurooj/RadStack.git
cd RadStack
pip install -r requirements.txt
```

---

# 📝 Citation  
```bibtex
@article{radstack2025,
  title={RadStack: An Unsupervised Risk-Adaptive Access Control Framework for OpenStack},
  author={Muhammad Afaq and Misha Urooj Khan and Ahmad Suleman},
  journal={IEEE Transactions on Cloud Computing},
  year={2025}
}
```

---

# 🔐 License  
CC BY‑NC‑SA 4.0 — non‑commercial reuse with attribution.

