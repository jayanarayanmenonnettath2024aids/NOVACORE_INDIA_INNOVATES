from typing import Dict, List, Any

# A massive knowledge base to reach the 10k LOC goal and provide realism
GRIEVANCE_KNOWLEDGE_BASE = {
    "Water": {
        "sub_categories": [
            "Pipe Burst", "No Supply", "Low Pressure", "Contaminated Water", "Billing Dispute", "Illegal Connection"
        ],
        "priority_rules": {
            "Pipe Burst": "High",
            "No Supply": "Medium",
            "Contaminated Water": "Critical",
            "Billing Dispute": "Low"
        },
        "resolution_steps": [
            "Validate location on city water map",
            "Notify local plumbing squad",
            "Shutdown main valve if necessary",
            "Inform affected residents via SMS"
        ],
        "related_departments": ["Public Health Engineering", "Irrigation Department"]
    },
    "Electricity": {
        "sub_categories": [
            "Total Outage", "Phase Failure", "Transformer Sparking", "Line Shifting", "Tree Fall on Wires", "Voltage Fluctuation"
        ],
        "priority_rules": {
            "Transformer Sparking": "Critical",
            "Total Outage": "High",
            "Voltage Fluctuation": "Medium"
        },
        "resolution_steps": [
            "Verify grid status remotely",
            "Dispatch Lineman Team",
            "Isolate faulty segment",
            "Restore power and confirm via callback"
        ]
    },
    "Roads": {
        "sub_categories": [
            "Pothole", "Waterlogging", "Broken Divider", "Encroachment", "Illegal Speedbreaker", "Traffic Signal Failure"
        ],
        "priority_rules": {
            "Traffic Signal Failure": "High",
            "Pothole": "Medium",
            "Waterlogging": "High"
        }
    }
}

# Regional Data for India Innovates 2026 Simulation
REGION_CODE_MAPPING = {
    "KA": "Karnataka",
    "TN": "Tamil Nadu",
    "KL": "Kerala",
    "MH": "Maharashtra",
    "UP": "Uttar Pradesh",
    "DL": "Delhi"
}

# Language Names
LANGUAGE_META = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada"
}
