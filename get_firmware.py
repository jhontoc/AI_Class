def fetch_firmware_info(session, url):
    """Queries firmwareCompRunning and parses node and component info."""
    fw_url = f"{url}/api/node/class/firmwareCompRunning.json"
    response = session.get(fw_url, verify=False)
    response.raise_for_status()
    
    data = response.json()['imdata']
    
    print(f"\n{'Node':<10} | {'Component':<15} | {'Version':<15} | {'Expected':<15} | {'Status'}")
    print("-" * 80)
    
    for item in data:
        attr = item['firmwareCompRunning']['attributes']
        dn = attr.get('dn', '')
        oper_st = attr.get('operSt', 'N/A')
        expected_ver = attr.get('expectedVer', 'N/A')
        version = attr.get('version', 'N/A')
        
        # Parsing Logic
        # Expected DN: topology/pod-1/node-202/sys/ch/supslot-1/sup/fpga-2/running
        try:
            parts = dn.split('/')
            node = [p for p in parts if p.startswith('node-')][0]
            # The component is the second to last part in the path
            component = parts[-2]
        except (IndexError, AttributeError):
            node = "Unknown"
            component = "Unknown"
            
        print(f"{node:<10} | {component:<15} | {version:<15} | {expected_ver:<15} | {oper_st}")