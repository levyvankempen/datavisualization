from dash import html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

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

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

# Create the layout
sidebar = html.Div(
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
                            id="team-dropdown",
                            options=[{"label": team, "value": team} for team in combined['team'].unique()],
                            value=combined['team'].unique()[0],
                            className="dropdown"
                        ),
                        html.P("Select Position:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="position-dropdown",
                            options=[{"label": position, "value": position} for position in
                                     combined['position'].unique()],
                            value=combined['position'].unique()[0],
                            className="dropdown"
                        ),
                        html.P("Select Feature:", className="dropdown-label"),
                        dcc.Dropdown(
                            id="feature-dropdown",
                            className="dropdown"
                        ),
                    ],
                ),
            ],
            style={'height': '50vh', 'margin': '8px'}
        )
    ],
)

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("barchart-container",
                               className='font-weight-bold'),
                        html.Div(id="barchart-container")
                    ]),
                dbc.Col(
                    [
                        html.P("boxplot-container",
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
                        html.P("scatterplot-container",
                               className='font-weight-bold'),
                        html.Div(id="scatterplot-container")
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
        )
    ]
)


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
            ],
        ),
    ],
    fluid=True
)

@app.callback(
    Output("feature-dropdown", "options"),
    Output("feature-dropdown", "value"),
    Input("team-dropdown", "value"),
    Input("position-dropdown", "value")
)
def update_feature_dropdown(team, position):
    mask = (combined["team"] == team) & (combined["position"] == position)

    relevant_features = position_features[position]
    feature_options = [{"label": feature, "value": feature} for feature in relevant_features if
                       feature not in ['player', 'team', 'position']]
    feature_value = feature_options[0]['value']

    return feature_options, feature_value


@app.callback(
    Output("barchart-container", "children"),
    Output("boxplot-container", "children"),
    Output("scatterplot-container", "children"),
    Input("team-dropdown", "value"),
    Input("position-dropdown", "value"),
    Input("feature-dropdown", "value"),
)
def update_visualizations(team, position, feature_y):
    mask = (combined["team"] == team) & (combined["position"] == position)
    filtered_df = combined[mask]

    position_mask = (combined["position"] == position)
    position_df = combined[position_mask]

    # Create your visualizations using the filtered_df DataFrame
    barchart = SimpleBarChart("Barchart 1", "player", feature_y, filtered_df)
    boxplot = BoxPlot("Box Plot", "position", feature_y, position_df)
    scatterplot = ScatterPlot("Scatter Plot", "player", feature_y, position_df)

    # Add your visualizations as children to the container
    return html.Div([barchart], className="graph_card"), html.Div([boxplot], className="graph_card"), html.Div(
        [scatterplot], className="graph_card")


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
