import plotly.graph_objects as go

def customize_run_rate_plot(fig):
    """Customize the appearance of the run rate plot."""
    fig.update_layout(
        xaxis_title="<b>Over</b>",
        yaxis_title="<b>Run Rate (Runs per Over)</b>",
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        plot_bgcolor="rgba(255,255,255,0.9)",
        paper_bgcolor="rgba(255,255,255,0.9)",
        hovermode="x unified",
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial, sans-serif"),
        legend=dict(
            title="<b>Innings</b>",
            font=dict(family="Arial, sans-serif", size=12, color="black"),
            bgcolor="rgba(255,255,255,0.9)",
            itemsizing="constant",
        ),
    )

    # Add subtle animation
    fig.update_layout(transition_duration=500)

    # Update marker and line properties for enhanced appearance
    fig.update_traces(marker=dict(size=8, opacity=0.9), line=dict(width=3))

    return fig

def add_wicket_circles(fig, wicket_info, run_rates_1, run_rates_2):
    """Add circles representing fall of wickets to the plot."""
    for inning, wickets_inning in enumerate(wicket_info, start=1):
        run_rates = run_rates_1 if inning == 1 else run_rates_2
        for over, wicket_count in wickets_inning:
            runs = run_rates[over - 1][1]  # Get the runs for the corresponding over
            for i in range(wicket_count):
                # Adjust y-coordinate for each additional wicket
                fig.add_trace(
                    go.Scatter(
                        x=[over],
                        y=[runs + i * 0.3],
                        mode="markers",
                        marker=dict(color="red", size=10),
                        name=None,
                        hoverinfo="skip",
                        showlegend=False,
                    )
                )
    return fig
def calculate_bar_width(fig, num_visible_traces):
    """
    Calculate the width of bars based on the number of visible traces.
    """
    num_visible_bars = sum(
        fig.data[i].visible == "legendonly" for i in range(num_visible_traces)
    )
    total_bar_width = 0.8  # Total width available for bars
    return total_bar_width / num_visible_bars if num_visible_bars > 0 else 0


def add_wicket_circles_for_bar_chart(
    fig, wicket_info_inning1, wicket_info_inning2, run_rates_1, run_rates_2
):
    """Add circles representing fall of wickets to the plot."""
    bar_width = 0.6  # Adjust this value according to the width of your bars

    # Plot circles for inning 1
    for over, wicket_count in wicket_info_inning1:
        runs = run_rates_1[over - 1][1]  # Get the runs for the corresponding over
        for i in range(wicket_count):
            # Calculate the x-coordinate to center the circle on top of the bar
            x_coord = over - 0.5 + bar_width / 2
            fig.add_trace(
                go.Scatter(
                    x=[x_coord],
                    y=[runs + (i * 0.3) + 0.2],
                    mode="markers",
                    marker=dict(color="red", size=10),
                    name=None,
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

    # Plot circles for inning 2
    for over, wicket_count in wicket_info_inning2:
        runs = run_rates_2[over - 1][1]  # Get the runs for the corresponding over
        for i in range(wicket_count):
            # Calculate the x-coordinate to center the circle on top of the bar
            x_coord = over - 0.075 + bar_width / 2
            fig.add_trace(
                go.Scatter(
                    x=[x_coord],
                    y=[runs + (i * 0.3) + 0.2],
                    mode="markers",
                    marker=dict(color="red", size=10),
                    name=None,
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

    return fig

def customize_bar_chart(fig, max_overs):
    """Customize the appearance of the bar chart."""
    fig.update_layout(
        title="<b>Run Rate Over Time - Innings 1 vs Innings 2</b>",
        xaxis_title="<b>Over</b>",
        yaxis_title="<b>Run Rate</b>",
        font=dict(
            family="Arial, sans-serif",
            size=14,  # Increased font size for better readability
            color="black",
        ),
        plot_bgcolor="rgba(240, 240, 240, 0.9)",  # Light gray background
        paper_bgcolor="rgba(240, 240, 240, 0.9)",  # Light gray paper background
        hovermode="x unified",  # Unified hover mode for better comparison
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial, sans-serif"),
        legend=dict(
            title="<b>Innings</b>",
            font=dict(family="Arial, sans-serif", size=12, color="black"),
            bgcolor="rgba(255, 255, 255, 0.9)",  # Light gray legend background
            itemsizing="constant",  # Ensure legend item size remains constant
        ),
        barmode="group",  # Grouped bars for better comparison
        bargap=0.1,  # Gap between bars of adjacent location coordinates
        bargroupgap=0.1,  # Gap between bars of the same location coordinate
    )

    # Add subtle animation
    fig.update_layout(transition_duration=500)

    # Update marker properties for enhanced appearance
    fig.update_traces(marker=dict(opacity=0.9))

    # Update x-axis tick labels to show every over
    fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(1, max_overs + 1)),
        tickfont=dict(
            size=12,  # Increased tick font size
            color="black",
        ),
    )

    return fig

def customize_plot_vs_score_plot(fig):
    # Update layout for enhanced appearance
    fig.update_layout(
        xaxis_title="<b>Delivery</b>",
        yaxis_title="<b>Score</b>",
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        plot_bgcolor="rgba(255,255,255,0.9)",
        paper_bgcolor="rgba(255,255,255,0.9)",
        hovermode="x unified",  # Unified hover mode for better comparison
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial, sans-serif"),
        legend=dict(
            title="<b>Innings</b>",
            font=dict(family="Arial, sans-serif", size=12, color="black"),
            bgcolor="rgba(255,255,255,0.9)",
            itemsizing="constant",  # Ensure legend item size remains constant
        ),
    )
    # fig.update_layout(
    #     updatemenus=[
    #         {
    #             "buttons": [
    #                 {
    #                     "args": [{"visible": [False, True]}, {"title": "Inning 1"}],
    #                     "label": "Inning 1",
    #                     "method": "update",
    #                 },
    #                 {
    #                     "args": [{"visible": [True, False]}, {"title": "Inning 2"}],
    #                     "label": "Inning 2",
    #                     "method": "update",
    #                 },
    #                 {
    #                     "args": [{"visible": [True, True]}, {"title": "Both Innings"}],
    #                     "label": "Both Innings",
    #                     "method": "update",
    #                 },
    #             ],
    #             "direction": "down",
    #             "showactive": True,
    #             "x": 0.5,
    #             "xanchor": "center",
    #             "y": 1.15,
    #             "yanchor": "top",
    #         },
    #     ]
    # )
    # Add subtle animation
    fig.update_layout(transition_duration=500)

    # Update marker and line properties for enhanced appearance
    fig.update_traces(marker=dict(size=8, opacity=0.9), line=dict(width=3))

    # Add annotations for key moments in the match (optional)
    fig.add_annotation(
        x=60,
        y=100,
        text="Halfway Mark",
        showarrow=True,
        arrowhead=1,
        ax=30,
        ay=-30,
        font=dict(color="black", size=12),
    )

    # Add custom hover information
    fig.update_traces(hovertemplate="Delivery: %{x}<br>Score: %{y}<br>")

    return fig
