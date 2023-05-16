from dash import dcc, html  # Importing the dcc and html modules from the dash library
import plotly.graph_objs as go  # Importing the go module from the plotly.graph_objs library
import pandas as pd  # Importing the pandas library

class BoxPlot(html.Div):
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
                html.H6(name),  # Adding a heading to the graph card
                dcc.Graph(id=self.html_id, figure=self.create_fig())  # Creating a graph using dcc.Graph and specifying its id and figure
            ],
        )

    # # Does not work unfortunately
    # def update_player(self, player):
    #     self.player = player
    #     self.update_figure()  # If needed, update the figure with new player data

    def create_fig(self):
        fig = go.Figure()  # Creating an empty figure using plotly.graph_objs.Figure()

        fig.add_trace(go.Box(
            y=self.df[self.y],
            x=self.df[self.x],
            name="All Players",  # Setting the trace name
            marker_color='#1f77b4',  # Setting the color of the boxes
            line=dict(color='#1f77b4'),  # Setting the color of the lines
            boxpoints='all'  # Displaying all the points
        ))

        # # player is the selected player from the clickdata
        # if self.player:  # Only add scatter trace if a player is selected
        #     player_data = self.df[self.df['player'] == self.player]
        #     if not player_data.empty:  # Only add scatter trace if player_data is not empty
        #         fig.add_trace(go.Scatter(
        #             x=[self.player] * len(player_data),
        #             y=player_data[self.y],
        #             mode='markers',
        #             marker=dict(
        #                 color='Red',
        #                 size=12,
        #                 line=dict(
        #                     color='Red',
        #                     width=2
        #                 )
        #             ),
        #             name=f'{self.player}'
        #         ))

        fig.update_layout(
            xaxis_title=self.x,  # Setting the x-axis title
            yaxis_title=self.y,  # Setting the y-axis title
            plot_bgcolor='rgba(255,255,255,1)',  # Setting the plot background color
            margin=dict(l=0, r=0, t=30, b=0),  # Setting the margin
            font=dict(family='Arial, sans-serif', size=14, color='#2c3e50'),  # Setting the font style
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the x-axis grid color
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the y-axis grid color
            clickmode='select'  # Setting the click mode for interactivity
        )

        return fig
