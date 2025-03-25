import sqlite3
import numpy as np
import random
from countries_cities import us_cities_for_db, asian_cities_for_db, european_cities_for_db, african_cities_for_db, oceania_cities_for_db, south_american_cities_for_db

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('synthetic_cities_kpi.db')
cursor = conn.cursor()

# Create a table for storing states, cities, and KPIs
cursor.execute('''
CREATE TABLE IF NOT EXISTS cities_kpis (
    id INTEGER PRIMARY KEY,
    state TEXT,
    city TEXT,
    country TEXT,
    kpi_1 REAL,
    kpi_2 REAL,
    kpi_3 REAL,
    kpi_4 REAL,
    kpi_5 REAL,
    kpi_6 REAL,
    kpi_7 REAL,
    kpi_8 REAL,
    kpi_9 REAL,
    kpi_10 REAL
)
''')

# US states with 2-4 major cities
us_states_cities = us_cities_for_db

# European countries with 2-4 major cities
europe_countries_cities = european_cities_for_db

african_countries_cities = african_cities_for_db
south_american_countries_cities = south_american_cities_for_db
asian_countries_cities = asian_cities_for_db
oceania_countries_cities = oceania_cities_for_db

# Combine all countries into a single dictionary
all_countries_cities = {**us_states_cities,
                        **europe_countries_cities,
                        **african_countries_cities,
                        **asian_countries_cities,
                        **oceania_countries_cities,
                        **south_american_countries_cities
                        }


# Function to generate random KPI data
def generate_kpi_data():
    kpi_1 = np.random.lognormal(mean=1, sigma=1) * random.randint(1, 1000)
    kpi_2 = np.random.normal(loc=50, scale=10) * random.randint(1, 1000)
    kpi_3 = np.random.normal(loc=30, scale=5) * random.randint(1, 500)
    kpi_4 = np.random.normal(loc=70, scale=15) * random.randint(1, 1000)
    kpi_5 = np.random.normal(loc=90, scale=20) * random.randint(1, 100)
    kpi_6 = np.random.normal(loc=10, scale=2) * random.randint(1, 100)
    kpi_7 = np.random.uniform(0, 1000)
    kpi_8 = np.random.exponential(scale=50)
    kpi_9 = np.random.binomial(n=100, p=0.5)  # Binomial distribution with n=100, p=0.5
    kpi_10 = np.random.exponential(scale=200)

    # Introduce some randomness and outliers
    if random.random() < 0.05:  # 5% chance for outlier
        kpi_1 *= random.randint(100, 1000)
        kpi_2 *= random.randint(50, 500)
    if random.random() < 0.02:  # 2% chance for outlier
        kpi_3 *= random.randint(-5, -1)
        kpi_4 *= random.randint(10, 1000)
    if random.random() < 0.01:  # 1% chance for outlier
        kpi_5 *= random.randint(10, 1000)
        kpi_6 *= random.randint(-10, -5)
        kpi_7 *= random.randint(100, 1000)
        kpi_8 *= random.randint(50, 500)
    if random.random() < 0.001:  # .1% chance for outlier
        kpi_9 *= random.randint(10, 1000)
        kpi_10 *= random.randint(1, 5)/10


    # Introduce some NaN values randomly
    kpi_values = [kpi_1, kpi_2, kpi_3, kpi_4, kpi_5, kpi_6, kpi_7, kpi_8, kpi_9, kpi_10]
    kpi_values = [None if random.random() < 0.01 else value for value in kpi_values]  # 1% chance of NaN

    return kpi_values


# Generate and insert the data
for country, cities in all_countries_cities.items():
    for city in cities:
        # For US states, add the state info
        state = next((state for state in us_states_cities if country == state), None)

        kpi_values = generate_kpi_data()
        cursor.execute('''
            INSERT INTO cities_kpis (state, city, country, kpi_1, kpi_2, kpi_3, kpi_4, kpi_5, kpi_6, kpi_7, kpi_8, kpi_9, kpi_10)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (state, city, country, *kpi_values))

# Commit the transaction and close the connection
conn.commit()

# Query to verify the data
cursor.execute('''SELECT * FROM cities_kpis where country is 'FI' LIMIT 10''')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
