from prompts import SYSTEM_PROMPTS

def route_and_respond(message: str, intent_data: dict):

    intent = intent_data["intent"]

    # If intent unclear
    if intent == "unclear":
        return "I couldn't clearly understand your request. Are you asking about coding, data analysis, writing help, or career advice?"

    # Simulated responses (since API is disabled)
    if intent == "code":
        return "To sort a list in Python you can use the built-in sorted() function or list.sort(). Example:\n\nnumbers = [3,1,4,2]\nnumbers.sort()\nprint(numbers)"

    elif intent == "data":
        return "To analyze data you can calculate statistics such as mean, median, and distribution. A bar chart or histogram would help visualize patterns."

    elif intent == "writing":
        return "Your writing may contain issues like passive voice or verbosity. Try shortening sentences and using active voice for clarity."

    elif intent == "career":
        return "To improve your career prospects, start by identifying your goals, improving relevant skills, and preparing a strong resume and portfolio."

    else:
        return "I'm not sure how to respond to that request."