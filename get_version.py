def fetch_version_info(session, url):
    """Queries the APIC for topSystem class version and reboot info."""
    version_url = f"{url}/api/node/class/topSystem.json"
    response = session.get(version_url, verify=False)
    response.raise_for_status()
    
    data = response.json()['imdata']
    
    # Header for the table output
    print(f"{'Node Name':<20} | {'Version':<15} | {'Last Reboot Time'}")
    print("-" * 65)
    
    for item in data:
        attr = item['topSystem']['attributes']
        name = attr.get('name')
        version = attr.get('version')
        reboot = attr.get('lastRebootTime')
        
        print(f"{name:<20} | {version:<15} | {reboot}")