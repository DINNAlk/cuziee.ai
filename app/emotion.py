def detect_emotion(text : str):
    text = text.lower()

    if "sad" in text or "hurt" in text :
        return "sad"

    if "jealous" in text:
        return "jealous"

    return "neutral"
