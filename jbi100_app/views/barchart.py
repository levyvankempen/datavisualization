from dash import dcc, html
import plotly.graph_objects as go


class SimpleBarChart(html.Div):
    def __init__(self, name, feature_x, feature_y, df, highlighted_team=None, highlighted_player=None):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.highlighted_team = highlighted_team
        self.highlighted_player = highlighted_player

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig())
            ],
        )

#     def create_fig(self):
#         fig = go.Figure()
#
#         x_values = self.df[self.feature_x]
#         y_values = self.df[self.feature_y]
#         bar_color = '#1f77b4'
#
#
#
#         fig.add_trace(go.Bar(
#             x=x_values,
#             y=y_values,
#             marker_color=bar_color
#         ))
#
#         fig.update_layout(
#             xaxis_title=self.feature_x,
#             yaxis_title=self.feature_y,
#             plot_bgcolor='rgba(255,255,255,1)',
#             margin=dict(l=0, r=0, t=30, b=0),
#             font=dict(family='Arial, sans-serif',
#                       size=14,
#                       color='#2c3e50'),
#             xaxis=dict(gridcolor='rgba(230,230,230,1)'),
#             yaxis=dict(gridcolor='rgba(230,230,230,1)'),
#         )
#         return fig
#
#

    def create_fig(self):
        fig = go.Figure()

        x_values = self.df[self.feature_x]
        y_values = self.df[self.feature_y]
        bar_color = '#1f77b4'

        # if self.highlighted_team is not None:
        #     bar_color = ['grey' if team != self.highlighted_team else '#1f77b4' for team in self.df["team"]]
        # elif self.highlighted_player is not None:
        #     bar_color = ['grey' if player != self.highlighted_player else '#1f77b4' for player in self.df["player"]]
        # else:
        #     bar_color = '#1f77b4'

        if self.highlighted_team is not None:
            # Find the indices of the highlighted team in the x_values array
            highlighted_indices = [i for i, x in enumerate(x_values) if x == self.highlighted_team]

            # Create a list of colors for each bar, with the highlighted team's bars set to a different color
            colors = [bar_color if i not in highlighted_indices else '#ff7f0e' for i in range(len(x_values))]

        elif self.highlighted_player is not None:
            # Find the index of the highlighted player in the x_values array
            highlighted_index = x_values.tolist().index(self.highlighted_player)

            # Create a list of colors for each bar, with the highlighted player's bar set to a different color
            colors = [bar_color if i != highlighted_index else '#ff7f0e' for i in range(len(x_values))]
        else:
            # If no team or player is highlighted, set all bars to the default color
            colors = [bar_color] * len(x_values)

        fig.add_trace(go.Bar(
            x=x_values,
            y=y_values,
            marker_color=colors
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

    def update_color(self, x_value):
        if self.highlighted_team is not None:
            bar_color = ['grey' if team != self.highlighted_team else '#1f77b4' for team in self.df["team"]]
        elif self.highlighted_player is not None:
            bar_color = ['grey' if player != self.highlighted_player else '#1f77b4' for player in self.df["player"]]
        else:
            bar_color = '#1f77b4'

        # Find the index of the x_value in the x-axis data
        idx = self.df[self.feature_x].tolist().index(x_value)

        # Update the color of the bar corresponding to the x_value
        self.fig.update_traces(marker_color=[bar_color[idx]], selector=dict(type='bar', x=x_value))

        return fig
