import json

with open('data.json') as f:
    data = json.load(f)

missing = [c for c in data['cities'] if 'latitude' not in c]
print(f"Cities without coords: {len(missing)}")
print("\nFirst 20 missing:")
for c in missing[:20]:
    print(f"{c['id']}: {c['name']}")
