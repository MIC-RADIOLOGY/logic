import pandas as pd

def load_matches():
    return pd.DataFrame({
        'home_team': ['Arsenal', 'Barcelona', 'Man City'],
        'away_team': ['Tottenham', 'Almeria', 'Sheffield'],
        'avg_home_goals': [2.1, 2.5, 2.7],
        'avg_away_goals': [1.8, 0.6, 0.5],
        'avg_home_corners': [6.5, 7.0, 8.0],
        'avg_away_corners': [5.0, 3.0, 2.5],
        'avg_home_cards': [1.2, 1.5, 1.1],
        'avg_away_cards': [2.0, 2.5, 1.8]
    })
