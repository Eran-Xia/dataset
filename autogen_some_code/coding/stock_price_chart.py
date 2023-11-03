# filename: stock_price_chart.py
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("stock_data.csv")

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Filter the data for YTD dates
current_year = pd.Timestamp.today().year
ytd_data = df[df['Date'].dt.year == current_year]

# Calculate the YTD price change
first_price = ytd_data.iloc[0]['Close']
ytd_data['Price Change YTD'] = ytd_data['Close'] - first_price

# Plot the chart
plt.figure(figsize=(12, 6))
plt.plot(ytd_data['Date'], ytd_data['Price Change YTD'])
plt.xlabel('Date')
plt.ylabel('Price Change YTD')
plt.title('Stock Price Change YTD')
plt.grid(True)

# Save the chart as PNG
plt.savefig('stock_price_ytd.png')

print("Chart saved as stock_price_ytd.png")