import json

class FloatWithFourDecimals(float):
    """Custom float class to format with 4 decimal places"""
    def __repr__(self):
        return f"{self:.4f}"

# Custom JSON encoder to format floats with 4 decimals
class CoordEncoder(json.JSONEncoder):
    def encode(self, o):
        if isinstance(o, float):
            return f"{o:.4f}"
        return super().encode(o)
    
    def iterencode(self, o, _one_shot=False):
        for chunk in super().iterencode(o, _one_shot):
            yield chunk

# Read current data
with open('data.json', 'r') as f:
    data = json.load(f)

# Convert coordinates to strings with 4 decimals, then convert back to float
for city in data['cities']:
    if 'latitude' in city and 'longitude' in city:
        lat = float(city['latitude'])
        lng = float(city['longitude'])
        # Format as string with 4 decimals, then convert to float
        city['latitude'] = float(f"{lat:.4f}")
        city['longitude'] = float(f"{lng:.4f}")

# Write with custom handling
with open('data.json', 'w') as f:
    json_str = json.dumps(data, indent=2)
    
    # Replace latitude and longitude values to ensure 4 decimal places
    lines = json_str.split('\n')
    output_lines = []
    
    for line in lines:
        if '"latitude":' in line:
            # Extract the number and reformat
            parts = line.split(':')
            value_part = parts[1].strip().rstrip(',')
            try:
                value = float(value_part)
                output_lines.append(f'      "latitude": {value:.4f},')
            except:
                output_lines.append(line)
        elif '"longitude":' in line:
            # Extract the number and reformat
            parts = line.split(':')
            value_part = parts[1].strip().rstrip(',')
            try:
                value = float(value_part)
                # Check if it's the last item (no comma after last longitude)
                if value_part.endswith(','):
                    output_lines.append(f'      "longitude": {value:.4f}')
                else:
                    output_lines.append(f'      "longitude": {value:.4f}')
            except:
                output_lines.append(line)
        else:
            output_lines.append(line)
    
    f.write('\n'.join(output_lines))

print("✓ All coordinates formatted with exactly 4 decimal places!")
