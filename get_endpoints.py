def fetch_local_endpoints(session, url):
    """Queries the APIC for local endpoints (fvCEp)."""
    ep_url = f"{url}/api/node/class/fvCEp.json"
    response = session.get(ep_url, verify=False)
    response.raise_for_status()
    
    data = response.json()['imdata']
    
    print(f"\n{'Node':<10} | {'MAC Address':<20} | {'IP Address':<15} | {'Encap'}")
    print("-" * 70)
    
    for item in data:
        attr = item['fvCEp']['attributes']
        dn = attr.get('fabricPathDn', '')
        mac = attr.get('mac', 'N/A') #topology/pod-1/paths-202/pathep-[eth1/1]
        ip = attr.get('ip', 'N/A')
        encap = attr.get('encap', 'N/A')
        
        # Parse Node from DN
        try:
            parts = dn.split('/')
            node = [p for p in parts if p.startswith('paths')][0]
        except IndexError:
            node = "Unknown"
            
        print(f"{node:<10} | {mac:<20} | {ip:<15} | {encap}")