# Do Local LLMs Fall for Belief Bias?  
**Evaluating Syllogistic Reasoning and Cognitive Bias in Offline Language Models**

![Example output: distribution of accuracy for conflictual and non-conflictual items for qwen3:8b](https://github.com/user-attachments/assets/0d3472a1-4a51-4941-b20c-805f718eb232)

This project investigates whether **local Large Language Models (LLMs)** running via [Ollama](https://ollama.com/) are subject to **Belief Bias (BB)**—a cognitive bias where logically invalid but *believable* conclusions are wrongly accepted. It compares model performance against human reasoning using a **syllogistic logic test**.

You can explore or take the test yourself:  
[Belief Bias Questionnaire (Live)](https://longocris.github.io/Belief-Bias-Questionnaire)  
[Questionnaire GitHub Repository](https://github.com/LongoCris/Belief-Bias-Questionnaire)

---

## What Is Belief Bias?

**Belief Bias** refers to the tendency to judge arguments based on the believability of their conclusions rather than their logical validity. This project builds on **Dual-Process Theory**:
- **System 1**: Fast, intuitive, belief-driven reasoning.
- **System 2**: Slow, analytical, logic-based reasoning.

By designing a logic test that creates **conflictual cases** (logical validity contradicts believability) and **non-conflictual cases** (validity aligns with belief), we assess whether local LLMs rely more on intuition (like humans) or on formal logic.

---

## Methodology

We designed a **16-item syllogistic test** comprising:
- 4 categories × 4 items each:
  - Valid–Believable (VB)
  - Invalid–Believable (IB)
  - Valid–Unbelievable (VU)
  - Invalid–Unbelievable (IU)
- Difficulty balance: 3 regular (2-premise) and 1 hard (3-premise) syllogism per category.
- Human participants had 20s per question to simulate System 1 bias.
- Each model was prompted in a controlled format:

```text
You will be shown a syllogism.
Your task is to determine whether the conclusion logically follows from the premises,
regardless of whether the conclusion is factually true or believable.
...
Question: Is the conclusion logically valid? Answer with Valid or Invalid and explain your reasoning.
```

## Models Evaluated

We tested the following local models with **Ollama** under two configurations (temperature = 0.0 and 0.7):

| Model         | Parameters | Type                          |
|---------------|------------|-------------------------------|
| LLaMa 3.2:1b  | 1B         | Lightweight, baseline         |
| Mistral:7b    | 7B         | Long-context, reasoning-tuned |
| Qwen 3:8b     | 8B         | Reasoning-focused, instruction-tuned |

---

## Results Summary

| Model         | Temperature | Accuracy     | Belief Bias Signal |
|---------------|-------------|--------------|---------------------|
| LLaMa3.2:1b   | 0.0         | Low          | Present             |
| LLaMa3.2:1b   | 0.7         | Low–Medium   | Present             |
| Mistral:7b    | 0.0         | Medium       | Moderate            |
| Mistral:7b    | 0.7         | Medium       | Moderate            |
| **Qwen3:8b**  | **0.0**     | **High**     | **Absent**          |
| Qwen3:8b      | 0.7         | High         | Low                 |

**Key Insight:** Only **Qwen 3:8b at temperature 0** showed strong logical consistency and no detectable belief bias.

---

## Human Benchmark

A control group of **9 human participants** (with minimum B2 English and Bachelor's degree) completed the same questionnaire. They exhibited **clear Belief Bias**, particularly in accepting *invalid–believable* conclusions. This mirrors known results in cognitive psychology and validates the questionnaire design.

---

## Conclusions

- **Belief Bias is not unique to humans.** Smaller, older LLMs can replicate it—especially under conflictual item types.
- **Architecture > Temperature.** Model scale and training strategy are more decisive than temperature for BB resistance.
- **Qwen 3:8b** is the most aligned with formal logic, showing near-complete immunity to BB at T=0.

---

## Future Work

The project can be expanded by:
- Testing **larger or more diverse models** (e.g., Qwen 14b+, LLaMa 3.4, Mixtral).
- **Improving the human study** with more participants and tracking response times.
- Applying **statistical analysis** to correlate accuracy drop with syllogism conflictuality.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SergioV3005/llm-belief-bias.git
cd llm-belief-bias
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama and Pull a Model
Install Ollama: [https://ollama.com/download](https://ollama.com/download)

Example for Mistral:
```bash
ollama pull mistral
ollama run mistral
```

The script communicates with `http://localhost:11434` by default.

---

## License

MIT License — free to use and modify.
