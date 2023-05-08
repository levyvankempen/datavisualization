from dash import dcc, html
import plotly.graph_objects as go


class SimpleBarChart(html.Div):
    def __init__(self, name, feature_x, feature_y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig())
            ],
        )

    def create_fig(self):
        fig = go.Figure()

        x_values = self.df[self.feature_x]
        y_values = self.df[self.feature_y]
        fig.add_trace(go.Bar(
            x=x_values,
            y=y_values,
            marker_color='rgb(200,200,200)'
        ))

        fig.update_layout(
            xaxis_title=self.feature_x,
            yaxis_title=self.feature_y,
        )

        return fig
