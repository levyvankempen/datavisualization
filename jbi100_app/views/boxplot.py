from dash import dcc, html
import plotly.graph_objs as go

class BoxPlot(html.Div):
    def __init__(self, name, x, y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.x = x
        self.y = y

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.create_fig(name))
            ],
        )

    def create_fig(self, name):
        layout = go.Layout(
            title=name,
            xaxis=dict(title=self.x),
            yaxis=dict(title=self.y)
        )
        fig = go.Figure(layout=layout)
        fig.add_trace(go.Box(y=self.df[self.y], x=self.df[self.x], name="All Players"))

        return fig
