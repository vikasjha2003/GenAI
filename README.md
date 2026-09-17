# GenAI

This repository is a personal learning repo where I explore Generative AI, LangChain, RAG, and agent/tool workflows while building small experiments and demos.

The goal is simple: learn by building. Most files here are practical experiments rather than polished production code.

## Repository structure

- `LangChain_Models/`
  - Experiments with LangChain model integrations
  - Includes chat models, embedding models, LLM examples, and sample projects
- `RAG/`
  - Retrieval-Augmented Generation experiments
  - Includes database setup, document loaders, retrievers, and vector store code
- `tools_and_agents/`
  - Experiments focused on tools, agents, runnable chains, and agent-style workflows

## Main topics covered

- Large Language Models (LLMs)
- Chat models from different providers
- Embedding models
- Prompt engineering basics
- Semantic search and retrieval
- Vector databases
- RAG pipelines
- Tool calling and model/tool interaction
- Agentic patterns and runnable workflows

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/vikasjha2003/GenAI.git
   cd GenAI
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   # or
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Add environment variables if needed
   Some examples may require API keys or model access. Create a `.env` file and include the required values.

## Notes

- This repo is meant for learning and experimentation.
- Code may be rough, exploratory, or based on tutorials.
- The focus is understanding how GenAI systems work in practice.

## Learning journey

This project is a collection of experiments across:

- LangChain basics
- LLM integration
- Embeddings and vector search
- RAG pipelines
- Tools and agent orchestration

## License

This project is for learning purposes and is not tied to a formal production license unless specified elsewhere.
