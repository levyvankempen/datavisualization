from dash import html  # Importing the html module from the dash library

class TeamInfo:
    def __init__(self, team, feature_value):
        self.team = team
        self.feature_value = feature_value

    def get_component(self):
        return html.Div([
            html.P(f"Team: {self.team}", className='font-weight-bold'),  # Displaying the team name in bold
            html.P(f"Feature Value: {self.feature_value}")  # Displaying the feature value
        ])
