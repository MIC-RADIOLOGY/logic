import streamlit as st
import pandas as pd

from data_loader import get_upcoming_fixtures
from predictor import (
    predict_winner,
    predict_goals,
    predict_cards,
    predict_corners,
    predict_btts,
)
from metrics import init_db, log_prediction, get_accuracy_by_league

st.set_page_config(page_title="AI Football Predictions", layout="wide")

init_db()

st.title("⚽ AI Match Prediction App")

# Fetch fixtures
fixtures = get_upcoming_fixtures()

# Sidebar filter by league
all_leagues = fixtures["league"].unique()
selected_leagues = st.sidebar.multiselect(
    "Select Leagues to Show", all_leagues, default=list(all_leagues)
)

filtered_fixtures = fixtures[fixtures["league"].isin(selected_leagues)]

if filtered_fixtures.empty:
    st.write("No fixtures available for selected leagues.")
else:
    for _, row in filtered_fixtures.iterrows():
        st.subheader(f"{row['date'][:10]} - {row['home']} vs {row['away']} ({row['league']})")

        winner_pred = predict_winner(row)
        goals_pred = predict_goals(row)
        cards_pred = predict_cards(row)
        corners_pred = predict_corners(row)
        btts_pred = predict_btts(row)

        st.write(f"🏆 Winner Prediction: {winner_pred['winner']} ({winner_pred['confidence']}% confidence)")
        st.write(f"🎯 Over/Under Goals: {goals_pred}")
        st.write(f"🟨 Cards Tip: {cards_pred}")
        st.write(f"🟦 Corners Tip: {corners_pred}")
        st.write(f"⚽ Both Teams to Score: {btts_pred}")
        st.markdown("---")

# Accuracy dashboard
st.header("Prediction Accuracy by League")
accuracy_df = get_accuracy_by_league()
if not accuracy_df.empty:
    st.bar_chart(accuracy_df.set_index("league")["accuracy"])
else:
    st.write("No accuracy data available yet.")
