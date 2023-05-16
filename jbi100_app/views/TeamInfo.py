from dash import html

class TeamInfo:
    def __init__(self, team, feature_value):
        self.team = team
        self.feature_value = feature_value

    def get_component(self):
        return html.Div([
            html.P(f"Team: {self.team}", className='font-weight-bold'),
            html.P(f"Feature Value: {self.feature_value}")
        ])
