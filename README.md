# Doctor Grade: The Approval Detective

**AI Model for Academic Performance Prediction in STEM Courses (UFFS Chapecó)**

---

## Overview

Machine learning project to predict student approval/failure in Computer Science, Mathematics, and Environmental Engineering courses at UFFS, based on parameters such as attendance, professor, course, and academic history.

---

## Main Achievements ✨

- **Final accuracy of 89.56%** (improvement of **16.87%** since 1st iteration).
- **AUC-ROC of 0.9545** and **Recall of 85.92%** for the "failed" class.
- Identification of **key variables** such as `professor`, `ccr` (course), and `attendance`.
- Correction of **critical inconsistencies** in the data (e.g., 100% attendance with failure).
- Integration of dropout data and criteria adjustments to improve generalization.

---

## Iteration Details

### Iteration 1: Initial Model

**Approach**:

- First version with LightGBM (`LGBMClassifier`).
- Attributes: `ccr` (course), `attendance`, `professor`.
- Simple validation (train-test split).

**Results**:

- **Accuracy**: 76.63%
- **Challenge**: High percentage of false negatives (59% FN).
- **Confusion Matrix**:
  - TP (Correct approvals): 91%
  - TN (Correct failures): 41%

![Feature Importance](/src/static/feature_importance/fi_1.png)  
![Confusion Matrix](/src/static/confusion_matrix/cm_1.png)

---

### Iteration 3: Attendance Inconsistency Correction

**Improvements**:

- Exclusion of records with `attendance = 100%` and `class_status = "FAILED"` (data entry errors).

**Results**:

- **Accuracy**: 83.92% (**+7.29%** vs. Iteration 1)
- **TN (Correct failures)**: 52% (**+11%**)
- **Learning**: Inconsistent data drastically impairs failure prediction.

![Feature Importance](/src/static/confusion_matrix/cm_3.png)

---

### Iteration 4: Inclusion of Relevant Cases

**Improvements**:

- Reintegration of students who failed due to **grades** or **grades + attendance**.

**Results**:

- **Recall (Failures)**: 73.79% (**+20%** vs. Iteration 3)
- **AUC-ROC**: 0.948 (**+6%**)
- **TN**: 74% (**+22%** since 1st iteration).

![Confusion Matrix](/src/static/confusion_matrix/cm_4.png)

---

### Iteration 7-8: Recent Professor Filtering

**Improvements**:

- Restriction to active professors from 2022 onwards.
- Correction of inclusion criteria (exact class matching).

**Results**:

- **Accuracy**: 88.46% (**+4.5%** vs. Iteration 6)
- **TN**: 80% (**+6%**).

![Confusion Matrix](/src/static/confusion_matrix/cm_8.png)

---

### Iteration 9: Course Code Mapping Correction

**Improvements**:

- Adjustment of course codes (e.g., Digital Systems from `GEX016` to `GEX606`).

**Results**:

- **AUC-ROC**: 0.9607
- **TN**: 83% (**+3%**).

---

### Iteration 10: Addition of Class Time

**Improvements**:

- Inclusion of `class_time` variable to capture temporal patterns.

**Results**:

- **Recall (Failures)**: 85.92% (**+111%** vs. Iteration 1)
- **TN**: 86% (best result).

![Feature Importance](/src/static/feature_importance/fi_10.png)

<!-- <img src="/src/static/feature_importance/fi_10.png" width="750"/> -->

---

## Metrics Summary

| Iteration | Accuracy | AUC-ROC | Recall (Failed) | TN (Correct Failures) | Main Improvements |
| --------- | -------- | ------- | --------------- | --------------------- | ----------------- |
| 1         | 76.63%   | 0.7884  | 40.70%          | 41%                   | Baseline          |
| 3         | 83.92%   | 0.8927  | 52.45%          | 52%                   | Consistent data   |
| 4         | 86.60%   | 0.9480  | 73.79%          | 74%                   | Failure cases     |
| 8         | 88.46%   | 0.9610  | 80.00%          | 80%                   | Professor filter  |
| 10        | 89.56%   | 0.9545  | 85.92%          | 86%                   | `class_time` var  |

---

## Lessons Learned

- **Data > Model**: Simple corrections (e.g., 100% attendance + failure) had more impact than hyperparameter adjustments.
- **Contextual variables**: `professor` and `class_time` are as critical as `attendance`.
- **Rigorous validation**: The confusion matrix revealed initial bias in favor of the "approved" class.

---

## Next Steps 🚀

- Test class balancing techniques (e.g., SMOTE).
- Develop a web interface for real-time simulations.
