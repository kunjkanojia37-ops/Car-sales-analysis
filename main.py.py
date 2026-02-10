import pandas as pd



# load file 
car_sales_dataframe = pd.read_csv(r"D:\python\project\car-sales-analysis\data\raw\car-sales-input.csv")
print(car_sales_dataframe)

# first rows
print(car_sales_dataframe.head())
print(car_sales_dataframe.info())

# creating columns
car_sales_dataframe["Non Taxable Amount"] = car_sales_dataframe["Price"] * car_sales_dataframe["Qty"]
car_sales_dataframe["CGST 9 %"] = car_sales_dataframe["Non Taxable Amount"] * 9/100
car_sales_dataframe["SGST 9 %"] = car_sales_dataframe["Non Taxable Amount"] * 9/100

car_sales_dataframe["Total Tax"] = car_sales_dataframe["CGST 9 %"] + car_sales_dataframe["SGST 9 %"]
print(car_sales_dataframe) # show total tax with CGST and SGST

# total payble
car_sales_dataframe.insert(7,"Total Sale",(car_sales_dataframe["Total Tax"] + car_sales_dataframe["Non Taxable Amount"]))
print(car_sales_dataframe)

# total Quantity
Total_qty = car_sales_dataframe["Qty"].sum()

# total revenue (before tax)
Total_revenue_before_tax = car_sales_dataframe["Non Taxable Amount"].sum()

# total tax collected
Total_tax = car_sales_dataframe["Total Tax"].sum()

# total sales ( after tax)
Total_sales = car_sales_dataframe["Total Sale"].sum()

# create KPI dictionary
Kpi_data = {
    "Metric" :["Total Quantity Sold",
               "Total Revenue (Before tax)",
               "Total Tax collected","Total Sale"],
               "value":[Total_qty,
                        Total_revenue_before_tax
                        ,Total_tax,Total_sales]}

KPI_df = pd.DataFrame(Kpi_data) # convert to dataframe

# export csv
output_file = r"D:\python\project\car-sales-analysis\data\processed\car-sales-output.xlsx"
car_sales_dataframe.to_excel(output_file , index= False)

with pd.ExcelWriter(output_file,engine="openpyxl",mode="a") as f:
    KPI_df.to_excel(f,sheet_name="KPI Summary",index=False)

print("we successfully complete our task.")

# show Total sales by Car Model

import matplotlib.pyplot as plt
import os
os.makedirs(r"D:\python\project\car-sales-analysis\data\processed",exist_ok=True)

print("\n Total sales by each car Model \n")
sale_by_model = car_sales_dataframe.groupby("Car Model")["Total Sale"].sum()
print(sale_by_model)

# Show total sales by each car Model in bar chart
sale_by_model.plot(kind="bar")
plt.title("Total sales by Car Model")
plt.xlabel("Car Model")
plt.ylabel("Total Sales")
plt.savefig("D:\python\project\car-sales-analysis\data\processed\sales_by_model.png",dpi =300)
plt.show()

print("Quantity of each car Model")
Qty_of_model = car_sales_dataframe.groupby("Car Model")["Qty"].sum()
print(Qty_of_model)

# Show quantity of each car Model in bar chart
sale_by_model.plot(kind="bar")
plt.title("Quantity of Car Model")
plt.xlabel("Car Model")
plt.ylabel("Car Quantity")
plt.savefig("D:\python\project\car-sales-analysis\data\processed\Quantity_of_model.png",dpi =300)
plt.show()
