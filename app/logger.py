import json
from datetime import datetime

def log_route(intent, confidence, user_message, final_response):

    log_entry = {
        "timestamp": str(datetime.utcnow()),
        "intent": intent,
        "confidence": confidence,
        "user_message": user_message,
        "final_response": final_response
    }

    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")