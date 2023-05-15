from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd


class SimpleBarChart(html.Div):
    def __init__(self, name, x, y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.x = x
        self.y = y

        if not isinstance(df, pd.DataFrame):
            raise ValueError("df must be a pandas DataFrame")
        if x not in df.columns or y not in df.columns:
            raise ValueError("x and y must be column names in df")

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig())
            ],
        )

    def create_fig(self):
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=self.df[self.x],
            y=self.df[self.y],
            name="Players",
            marker_color='#1f77b4'
        ))

        fig.update_layout(
            xaxis_title=self.x,
            yaxis_title=self.y,
            plot_bgcolor='rgba(255,255,255,1)',
            margin=dict(l=0, r=0, t=30, b=0),
            font=dict(family='Arial, sans-serif', size=14, color='#2c3e50'),
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),
            clickmode='event+select'
        )

        return fig
