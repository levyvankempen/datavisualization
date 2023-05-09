from dash import dcc, html
import plotly.graph_objs as go

class BoxPlot(html.Div):
    def __init__(self, name, x, y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.x = x
        self.y = y

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig(name))
            ],
        )

    def create_fig(self, name):
        fig = go.Figure()

        fig.add_trace(go.Box(
            y=self.df[self.y],
            x=self.df[self.x],
            name="All Players",
            marker_color='#1f77b4',
            line=dict(color='#1f77b4')
        ))

        fig.update_layout(
            title=dict(text=name, font=dict(size=18, color='#2c3e50')),
            xaxis_title=self.x,
            yaxis_title=self.y,
            plot_bgcolor='rgba(255,255,255,1)',
            margin=dict(l=0, r=0, t=30, b=0),
            font=dict(family='Arial, sans-serif',
                      size=14,
                      color='#2c3e50'),
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),
        )

        return fig
