from dash import dcc, html  # Importing the dcc and html modules from the dash library
import plotly.graph_objects as go  # Importing the go module from the plotly.graph_objects library


class BarChart(html.Div):
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
                html.H6("Compare team aggregates per position"),  # Adding a heading to the graph card
                dcc.Graph(id=self.html_id, figure=self.create_fig())
                # Creating a graph using dcc.Graph and specifying its id and figure
            ],
        )

    def create_fig(self):
        fig = go.Figure()  # Creating an empty figure using plotly.graph_objects.Figure()

        x_values = self.df[self.feature_x]  # Extracting x-axis values from the DataFrame
        y_values = self.df[self.feature_y]  # Extracting y-axis values from the DataFrame
        bar_color = '#1f77b4'  # Setting the default color for the bars

        # Conditional coloring based on highlighted_team and highlighted_player
        if self.highlighted_team is not None:
            # Find the indices of the highlighted team in the x_values array
            highlighted_indices = [i for i, x in enumerate(x_values) if x == self.highlighted_team]

            # Create a list of colors for each bar, with the highlighted team's bars set to a different color
            colors = [bar_color if i not in highlighted_indices else 'lightsalmon' for i in range(len(x_values))]

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
        ))  # Adding a bar trace to the figure with specified x and y values and marker colors

        fig.update_layout(
            xaxis_title=self.feature_x,  # Setting the x-axis title
            yaxis_title=self.feature_y,  # Setting the y-axis title
            plot_bgcolor='rgba(255,255,255,1)',  # Setting the plot background color
            margin=dict(l=0, r=0, t=30, b=0),  # Setting the margin
            font=dict(family='Arial, sans-serif', size=14, color='#2c3e50'),  # Setting the font style
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the x-axis grid color
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the y-axis grid color
        )
        return fig

    def update_color(self, x_value):
        if self.highlighted_team is not None:
            bar_color = ['grey' if team != self.highlighted_team else '#1f77b4' for team in self.df["team"]]
        elif self.highlighted_player is not None:
            bar_color = ['grey' if player != self.highlighted_player else '#1f77b4' for player in self.df["player"]]
        else:
            bar_color = '#1f77b4'

        idx = self.df[self.feature_x].tolist().index(x_value)  # Find the index of the x_value in the x-axis data

        self.fig.update_traces(marker_color=[bar_color[idx]],
                               selector=dict(type='bar', x=x_value))  # Update the color of the bar corresponding to the x_value

        return fig
