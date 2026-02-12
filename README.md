# 🚗 Car Sales Analysis using Python

This project performs end-to-end sales data analysis using:

- Python
- Pandas
- Matplotlib
- OpenPyXL

It calculates revenue, profit, tax, performs monthly growth analysis, generates charts, and exports a fully formatted Excel report.

---

## 📁 Project Structure

car-sales-analysis/
│
├── data/
│   ├── raw/
│   │   └── car-sales-input.csv
│   │
│   └── processed/
│       ├── car-sales-output.xlsx
│       ├── profit_by_model.png
│       └── monthly_growth.png
│
├── main.py
├── requirements.txt
└── README.md

---

## 📊 Features

### ✅ Data Processing
- Calculates:
  - Total Tax (CGST + SGST)
  - Revenue
  - Profit
- Model-wise profit analysis
- Monthly revenue & MoM growth %

### 📈 Visualization
- Profit by Model (Bar Chart)
- Month-to-Month Growth (Line Chart)

Charts are automatically saved inside the `processed` folder.

### 📑 Excel Report Automation
- Multiple sheets in one Excel file
- Auto-adjust column width
- Center alignment
- All cell borders applied
- KPI Summary sheet included

---

## 📥 Input File Format

Your `car-sales-input.csv` should contain at least:

- Model
- Date
- Quantity
- Selling price
- Cost price
- CGST
- SGST
- Discount
- Mode

---

## ▶️ How to Run

### 1️⃣ Clone the repository

git clone <your-repository-url>  
cd car-sales-analysis

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the script

python main.py

---

## 📦 Output

After execution, you will get:

📊 Charts saved in:
data/processed/

📄 Excel report:
data/processed/car-sales-output.xlsx

The Excel file contains:
- Full cleaned dataset
- KPI Summary sheet
- Proper formatting (auto-width, borders, centered text)

---

## 🧠 Skills Demonstrated

- Data Cleaning & Transformation
- GroupBy & Aggregation
- Time Series Analysis
- Data Visualization
- Excel Automation using OpenPyXL
- File Path Management using os

---

## 👨‍💻 Author

Kunj Kanojia  
Python Learner | Data Analysis Enthusiast
