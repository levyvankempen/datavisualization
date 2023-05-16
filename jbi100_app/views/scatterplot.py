from dash import dcc, html  # Importing the dcc and html modules from the dash library
import plotly.graph_objects as go  # Importing the go module from the plotly.graph_objects library
import numpy as np  # Importing the numpy library

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
                html.H6(name),  # Adding a heading to the graph card
                dcc.Graph(id=self.html_id, figure=self.create_fig())  # Creating a graph using dcc.Graph and specifying its id and figure
            ],
        )

    def create_fig(self):
        fig = go.Figure()  # Creating an empty figure using plotly.graph_objects.Figure()

        x_values = self.df[self.feature_x]  # Extracting x-axis values from the DataFrame
        y_values = self.df[self.feature_y]  # Extracting y-axis values from the DataFrame

        # Calculate coefficients for the polynomial (line)
        m, b = np.polyfit(x_values, y_values, 1)  # Performing linear regression using numpy.polyfit

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(
                size=10,
                color='#1f77b4',
            ),
            text=self.df['player'],  # Setting the text for hover labels
            hovertemplate='<b>%{text}</b><br><br>' + self.feature_x + ': %{x}<br>' + self.feature_y + ': %{y}<extra></extra>',  # Setting the hover template
            name="All Players Same Position"  # Setting the trace name
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
            visible="legendonly"  # Setting the visibility of the trace in the legend
        ))

        if self.selected_player:
            player_data = self.df[self.df['player'] == self.selected_player]  # Filter data for the selected player
            if not player_data.empty:  # Check if the filtered data is not empty
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
                    text=player_data['player'],  # Setting the text for hover labels
                    hovertemplate='<b>%{text}</b><br><br>' + self.feature_x + ': %{x}<br>' + self.feature_y + ': %{y}<extra></extra>',  # Setting the hover template
                    name=self.selected_player  # Setting the trace name
                ))

        fig.update_layout(
            xaxis_title=self.feature_x,  # Setting the x-axis title
            yaxis_title=self.feature_y,  # Setting the y-axis title
            clickmode='event+select'  # Setting the click mode for interactivity
        )

        return fig
