import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('TopGoalScorer.csv')

# --------------------------------------------------------------Code to Generate Bar Chart Comparing Total Goals by Club:----------------------------------
# Remove non-numeric characters and convert 'Goals' to numeric
df['Goals'] = df['Goals'].str.extract('(\d+)')
df['Goals'] = pd.to_numeric(df['Goals'])

# Group by club and calculate total goals for each club
club_comparison = df.groupby('Club')['Goals'].sum().reset_index()

# Sort clubs by total goals for better visualization
club_comparison = club_comparison.sort_values(by='Goals', ascending=False)

# Plotting a bar chart
plt.figure(figsize=(12, 6))
plt.bar(club_comparison['Club'], club_comparison['Goals'], color='skyblue')
plt.title('Total Goals by Club', fontsize=16)
plt.xlabel('Club', fontsize=12)
plt.ylabel('Total Goals', fontsize=12)
plt.xticks(rotation=90)  # Rotate x labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------Correlation Analysis----------------------------------------------------------------------
# # Remove non-numeric characters and convert 'Goals' and 'Appearances' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')
# df['Goals'] = pd.to_numeric(df['Goals'])

# df['Appearances'] = df['Appearances'].str.extract('(\d+)')
# df['Appearances'] = pd.to_numeric(df['Appearances'])

# # Calculate the correlation coefficient between goals and appearances
# correlation = df['Goals'].corr(df['Appearances'])
# print(f'Correlation between Goals and Appearances: {correlation}')

# # Scatter plot to visualize the relationship between goals and appearances
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Appearances'], df['Goals'], color='purple', alpha=0.6)
# plt.title(f'Correlation between Goals and Appearances: {correlation:.2f}', fontsize=16)
# plt.xlabel('Appearances', fontsize=12)
# plt.ylabel('Goals', fontsize=12)
# plt.grid(True)
# plt.show()
# ------------------------------------------------------------Appearance Over Time-----------------------------------------------------------------------
# # Remove non-numeric characters and convert 'Appearances' to numeric
# df['Appearances'] = df['Appearances'].str.extract('(\d+)')
# df['Appearances'] = pd.to_numeric(df['Appearances'])

# # Group by year (season) and calculate the average appearances in each season
# appearances_comparison = df.groupby('Year')['Appearances'].mean()

# # Plot average appearances over time
# plt.figure(figsize=(10, 6))
# appearances_comparison.plot(kind='line', marker='o', color='g')
# plt.title('Average Appearances per Season', fontsize=16)
# plt.xlabel('Year', fontsize=12)
# plt.ylabel('Average Appearances', fontsize=12)
# plt.grid(True)
# plt.show()

# # ---------------------------------------------------------Visualize the average goal scored over time -----------------------------------------------
# # Remove non-numeric characters and convert 'Goals' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')
# df['Goals'] = pd.to_numeric(df['Goals'])

# # Group by year (season) and calculate the average goals scored in each season
# season_comparison = df.groupby('Year')['Goals'].mean()

# # Plot average goals over time
# plt.figure(figsize=(10, 6))
# season_comparison.plot(kind='line', marker='o', color='b')
# plt.title('Average Goals per Season', fontsize=16)
# plt.xlabel('Year', fontsize=12)
# plt.ylabel('Average Goals', fontsize=12)
# plt.grid(True)
# plt.show()
# # -----------------------------------------------------Code For Comparing Seasons-----------------------------------------------------------------
# # Remove non-numeric characters and convert 'Goals' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')
# df['Goals'] = pd.to_numeric(df['Goals'])

# # Group by year (season) and calculate average goals scored in each season
# season_comparison = df.groupby('Year')['Goals'].mean().reset_index()

# # Display the result
# print(season_comparison)


# # -------------------------------------------------Code For Comparing Clubs-------------------------------------------------------------------
# # Remove non-numeric characters and convert 'Goals' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')
# df['Goals'] = pd.to_numeric(df['Goals'])

# # Group by club and calculate total goals scored by each club
# club_comparison = df.groupby('Club')['Goals'].sum().reset_index()

# # Display the result
# print(club_comparison)

# ----------------------------------------------Code for Comparing Players -----------------------------------------------------------------
# # Remove non-numeric characters and convert 'Goals' and 'Appearances' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')
# df['Goals'] = pd.to_numeric(df['Goals'])

# df['Appearances'] = df['Appearances'].str.extract('(\d+)')
# df['Appearances'] = pd.to_numeric(df['Appearances'])

# # Group by players and calculate total goals and appearances
# player_comparison = df.groupby('Player')[['Goals', 'Appearances']].sum().reset_index()

# # Display the result
# print(player_comparison)

# # -------------------------------------------------------Club Players Frequency Distribution -------------------------------------------
# # Player Frequency Distribution: Count the number of times each player appears
# player_frequency = df['Player'].value_counts()

# # Club Frequency Distribution: Count the number of times each club appears
# club_frequency = df['Club'].value_counts()

# # Display the results
# print("Player Frequency Distribution:")
# print(player_frequency)

# print("\nClub Frequency Distribution:")
# print(club_frequency)

# # ----------------------------------------------------Average Number of Appearances per Season-------------------------------------
# # Remove non-numeric characters and convert 'Appearances' to numeric
# df['Appearances'] = df['Appearances'].str.extract('(\d+)')  # Extract digits
# df['Appearances'] = pd.to_numeric(df['Appearances'])  # Convert to numeric

# # Group by 'Year' and calculate the average number of appearances per season
# avg_appearances_per_season = df.groupby('Year')['Appearances'].mean()

# # Display the result
# print(avg_appearances_per_season)


# ------------------------------------------------Average number of goals per season --------------------------------------------
# Remove non-numeric characters and convert 'Goals' to numeric
# df['Goals'] = df['Goals'].str.extract('(\d+)')  # Extract digits
# df['Goals'] = pd.to_numeric(df['Goals'])  # Convert to numeric

# # Group by 'Year' and calculate the average number of goals per season
# avg_goals_per_season = df.groupby('Year')['Goals'].mean()

# # Display the result
# print(avg_goals_per_season)

