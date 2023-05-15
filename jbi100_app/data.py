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
    useful_cols_GK = ['player', 'position', 'club', 'team', 'age', 'gk_clean_sheets_pct', 'gk_goals_against', 'gk_goals_against_per90', 'gk_passes_completed_launched',
                      'gk_saves', 'gk_save_pct', 'gk_pens_saved_pct', 'gk_crosses_stopped_pct']

    useful_cols_DF = ['player', 'position', 'club', 'team', 'age', 'tackles_won', 'interceptions',
                      'clearances', 'aerials_won_pct', 'blocks', 'passes_completed', 'tackles_def_3rd', 'fouls', 'tackles_interceptions',
                      'ball_recoveries']

    useful_cols_MF = ['player', 'position', 'club', 'team', 'age', 'goals_assists_per90',
                      'xg_xg_assist_per90', 'tackles_won', 'interceptions', 'passes_pct', 'touches_mid_3rd',
                      'touches']

    useful_col_FW = ['player', 'position', 'club', 'team', 'age', 'goals', 'assists', 'shots_per90',
                     'shots_on_target_pct', 'aerials_won_pct', 'gca_per90', 'xg', 'xg_per90', 'xg_assist', 'xg_assist_per90',
                     'shots','pens_made', 'dribbles_completed_pct']

    return useful_cols_GK, useful_cols_DF, useful_cols_MF, useful_col_FW

