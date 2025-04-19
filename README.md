# 🩺 Breast Cancer Prediction App

A Streamlit-powered web application that predicts whether a breast tumor is malignant or benign using machine learning. The model is trained on the **Breast Cancer dataset available via Seaborn**, which includes features extracted from digitized images of fine needle aspirates (FNA) of breast masses.

## 🔍 Features

- Predicts if a tumor is **malignant** or **benign**
- User input form for 30 real-valued features
- Clean and intuitive Streamlit UI
- Displays prediction result with model confidence
- Includes explanations for each feature

## 📊 Dataset

- **Source**: `seaborn.load_dataset('breast_cancer')`  
- **Origin**: Based on the Breast Cancer Wisconsin (Diagnostic) Dataset  
- **Samples**: 569
- **Features**: 30 real-valued features + target label (`diagnosis`)
- **Target Labels**:  
  - `M` = Malignant  
  - `B` = Benign

## 🧠 Machine Learning Model

- Supervised classification model (e.g., Logistic Regression or Random Forest)
- Preprocessing:
  - Label encoding for target
  - Feature scaling
- Evaluated on test split with high accuracy and performance

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Evertte/breast-cancer-prediction-app.git
   cd breast-cancer-prediction-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🧾 Feature Overview

Each tumor sample includes:
- **Shape Features**: Radius, Perimeter, Area
- **Texture Features**: Texture, Smoothness
- **Structural Features**: Concavity, Compactness, Symmetry, Fractal dimension
- Each measured by:
  - **Mean**
  - **Standard Error**
  - **Worst** (largest mean value of worst 3 measurements)

## 🛠️ Tools & Libraries

- Python
- Seaborn (for dataset)
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib or Seaborn for visualizations

## 📸 Screenshot

> *(Optional: Add a screenshot of your app UI here)*
> <img width="1439" alt="Screenshot 2025-04-19 at 11 34 53 AM" src="https://github.com/user-attachments/assets/0b150338-3953-44aa-beb7-41c86ff838b9" />

> <img width="1439" alt="Screenshot 2025-04-19 at 11 35 13 AM" src="https://github.com/user-attachments/assets/c5fbcbfd-e738-4894-add1-aff979131a5e" />


## 📬 Contact

Built by [Your Name]  
[GitHub](https://github.com/Evertte) • [LinkedIn](https://linkedin.com/in/Evertte)

---
