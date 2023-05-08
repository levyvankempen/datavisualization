from jbi100_app.main import app
from jbi100_app.data import get_data
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.barchart import SimpleBarChart
from jbi100_app.views.boxplot import BoxPlot

from dash import html, dcc, html, Input, Output
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    df, keepers, defenders, midfielders, attackers, combined = get_data()

    app.layout = html.Div(
        id="app-container",
        children=[
            # Dropdowns
            html.Div(
                children=[
                    # Selecting Team
                    html.Label("Select Team:"),
                    dcc.Dropdown(
                        id="team-dropdown",
                        options=[{"label": team, "value": team} for team in combined['team'].unique()],
                        value=combined['team'].unique()[0],
                        style={'width': '250px'}
                    ),

                    # Selecting Position
                    html.Label("Select Position:"),
                    dcc.Dropdown(
                        id="position-dropdown",
                        options=[{"label": position, "value": position} for position in combined['position'].unique()],
                        value=combined['position'].unique()[0],
                        style={'width': '250px'}
                    ),

                    # Selecting Feature
                    html.Label("Select Feature:"),
                    dcc.Dropdown(
                        id="feature-dropdown",
                        style={'width': '250px'}
                    ),
                ],
                style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '20px'}
            ),

            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    html.Div(id="visualizations-container")
                ],
            ),
        ],
    )
    @app.callback(
        Output("feature-dropdown", "options"),
        Output("feature-dropdown", "value"),
        Input("team-dropdown", "value"),
        Input("position-dropdown", "value")
    )
    def update_feature_dropdown(team, position):
        mask = (combined["team"] == team) & (combined["position"] == position)
        filtered_df = combined[mask]

        feature_options = [{"label": feature, "value": feature} for feature in combined.columns if
                           feature not in ['player', 'team', 'position']]
        feature_value = feature_options[0]['value']

        return feature_options, feature_value


    # Update visualizations based on team and position selection
    @app.callback(
        Output("visualizations-container", "children"),
        Input("team-dropdown", "value"),
        Input("position-dropdown", "value"),
        Input("feature-dropdown", "value")
    )
    def update_visualizations(team, position, feature):
        mask = (combined["team"] == team) & (combined["position"] == position)
        filtered_df = combined[mask]

        position_mask = (combined["position"] == position)
        position_df = combined[position_mask]

        # Create your visualizations using the filtered_df DataFrame
        barchart = SimpleBarChart("Barchart 1", "player", feature, filtered_df)
        boxplot = BoxPlot("Box Plot", "position", feature, position_df)

        # Add your visualizations as children to the container
        return [
            barchart,
            boxplot
        ]

    app.run_server(debug=False, dev_tools_ui=False)