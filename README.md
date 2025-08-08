# 🏡 Housing Price Prediction using Linear Regression

This project is a **Machine Learning-based Housing Price Predictor** that leverages linear regression to estimate house prices based on various area-related features.

## 📌 Project Objective

The goal of this project is to **predict house prices** using a regression model trained on the **USA Housing dataset**. The model learns patterns between house prices and area-specific factors like income, number of rooms, and population.

---

## 📊 Dataset Description

The dataset used is `USA_Housing.csv` and includes the following features:

| Feature                      | Description                                |
|-----------------------------|--------------------------------------------|
| Avg. Area Income            | Average income of residents in the area    |
| Avg. Area House Age         | Average age of the houses in the area      |
| Avg. Area Number of Rooms   | Average number of rooms per house          |
| Avg. Area Number of Bedrooms| Average number of bedrooms per house       |
| Area Population             | Population of the area                     |
| Price (Target)              | House price (in USD)                       |

---

## 🧠 Machine Learning Model

The project uses **Linear Regression** from `scikit-learn` to:

- Train the model on given features
- Evaluate performance using `R² score`
- Visualize results via scatter plots and heatmaps

---

## 📈 Performance Metrics

- **Model Type:** Linear Regression
- **Evaluation Metric:** R² Score
- The model performs well with a high R² score, indicating strong correlation between features and target price.

---

## 🚀 Streamlit App Demo
[house_price_predictor_streamlit.webm](https://github.com/user-attachments/assets/e0db750e-87bb-489e-9a43-65c4a33c0c0a)

A `Streamlit` interface is available to test predictions using user-input features:


```bash
streamlit run app.py
