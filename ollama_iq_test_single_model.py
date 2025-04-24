"""
In this script, we will run a high-range IQ test using the Ollama on local LLMs
"""

import requests

# Select the model and define the endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  

# Define IQ questions
questions = [
    {
        "id": 1,
        "prompt": "IQ Test Item #1:\n\nComplete the sequence logically: 2, 6, 12, 20, 30, ?\nExplain your reasoning.",
    },
    {
        "id": 2,
        "prompt": "IQ Test Item #2:\n\nComplete the sequence logically: 1, 4, 9, 16, 25, ?\nExplain your reasoning.",
    },
    {
        "id": 3,
        "prompt": "IQ Test Item #3:\n\nIf some bloops are razzies, and all razzies are lazzies, are all bloops definitely lazzies?\nExplain using syllogistic logic.",
    },
]

# Query the model
def query_ollama(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

def run_iq_test():
    print("Running High-Range IQ Test on Ollama model:", MODEL_NAME)
    results = []
    for q in questions:
        print(f"\n=== Question {q['id']} ===")
        print(q["prompt"])
        answer = query_ollama(q["prompt"])
        print("Response:\n", answer)
        results.append({
            "question_id": q["id"],
            "question": q["prompt"],
            "answer": answer
        })
    return results

if __name__ == "__main__":
    run_iq_test()