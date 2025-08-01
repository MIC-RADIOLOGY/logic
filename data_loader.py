import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"  # Replace with your real API key
BASE_URL = "https://api.sportmonks.com/v3/football"

def get_upcoming_fixtures(days=7):
    """Fetch upcoming fixtures within next `days` days"""
    today = pd.Timestamp.today().date()
    end_date = today + pd.Timedelta(days=days)
    url = f"{BASE_URL}/fixtures/between/{today}/{end_date}"
    params = {"api_token": API_KEY, "include": "league,localTeam,visitorTeam"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json().get("data", [])
    matches = []
    for fix in data:
        league = fix.get("league", {}).get("data", {}).get("name", "Unknown League")
        home = fix.get("localTeam", {}).get("data", {}).get("name", "Home Team")
        away = fix.get("visitorTeam", {}).get("data", {}).get("name", "Away Team")
        date = fix.get("starting_at", "")
        matches.append({
            "fixture_id": fix["id"],
            "league": league,
            "home": home,
            "away": away,
            "date": date
        })
    return pd.DataFrame(matches)
