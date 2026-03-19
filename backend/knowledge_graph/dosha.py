# backend/knowledge_graph/dosha.py

def infer_dosha(text):
    text = text.lower()

    if any(x in text for x in ["dry", "anxiety", "insomnia"]):
        return "Vata"
    elif any(x in text for x in ["heat", "acidity", "anger"]):
        return "Pitta"
    elif any(x in text for x in ["heavy", "lazy", "cold"]):
        return "Kapha"
    
    return "Unknown"