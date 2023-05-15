from dash import html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np

from jbi100_app.data import get_data
from jbi100_app.data import get_relevant_features
from jbi100_app.views.barchart import SimpleBarChart
from jbi100_app.views.scatterplot import ScatterPlot
from jbi100_app.views.boxplot import BoxPlot

# Create data
df, keepers, defenders, midfielders, attackers, combined = get_data()

# Get relevant position features
useful_cols_GK, useful_cols_DF, useful_cols_MF, useful_col_FW = get_relevant_features()

position_features = {
    "GK": useful_cols_GK,
    "DF": useful_cols_DF,
    "MF": useful_cols_MF,
    "FW": useful_col_FW
}

position_features = {
    "Goalkeeper": useful_cols_GK,
    "Defender": useful_cols_DF,
    "Midfielder": useful_cols_MF,
    "Forward": useful_col_FW
}

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

# Create the layout
sidebar1 = html.Div(
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
                            id="team-dropdown1",
                            #options=[{"label": team, "value": team} for team in combined['team'].unique()],
                            options=[{"label": team, "value": team} for team in np.sort(combined['team'].unique())],
                            value=combined['team'].unique()[0],
                            className="dropdown",
                            clearable=True,
                            searchable=True,
                            placeholder='Type or select an option...'
                        ),
                        html.P("Select Position:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="position-dropdown1",
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
                            id="feature-dropdown1",
                            className="dropdown",
                            clearable=True,
                            searchable=True,
                            placeholder='Type or select an option...'
                        ),
                        html.P("Select other feature to see relation:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="feature-dropdown1_2",
                            className="dropdown",
                            clearable=True,
                            searchable=True,
                            placeholder='Type or select an option...'
                        )
                    ],
                ),
            ],
            style={'height': '50vh', 'margin': '8px'}
        )
    ],
)

sidebar2 = html.Div(
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
                            id="team-dropdown2",
                            #options=[{"label": team, "value": team} for team in combined['team'].unique()],
                            options=[{"label": team, "value": team} for team in np.sort(combined['team'].unique())],
                            value=combined['team'].unique()[0],
                            className="dropdown"
                        ),
                        html.P("Select Position:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="position-dropdown2",
                            options=[{"label": position, "value": position} for position in
                                     combined['position'].unique()],
                            value=combined['position'].unique()[0],
                            className="dropdown"

                        ),
                        html.P("Select Feature:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="feature-dropdown2",
                            className="dropdown"
                        ),
                    ],
                ),
            ],
            style={'height': '50vh', 'margin': '8px'}
        )
    ],
)

content_tab1 = html.Div(
    [
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
                   'margin-top': '16px', 'margin-left': '8px',
                   'margin-bottom': '8px', 'margin-right': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="scatterplot-container")
                    ]),
                dbc.Col(
                    [
                        html.P(
                               className='font-weight-bold'),
                        html.Div(id="textcontainer")
                    ])

            ],
            style={'height': '50vh', 'margin': '8px'}
        )
    ]
)

content_tab2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("barchart2-container",
                               className='font-weight-bold'),
                        html.Div(id="barchart2-container")
                    ])
            ],
            style= {'height': '50vh', 'margin': '8px'}
        )
    ]
)


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

#
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(sidebar, width=3, className='bg-light'),
#                 dbc.Col(content, width=9)
#             ],
#         ),
#     ],
#     fluid=True
# )

@app.callback(
    Output("feature-dropdown1", "options"),
    Output("feature-dropdown1", "value"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value")
)

def update_feature_dropdown_y(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)

    relevant_features = position_features[position]
    feature_options = [{"label": feature, "value": feature} for feature in relevant_features if
                       feature not in ['player', 'team', 'position', 'club', 'age']]
    feature_value = feature_options[0]['value']

    return feature_options, feature_value

@app.callback(
    Output("feature-dropdown1_2", "options"),
    Output("feature-dropdown1_2", "value"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value")
)

def update_feature_dropdown_x(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)

    relevant_features = position_features[position]
    feature_options = [{"label": feature, "value": feature} for feature in relevant_features if
                       feature not in ['player', 'team', 'position', 'club', 'age']]
    feature_value = feature_options[0]['value']

    return feature_options, feature_value

@app.callback(
    Output("feature-dropdown2", "options"),
    Output("feature-dropdown2", "value"),
    Input("team-dropdown2", "value"),
    Input("position-dropdown2", "value")
)
def update_feature_dropdown(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)

    relevant_features = position_features[position]
    feature_options = [{"label": feature, "value": feature} for feature in relevant_features if
                       feature not in ['player', 'team', 'position', 'club', 'age']]
    feature_value = feature_options[0]['value']

    return feature_options, feature_value

@app.callback(
    Output("barchart-container", "children"),
    Output("boxplot-container", "children"),
    Output("scatterplot-container", "children"),
    Input("team-dropdown1", "value"),
    Input("position-dropdown1", "value"),
    Input("feature-dropdown1", "value"),
    Input("feature-dropdown1_2", "value"),
)
def update_visualizations_tab1(team, position, feature_y, feature_x):
    mask = (combined["team"] == team) & (combined["position"] == position)
    filtered_df = combined[mask]

    position_mask = (combined["position"] == position)
    position_df = combined[position_mask]

    # Create your visualizations using the filtered_df DataFrame
    barchart = SimpleBarChart("What are the statistics of the players?", "player", feature_y, filtered_df)
    boxplot = BoxPlot("How is the statistic compared to the average?", "position", feature_y, position_df)
    scatterplot = ScatterPlot("How does the statistic relate to other statistics", feature_x, feature_y, position_df)


    # Add your visualizations as children to the container
    return html.Div([barchart], className="graph_card"), html.Div([boxplot], className="graph_card"), html.Div(
        [scatterplot], className="graph_card")


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

    # Create your visualizations using the filtered_df DataFrame
    barchart2 = SimpleBarChart("Barchart 2", "team", feature_y, aggregate_df, team, None)

    # Add your visualizations as children to the container
    return html.Div([barchart2], className="graph_card")


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
