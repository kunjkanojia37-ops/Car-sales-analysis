import pandas as pd


# load file 
auto_dataframe = pd.read_csv(r"D:\python\project\car-sales-analysis\data\raw\car-sales-input.csv")
print(auto_dataframe)

# first rows
print(auto_dataframe.head())
print(auto_dataframe.info())

# creating columns
auto_dataframe["Non Taxable"] = auto_dataframe["Price"] * auto_dataframe["Qty"]
auto_dataframe["CGST 9 %"] = auto_dataframe["Non Taxable"] * 9/100
auto_dataframe["SGST 9 %"] = auto_dataframe["Non Taxable"] * 9/100

auto_dataframe["Total Tax"] = auto_dataframe["CGST 9 %"] + auto_dataframe["SGST 9 %"]
print(auto_dataframe) # show total tax with CGST and SGST

# total payble
auto_dataframe.insert(7,"Total Sale",(auto_dataframe["Total Tax"] + auto_dataframe["Non Taxable"]))
print(auto_dataframe)


# export csv
output_file = r"D:\python\project\car-sales-analysis\data\processed\car-sales-output.csv"
auto_dataframe.to_csv(output_file , index= False)
print("we successfully complete our task.")

# show Total sales by Car Model

import matplotlib.pyplot as plt

sale_by_model =auto_dataframe.groupby("Car Model")["Total Sale"].sum()

sale_by_model.plot(kind="bar")
plt.title("Total sales by Car Model")
plt.xlabel("Car Model")
plt.ylabel("Total Sales")
plt.show()