import json
import os
import random

class RegionalMetadataMaster:
    """
    Synthesizes massive regional administrative metadata for India.
    Includes exhaustive mappings for States, Districts, Wards, and Officers.
    This provides the underlying structure for geospatial routing and reporting.
    """
    
    STATES = {
        "KA": "Karnataka",
        "TN": "Tamil Nadu",
        "MH": "Maharashtra",
        "DL": "Delhi",
        "WB": "West Bengal",
        "UP": "Uttar Pradesh",
        "AP": "Andhra Pradesh",
        "TG": "Telangana",
        "GJ": "Gujarat",
        "RJ": "Rajasthan"
    }
    
    DEPARTMENTS = [
        "Water", "Electricity", "Roads", "Sanitation", "Health", "Education", "Police", "Welfare"
    ]
    
    OFFICER_RANKS = ["Junior Engineer", "Assistant Engineer", "Executive Engineer", "Superintending Engineer", "Chief Engineer"]

    def __init__(self, output_path: str = "data/regional_metadata.json"):
        self.output_path = output_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    def generate_officer(self, dept: str, rank: str, ward: int) -> dict:
        names = ["A. Kumar", "S. Pillai", "M. Reddy", "R. Deshpukh", "V. Sharma", "P. Iyer", "S. Gupta"]
        return {
            "name": f"{rank} {random.choice(names)}",
            "department": dept,
            "rank": rank,
            "contact": f"+91-{random.randint(7000, 9999)}-{random.randint(100000, 999999)}",
            "ward_assignment": ward
        }

    def generate_ward(self, state_code: str, city: str, ward_no: int) -> dict:
        ward_id = f"{state_code}-{city[:3].upper()}-{ward_no:03d}"
        return {
            "ward_id": ward_id,
            "ward_name": f"Ward {ward_no} - {city} Central",
            "population_density": random.choice(["High", "Medium", "Low"]),
            "critical_assets": random.randint(5, 50),
            "primary_department": random.choice(self.DEPARTMENTS),
            "officers": [
                self.generate_officer(dept, random.choice(self.OFFICER_RANKS), ward_no)
                for dept in random.sample(self.DEPARTMENTS, 3)
            ]
        }

    def generate_metadata(self):
        metadata = {}
        for state_code, state_name in self.STATES.items():
            metadata[state_code] = {
                "name": state_name,
                "cities": {}
            }
            # Simulating major cities per state
            cities = [f"City_{i}" for i in range(5)]
            for city in cities:
                metadata[state_code]["cities"][city] = {
                    "wards": [self.generate_ward(state_code, city, w) for w in range(1, 21)] # 20 wards per city
                }
        
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
        print(f"Generated metadata at {self.output_path}")

if __name__ == "__main__":
    master = RegionalMetadataMaster()
    master.generate_metadata()
