### Belief Bias evaluation of local LLMs with Ollama 

![Example output: distribution of accuracy for conflictual and non-conflictual items for [qwen3:8b](https://ollama.com/library/qwen3)](https://github.com/user-attachments/assets/0d3472a1-4a51-4941-b20c-805f718eb232)

This project tests Local Large Language Models (LLMs) using **syllogisms** to detect the presence of **Belief Bias (BB)**. It uses [Ollama](https://ollama.com/) to run the models model locally. The test is defined in the file belief_bias_questions.json and it was created by the authors of the repository.\
You can test yourself by clicking [here](https://longocris.github.io/Belief-Bias-Questionnaire/) or you can check out the [quiz repository](https://github.com/LongoCris/Belief-Bias-Questionnaire)

In particular, the following LLMs are tested:
1. [llama3.2:1b](https://ollama.com/library/llama3.2)
2. [Mistral](https://ollama.com/library/mistral)
3. [qwen3:8b](https://ollama.com/library/qwen3)

The experiments involve the test of each LLM (configured with **temperature** equal to 0 and to 0.7) to see the distribution of accuracy in **conflictual** and **non-conflictual** items. In particular, the conflictual items are defined as the valid-inbelievable and the invalid-believable items, while the non-conflictual ones as the valid-believable and invalid-unbelievable ones. If the errors display correlation between the conflictuality and non-conflictuality of the item, then there is a signal of BB.  

![image](https://github.com/user-attachments/assets/f95062ba-f9fc-4a5d-a186-6f7269ca605f)

For a comparison, the test is also experimented on a set of humans.

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
