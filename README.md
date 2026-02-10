#  Car Sales Analysis using Python

This project analyzes car sales data using **Python**, **Pandas**, and **Matplotlib**.  
It calculates taxes (CGST & SGST), total sales, exports the processed data, and visualizes total sales by car model.

---

##  Project Structure

car-sales-analysis/
│
├── data/
│ ├── raw/
│ │ └── car-sales-input.csv
│ └── processed/
│ └── car-sales-output.csv
│
├── car_sales_analysis.py
├── README.md
└── requirements.txt


---

## Input Data

The input CSV file should contain at least the following columns:

- **Car Model**
- **Price**
- **Qty**

Example:
Car Model , Price , Qty
Swift,     600000,  2
Creta,    1200000,  1


---

##  Features

- Loads car sales data from CSV
- Displays basic dataset information
- Calculates:
  - Non Taxable Amount
  - CGST (9%)
  - SGST (9%)
  - Total Tax
  - Total Sale Amount
  - KPI summary
- Exports processed data to a new CSV file
- Visualizes total sales and Quantity by car model using a bar chart

---

##  How to Run

1. **Clone the repository**
   ```bash
   git clone <repository-url>

## Install dependencies

pip install -r requirements.txt

---
## Run the script

python car_sales_analysis.py

---

data/processed/car-sales-output.csv

## Output

- Processed CSV file saved at:

 - data/processed/car-sales-output.csv

- Processed Image file saved at:

 - data\processed\sales_by_model.png
 
 - data\processed\Quantity_of_model.png



---