import requests
import datetime
import os

# Define the endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# List of models to use for IQ tests
MODEL_NAMES = ["llama3.2:1b", "llama3.2", "mistral", "deepseek-r1:8b"]

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
def query_ollama(model_name, prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": model_name,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

def run_iq_test(model_name):
    print(f"\nRunning High-Range IQ Test on Ollama model: {model_name}")
    results = []
    for q in questions:
        print(f"\n=== Question {q['id']} ===")
        print(q["prompt"])
        answer = query_ollama(model_name, q["prompt"])
        print("Response:\n", answer)
        results.append({
            "question_id": q["id"],
            "question": q["prompt"],
            "answer": answer
        })
    return results

import os

def save_results(results, model_name):
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = f"{output_dir}/iq_test_results_{model_name}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(f"## Question {result['question_id']}\n\n")
            file.write(f"**Question:**\n{result['question']}\n\n")
            file.write(f"**Answer:**\n{result['answer']}\n\n")
        print(f"\nResults saved to {filename}")


if __name__ == "__main__":
    all_results = []
    for model in MODEL_NAMES:
        results = run_iq_test(model)
        save_results(results, model)
        all_results.extend(results)