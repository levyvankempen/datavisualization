from dash import dcc, html
import plotly.graph_objects as go
import numpy as np


class ScatterPlot(html.Div):
    def __init__(self, name, feature_x, feature_y, df, selected_player=None):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.selected_player = selected_player

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

        # Calculate coefficients for the polynomial (line)
        m, b = np.polyfit(x_values, y_values, 1)

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(
                size=10,
                color='#1f77b4',
            ),
            text=self.df['player'],
            hovertemplate='<b>%{text}</b><br><br>' + self.feature_x + ': %{x}<br>' + self.feature_y + ': %{y}<extra></extra>',
            name="All Players Same Position"
        ))

        # Add the regression line
        fig.add_trace(go.Scatter(
            x=x_values,
            y=m*x_values + b,
            mode='lines',
            line=dict(
                color='grey',
                dash='10px,25px'
            ),
            name="Line of Best Fit",
            visible="legendonly"
        ))

        if self.selected_player:
            player_data = self.df[self.df['player'] == self.selected_player]
            if not player_data.empty:
                fig.add_trace(go.Scatter(
                    x=player_data[self.feature_x],
                    y=player_data[self.feature_y],
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='lightsalmon',
                        line=dict(
                            color='lightsalmon',
                            width=2
                        )
                    ),
                    text=player_data['player'],
                    hovertemplate='<b>%{text}</b><br><br>' + self.feature_x + ': %{x}<br>' + self.feature_y + ': %{y}<extra></extra>',
                    name=self.selected_player
                ))

        fig.update_layout(
            xaxis_title=self.feature_x,
            yaxis_title=self.feature_y,
            clickmode='event+select'
        )

        return fig
