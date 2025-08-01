import random

def predict_match(match):
    winner = match['home_team'] if match['avg_home_goals'] > match['avg_away_goals'] else match['away_team']
    confidence = round(random.uniform(70, 90), 2)

    goals_avg = match['avg_home_goals'] + match['avg_away_goals']
    over_under_goals = "Over 2.5" if goals_avg >= 2.5 else "Under 2.5"

    corners_avg = match['avg_home_corners'] + match['avg_away_corners']
    corners_tip = "Over 9.5" if corners_avg > 9.5 else "Under 9.5"

    cards_avg = match['avg_home_cards'] + match['avg_away_cards']
    cards_tip = "Over 3.5" if cards_avg > 3.5 else "Under 3.5"

    btts_tip = "Yes" if match['avg_home_goals'] > 1 and match['avg_away_goals'] > 1 else "No"

    return {
        'winner': winner,
        'winner_confidence': confidence,
        'over_under_goals': over_under_goals,
        'corners': corners_tip,
        'cards': cards_tip,
        'btts': btts_tip
    }
