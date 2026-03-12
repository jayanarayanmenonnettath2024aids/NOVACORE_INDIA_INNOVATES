def detect_language(text):
    """
    Placeholder for language detection logic.
    In a real system, this would use an AI model (e.g., Sarvam AI).
    """
    # Simple heuristic for dummy implementation
    return "English"

def process_complaint(text):
    """
    Analyzes complaint text to determine category and priority.
    """
    category = "General"
    priority = "Low"
    
    clean_text = text.lower()

    # Category Mapping
    if any(k in clean_text for k in ["road", "pothole", "traffic"]):
        category = "Roads"
    elif any(k in clean_text for k in ["water", "leakage", "pipe", "supply"]):
        category = "Water"
    elif any(k in clean_text for k in ["electricity", "power", "current", "light"]):
        category = "Electricity"
    elif any(k in clean_text for k in ["garbage", "dump", "dirty", "trash", "sanitation"]):
        category = "Sanitation"
    elif any(k in clean_text for k in ["crime", "police", "safety", "threat", "theft"]):
        category = "Public Safety"

    # Priority Scoring
    if any(k in clean_text for k in ["danger", "emergency", "immediate", "hazard", "threat", "accident", "broken signal"]):
        priority = "High"
    elif any(k in clean_text for k in ["leakage", "overflow", "outage", "broken"]):
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "text": text,
        "category": category,
        "priority": priority,
        "language": detect_language(text)
    }
