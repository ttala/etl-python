import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL to scrap
URL = "https://en.wikipedia.org/wiki/List_of_airports_in_France"

response = requests.get(URL)
response.raise_for_status()

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables with class "wikitable"
tables = soup.find_all('table', {'class': 'wikitable'})


airport_data = []
current_date = datetime.now().strftime("%d/%m/%Y")
for table in tables:
    headers = [th.get_text(strip=True) for th in table.find_all('th')]

    # Determine if the table includes the expected headers
    if any("IATA" in h for h in headers):
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                # Filtering for non empty icao code
                if cols[2].get_text(strip=True):
                    city = cols[0].get_text(strip=True)
                    airport_name = cols[3].get_text(strip=True)
                    iata_code = cols[2].get_text(strip=True)
                    icao_code = cols[1].get_text(strip=True)

                    airport_data.append({
                        'Airport Name': airport_name,
                        'City': city,
                        'ICAO': icao_code,
                        'IATA': iata_code
                    })

# Convert to DataFrame
df = pd.DataFrame(airport_data)

# Drop empty or invalid IATA codes (optional)
df = df[df['IATA'] != '']

#Add column to hold current date 
df['Exported date'] = current_date

# Save to CSV
df.to_csv('_airports.csv', index=False)

# Print result
print(df.head())
