# 🚗 Car Sales Analysis & Profit Prediction

A complete Data Analytics and Machine Learning project built using Python, Pandas, Matplotlib, OpenPyXL, and Scikit-Learn.

This project analyzes car sales data, generates business reports, creates visualizations, exports Excel reports, and trains a Machine Learning model to predict profit.

---

# 📌 Features

## Data Analysis

* Revenue Calculation
* Profit Calculation
* Tax Calculation (CGST + SGST)
* Monthly Growth Analysis
* City-wise Profit Analysis
* Model-wise Profit Analysis

## Data Visualization

Generates:

* Profit by Model Chart
* Profit by City Chart
* Month-to-Month Growth Chart

All charts are automatically saved as PNG files.

---

# 🤖 Machine Learning

Random Forest Regression model is trained to predict profit using:

* Quantity
* Cost Price
* Selling Price
* Discount

Model Performance:

| Metric                    | Value   |
| ------------------------- | ------- |
| Mean Absolute Error (MAE) | 2965.55 |
| R² Score                  | 0.9951  |

Model is saved as:

```text
car_sales_model.joblib
```

---

# 📂 Project Structure

```text
car-sales-analysis/
│
├── main.py
│
├── data/
│   ├── raw/
│   │   └── car-sales-input.csv
│   │
│   └── processed/
│       ├── car-sales-output.xlsx
│       ├── profit_by_model.png
│       ├── profit_in_city.png
│       └── monthly_growth.png
│
├── car_sales_model.joblib
├── requirements.txt
└── README.md
```

---

# 📊 KPI Summary

The project automatically generates KPI reports:

* Total Quantity Sold
* Total Revenue
* Total Profit
* Top Performing Model
* Worst Performing Model

---

# 📈 Generated Reports

## Excel Report

```text
car-sales-output.xlsx
```

Contains:

* Full Data
* KPI Summary

Features:

* Auto-adjusted column width
* Center alignment
* Cell borders

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/kunjkanojia37-ops/car-sales-analysis.git
```

Move to project folder:

```bash
cd car-sales-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python main.py
```

Expected Output:

```text
Project executed successfully!

Mean Absolute Error: 2965.5452666666647

R-squared: 0.9951475080417692

Model saved successfully!
```

---

# 🛠 Technologies Used

* Python
* Pandas
* Matplotlib
* OpenPyXL
* Scikit-Learn
* Joblib

---

# 📚 Learning Outcomes

Through this project I learned:

* Data Cleaning
* Business KPI Analysis
* Data Visualization
* Excel Report Automation
* Machine Learning Regression
* Model Evaluation
* Model Persistence using Joblib

---

# 👨‍💻 Author

Kunj Kanojia

Aspiring Data Analyst | Python Developer | AI Enthusiast

GitHub:
https://github.com/kunjkanojia37-ops
