# Import necessary libraries and modules
from dash import html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np

# Import modules for data processing and views from the application
from jbi100_app.data import get_data, get_relevant_features
from jbi100_app.views.barchart import BarChart
from jbi100_app.views.scatterplot import ScatterPlot
from jbi100_app.views.PlayerInfo import PlayerInfo
from jbi100_app.views.BarChartUpdate import SimpleBarChart
from jbi100_app.views.BoxPlotUpdate import SimpleBoxPlot

# Get the combined data from the get_data function
combined = get_data()

# Get relevant position features
useful_cols_GK, useful_cols_DF, useful_cols_MF, useful_col_FW = get_relevant_features()

# Map the relevant features to their respective player positions
position_features = {
    "GK": useful_cols_GK,
    "DF": useful_cols_DF,
    "MF": useful_cols_MF,
    "FW": useful_col_FW
}

# Map the relevant features to their respective player positions
position_features = {
    "Goalkeeper": useful_cols_GK,
    "Defender": useful_cols_DF,
    "Midfielder": useful_cols_MF,
    "Forward": useful_col_FW
}

# Create a Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

# Define a function to create a sidebar for the dashboard
def create_sidebar(id_suffix):
    # The sidebar contains dropdowns for selecting team, position, and features
    return html.Div(
        [
            dbc.Row(
                [
                    html.H5('Settings',
                            style={'margin-top': '12px', 'margin-left': '24px'})
                ],
                style={"height": "5vh"},
                className='bg-primary text-white'
            ),
            dbc.Row(
                [
                    html.Div(
                        [
                            html.P("Select Team:",
                                   style={'margin-top': '8px', 'margin-bottom': '4px'},
                                   className="dropdown-label"),
                            dcc.Dropdown(
                                id=f"team-dropdown{id_suffix}",
                                options=[{"label": team, "value": team} for team in np.sort(combined['team'].unique())],
                                value=combined['team'].unique()[0],
                                className="dropdown",
                                clearable=True,
                                searchable=True,
                                placeholder='Type or select an option...'
                            ),
                            html.P("Select Position:", className="dropdown-label"),
                            dcc.Dropdown(
                                id=f"position-dropdown{id_suffix}",
                                options=[{"label": position, "value": position} for position in
                                         combined['position'].unique()],
                                value=combined['position'].unique()[0],
                                className="dropdown",
                                clearable=True,
                                searchable=True,
                                placeholder='Type or select an option...'
                            ),
                            html.P("Select Feature:", className="dropdown-label"),
                            dcc.Dropdown(
                                id=f"feature-dropdown{id_suffix}",
                                className="dropdown",
                                clearable=True,
                                searchable=True,
                                placeholder='Type or select an option...'
                            ),
                            html.P("Select other feature to see relation:", className="dropdown-label") if id_suffix == '1' else None,
                            dcc.Dropdown(
                                id=f"feature-dropdown{id_suffix}_2",
                                className="dropdown",
                                clearable=True,
                                searchable=True,
                                placeholder='Type or select an option...'
                            ) if id_suffix == '1' else None,
                            html.P("Select player to highlight them:", className="dropdown-label") if id_suffix == '1' else None,
                            dcc.Dropdown(
                                id=f"select-player",
                                options=[{"label": player, "value": player} for player in
                                         combined['player'].unique()],
                                className="dropdown",
                                clearable=True,
                                searchable=True,
                                placeholder='Type or select an option...'
                            ) if id_suffix == '1' else None
                        ],
                    ),
                ],
                style={'height': '50vh', 'margin': '8px'}
            )
        ],
    )


sidebar1 = create_sidebar('1')
sidebar2 = create_sidebar('2')

# Define the layout for the content of the first tab
content_tab1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            className='font-weight-bold'),
                        html.Div(id="player-info-container")
                    ])
            ],
            style={'height': '10vh',
                   'margin-top': '16px', 'margin-left': '8px',
                   'margin-bottom': '0px', 'margin-right': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="barchart-container")
                    ]),
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="boxplot-container")
                    ])
            ],
            style={'height': '50vh',
                   'margin-top': '0px', 'margin-left': '8px',
                   'margin-bottom': '8px', 'margin-right': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="scatterplot-container")
                    ]),
            ],
            style={'height': '50vh',
                   'margin-top': '20px', 'margin-left': '8px',
                   'margin-bottom': '8px', 'margin-right': '8px'})
    ]
)

# Define the layout for the content of the second tab
content_tab2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="barchart2-container")
                    ])
            ],
            style= {'height': '50vh', 'margin': '8px'})
    ]
)

# Set the app layout
app.layout = dbc.Container(
    [
    dbc.Tabs(id='tabs', active_tab='tab-1', children=[
        dbc.Tab(label='Player Statistics', tab_id='tab-1', children=[
            dbc.Row(
                [
                    dbc.Col(sidebar1, width=3, className='bg-light'),
                    dbc.Col(content_tab1, width=9)
                ]
            )
        ]),
        dbc.Tab(label='Team Statistics',tab_id='tab-2', children=[
            dbc.Row(
                    [
                    dbc.Col(sidebar2, width=3, className='bg-light'),
                    dbc.Col(content_tab2, width=9)
                    ]
            )
        ])
    ])
])

# Define a function to get feature options and values based on selected team and position
def get_feature_options_values(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)

    relevant_features = position_features[position]
    feature_options = [{"label": feature, "value": feature} for feature in relevant_features if
                       feature not in ['player', 'team', 'position', 'club', 'age']]
    feature_value = feature_options[0]['value']

    return feature_options, feature_value

# Define callbacks for updating feature dropdowns
@app.callback(
    Output("feature-dropdown1", "options"),
    Output("feature-dropdown1", "value"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value")
)
def update_feature_dropdown_y(team, position):
    return get_feature_options_values(team, position)

@app.callback(
    Output("feature-dropdown1_2", "options"),
    Output("feature-dropdown1_2", "value"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value")
)
def update_feature_dropdown_x(team, position):
    feature_options, _ = get_feature_options_values(team, position)
    # Choose the second feature from the list for this dropdown
    feature_value = feature_options[1]['value'] if len(feature_options) > 1 else feature_options[0]['value']
    return feature_options, feature_value


@app.callback(
    Output("feature-dropdown2", "options"),
    Output("feature-dropdown2", "value"),
    Input("team-dropdown2", "value"),
    Input("position-dropdown2", "value")
)
def update_feature_dropdown(team, position):
    return get_feature_options_values(team, position)

# Define callback for updating player dropdown
@app.callback(
    Output("select-player", "options"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value")
)
def update_player_dropdown(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)
    filtered_df = combined[mask]
    player_options = [{"label": player, "value": player} for player in filtered_df['player']]

    return player_options

# Define callback for updating player info
@app.callback(
    Output("player-info-container", "children"),
    Input("select-player", "value"),
)
def update_player_info(selected_player):
    # Assuming 'combined' is your DataFrame and 'player' is the column with player names
    player_data = combined[combined['player'] == selected_player].iloc[0]

    # Create the PlayerInfo component
    player_info = PlayerInfo(player_data)

    return player_info.get_component()

# Define callback for updating visualizations in the first tab
@app.callback(
    Output("barchart-container", "children"),
    Output("boxplot-container", "children"),
    Output("scatterplot-container", "children"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value"),
    Input("feature-dropdown1", "value"),
    Input("feature-dropdown1_2", "value"),
    Input("select-player", "value")
)
def update_visualizations_tab1(team, position, feature_y, feature_x, selected_player):
    mask = (combined["team"] == team) & (combined["position"] == position)
    filtered_df = combined[mask]

    position_mask = (combined["position"] == position)
    position_df = combined[position_mask]

    # Create the visualizations using the filtered_df DataFrame
    barchart = SimpleBarChart("What are the statistics of the players?", "player", feature_y, filtered_df, selected_player)
    boxplot = SimpleBoxPlot("How is the statistic compared to the average?", "position", feature_y, position_df, selected_player)
    scatterplot = ScatterPlot("How does the statistic relate to other statistics?", feature_x, feature_y, position_df, selected_player)

    # Add the visualizations as children to the container
    return html.Div([barchart], className="graph_card"), html.Div([boxplot], className="graph_card"), html.Div(
        [scatterplot], className="graph_card")

# Define callback for updating visualizations in the second tab
@app.callback(
    Output("barchart2-container", "children"),
    Input("team-dropdown2", "value"),
    Input("position-dropdown2", "value"),
    Input("feature-dropdown2", "value")
)
def update_visualizations_tab2(team, position, feature_y):
    mask = (combined["team"] == team) & (combined["position"] == position)
    filtered_df = combined[mask]

    position_mask = (combined["position"] == position)
    position_df = combined[position_mask]

    aggregate_df = combined.groupby(["team"], as_index=False)[feature_y].mean() # hier klopt iets niet

    # Create the visualizations using the filtered_df DataFrame
    barchart2 = BarChart("Barchart 2", "team", feature_y, aggregate_df, team, None)

    # Add the visualizations as children to the container
    return html.Div([barchart2], className="graph_card")


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
