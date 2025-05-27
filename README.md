### Belief Bias evaluation of local LLMs with Ollama 

![Example output: distribution of accuracy for conflictual and non-conflictual items for [qwen3:8b](https://ollama.com/library/qwen3)](https://github.com/user-attachments/assets/0d3472a1-4a51-4941-b20c-805f718eb232)

This project tests Local Large Language Models (LLMs) using **syllogisms** to detect the presence of **Belief Bias (BB)**. It uses [Ollama](https://ollama.com/) to run the models model locally. The test is defined in the file **belief_bias_questions.json** and it was created by the authors of the repository.\

**You can test yourself by clicking [here](https://longocris.github.io/Belief-Bias-Questionnaire/) or you can check out the [quiz repository](https://github.com/LongoCris/Belief-Bias-Questionnaire)**

In particular, the following LLMs are tested:
1. [llama3.2:1b](https://ollama.com/library/llama3.2): a lightweight baseline model from LLaMa 3.2 family
2. [Mistral](https://ollama.com/library/mistral): a 7b model designed for long-context reasoning
3. [qwen3:8b](https://ollama.com/library/qwen3): a very recent model optimized for instructions and logical tasks

The experiments involve the test of each LLM (configured with **temperature** equal to 0 and to 0.7) to see the distribution of accuracy in **conflictual** and **non-conflictual** items. 

In particular, the conflictual items are defined as the valid-inbelievable and the invalid-believable items, while the non-conflictual ones as the valid-believable and invalid-unbelievable ones. If the errors display correlation between the conflictuality and non-conflictuality of the items, then there is a signal of BB.  

![image](https://github.com/user-attachments/assets/f95062ba-f9fc-4a5d-a186-6f7269ca605f)

For a comparison, the test is also experimented on a set of humans, as shown in the presentation and in the report.

### Belief Bias Questionnaire

The questionnaire consists of **16 items** balanced across the four categories:
* Valid-Believable (VB): 4 items
* Invalid-Believable (IB): 4 items
* Valid-Unbelievable (VU): 4 items 
* Invalid-Unbelievable (IU): 4 items

In each category, three items are of **regular** difficulty (being composed of two premises and one conclusion), while one item is **hard** (being composed of three premises and the conclusion). This, for the set of humans, is done to avoid adaptation to the difficulty of the item.

For the humans, one neutral item was added to the questionnaire to stimulate **attention**. Each item required valid or invalid responses within **20 seconds**, to encourage intuitive processing. One item included open-ended explanation to examine the reasoning behind the decision and to compare it to LLMs.

### Results

| Model         | Temperature | Average Accuracy | Belief Bias Signal |
|---------------|-------------|------------------|--------------------|
| Llama3.2:1b   | 0.0         | Low              | Present            |
| Llama3.2:1b   | 0.7         | Low–Medium       | Present            |
| Mistral:7b    | 0.0         | Medium           | Moderate           |
| Mistral:7b    | 0.7         | Medium           | Moderate           |
| **Qwen3:8b**  | **0.0**     | **High**         | **Absent**         |
| Qwen3:8b      | 0.7         | High             | Low                |

The precise distribution of the errors can be found in the presentation.

As for the control group of humans (balanced gender, minimum B2 english and Bachelor's degree holders), the results showed expression of BB, especially due to the time pressure.

### Conclusions

BB is not unique to humans. Some LLMs mimic it under certain configurations. Model complexity and architecture (not temperature alone) determine the expression of BB.

For deeper insights, see our report.

## Setup Instructions

Followingly, a quick-guide on how to reproduce the project.

### 1. Clone the Repository
```bash
bash
git clone https://github.com/SergioV3005/llm-belief-bias.git
cd llm-belief-bias
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Activate it
# macOS/Linux
source venv/bin/activate
# Windows PowerShell
venv\Scripts\activate
```

### 3. Install Dependencies

To install the needed libraries in the virtual enviroment, run the following command.

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Follow installation instructions for your OS here:  
[https://ollama.com/download](https://ollama.com/download)

### 5. Start Ollama and Download the Model

For example, in Mistral case, the command is as follows.

```bash
ollama pull mistral
```

Then you can run the model manually if needed:

```bash
ollama run mistral
```

The script communicates with http://localhost:11434 by default.

## License

MIT License. Free to use and modify.
