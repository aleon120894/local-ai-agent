# Local AI Agent

Local AI assistant powered by Ollama and Python.

The project is focused on learning and experimenting with:

* Local LLMs
* AI agents
* Tool calling
* Memory systems
* Retrieval-Augmented Generation (RAG)
* AI security concepts
* OSINT and cybersecurity workflows

---

# Features

Current features:

* Local LLM integration with Ollama
* Simple chatbot interface
* Python-based architecture

Planned features:

* Conversation memory
* Structured JSON outputs
* Tool calling
* Local RAG pipeline
* Vector database integration
* FastAPI backend
* Web UI
* AI security experiments
* OSINT integrations

---

# Project Structure

```text
local-ai-agent/
│
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
│
├── agent/
│   ├── core.py
│   ├── planner.py
│   └── memory.py
│
├── tools/
│   ├── log_tools.py
│   ├── network_tools.py
│   └── osint_tools.py
│
├── prompts/
│   └── system_prompt.txt
│
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   └── ingest.py
│
├── memory/
│
├── tests/
│
├── data/
│   ├── logs/
│   └── documents/
│
└── configs/
```

---

# Tech Stack

* Python
* Ollama
* Qwen / Mistral
* Pydantic
* Rich

Planned:

* FastAPI
* Qdrant
* Redis
* Docker

---

# Installation

## Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/local-ai-agent.git
cd local-ai-agent
```

## Create virtual environment

```bash
python3 -m venv venv
```

## Activate virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Official website:

https://ollama.com

Linux install:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

# Pull a local model

Example:

```bash
ollama pull qwen2.5:1.5b
```

Alternative lightweight models:

* mistral
* gemma3:1b

---

# Run CLI

```bash
python cli.py
```

# Run Back-End server

```bash
uvicorn main:app --reload
```

# Run Front-End

```bash
cd web-ui
npm run dev
```

---

# Example

```text
> Explain TCP briefly

TCP (Transmission Control Protocol) is a reliable transport protocol...
```

---

# Goals

The project is intended as:

* AI engineering learning platform
* Local AI experimentation environment
* AI security research playground
* OSINT automation platform
* Cybersecurity assistant prototype

---

# Planned Roadmap

## v0.1

* [x] Local chatbot
* [x] Ollama integration

## v0.2

- [x] Interactive chat
- [x] Conversation memory
- [x] Agent class
- [x] Conversation reset

## v0.3

* [x] Tools package
* [x] File tool
* [x] Tool registry

## v0.4

* [x] Tool calling
* [x] Structured JSON outputs
* [x] Validation
* [x] JSON parser


## v0.5

* [x] Vector database (FAISS)
* [x] Embedding pipeline
* [x] Retrieval layer (search_docs tool)
* [⚠] RAG integration (basic, not fully stable in agent loop)

## v0.6

* [x] FastAPI backend

## v0.7

* [x] React UI
* [x] Chat page
* [x] Connect to FastAPI
* [x] Display chat history
* [x] Loading indicator
* [x] UI improvements

## TODO
## v0.8

### Memory
* [x] Persistent memory
* [x] Save conversations
* [x] Load conversations

### Knowledge Base
* [ ] Auto-index documents
* [ ] Knowledge base management
* [ ] Rebuild index command

### Pentest Features
* [ ] Nmap output analyzer
* [ ] Pentest RAG dataset
* [ ] Enumeration recommendations

### UI
* [ ] Upload file button
* [ ] Display uploaded files

## v1.0

* [ ] Local AI security assistant

---

# Security Notes

This project may eventually include:

* Tool execution
* Log analysis
* OSINT automation
* Local file access

Never provide unrestricted shell access to AI agents without sandboxing and validation.

---

# Learning Goals

Topics explored in this project:

* AI agents
* Context engineering
* Local LLMs
* Tool orchestration
* Retrieval-Augmented Generation
* Prompt engineering
* AI security
* Prompt injection
* Memory systems

---

# License
MIT License
