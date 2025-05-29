import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page
URL = "https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm"

# Send a GET request
response = requests.get(URL)
#response.raise_for_status()  # Ensure we got a valid response

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find the table (it's the first one with class 'standard_tabelle')
table = soup.find("table", class_="standard_tabelle")

# Extract rows
rows = table.find_all("tr")

# List to store results
data = []

# Iterate over rows (skip header)
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) == 3:
        city_airport = cols[0].get_text(strip=True)
        country = cols[1].get_text(strip=True)
        iata_code = cols[2].get_text(strip=True)
        data.append([city_airport, country, iata_code])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["City/Airport", "Country", "IATA Code"])

# Save to CSV (optional)
df.to_csv("airport_codes.csv", index=False)

print(df.head())
