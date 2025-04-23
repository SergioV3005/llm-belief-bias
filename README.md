### Ollama IQ Test Project

This project tests a local large language model (LLM) using IQ logic questions. It uses [Ollama](https://ollama.com/) to run the `mistral` model locally and queries it via a Python script.

## Setup Instructions

Followingly, a quick-guide on how to reproduce the project.

### 1. Clone the Repository

```bash
git clone https://github.com/SergioV3005/ollama-iq-test.git
cd ollama-iq-test
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

Currently, only `requests` is required.

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Follow installation instructions for your OS here:  
👉 [https://ollama.com/download](https://ollama.com/download)

### 5. Start Ollama and Download the Model

```bash
ollama pull mistral
```

Then you can run the model manually if needed:
```bash
ollama run mistral
```

The script communicates with `http://localhost:11434` by default.

## License

MIT License. Free to use and modify.