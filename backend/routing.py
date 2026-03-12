def route_department(category):

    mapping = {
        "Roads": "Municipal Roads Department",
        "Water": "Water Supply Department",
        "Electricity": "Electricity Board",
        "Sanitation": "City Sanitation Department",
        "Public Safety": "Police Department"
    }

    return mapping.get(category, "General Department")
