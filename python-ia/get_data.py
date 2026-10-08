import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from google import genai

# ===== Récuperation Emplacement =======

url = "https://geocoding-api.open-meteo.com/v1/search"
city = input('\nwhat is your city (fr) : ')

params = {
    "name": city,
    "count": 1,
    "language": "fr",
    "format": "json"
}

r = requests.get(url, params=params)
r.raise_for_status()

data_recup = r.json()
location_information = data_recup['results']
latitude = location_information[0]['latitude']
longitude = location_information[0]['longitude']

# ============= METEO API ==============

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=30)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data_meteo = response.json()

# ========= Formatage En Colonne =======

# Extract the daily data
daily_data = data_meteo['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

# ========= Creation Graphique ===========

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title(f'{city} Weather - Past 30 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# ================= Save CSV =============

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv(f'data/{city}.csv', index=False)
print(f"Data saved to data/{city}_weather.csv")