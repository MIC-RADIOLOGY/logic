import requests
import pandas as pd

API_URL = "https://api.football-data.org/v2/matches?status=SCHEDULED"
API_KEY = "c9d42b0cd018e4d5f7dac2950c8ab3e0"  # Replace this with your real API key

def get_upcoming_fixtures():
    headers = {"X-Auth-Token": API_KEY}
    try:
        resp = requests.get(API_URL, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        matches = []
        for match in data.get("matches", []):
            matches.append({
                "fixture_id": match.get("id"),
                "league": match.get("competition", {}).get("name", "Unknown League"),
                "home": match.get("homeTeam", {}).get("name", "Home"),
                "away": match.get("awayTeam", {}).get("name", "Away"),
                "date": match.get("utcDate", "Unknown Date")
            })

        return pd.DataFrame(matches)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code} - {e.response.reason}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Other error: {e}")
        return pd.DataFrame()
