from dash import dcc, html
import plotly.graph_objects as go


class ScatterPlot(html.Div):
    def __init__(self, name, feature_x, feature_y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                # dcc.Dropdown(
                #     id="feature-x-dropdown",
                #     options=[{"label": feature, "value": feature} for feature in df.columns if
                #              feature not in ['player', 'team', 'position']],
                #     value=feature_x,
                #     style={'width': '250px'}
                # ),
                dcc.Graph(id=self.html_id, figure=self.create_fig())
            ],
        )

    def create_fig(self):
        fig = go.Figure()

        x_values = self.df[self.feature_x]
        y_values = self.df[self.feature_y]

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(200,200,200)',
                line=dict(
                    width=2,
                    color='rgb(0,0,0)'
                )
            ),
            text=self.df['player'],
            hovertemplate='<b>%{text}</b><br><br>' + self.feature_x + ': %{x}<br>' + self.feature_y + ': %{y}<extra></extra>'
        ))

        fig.update_layout(
            xaxis_title=self.feature_x,
            yaxis_title=self.feature_y,
        )

        return fig

