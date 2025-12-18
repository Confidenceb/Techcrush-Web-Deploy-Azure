import json

# Read current data
with open('data.json', 'r') as f:
    data = json.load(f)

# Fix all coordinates to have exactly 4 decimal places
fixed_count = 0
for city in data['cities']:
    if 'latitude' in city and 'longitude' in city:
        # Convert to float, then format with 4 decimal places
        lat = float(city['latitude'])
        lng = float(city['longitude'])
        
        # Round to 4 decimal places
        city['latitude'] = round(lat, 4)
        city['longitude'] = round(lng, 4)
        fixed_count += 1

# Write updated data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Fixed {fixed_count} cities with consistent 4-decimal precision!")
print(f"✓ All coordinates now have format: lat.xxxx, lng.xxxx")
