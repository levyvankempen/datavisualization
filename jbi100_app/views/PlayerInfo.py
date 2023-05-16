from dash import html
import dash_bootstrap_components as dbc

class PlayerInfo:
    def __init__(self, player_data):
        self.player_data = player_data

    def get_component(self):
        return dbc.Row([
            dbc.Col([html.Strong("Name: "), html.Span(self.player_data['player'])], width=3),
            dbc.Col([html.Strong("Age: "), html.Span(self.player_data['age'])], width=3),
            dbc.Col([html.Strong("Team: "), html.Span(self.player_data['team'])], width=3),
            dbc.Col([html.Strong("Club: "), html.Span(self.player_data['club'])], width=3)
        ], className="player_info_card")
