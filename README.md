# LLM-Powered Prompt Router for Intent Classification

## Project Overview

This project implements an **LLM-powered prompt router** that classifies a user's message into different intents and routes it to specialized AI personas.
Instead of using one large prompt, the system first detects the user's intent and then sends the request to a specific expert prompt. This improves response quality, modularity, and system design.

The application follows a **two-step pipeline**:

1. **Intent Classification** – Detect the user's intent from their message.
2. **Prompt Routing** – Route the message to a specialized expert persona and generate a response.

All requests and routing decisions are logged in a JSON Lines log file for observability.

---

## Supported Intents

The system supports the following intents:

| Intent  | Description                                        |
| ------- | -------------------------------------------------- |
| code    | Programming help, debugging, or software questions |
| data    | Data analysis, statistics, datasets                |
| writing | Writing improvement and feedback                   |
| career  | Career advice and professional guidance            |
| unclear | Ambiguous or unclear user request                  |

---

## System Architecture

User Message
↓
Intent Classification (`classify_intent`)
↓
Intent Label + Confidence Score
↓
Prompt Router (`route_and_respond`)
↓
Specialized Expert Persona
↓
Final Response to User
↓
Log entry stored in `route_log.jsonl`

---

## Expert Personas

### Code Expert

Provides programming solutions with structured code examples and technical explanations.

### Data Analyst

Analyzes datasets and explains patterns using statistical reasoning and visualization suggestions.

### Writing Coach

Identifies writing issues such as passive voice, unclear phrasing, or verbosity and provides improvement suggestions.

### Career Advisor

Offers practical career advice and asks clarifying questions about the user's experience and goals.

---

## Project Structure

```
llm-prompt-router
│
├── app
│   ├── main.py
│   ├── classifier.py
│   ├── router.py
│   ├── prompts.py
│   └── logger.py
│
├── tests
│   └── test_inputs.txt
│
├── route_log.jsonl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Key Components

### classify_intent(message: str)

Detects the user intent and returns a JSON object:

```
{
 "intent": "code",
 "confidence": 0.9
}
```

Handles invalid outputs safely and defaults to `unclear`.

---

### route_and_respond(message, intent_data)

Routes the message to the correct expert persona and generates the final response.

If the intent is **unclear**, the system asks the user for clarification.

---

### Logging System

Every request is logged in:

```
route_log.jsonl
```

Each entry contains:

```
{
 "intent": "code",
 "confidence": 0.9,
 "user_message": "...",
 "final_response": "..."
}
```

This allows tracking and debugging of routing decisions.

---

## Installation

Clone the repository:

```
git clone <repository-url>
cd llm-prompt-router
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Run the program:

```
python app/main.py
```

Example:

```
User: how do i sort list in python

Intent: code
Confidence: 0.9
Response:
Use the Python list.sort() function or sorted().
```

---

## Running with Docker

Build the container:

```
docker-compose build
```

Run the container:

```
docker-compose up
```

---

## Testing

Example test inputs:

```
how do i sort a list of objects in python
explain this sql query
Rewrite this sentence professionally
I'm preparing for a job interview
what is pivot table
hey
```

Expected outputs:

| Input              | Intent  |
| ------------------ | ------- |
| Python sorting     | code    |
| SQL query          | code    |
| Rewrite sentence   | writing |
| Job interview tips | career  |
| Pivot table        | data    |
| hey                | unclear |

---

## Environment Variables

Create a `.env` file using the template:

```
.env.example
```

Example:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit your real API keys.

---

## Technologies Used

- Python
- OpenAI API
- Prompt Engineering
- Docker
- JSON Logging
- CLI Interface

---

## Learning Outcomes

This project demonstrates:

- Prompt engineering for classification
- Intent-based routing architecture
- Modular AI system design
- Error handling and logging
- Containerized deployment with Docker

---

## Conclusion

This project demonstrates how **intent classification and prompt routing** can improve AI application design by delegating tasks to specialized expert prompts rather than relying on a single monolithic prompt.

The system is modular, observable, and easily extensible for additional intents and expert personas.

---
