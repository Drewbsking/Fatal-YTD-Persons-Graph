import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file (assuming it's in the same folder as the script)
file_name = "Seasonal Factor Table.xlsx"  # Change this if needed
df = pd.read_excel(file_name, sheet_name='Seasonal_Factor_Table')

# Define the ordered days (starting from Monday)
ordered_days = ['MONFAC', 'TUEFAC', 'WEDFAC', 'THURFAC', 'FRIFAC', 'SATFAC', 'SUNFAC']

# Define an explicit month order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Convert MONTH column to a categorical type with the desired order
df['MONTH'] = pd.Categorical(df['MONTH'], categories=month_order, ordered=True)

# Filter data for the years 2021 to 2023
df_recent = df[df['YEAR'].between(2021, 2023)]

# Determine global min and max values for a common color scale
global_min = df_recent[ordered_days].min().min()
global_max = df_recent[ordered_days].max().max()


# Function to format annotation values
def format_value(val):
    """Bold numbers if between 0.95 and 1.05."""
    return f"{val:.2f}" if not (0.95 <= val <= 1.05) else f"**{val:.2f}**"


# Create the heatmaps for each year with a common scale
for year in range(2021, 2023 + 1):
    df_year = df[df['YEAR'] == year]

    # Melt the data so each row is (MONTH, Day, Factor)
    df_heatmap = df_year.melt(
        id_vars=['MONTH'],
        value_vars=ordered_days,
        var_name="Day",
        value_name="Factor"
    )

    # Pivot to get MONTH as rows and Days as columns
    df_pivot = df_heatmap.pivot(index="MONTH", columns="Day", values="Factor")[ordered_days]

    # (Optional) If you want *all* 12 months to appear even if data is missing, do:
    # df_pivot = df_pivot.reindex(month_order)
    # This will include months that are not present in df_year, but fill them with NaN.

    # Set up the figure size
    plt.figure(figsize=(10, 6))

    # Create a diverging colormap centered at 1.0
    cmap = sns.diverging_palette(240, 10, as_cmap=True)

    # Create an annotation DataFrame
    annot_df = df_pivot.applymap(lambda v: format_value(v))

    # Create the heatmap with the same scale for all years
    ax = sns.heatmap(
        df_pivot,
        cmap=cmap,
        linewidths=0.5,
        cbar_kws={'label': 'Factor'},
        center=1.0,
        annot=annot_df,
        fmt="s",
        annot_kws={"size": 10},
        vmin=global_min,
        vmax=global_max
    )

    # Add title and labels
    plt.title(f"Seasonal Factors Heatmap ({year}) - Common Scale")
    plt.xlabel("Day of the Week")
    plt.ylabel("Month")

    # Save each heatmap as an image file
    plt.savefig(f"heatmap_{year}_common_scale.png", dpi=300)

    # Show the plot
    plt.show()

print("Heatmaps have been generated with a common scale and saved as PNG files.")
