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

def get_relevant_features():
    # define features
    useful_cols_GK = ['gk_clean_sheets', 'gk_goals_against', 'gk_goals_against_per90', 'gk_shots_on_target_against',
                      'gk_saves', 'gk_save_pct', 'gk_pens_saved', 'gk_pens_att_against', 'gk_crosses_stopped_pct',
                      'gk_aerials_won_pct']

    useful_cols_DF = ['player', 'position', 'club', 'team', 'age', 'minutes_90s', 'tackles_won', 'interceptions',
                      'clearances', 'aerials_won_pct', 'blocks', 'cards_yellow', 'cards_red', 'fouls', 'own_goals',
                      'ball_recoveries']

    useful_cols_MF = ['player', 'position', 'club', 'team', 'age', 'games_starts', 'minutes_90s', 'goals_assists_per90',
                      'xg_xg_assist_per90', 'tackles_won', 'interceptions', 'passes_pct', 'gca_passes_live',
                      'gca_passes_dead']

    useful_col_FW = ['player', 'position', 'club', 'team', 'age', 'goals', 'assists', 'shots_per90',
                     'shots_on_target_pct', 'xg', 'npxg', 'xg_per90', 'xg_assist', 'xg_assist_per90',
                     'dribbles_completed_pct']

    return useful_cols_GK, useful_cols_DF, useful_cols_MF, useful_col_FW

