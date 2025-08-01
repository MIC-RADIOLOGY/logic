import streamlit as st
import pandas as pd
from data_loader import get_upcoming_fixtures
from predictor import (
    predict_winner,
    predict_goals,
    predict_cards,
    predict_corners,
    predict_btts
)
from metrics import init_db, log_prediction, get_accuracy_by_league

st.set_page_config(page_title="⚽ AI Football Match Predictor", layout="wide")
st.title("⚽ AI Football Match Predictor")

# Initialize local database
init_db()

# Load fixtures
fixtures = get_upcoming_fixtures()

# Handle empty or missing data safely
if fixtures.empty or "league" not in fixtures.columns:
    st.warning("⚠️ No fixture data available. Check your API key or try again later.")
else:
    # League selector
    all_leagues = fixtures["league"].unique()
    selected_leagues = st.sidebar.multiselect(
        "Select Leagues to Show", all_leagues, default=list(all_leagues)
    )

    # Filter matches by league
    filtered_fixtures = fixtures[fixtures["league"].isin(selected_leagues)]

    if filtered_fixtures.empty:
        st.info("No fixtures in selected leagues.")
    else:
        # Loop through each fixture and show predictions
        for _, row in filtered_fixtures.iterrows():
            st.subheader(f"📅 {row['date'][:10]} - {row['home']} vs {row['away']} ({row['league']})")

            # AI Predictions
            winner = predict_winner(row)
            goals = predict_goals(row)
            cards = predict_cards(row)
            corners = predict_corners(row)
            btts = predict_btts(row)

            # Display Predictions
            st.write(f"🏆 **Winner Prediction:** {winner['winner']} ({winner['confidence']}% confidence)")
            st.write(f"🎯 **Over/Under Goals:** {goals}")
            st.write(f"🟨 **Cards Tip:** {cards}")
            st.write(f"🟦 **Corners Tip:** {corners}")
            st.write(f"⚽ **Both Teams to Score:** {btts}")
            st.markdown("---")

# Accuracy dashboard (bottom of page)
st.header("📊 Prediction Accuracy by League")
accuracy_df = get_accuracy_by_league()

if not accuracy_df.empty:
    st.bar_chart(accuracy_df.set_index("league")["accuracy"])
else:
    st.info("No prediction accuracy data available yet.")
