import requests
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
APIC_URL = "https://10.66.93.17"
USERNAME = "cisco"
PASSWORD = "cisco.123"

def get_apic_session():
    """Logs into APIC and returns an authenticated session object."""
    login_url = f"{APIC_URL}/api/aaaLogin.json"
    payload = {
        "aaaUser": {
            "attributes": {
                "name": USERNAME,
                "pwd": PASSWORD
            }
        }
    }
    
    session = requests.Session()
    response = session.post(login_url, json=payload, verify=False)
    response.raise_for_status()
    
    token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
    session.cookies.set('APIC-cookie', token)
    return session

def refresh_apic_session(session):
    """Refreshes the session to keep it alive."""
    refresh_url = f"{APIC_URL}/api/aaaRefresh.json"
    session.get(refresh_url, verify=False)
    print("Session refreshed successfully.")