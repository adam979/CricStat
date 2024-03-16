import plotly.graph_objects as go

def customize_run_rate_plot(fig):
    """Customize the appearance of the run rate plot."""
    fig.update_layout(
        xaxis_title="<b>Over</b>",
        yaxis_title="<b>Run Rate (Runs per Over)</b>",
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="black"
        ),
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='rgba(255,255,255,0.9)',
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial, sans-serif"
        ),
        legend=dict(
            title="<b>Innings</b>",
            font=dict(
                family="Arial, sans-serif",
                size=12,
                color="black"
            ),
            bgcolor='rgba(255,255,255,0.9)',
            itemsizing='constant'
        )
    )

    # Add subtle animation
    fig.update_layout(transition_duration=500)

    # Update marker and line properties for enhanced appearance
    fig.update_traces(marker=dict(size=8, opacity=0.9),
                      line=dict(width=3))

    return fig



def add_wicket_circles(fig, wicket_info, run_rates_1, run_rates_2):
    """Add circles representing fall of wickets to the plot."""
    for inning, wickets_inning in enumerate(wicket_info, start=1):
        run_rates = run_rates_1 if inning == 1 else run_rates_2
        for over, wicket_count in wickets_inning:
            runs = run_rates[over - 1][1]  # Get the runs for the corresponding over
            for i in range(wicket_count):
                # Adjust y-coordinate for each additional wicket
                fig.add_trace(go.Scatter(x=[over], y=[runs + i * 0.2], mode='markers', marker=dict(color='red', size=8),
                                         name='Wicket' if inning == 1 else None))
    return fig




def customize_plot_vs_score_plot(fig):
    # Update layout for enhanced appearance
            fig.update_layout(
                xaxis_title="<b>Delivery</b>",
                yaxis_title="<b>Score</b>",
                font=dict(
                    family="Arial, sans-serif",
                    size=12,
                    color="black"
                ),
                plot_bgcolor='rgba(255,255,255,0.9)',
                paper_bgcolor='rgba(255,255,255,0.9)',
                hovermode="x unified",  # Unified hover mode for better comparison
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=12,
                    font_family="Arial, sans-serif"
                ),
                legend=dict(
                    title="<b>Innings</b>",
                    font=dict(
                        family="Arial, sans-serif",
                        size=12,
                        color="black"
                    ),
                    bgcolor='rgba(255,255,255,0.9)',
                    itemsizing='constant'  # Ensure legend item size remains constant
                )
            )

            # Add subtle animation
            fig.update_layout(transition_duration=500)

            # Update marker and line properties for enhanced appearance
            fig.update_traces(marker=dict(size=8, opacity=0.9),
                            line=dict(width=3))

            # Add annotations for key moments in the match (optional)
            fig.add_annotation(x=60, y=100, text="Halfway Mark", showarrow=True, arrowhead=1, ax=30, ay=-30, font=dict(color="black", size=12))

            # Add custom hover information
            fig.update_traces(hovertemplate="Delivery: %{x}<br>Score: %{y}<br>")

            return fig