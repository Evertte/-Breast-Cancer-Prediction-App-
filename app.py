import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load("grid.pkl")

# Set page config
st.set_page_config(page_title="Breast Cancer Predictor", page_icon="🧬", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        text-shadow: 1px 1px 4px #000;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #ffffff;
    }
    .stApp {
        background: linear-gradient(to right, #8360c3, #2ebf91);
        padding: 10px;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #ddd;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🔬 Breast Cancer Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter the 30 diagnostic features to predict if a tumor is malignant or benign.</div>', unsafe_allow_html=True)

# Feature inputs
feature_names = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
    'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

features = []
with st.form("prediction_form"):
    st.subheader("🧾 Input Features")
    cols = st.columns(3)
    for i, name in enumerate(feature_names):
        with cols[i % 3]:
            val = st.number_input(f"{name}", key=name, format="%.3f")
            features.append(val)
    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    input_data = np.array([features])
    prediction = model.predict(input_data)[0]
    result = "🟢 Benign" if prediction == 1 else "🔴 Malignant"
    st.success(f"### ✅ Prediction: {result}")

# Feature descriptions
with st.expander("📘 Learn About These Features"):
    st.markdown("""
    These 30 features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.
    
    Each is a measurement of the **cell nucleus**, used to determine whether a tumor is likely to be cancerous or not.

    **Feature Types:**
    - **Mean**: Average value over all nuclei in the image.
    - **Error**: Variation or standard error of the feature.
    - **Worst**: Maximum value observed (not "worst" in quality, just the largest).

    **Descriptions:**

    - `radius`: Distance from the center to the edge of the nucleus.
    - `texture`: Variance in gray-scale pixel values (roughness).
    - `perimeter`: Length around the nucleus boundary.
    - `area`: Total size of the nucleus.
    - `smoothness`: Consistency of the nucleus edge.
    - `compactness`: How tightly packed the shape is (Perimeter² / Area - 1).
    - `concavity`: Depth of concave parts of the contour.
    - `concave points`: Number of concave edges.
    - `symmetry`: Symmetry of the cell shape.
    - `fractal dimension`: Complexity of the edge, like a "jaggedness" metric.
    """)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit | Dataset: Breast Cancer Wisconsin (Diagnostic)</div>', unsafe_allow_html=True)
