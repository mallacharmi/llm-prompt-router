import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def route_and_respond(message: str, intent_data: dict):

    intent = intent_data["intent"]

    if intent == "unclear":
        return "I'm not sure what you need. Are you asking about coding, data analysis, writing help, or career advice?"

    system_prompt = SYSTEM_PROMPTS.get(intent)

    try:
        # Try LLM response generation
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content

    except Exception:
        # Fallback responses
        if intent == "code":
            return "Example Python sorting:\n\nnumbers = [3,1,4,2]\nnumbers.sort()\nprint(numbers)"

        elif intent == "data":
            return "A pivot table summarizes data by grouping values. It is commonly used in Excel for analyzing datasets."

        elif intent == "writing":
            return "Your writing may be verbose. Try using shorter sentences and active voice."

        elif intent == "career":
            return "Start by identifying your career goals, improving skills, and preparing a strong resume."

        return "Unable to generate response."