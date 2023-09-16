import matplotlib.pyplot as plt
import pandas as pd

# Load data from the CSV file using pandas, specifying the delimiter as a comma
data = pd.read_csv('your_csv_file.csv', delimiter=',')

# Extract data into separate lists
years = data['Year']
co2 = data['CO2']
temp = data['Temperature']

# Create subplots
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Show the figure
plt.tight_layout()
plt.show()

# Save the figure as an image
plt.savefig("co2_temp_2.png")


