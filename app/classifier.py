import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CLASSIFIER_PROMPT = """
Classify the user's intent.

Choose ONLY one label:
code
data
writing
career
unclear

Return JSON only:

{
 "intent": "label",
 "confidence": 0.0
}
"""

def classify_intent(message: str):

    try:
        # Try LLM call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        result = response.choices[0].message.content
        parsed = json.loads(result)

        return {
            "intent": parsed.get("intent", "unclear"),
            "confidence": float(parsed.get("confidence", 0.0))
        }

    except Exception:
        # Fallback classifier if API fails
        text = message.lower()

        if any(x in text for x in ["python", "code", "bug", "function"]):
            return {"intent": "code", "confidence": 0.8}

        elif any(x in text for x in ["data", "average", "pivot"]):
            return {"intent": "data", "confidence": 0.8}

        elif any(x in text for x in ["rewrite", "sentence", "paragraph"]):
            return {"intent": "writing", "confidence": 0.8}

        elif any(x in text for x in ["career", "job", "resume", "interview"]):
            return {"intent": "career", "confidence": 0.8}

        else:
            return {"intent": "unclear", "confidence": 0.0}