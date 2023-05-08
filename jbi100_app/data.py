import pandas as pd
import plotly.express as px


def get_data():
    # Read data
    df = px.data.iris()

    # Any further data preprocessing can go her

    keepers = pd.read_csv('https://raw.githubusercontent.com/levyvankempen/viz/main/position_data/keepers.csv')
    defenders = pd.read_csv('https://raw.githubusercontent.com/levyvankempen/viz/main/position_data/defenders.csv')
    midfielders = pd.read_csv('https://raw.githubusercontent.com/levyvankempen/viz/main/position_data/midfielders.csv')
    attackers = pd.read_csv('https://raw.githubusercontent.com/levyvankempen/viz/main/position_data/forwarders.csv')
    combined = pd.read_csv('https://raw.githubusercontent.com/levyvankempen/viz/main/position_data/combined.csv')

    return df, keepers, defenders, midfielders, attackers, combined
