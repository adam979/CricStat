import pandas as pd

# Assuming all CSV files are in the same directory
input_file = "C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\modified_merged_player_data.csv"
output_file = "C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\playerdata.csv"

# Read the CSV file with default settings
merged_df = pd.read_csv(input_file)



# Print the columns of the DataFrame to confirm proper parsing
print("Columns in DataFrame:", merged_df.columns)

# Rename the columns
merged_df = merged_df.rename(
    columns={
        "Player Name": "player",
        "Team Acronym": "team",
        "Batting Hand": "battinghand",
        "Bowling Hand": "bowlinghand",
        "Bowling Type": "bowlingtype",
        "Nationality": "nationality",
    }
)

merged_df = merged_df.drop(columns= ['Team Name'])

# Write the modified DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)

print("Modified merged data saved to:", output_file)
