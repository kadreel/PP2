import json

with open('lab 4\json\sample-data.json', 'r') as file:
    data = json.load(file)

def print_interface_status(data):
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
    print("-" * 80)

    for entry in data['imdata']:
        attributes = entry['l1PhysIf']['attributes']
        dn = attributes.get('dn', 'N/A')
        description = attributes.get('descr', 'N/A')
        speed = attributes.get('speed', 'N/A')
        mtu = attributes.get('mtu', 'N/A')

        print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<5}")

print_interface_status(data)
