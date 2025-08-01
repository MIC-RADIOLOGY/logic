import joblib
import pandas as pd

# Load your pre-trained ML models here
# For demo, dummy prediction logic
# Replace with actual ML model loading & inference

def predict_winner(fixture_row):
    # Stub: dummy logic - always pick home team with 70% confidence
    return {
        "winner": fixture_row["home"],
        "confidence": 70.0
    }

def predict_goals(fixture_row):
    return "Over 2.5"

def predict_cards(fixture_row):
    return "Under 3.5"

def predict_corners(fixture_row):
    return "Over 9.5"

def predict_btts(fixture_row):
    return "Yes"

       
