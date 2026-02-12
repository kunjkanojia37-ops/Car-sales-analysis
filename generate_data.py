import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


# -----------------------------
# CONFIGURATION
# -----------------------------
num_rows = 1000
start_date = datetime(2026, 1, 1)

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad"]
salespersons = ["Rahul", "Priya", "Amit", "Sneha", "Karan", "Neha"]

car_models = {
    "SUV-X": 950000,
    "Sedan-Z": 750000,
    "XL6-Alpha": 800000,
    "Dzire LX": 1200000,
    "Swift ZXI": 1000000,
    "Eeco Cargo": 1100000
}

fuel_types = ["Petrol", "Diesel", "Electric"]
payment_modes = ["Cash", "EMI"]

# -----------------------------
# DATA GENERATION
# -----------------------------
data = []

for i in range(num_rows):
    invoice_id = f"INV{1000 + i}"
    
    random_days = random.randint(0, 364)
    date = start_date + timedelta(days=random_days)
    month = date.strftime("%B")

    city = random.choice(cities)
    salesperson = random.choice(salespersons)
    model = random.choice(list(car_models.keys()))
    
    base_price = car_models[model]
    qty = 1

    discount = random.randint(10000, 50000)
    selling_price = base_price - discount
    cost_price = base_price * random.uniform(0.80, 0.90)

    cgst = selling_price * 0.09
    sgst = selling_price * 0.09

    fuel_type = random.choice(fuel_types)
    payment_mode = random.choice(payment_modes)

    data.append([
        invoice_id, date, month, city, salesperson,
        model, fuel_type, qty,
        round(selling_price),
        discount,
        round(cost_price),
        round(cgst),
        round(sgst),
        payment_mode
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data, columns=[
    "Invoice No", "Date", "Month", "City", "Sales Person",
    "Model", "Fuel Type", "Quantity", "Selling Price",
    "Discount", "Cost Price", "CGST", "SGST", "Payment Mode"
])

# -----------------------------
# SAVE FILE
# -----------------------------
output_path = r"D:\python\project\car-sales-analysis\data\raw\car-sales-input.csv"
df.to_csv(output_path, index=False)

print("✅ Dataset generated successfully")
print(df.head())
