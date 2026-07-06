def fetch_interface_status(session, url):
    """Queries the APIC for ethpmPhysIf status and prints in the requested format."""
    # Targeting ethpmPhysIf class
    int_url = f"{url}/api/node/class/ethpmPhysIf.json"
    response = session.get(int_url, verify=False)
    response.raise_for_status()
    
    data = response.json()['imdata']
    
    # Header format
    print(f"\n{'Node':<8} | {'Interface':<45} | {'Status':<10} | {'Speed'}")
    print("-" * 85)
    
    for item in data:
        attr = item['ethpmPhysIf']['attributes']
        dn = attr.get('dn', '')
        status = attr.get('operSt', 'Unknown')
        # Note: ethpmPhysIf may not always have a 'speed' attribute 
        # depending on the firmware/hardware; defaulting to 'N/A'
        speed = attr.get('speed', 'N/A')
        
        # Parse Node and Interface from DN
        # DN format: topology/pod-1/node-209/sys/phys-[eth1/1]
        try:
            parts = dn.split('/')
            node = [p for p in parts if p.startswith('node-')][0]
            interface = dn.split('phys-[')[-1].replace(']', '')
        except (IndexError, AttributeError):
            node = "Unknown"
            interface = "Unknown"
        
        print(f"{node:<8} | {interface:<45} | {status:<10} | {speed}")