# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# from match import Match
# import plotting_utils as pu

# # Load your data
# df = pd.read_csv("C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\0.csv")

# # Initialize the Dash app
# app = dash.Dash(__name__)
# match = Match("C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\0.csv")
# match.read_csv()
# match.preprocess_data()
# # Define the layout of the app
# app.layout = html.Div(
#     [
#         # Dropdown for selecting innings
#         dcc.Dropdown(
#             id="inning-dropdown",
#             options=[
#                 {"label": "Inning 1", "value": 1},
#                 {"label": "Inning 2", "value": 2},
#             ],
#             value=1,
#         ),
#         # Toggle for selecting powerplay or middle overs
#         dcc.RadioItems(
#             id="over-type-toggle",
#             options=[
#                 {"label": "Powerplay", "value": "Powerplay"},
#                 {"label": "Middle Overs", "value": "Middle Overs"},
#                 {"label": "Death Overs", "value": "Death Overs"},
#             ],
#             value="Powerplay",
#         ),
#         # Graph component
#         dcc.Graph(id="score-vs-delivery-graph"),
#     ]
# )


# # Define callback to update the graph based on user inputs
# @app.callback(
#     Output("score-vs-delivery-graph", "figure"),
#     [Input("inning-dropdown", "value"), Input("over-type-toggle", "value")],
# )
# def update_graph(inning, over_type):
#     # Filter the data based on selected inning
#     if inning == 1:
#         filtered_df = df[df["innings"] == 1]
#     elif inning == 2:
#         filtered_df = df[df["innings"] == 2]
#     else:
#         filtered_df = df.copy()  # No inning selected, use the entire DataFrame

#     # Determine the over type dynamically based on over number
#     if over_type == "Powerplay":
#         filtered_df = filtered_df[filtered_df["over"] <= 6]
#     elif over_type == "Middle Overs":
#         filtered_df = filtered_df[
#             (filtered_df["over"] >= 7) & (filtered_df["over"] <= 15)
#         ]
#     elif over_type == "Death Overs":
#         filtered_df = filtered_df[filtered_df["over"] > 15]

#     # Create the graph using Plotly Express or Plotly Graph Objects
#     fig = px.line(filtered_df, x="delivery", y="score", title="Score vs Delivery")
#     fig = pu.customize_plot_vs_score_plot(fig)

#     return fig

# def update_score_vs_delivery(inning, over_type):
#     return match.generate_plot_score_vs_delivery(inning, over_type)


# # Run the Dash app
# if __name__ == "__main__":
#     app.run_server(debug=True)



import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from match import Match

# Initialize the Dash app
app = dash.Dash(__name__)
match = Match("C:\\Users\\sufiy\\OneDrive\\Desktop\\Projects\\CricStat\\data\\0.csv")
match.read_csv()
match.preprocess_data()

# Define the layout of the app
app.layout = html.Div(
    [
        # Dropdown for selecting innings
        dcc.Dropdown(
            id="inning-dropdown",
            options=[
                {"label": "Inning 1", "value": "Inning 1"},
                {"label": "Inning 2", "value": "Inning 2"},
            ],
            value="Inning 1",
        ),
        # Toggle for selecting over type
        dcc.RadioItems(
            id="over-type-toggle",
            options=[
                {"label": "Powerplay", "value": "Powerplay"},
                {"label": "Middle Overs", "value": "Middle Overs"},
                {"label": "Death Overs", "value": "Death Overs"},
            ],
            value="Powerplay",
        ),
        # Graph component
        dcc.Graph(id="score-vs-delivery-graph"),
    ]
)


# Define callback to update the graph based on user inputs
@app.callback(
    Output("score-vs-delivery-graph", "figure"),
    [Input("inning-dropdown", "value"), Input("over-type-toggle", "value")],
)
def update_graph(inning_toggle, over_type_toggle):
    return match.generate_plot_score_vs_delivery(inning_toggle, over_type_toggle)


# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
