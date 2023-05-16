from dash import html, dcc  # Importing the html and dcc modules from the dash library
import plotly.graph_objs as go  # Importing the go module from the plotly.graph_objs library
import pandas as pd  # Importing the pandas library

class SimpleBarChart(html.Div):
    def __init__(self, name, x, y, df, selected_player=None):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.x = x
        self.y = y
        self.selected_player = selected_player

        if not isinstance(df, pd.DataFrame):
            raise ValueError("df must be a pandas DataFrame")
        if x not in df.columns or y not in df.columns:
            raise ValueError("x and y must be column names in df")

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),  # Adding a heading to the graph card
                dcc.Graph(id=self.html_id, figure=self.create_fig())  # Creating a graph using dcc.Graph and specifying its id and figure
            ],
        )

    def create_fig(self):
        fig = go.Figure()  # Creating an empty figure using plotly.graph_objs.Figure()

        # Create a list of colors for the bars
        colors = ['lightsalmon' if player == self.selected_player else '#1f77b4' for player in self.df[self.x]]

        fig.add_trace(go.Bar(
            x=self.df[self.x],
            y=self.df[self.y],
            name="Players",  # Setting the trace name
            marker_color=colors  # Setting the color of the bars
        ))

        fig.update_layout(
            xaxis_title=self.x,  # Setting the x-axis title
            yaxis_title=self.y,  # Setting the y-axis title
            plot_bgcolor='rgba(255,255,255,1)',  # Setting the plot background color
            margin=dict(l=0, r=0, t=30, b=0),  # Setting the margin
            font=dict(family='Arial, sans-serif', size=14, color='#2c3e50'),  # Setting the font style
            xaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the x-axis grid color
            yaxis=dict(gridcolor='rgba(230,230,230,1)'),  # Setting the y-axis grid color
            clickmode='event+select'  # Setting the click mode for interactivity
        )

        return fig
