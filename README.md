# Hellobooks AI Assistant

## Overview

Hellobooks AI Assistant is a **Retrieval-Augmented Generation (RAG) based AI assistant** that answers accounting-related questions using a small knowledge base.

The system loads accounting documents, converts them into embeddings, stores them in a FAISS vector database, and retrieves relevant information to generate answers.

This project demonstrates a simple **AI-powered bookkeeping knowledge assistant**.

---

## Features

* Knowledge base with accounting topics
* Retrieval-Augmented Generation (RAG)
* HuggingFace sentence embeddings
* FAISS vector database
* CLI-based AI assistant
* Docker container support

---

## Knowledge Base Topics

The assistant includes documents covering:

* Bookkeeping
* Invoices
* Profit & Loss
* Balance Sheet
* Cash Flow

These documents are stored in the `data/` folder as Markdown files.

---

## Project Structure

```
hellobooks-ai-assistant
│
├── data
│   ├── balance_sheet.md
│   ├── bookkeeping.md
│   ├── cash_flow.md
│   ├── invoices.md
│   └── profit_loss.md
│
├── src
│   ├── assistant.py
│   ├── create_vector_db.py
│   └── load_documents.py
│
├── vector_db
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## How It Works

1. Documents are loaded from the `data` folder.
2. Documents are split into smaller text chunks.
3. Embeddings are generated using a HuggingFace model.
4. Embeddings are stored in a **FAISS vector database**.
5. When a user asks a question:

   * Relevant documents are retrieved
   * Context is passed to the language model
   * The assistant generates an answer.

Flow:

```
User Question
      ↓
Retrieve relevant documents
      ↓
Provide context to LLM
      ↓
Generate answer
```

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/hellobooks-ai-assistant.git
cd hellobooks-ai-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Create the Vector Database

Run the following command to generate embeddings and store them in FAISS:

```
python src/create_vector_db.py
```

---

## Run the Assistant

Start the AI assistant:

```
python src/assistant.py
```

Example:

```
Ask accounting question: What is bookkeeping?
```

Output:

```
Bookkeeping is the process of recording financial transactions such as sales, purchases, receipts, and payments.
```

---

## Run Using Docker

Build the Docker image:

```
docker build -t hellobooks-ai .
```

Run the container:

```
docker run -it hellobooks-ai
```

---

## Technologies Used

* Python
* LangChain
* HuggingFace Embeddings
* FAISS Vector Store
* Docker

---

## Author

Atchuth Kumar
