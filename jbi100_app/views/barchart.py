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
            marker_color='#1f77b4'
        ))

        fig.update_layout(
            xaxis_title=self.feature_x,
            yaxis_title=self.feature_y,
            plot_bgcolor='rgba(255,255,255,1)',
            margin=dict(l=0, r=0, t=30, b=0),
            font=dict(family='Arial, sans-serif',
                      size=14,
                      color='#2c3e50'),
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),
        )

        return fig
