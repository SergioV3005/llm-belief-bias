import requests
import re
import json
import csv
import os
import argparse
import matplotlib.pyplot as plt
from collections import defaultdict

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_FILE = os.path.join(BASE_DIR, "test", "belief_bias_questions.json")
CSV_OUTPUT = os.path.join(BASE_DIR, "output", "model_belief_bias_results.csv")
PNG_OUTPUT = os.path.join(BASE_DIR, "output", "model_belief_bias_chart.png")

# Load questions
with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

def query_ollama(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    })
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

def extract_answer(response_text):
    matches = re.findall(r"\b(Valid|Invalid)\b", response_text, re.IGNORECASE)
    if matches:
        return matches[-1].capitalize()  # Take the last occurrence
    else:
        print(" Unable to parse response:", response_text[:100])
        return "Unclear"
    
def run_belief_bias_test():
    print("Running Belief Bias Test on Ollama model:", MODEL_NAME)
    results = []

    for q in questions:

        print(f"\n=== Question {q['id']} ===")
        print(q["prompt"])
        response = query_ollama(q["prompt"])
        parsed = extract_answer(response)
        correct = parsed == q["expected_answer"]
        
        print("Response:\n", response)
        print(f"Extracted answer: {parsed} | Expected: {q['expected_answer']} | Correct: {correct}")

        results.append({
            "id": q["id"],
            "logical_validity": q["logical_validity"],
            "believability": q["believability"],
            "expected_answer": q["expected_answer"],
            "llm_response": response,
            "parsed_answer": parsed,
            "is_correct": correct
        })

    return results

def export_to_csv(results):
    with open(CSV_OUTPUT, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print(f"Results saved to {CSV_OUTPUT}")

def analyze_and_plot(results):
    categories = defaultdict(lambda: {"correct": 0, "incorrect": 0})

    for r in results:
        category = f"{r['logical_validity']}-{r['believability']}"
        if r["is_correct"]:
            categories[category]["correct"] += 1
        else:
            categories[category]["incorrect"] += 1

    # Print summary
    print("\nBelief Bias Summary:")
    for cat, counts in categories.items():
        total = counts["correct"] + counts["incorrect"]
        print(f"{cat}: {counts['correct']} correct out of {total}")

    # Plotting
    labels = list(categories.keys())
    correct_vals = [categories[l]["correct"] for l in labels]
    incorrect_vals = [categories[l]["incorrect"] for l in labels]

    x = range(len(labels))
    plt.figure(figsize=(10, 6))

    # Green for correct, red for incorrect
    plt.bar(x, correct_vals, label='Correct', color='green')
    plt.bar(x, incorrect_vals, bottom=correct_vals, label='Incorrect', color='red')

    plt.xticks(x, labels, rotation=45)
    plt.ylabel("Number of Responses")
    plt.title(f"Belief Bias Evaluation - {MODEL_NAME}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(PNG_OUTPUT)
    print(f"Chart saved as {PNG_OUTPUT}")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Belief Bias Model Runner")
    parser.add_argument("--model_name", type=str, default="qwen3:8b", help="Name of the model to use. Ensure to have previously downloaded the model from Ollama. Default is 'llama3.2:1b'.")
    args = parser.parse_args()

    MODEL_NAME = args.model_name
    
    print(f"Using model: {MODEL_NAME}")
    
    results = run_belief_bias_test()
    export_to_csv(results)
    analyze_and_plot(results)
