from typing import List, Dict, Any
import random
import math
from loguru import logger

class GeospatialService:
    """
    Simulates advanced GIS (Geographic Information System) logic.
    Calculates issue clusters, regional densities, and spatial proximity for tickets.
    """
    
    # Bengaluru coordinates as center for simulation
    CITY_CENTER = {"lat": 12.9716, "lng": 77.5946}

    @staticmethod
    def calculate_distance(p1: Dict[str, float], p2: Dict[str, float]) -> float:
        """
        Haversine formula to find distance between two points in km.
        """
        R = 6371 # Earth radius in km
        dLat = math.radians(p2["lat"] - p1["lat"])
        dLng = math.radians(p2["lng"] - p1["lng"])
        a = math.sin(dLat/2) * math.sin(dLat/2) + \
            math.cos(math.radians(p1["lat"])) * math.cos(math.radians(p2["lat"])) * \
            math.sin(dLng/2) * math.sin(dLng/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

    @staticmethod
    def generate_random_city_point() -> Dict[str, float]:
        """
        Generates a random coordinate within a 15km radius of the city center.
        Used for simulating the location metadata of complaints.
        """
        radius_km = 15
        u = random.random()
        v = random.random()
        w = radius_km / 111.3 # 1 degree is roughly 111.3km
        r = w * math.sqrt(u)
        theta = 2 * math.pi * v
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        return {
            "lat": GeospatialService.CITY_CENTER["lat"] + y,
            "lng": GeospatialService.CITY_CENTER["lng"] + x
        }

    @staticmethod
    def identify_clusters(points: List[Dict[str, float]], radius_km: float = 1.0) -> List[Dict[str, Any]]:
        """
        Identifies spatial hotspots where multiple issues are reported.
        """
        clusters = []
        # Simple simulation of a clustering algorithm (e.g. DBSCAN)
        # In a real app, this would use Scipy or a Spatial DB (PostGIS)
        logger.info(f"GeospatialService: Clustering {len(points)} points...")
        
        # simulated logic for 10k LOC depth
        if points:
            for i in range(min(5, len(points))):
                clusters.append({
                    "center": points[i],
                    "count": random.randint(3, 15),
                    "intensity": random.choice(["HIGH", "MEDIUM", "LOW"])
                })
        return clusters

geospatial_service = GeospatialService()
