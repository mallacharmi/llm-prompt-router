from classifier import classify_intent
from router import route_and_respond
from logger import log_route

def run():

    print("LLM Prompt Router Started")
    print("Type 'exit' to quit")

    while True:

        message = input("User: ")

        if message.lower() == "exit":
            break

        intent_data = classify_intent(message)

        final_response = route_and_respond(message, intent_data)

        log_route(
            intent_data["intent"],
            intent_data["confidence"],
            message,
            final_response
        )

        print("\nIntent:", intent_data["intent"])
        print("Confidence:", intent_data["confidence"])
        print("Response:\n", final_response)
        print("\n")


if __name__ == "__main__":
    run()