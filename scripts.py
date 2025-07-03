import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# # Load dataset
# df = pd.read_csv("illinois_crash_data.csv")

# # # Group by vehicle type and calculate mean and standard deviation
# # summary_stats = df.groupby("Vehicle Type")["Total Crashes"].agg(["mean", "std"]).reset_index()

# # # Rename columns for clarity
# # summary_stats.columns = ["Vehicle Type", "Mean Total Crashes", "Std Dev Total Crashes"]

# # # Display the results
# # print(summary_stats)


# # Total Crashes
# crashes_stats = df.groupby("Vehicle Type")["Total Crashes"].agg(["mean", "std"]).reset_index()
# crashes_stats.columns = ["Vehicle Type", "Mean Total Crashes", "Std Dev Total Crashes"]
# print("\nTotal Crashes Summary:")
# print(crashes_stats.to_string(index=False))

# # Fatalities
# fatalities_stats = df.groupby("Vehicle Type")["Fatalities"].agg(["mean", "std"]).reset_index()
# fatalities_stats.columns = ["Vehicle Type", "Mean Fatalities", "Std Dev Fatalities"]
# print("\nFatalities Summary:")
# print(fatalities_stats.to_string(index=False))

# # Injuries
# injuries_stats = df.groupby("Vehicle Type")["Injuries"].agg(["mean", "std"]).reset_index()
# injuries_stats.columns = ["Vehicle Type", "Mean Injuries", "Std Dev Injuries"]
# print("\nInjuries Summary:")
# print(injuries_stats.to_string(index=False))


# # Sample data — replace with actual computed values
# crash_data = {
#     "Vehicle Type": ["Bus", "Large Truck", "Motorcycle", "Other Vehicle Types", "Passenger Car", "Pickup Trucks"],
#     "Mean": [4300.6, 12500.4, 3301.2, 11762.8, 270453.2, 35670.6],
#     "Std Dev": [185.3, 536.2, 189.6, 364.1, 5952.8, 885.4]
# }

# fatality_data = {
#     "Vehicle Type": ["Bus", "Large Truck", "Motorcycle", "Other Vehicle Types", "Passenger Car", "Pickup Trucks"],
#     "Mean": [2.2, 160.4, 156.2, 70.6, 700.4, 350.0],
#     "Std Dev": [1.6, 12.0, 10.6, 6.2, 42.7, 18.3]
# }

# injury_data = {
#     "Vehicle Type": ["Bus", "Large Truck", "Motorcycle", "Other Vehicle Types", "Passenger Car", "Pickup Trucks"],
#     "Mean": [860.0, 2800.6, 2488.8, 1200.8, 65000.6, 14000.4],
#     "Std Dev": [21.5, 170.1, 55.3, 60.4, 1500.2, 480.9]
# }

# # Convert to DataFrames
# crash_df = pd.DataFrame(crash_data)
# fatality_df = pd.DataFrame(fatality_data)
# injury_df = pd.DataFrame(injury_data)

# # Function to draw each table
# def plot_summary_table(df, title, ax):
#     ax.axis('tight')
#     ax.axis('off')
#     table = ax.table(
#         cellText=np.round(df.iloc[:, 1:].values, 1),
#         rowLabels=df["Vehicle Type"],
#         colLabels=["Mean", "Std Dev"],
#         loc='center',
#         cellLoc='center'
#     )
#     table.auto_set_font_size(False)
#     table.set_fontsize(10)
#     table.scale(1.2, 1.5)
#     ax.set_title(title, fontsize=14, fontweight='bold')

# # Plot all three side by side
# fig, axs = plt.subplots(1, 3, figsize=(20, 6))
# plot_summary_table(crash_df, "Total Crashes Summary", axs[0])
# plot_summary_table(fatality_df, "Fatalities Summary", axs[1])
# plot_summary_table(injury_df, "Injuries Summary", axs[2])

# plt.tight_layout()

# # Save the figure
# plt.savefig("crash_summary_tables.png", dpi=300)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset
df = pd.read_csv("illinois_crash_data.csv")

# Compute summary statistics dynamically
crashes_stats = df.groupby("Vehicle Type")["Total Crashes"].agg(["mean", "std"]).reset_index()
crashes_stats.columns = ["Vehicle Type", "Mean", "Std Dev"]

fatalities_stats = df.groupby("Vehicle Type")["Fatalities"].agg(["mean", "std"]).reset_index()
fatalities_stats.columns = ["Vehicle Type", "Mean", "Std Dev"]

injuries_stats = df.groupby("Vehicle Type")["Injuries"].agg(["mean", "std"]).reset_index()
injuries_stats.columns = ["Vehicle Type", "Mean", "Std Dev"]

# Plot function for each summary table
def plot_summary_table(df, title, ax):
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(
        cellText=np.round(df[["Mean", "Std Dev"]].values, 1),
        rowLabels=df["Vehicle Type"],
        colLabels=["Mean", "Std Dev"],
        cellLoc='center',
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)
    ax.set_title(title, fontsize=14, fontweight='bold')

# Create side-by-side plot for all three metrics
fig, axs = plt.subplots(1, 3, figsize=(15, 6))
plot_summary_table(crashes_stats, "Total Crashes Summary", axs[0])
plot_summary_table(fatalities_stats, "Fatalities Summary", axs[1])
plot_summary_table(injuries_stats, "Injuries Summary", axs[2])

plt.tight_layout()
plt.show()
