def fetch_node_modules(session, url):
    """Queries the APIC for equipment module information."""
    # We query the 'eqptLC' (Line Cards) and 'eqptSupC' (Supervisor Cards)
    # Using a list to iterate through common hardware classes
    classes = ['eqptLC', 'eqptSupC']
    
    print(f"\n{'Node':<8} | {'Module':<20} | {'Model':<25} | {'Oper State'}")
    print("-" * 75)
    
    for cls in classes:
        mod_url = f"{url}/api/node/class/{cls}.json"
        response = session.get(mod_url, verify=False)
        response.raise_for_status()
        
        data = response.json().get('imdata', [])
        
        for item in data:
            # Dynamically get the attributes based on the class name
            attr = item.get(cls, {}).get('attributes', {})
            dn = attr.get('dn', '')
            model = attr.get('model', 'N/A')
            state = attr.get('operSt', 'N/A')
            module_name = attr.get('name', 'Unknown')
            
            # Parse Node from DN
            try:
                parts = dn.split('/')
                node = [p for p in parts if p.startswith('node-')][0]
            except IndexError:
                node = "Unknown"
                
            print(f"{node:<8} | {module_name:<20} | {model:<25} | {state}")