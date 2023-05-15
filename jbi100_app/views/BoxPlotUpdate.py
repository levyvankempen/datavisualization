from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd


class SimpleBoxPlot(html.Div):
    def __init__(self, name, x, y, df, player=None):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.x = x
        self.y = y
        self.player = player

        if not isinstance(df, pd.DataFrame):
            raise ValueError("df must be a pandas DataFrame")
        if x not in df.columns or y not in df.columns:
            raise ValueError("x and y must be column names in df")
        if player and player not in df['player'].unique():
            raise ValueError(f"player {player} not found in df['player']")

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig())
            ],
        )

    def update_player(self, player):
        self.player = player
        self.graph.figure = self.create_figure()

    def create_fig(self):
        fig = go.Figure()

        fig.add_trace(go.Box(
            y=self.df[self.y],
            x=self.df[self.x],
            name="All Players",
            marker_color='#1f77b4',
            line=dict(color='#1f77b4'),
            boxpoints="all"
        ))

        if self.player:
            player_data = self.df[self.df['player'] == self.player]
            if not player_data.empty:
                fig.add_trace(go.Scatter(
                    x=[self.player] * len(player_data),
                    y=player_data[self.y],
                    mode='markers',
                    marker=dict(
                        color='Red',
                        size=12,
                        line=dict(
                            color='Red',
                            width=2
                        )
                    ),
                    name=self.player
                ))

        fig.update_layout(
            xaxis_title=self.x,
            yaxis_title=self.y,
            plot_bgcolor='rgba(255,255,255,1)',
            margin=dict(l=0, r=0, t=30, b=0),
            font=dict(family='Arial, sans-serif', size=14, color='#2c3e50'),
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),
            clickmode='select'
        )

        return fig
