import requests

API_URL = "https://api.football-data.org/v2/matches?status=SCHEDULED"
API_KEY = "olN2j1ncmVXENJC5l2058uoNpTePACspeVvL95UJFyEfqfZm5cPIUPRjhR2AJ6GcVkxW7aZXcHXbtaSIIcnWetLx0VmCD7saTchPs96g9vpyq9Z41DlcwNmm6DBtFijk
"  # <-- Replace with your actual API key

def get_upcoming_fixtures():
    headers = {"X-Auth-Token": API_KEY}
    try:
        resp = requests.get(API_URL, headers=headers)
        resp.raise_for_status()  # Raises HTTPError for bad responses
        data = resp.json()
        return data.get("matches", [])
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return []

           
