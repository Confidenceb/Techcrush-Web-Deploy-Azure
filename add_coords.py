import json

# Mapping of Lagos cities/areas to their approximate coordinates
coords_map = {
    "Abule Egba": (6.5667, 3.3333),
    "Agbara": (6.3056, 3.4028),
    "Agege": (6.6167, 3.3500),
    "AGUNGI (LEKKI)": (6.4333, 3.5833),
    "Ajah": (6.3833, 3.7167),
    "AJAO ESTATE": (6.5167, 3.3667),
    "AMUWO": (6.4500, 3.3167),
    "ANTHONY VILLAGE": (6.4333, 3.3667),
    "Apapa": (6.4500, 3.3333),
    "AWOYAYA": (6.4000, 3.6000),
    "Badagry": (6.3944, 2.8917),
    "BERGER": (6.6000, 3.4167),
    "Bogije": (6.3500, 3.7167),
    "Coker": (6.4167, 3.7500),
    "Egbeda (Shasha)": (6.5833, 3.4167),
    "Ejigbo": (6.4833, 3.4333),
    "EPE": (6.5833, 4.0000),
    "Fagba": (6.6500, 3.4000),
    "FESTAC": (6.4667, 3.2667),
    "Gbagada": (6.5500, 3.4667),
    "Ibeju-Lekki": (6.3333, 3.8333),
    "IDIMU": (6.5333, 3.4000),
    "IGANDO": (6.5500, 3.3667),
    "IJANIKIN": (6.4500, 3.2500),
    "IJEGUN IKOTUN": (6.5667, 3.4000),
    "IJORA": (6.4667, 3.3333),
    "Ikeja": (6.5833, 3.3667),
    "IKORODU": (6.5500, 3.5167),
    "IKOTA": (6.4667, 3.6000),
    "IKOTUN": (6.5500, 3.4333),
    "Ikoyi": (6.4667, 3.4333),
    "ILAJE (BARIGA)": (6.4500, 3.4000),
    "ILUPEJU (Lagos)": (6.5667, 3.4167),
    "ISHERI IKOTUN": (6.5167, 3.4333),
    "ISHERI MAGODO": (6.4833, 3.5333),
    "ISOLO": (6.5167, 3.4667),
    "IYANA IBA": (6.4500, 3.2667),
    "Iyana Ipaja": (6.5667, 3.3500),
    "JAKANDE (LEKKI)": (6.4333, 3.6000),
    "JANKANDE (ISOLO)": (6.5167, 3.4667),
    "Ketu": (6.4333, 3.4500),
    "Lagos Island": (6.4333, 3.4500),
    "Lakowe": (6.3833, 3.7000),
    "LEKKI": (6.4333, 3.5833),
    "Magboro": (6.6333, 3.4500),
    "MAGODO": (6.5333, 3.5000),
    "MARYLAND": (6.5000, 3.4667),
    "MILE 12": (6.3833, 3.3167),
    "MILE 2": (6.4000, 3.3500),
    "Mushin": (6.4833, 3.3833),
    "Ogba": (6.5833, 3.4167),
    "OGUDU": (6.4167, 3.5500),
    "Ojo": (6.4500, 3.3167),
    "OJODU": (6.5500, 3.3833),
    "OJOKORO": (6.5000, 3.3333),
    "OJOTA": (6.4667, 3.3833),
    "OKOKOMAIKO": (6.4500, 3.2833),
    "OKOTA": (6.4667, 3.4333),
    "Omole": (6.6167, 3.3833),
    "Oniru": (6.4500, 3.4833),
    "OREGUN": (6.5333, 3.3833),
    "ORILE": (6.4667, 3.3333),
    "OSAPA (LEKKI)": (6.4667, 3.5500),
    "OSHODI": (6.5500, 3.4000),
    "Satelite-Town": (6.4167, 3.4500),
    "SOMOLU": (6.4500, 3.3833),
    "Surulere": (6.4833, 3.3833),
    "Victoria Island": (6.4333, 3.4500),
    "Yaba": (6.5000, 3.4167),
}

def get_coords(city_name):
    """Extract base location from city name and return coordinates"""
    for key, coords in coords_map.items():
        if key.lower() in city_name.lower():
            return coords
    # Default to Lagos center if not found
    return (6.5244, 3.3792)

# Read current data
with open('data.json', 'r') as f:
    data = json.load(f)

# Add coordinates to each city
for city in data['cities']:
    lat, lng = get_coords(city['name'])
    city['latitude'] = lat
    city['longitude'] = lng

# Write updated data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✓ Coordinates added to all cities!")
