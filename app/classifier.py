import json

def classify_intent(message: str):

    message = message.lower()

    # Simple rule based classification
    if any(word in message for word in ["python", "code", "bug", "function", "program", "sql"]):
        intent = "code"
        confidence = 0.9

    elif any(word in message for word in ["data", "average", "mean", "pivot", "analysis"]):
        intent = "data"
        confidence = 0.85

    elif any(word in message for word in ["rewrite", "sentence", "paragraph", "writing"]):
        intent = "writing"
        confidence = 0.85

    elif any(word in message for word in ["career", "job", "resume", "interview"]):
        intent = "career"
        confidence = 0.85

    else:
        intent = "unclear"
        confidence = 0.5

    return {
        "intent": intent,
        "confidence": confidence
    }