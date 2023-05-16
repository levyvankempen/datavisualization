from dash import html  # Importing the html module from the dash library
import dash_bootstrap_components as dbc  # Importing the dash_bootstrap_components library

class PlayerInfo:
    def __init__(self, player_data):
        self.player_data = player_data  # Initializing the PlayerInfo class with player_data as a parameter

    def get_component(self):
        return dbc.Row([
            dbc.Col([html.Strong("Name: "), html.Span(self.player_data['player'])], width=3),  # Creating a column with player's name
            dbc.Col([html.Strong("Age: "), html.Span(self.player_data['age'])], width=3),  # Creating a column with player's age
            dbc.Col([html.Strong("Team: "), html.Span(self.player_data['team'])], width=3),  # Creating a column with player's team
            dbc.Col([html.Strong("Club: "), html.Span(self.player_data['club'])], width=3)  # Creating a column with player's club
        ], className="player_info_card")  # Returning a row with player information, with a CSS class "player_info_card"
