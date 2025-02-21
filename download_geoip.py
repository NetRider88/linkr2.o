import os
import requests
import tarfile
from pathlib import Path

def download_geoip():
    # Create geoip directory if it doesn't exist
    geoip_dir = Path('geoip')
    geoip_dir.mkdir(exist_ok=True)
    
    # URL for the free GeoLite2 City database
    url = "https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb"
    
    # Download the database
    print("Downloading GeoLite2-City database...")
    response = requests.get(url)
    
    if response.status_code == 200:
        # Save the database
        db_path = geoip_dir / 'GeoLite2-City.mmdb'
        with open(db_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded GeoLite2-City database to {db_path}")
    else:
        print(f"Failed to download database. Status code: {response.status_code}")

if __name__ == '__main__':
    download_geoip() 