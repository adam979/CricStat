import pandas as pd
import plotly.express as px
import plotting_utils as pu
import plotly.graph_objects as go
from color_scheme import ColorScheme


class Match:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.df = None
        self.primary_colors = None
        self.primary_color = None
        self.secondary_colors = None
        self.secondary_color = None
        self.team = None
    

    def read_csv(self):
        """Read the CSV file and load the data into a pandas DataFrame."""
        try:
            self.df = pd.read_csv(self.csv_file_path)
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file_path}' not found.")
            self.df = None

    def preprocess_data(self):
        """Preprocess the data as needed."""
        if self.df is not None:
            # Convert overs to balls
            def overs_to_balls(over):
                try:
                    overs, balls = map(int, str(over).split("."))
                    return overs * 6 + balls
                except ValueError:
                    return None

            self.df["ball"] = self.df["delivery"].apply(overs_to_balls)
            # Convert 'res' column to numeric dtype
            self.df["res"] = pd.to_numeric(self.df["res"], errors="coerce")

            # Other preprocessing steps can be added here if needed

        else:
            print("Error: DataFrame is empty. Please read CSV file first.")
    
    def set_team_colors(self,team):
        primary_colors, secondary_colors = ColorScheme.get_colors(team)
        if primary_colors and secondary_colors:
            self.primary_color = primary_colors[0]
            self.secondary_color = secondary_colors[0]
            
        else:
            print(f"Error: Color scheme not found for team '{team}'.")
        
    

    def plot_score_vs_delivery(self):
        if self.df is not None:
            # Split dataframe based on innings
            innings_1 = self.df[self.df["innings"] == 1]
            innings_2 = self.df[self.df["innings"] == 2]

            # Create a figure
            fig = px.line(title="Score Progression - Innings 1 vs Innings 2")

            # Add traces for each inning with filled areas under the curve
            fig.add_scatter(
                x=innings_1["ball"],
                y=innings_1["score"],
                mode="lines",
                name=f"{innings_1['battingteam'].iloc[0]} (Inning 1)",
                line=dict(color="#1f77b4"),
                fill="tozeroy",
            )
            fig.add_scatter(
                x=innings_2["ball"],
                y=innings_2["score"],
                mode="lines",
                name=f"{innings_2['battingteam'].iloc[0]} (Inning 2)",
                line=dict(color="#ff7f0e"),
                fill="tozeroy",
            )

            fig = pu.customize_plot_vs_score_plot(fig)
            # Show the plot
            fig.show()
        else:
            print("Error: DataFrame is empty. Please read CSV file first.")

    def calculate_run_rate(self):
        run_rates_1 = []  # Run rates for innings 1
        run_rates_2 = []  # Run rates for innings 2

        for inning in [1, 2]:
            inning_df = self.df[self.df["innings"] == inning]
            over = 0

            for i in range(5, len(inning_df), 6):
                over += 1
                total_run = inning_df.iloc[i]["score"]
                run_rate = round((total_run / over), 2)

                if inning == 1:
                    run_rates_1.append((over, run_rate))
                else:
                    run_rates_2.append((over, run_rate))

        return run_rates_1, run_rates_2

    def number_of_wicket_fell_in_an_over(self):
        wicket_inning_1 = []
        wicket_inning_2 = []

        for inning in [1, 2]:
            inning_df = self.df[self.df["innings"] == inning]
            over = 0
            prev_wicket = 0
            for i in range(5, len(inning_df), 6):
                over += 1
                currentWicket = inning_df.iloc[i]["wicketfell"] - prev_wicket
                if inning == 1:
                    wicket_inning_1.append((over, currentWicket))
                else:
                    wicket_inning_2.append((over, currentWicket))

                prev_wicket = inning_df.iloc[i]["wicketfell"]

        return wicket_inning_1, wicket_inning_2

    # Add more plotting methods for other metrics as needed
    def plot_run_rate(self):
        if self.df is not None:
            innings_1 = self.df[self.df["innings"] == 1]
            innings_2 = self.df[self.df["innings"] == 2]

            # Calculate run rates for each innings
            run_rates_1, run_rates_2 = self.calculate_run_rate()

            # Extract overs and runs for each innings
            overs_1, runs_1 = zip(*run_rates_1)
            overs_2, runs_2 = zip(*run_rates_2)

            # Get batting team names for both innings
            batting_team_1 = innings_1["battingteam"].iloc[0]
            batting_team_2 = innings_2["battingteam"].iloc[0]

            # Plot run rate over time for each innings
            fig = px.line(title="Run Rate Over Time - Innings 1 vs Innings 2")

            fig.add_scatter(
                x=overs_1,
                y=runs_1,
                mode="lines",
                name=f"{batting_team_1} (Inning 1)",
                line=dict(color="#1f77b4"),
            )
            fig.add_scatter(
                x=overs_2,
                y=runs_2,
                mode="lines",
                name=f"{batting_team_2} (Inning 2)",
                line=dict(color="#ff7f0e"),
            )

            # # Customize the plot
            fig = pu.customize_run_rate_plot(fig)
            fig = pu.add_wicket_circles(
                fig, self.number_of_wicket_fell_in_an_over(), *self.calculate_run_rate()
            )
            fig.show()

        else:
            print("Error: DataFrame is empty. Please read CSV file first.")

    def plot_run_rate_bar_chart(self):
        if self.df is not None:
            innings_1 = self.df[self.df["innings"] == 1]
            innings_2 = self.df[self.df["innings"] == 2]
            
            # Get batting team names for both innings
            batting_team_1 = innings_1["battingteam"].iloc[0]
            batting_team_2 = innings_2["battingteam"].iloc[0]
            
            # Set primary and secondary colors for both batting teams
            self.set_team_colors(batting_team_1)
            primary_color_1 = self.primary_color
            self.set_team_colors(batting_team_2)
            primary_color_2 = self.primary_color
            
            # Calculate run rates for each innings
            run_rates_1, run_rates_2 = self.calculate_run_rate()

            # Extract overs and runs for each innings
            overs_1, runs_1 = zip(*run_rates_1)
            overs_2, runs_2 = zip(*run_rates_2)

            # Create a bar chart for run rate over time
            fig = go.Figure()
            
            # Add bar traces for each inning
            fig.add_trace(
                go.Bar(
                    x=overs_1,
                    y=runs_1,
                    name=f"{batting_team_1} (Inning 1)",
                    marker_color=primary_color_1,
                )
            )
            fig.add_trace(
                go.Bar(
                    x=overs_2,
                    y=runs_2,
                    name=f"{batting_team_2} (Inning 2)",
                    marker_color=primary_color_2,
                )
            )
            
            fig = pu.customize_bar_chart(fig, 20)
            fig = pu.add_wicket_circles_for_bar_chart(
                fig,
                *self.number_of_wicket_fell_in_an_over(),
                *self.calculate_run_rate(),
            )
            
            fig.show()
        else:
            print("Error: DataFrame is empty. Please read CSV file first.")

    
    def plot_scatter_chart(self):
        if self.df is not None: 
            
            df_res_0 = self.df[self.df["res"] == 0]

            # Plot the scatter plot with different colors based on innings for res=0
            fig = px.scatter(
                df_res_0,
                x="delivery",
                y="innings",
                color="innings",
                color_discrete_sequence=px.colors.qualitative.Set1,
                title="Scatter Plot of RES = 0 vs Over",
            )

            # Update layout
            fig.update_layout(
                xaxis_title="Overs", 
                yaxis_title="Innings", 
                height=300,
                font=dict(family="Arial, sans-serif", size=12, color="black")
            )
            fig.update_traces(marker=dict(size=12, opacity=0.8))

            # Set x-axis tick mode and initial tick value
            fig.update_xaxes(tickmode="linear", tick0=1, dtick=1)
            
            # Set y-axis tick mode and initial tick value
            fig.update_yaxes(tickmode="linear", tick0=0, dtick=1)
            
            fig.show()
        else:
            print("Error: DataFrame is empty. Please read CSV file first.")

        # Show plot



# Test the Match class
if __name__ == "__main__":
    match = Match(
        "C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\1.csv"
    )
    match.read_csv()
    match.preprocess_data()
    match.team = 'CSK'
    
    #match.plot_run_rate()
    #match.plot_score_vs_delivery()
    match.plot_run_rate_bar_chart()
    # match.plot_scatter_chart()
