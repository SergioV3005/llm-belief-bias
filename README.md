### Belief Bias evaluation of local LLMs with Ollama 

![Example output: distribution of accuracy for conflictual and non-conflictual items for [qwen3:8b](https://ollama.com/library/qwen3)](https://github.com/user-attachments/assets/0d3472a1-4a51-4941-b20c-805f718eb232)

This project tests local large language model (LLM) using syllogisms to detect the presence of belief bias. It uses [Ollama](https://ollama.com/) to run the models model locally. The test is defined in the file belief_bias_questions.json.

In particular, the following LLMs are tested:
1. [llama3.2:1b](https://ollama.com/library/llama3.2)
2. [Mistral](https://ollama.com/library/mistral)
3. [qwen3:8b](https://ollama.com/library/qwen3)

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
