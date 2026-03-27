import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 7.xlsx",sheet_name="Dataset")

#df["Revenue"]=df["Orders"]* df["AvgPrice"]

#Total Revenue
#print(df["Revenue"].sum()) (already in the excel sheet)

#Revenue by Cuisine
print("\nRevenue by Cuisine\n",df.groupby("Cuisine")["Revenue"].sum().sort_values(ascending=False))

#Revenue by City
print("\nRevenue by City\n",df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

#Revenue by Restaurant
print("\nRevenue by Restaurant\n",df.groupby("Restaurant")["Revenue"].sum().sort_values(ascending=False))

#Avg Delivery Time
print("\nAvg delivery time\n",df.groupby("Cuisine")["DeliveryTime_Min"].mean().sort_values(ascending=False))

#Visualization
df.groupby("Cuisine")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Cuisine")
plt.show()

df.groupby("Restaurant")["Revenue"].sum().plot(kind="pie")
plt.title("Revenue by Restaurant")
plt.show()

df.groupby("OrderDate")["Orders"].sum().plot(kind="line")
plt.title("Orders by OrderDate")
plt.show()
