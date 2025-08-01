import requests
import pandas as pd

API_URL = API_URL = "https://api.football-data.org/v2/matches?status=FINISHED"

API_KEY = "af56a1c0b4654b80a8400478462ae75"  # Replace with your actual API key

def get_upcoming_fixtures():
    headers = {"X-Auth-Token": API_KEY}
    try:
        resp = requests.get(API_URL, headers=headers)
        resp.raise_for_status()  # Raises error for bad responses
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
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return pd.DataFrame()
