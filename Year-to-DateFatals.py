import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load your Excel file
file_path = r"C:\Users\abates\OneDrive - Road Commission for Oakland County\Desktop\Book1.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Crash Summaries')

# Process the data (same steps as before)
df_valid = df[~df['Date'].astype(str).str.contains('Total', case=False, na=False)]
df_valid['Year'] = pd.to_datetime(df_valid['Date']).dt.year
filtered_data = df_valid[df_valid['Year'] >= 2015]
filtered_data['Month'] = pd.to_datetime(filtered_data['Date']).dt.month

all_months = pd.DataFrame([(year, month) for year in range(2015, 2026) for month in range(1, 13)],
                          columns=['Year', 'Month'])
monthly_fatalities = filtered_data.groupby(['Year', 'Month'])['Fatal Persons'].sum().reset_index()
complete_data = pd.merge(all_months, monthly_fatalities, on=['Year', 'Month'], how='left').fillna(0)
pivot_complete = complete_data.pivot(index='Month', columns='Year', values='Fatal Persons').cumsum()

# Plot
num_years = len(pivot_complete.columns)
color_map = cm.get_cmap('tab10', num_years)
colors = [color_map(i) for i in range(num_years)]
unique_markers = ['o', 's', 'D', '^', 'v', '*', 'P', 'X', 'H', '<', '>']
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(12, 7))
for i, (year, color) in enumerate(zip(pivot_complete.columns, colors)):
    linestyle = '-' if year == 2025 else ':'
    marker_style = unique_markers[i % len(unique_markers)]
    plt.plot(pivot_complete.index, pivot_complete[year],
             marker=marker_style,
             linestyle=linestyle,
             color=color,
             label=int(year))

plt.xticks(ticks=range(1, 13), labels=month_labels)
plt.title('Year-to-Date Fatalities by Month (2015–2025): Traffic-Related Deaths')
plt.xlabel('Month')
plt.ylabel('Cumulative Fatalities (Persons)')
plt.legend(title='Year')
plt.grid(True)
plt.show()
