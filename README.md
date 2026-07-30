---
title: Wellness Tourism Prediction
emoji: ✈️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 8501
pinned: false
---

# ✈️ Wellness Tourism Package Prediction

This Space predicts the likelihood of a customer purchasing the **Wellness Tourism Package** based on their demographic profile and sales-interaction data.

Built with **Streamlit** and an **XGBoost** classifier trained on customer data from "Visit with Us."

## How to use

1. Enter the customer's demographic details (age, occupation, gender, income, etc.)
2. Enter their interaction data (pitch duration, follow-ups, satisfaction score, etc.)
3. Click **Predict Purchase Likelihood** to see the prediction and confidence score

## Model

The underlying model is hosted separately on the Hugging Face Hub at [`rohit-tiwari04/tourism-prediction-model`](https://huggingface.co/rohit-tiwari04/tourism-prediction-model), and is loaded automatically when this app starts.