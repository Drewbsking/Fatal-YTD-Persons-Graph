from datetime import datetime
import csv

# Function to parse dates from strings
def parse_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y")

# Read data from CSV
data_file = r'P:\My Drive\_TS\Code\Data Analysis\RSAM\240422OpenWO.csv'  # Replace 'your_data_file.csv' with the path to your CSV file
data = []
with open(data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        creation_date_str = row['Creation Date']
        data.append(creation_date_str)

# Current date
current_date = datetime.now()

# Count of entries older than 90 days
count_older_than_90_days = sum((current_date - parse_date(entry)).days > 90 for entry in data)

print("Number of entries older than 90 days:", count_older_than_90_days)
