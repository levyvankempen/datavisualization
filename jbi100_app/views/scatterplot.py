from dash import dcc, html
import plotly.graph_objects as go


class Scatterplot(html.Div):
    def __init__(self, name, feature_x, feature_y, df, dropdown_options):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.dropdown_options = dropdown_options

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Dropdown(
                    id=f"{self.html_id}-dropdown",
                    options=self.dropdown_options,
                    value=self.dropdown_options[0]['value'],
                    style={'width': '250px'}
                ),
                dcc.Graph(id=f"{self.html_id}-graph")
            ],
        )

    def update(self, feature_x, feature_y):
        fig = go.Figure()

        x_values = self.df[feature_x]
        y_values = self.df[feature_y]
        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker_color='rgb(200,200,200)'
        ))
        fig.update_traces(mode='markers', marker_size=10)
        fig.update_layout(
            yaxis_zeroline=False,
            xaxis_zeroline=False,
            dragmode='select'
        )
        fig.update_xaxes(fixedrange=True)
        fig.update_yaxes(fixedrange=True)

        fig.update_layout(
            xaxis_title=feature_x,
            yaxis_title=feature_y,
        )

        return fig
