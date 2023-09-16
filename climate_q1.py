import matplotlib.pyplot as plt
import sqlite3

# Initialize empty lists to store data
years = []
co2 = []
temp = []

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Query the database to fetch data
cursor.execute("SELECT year, co2, temperature FROM climate_data")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Populate the lists with the fetched data
for row in rows:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# Close the database connection
conn.close()

# Plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
