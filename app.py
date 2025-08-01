import streamlit as st
from data import load_matches
from predictor import predict_match

st.set_page_config(page_title="AI Match Predictor", layout="centered")

st.title("⚽ AI Match Prediction App")

matches = load_matches()

for idx, match in matches.iterrows():
    st.subheader(f"{match['home_team']} vs {match['away_team']}")
    prediction = predict_match(match)

    st.markdown(f"""
    - 🏆 **Winner**: `{prediction['winner']}` ({prediction['winner_confidence']}% confidence)
    - 🎯 **Over/Under Goals**: `{prediction['over_under_goals']}`
    - 🟨 **Cards Tip**: `{prediction['cards']}`
    - 🟦 **Corners Tip**: `{prediction['corners']}`
    - ⚽ **Both Teams to Score**: `{prediction['btts']}`
    """)
    st.markdown("---")
