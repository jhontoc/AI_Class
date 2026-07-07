import requests
import urllib3
import os
from dotenv import load_dotenv


# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration

load_dotenv()
APIC_URL = os.getenv("APIC_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")



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