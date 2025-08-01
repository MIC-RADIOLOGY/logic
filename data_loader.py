import requests
import pandas as pd
from datetime import datetime, timedelta

API_URL = "https://v3.football.api-sports.io/fixtures"
API_KEY = "c9d42b0cd018e4d5f7dac2950c8ab3e0"  # Your API key

def get_upcoming_fixtures():
    headers = {
        "x-apisports-key": API_KEY
    }

    today = datetime.utcnow().strftime('%Y-%m-%d')
    end_date = (datetime.utcnow() + timedelta(days=7)).strftime('%Y-%m-%d')

    params = {
        "date": today,
        "to": end_date,
        "status": "NS"  # Not Started matches only
    }

    try:
        resp = requests.get(API_URL, headers=headers, params=params)
        print(f"Status code: {resp.status_code}")  # Debug print
        resp.raise_for_status()
        data = resp.json()
        print(f"API response keys: {list(data.keys())}")  # Debug print
        print(f"Number of matches returned: {len(data.get('response', []))}")  # Debug print

        matches = []
        for fixture in data.get("response", []):
            info = fixture.get("fixture", {})
            league = fixture.get("league", {})
            teams = fixture.get("teams", {})

            matches.append({
                "fixture_id": info.get("id"),
                "league": league.get("name", "Unknown League"),
                "home": teams.get("home", {}).get("name", "Home"),
                "away": teams.get("away", {}).get("name", "Away"),
                "date": info.get("date", "Unknown Date")
            })

        df = pd.DataFrame(matches)
        print(df.head())  # Debug print of first few fixtures
        return df

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()

   
