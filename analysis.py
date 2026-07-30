# ==========================
# Weather Data Analysis
# ==========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("weather.csv")

# Display Dataset
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Highest and Lowest Temperature
print("\nHighest Temperature")
print(df.loc[df["Temperature"].idxmax()])

print("\nLowest Temperature")
print(df.loc[df["Temperature"].idxmin()])

# Average Values
print("\nAverage Temperature:", round(df["Temperature"].mean(),2))
print("Average Humidity:", round(df["Humidity"].mean(),2))
print("Average Rainfall:", round(df["Rainfall"].mean(),2))
print("Average Wind Speed:", round(df["Wind_Speed"].mean(),2))

# ---------------------------------
# Temperature Trend
# ---------------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ---------------------------------
# Humidity Trend
# ---------------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Humidity"], marker="o", color="green")
plt.title("Humidity Trend")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ---------------------------------
# Rainfall Analysis
# ---------------------------------
plt.figure(figsize=(10,5))
plt.bar(df["Date"], df["Rainfall"], color="skyblue")
plt.title("Rainfall Analysis")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.show()

# ---------------------------------
# Wind Speed
# ---------------------------------
plt.figure(figsize=(10,5))
plt.scatter(df["Date"], df["Wind_Speed"], color="red")
plt.title("Wind Speed Analysis")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
plt.xticks(rotation=45)
plt.show()

# ---------------------------------
# Pressure Trend
# ---------------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Pressure"], marker="o", color="purple")
plt.title("Pressure Trend")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ---------------------------------
# Correlation Heatmap
# ---------------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ---------------------------------
# Insights
# ---------------------------------
print("\n========== KEY INSIGHTS ==========")

print("Highest Temperature :", df["Temperature"].max(), "°C")
print("Lowest Temperature :", df["Temperature"].min(), "°C")

print("Highest Rainfall :", df["Rainfall"].max(), "mm")
print("Lowest Rainfall :", df["Rainfall"].min(), "mm")

print("Highest Humidity :", df["Humidity"].max(), "%")
print("Lowest Humidity :", df["Humidity"].min(), "%")

print("Highest Wind Speed :", df["Wind_Speed"].max(), "km/h")

print("Average Pressure :", round(df["Pressure"].mean(),2), "hPa")

print("\nWeather Data Analysis Completed Successfully!")