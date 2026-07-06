import time
from apic_auth import get_apic_session, refresh_apic_session, APIC_URL
from get_version import fetch_version_info
from get_interfaces import fetch_interface_status
from get_endpoints import fetch_local_endpoints
from get_modules import fetch_node_modules
from get_firmware import fetch_firmware_info

def run_collection(session):
    print(f"\n--- Data Collection Run: {time.ctime()} ---")
    fetch_version_info(session, APIC_URL)
    fetch_interface_status(session, APIC_URL)
    fetch_local_endpoints(session, APIC_URL)
    fetch_node_modules(session, APIC_URL)
    fetch_firmware_info(session, APIC_URL)

if __name__ == "__main__":
    try:
        session = get_apic_session()
        start_time = time.time()
        
        print("Session established. You can now fetch data on-demand.")
        
        while time.time() - start_time < 3600:
            user_input = input("\nDo you want to fetch the latest data? (y/n): ").lower()
            
            if user_input == 'y':
                run_collection(session)
                # Keep session alive by performing a refresh after a successful fetch
                refresh_apic_session(session)
            elif user_input == 'n':
                print("Exiting application.")
                break
            else:
                print("Invalid input. Please enter 'y' to fetch or 'n' to exit.")
            
        if time.time() - start_time >= 3600:
            print("Session duration reached (1 hour). Please restart the script.")
            
    except Exception as e:
        print(f"An error occurred: {e}")