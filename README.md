# **DocChat Lanka** - File Processor & Q&A System

**DocChat Lanka** is a smart file processing and document Q&A web application, built using Meta LLAMA 3.1 (70B) model with Groq hardware acceleration, ChromaDB for storing and retrieving document embeddings, and Langchain for handling Retrieval Augmented Generation (RAG) queries. The app allows users to upload documents, ask questions about their contents, and receive accurate answers based on the file's data.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
  - [Running the Application](#running-the-application)
  - [Embedding Persistence](#embedding-persistence)
- [Usage Guide](#usage-guide)
- [Example Queries](#example-queries)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Screenshot](#Screenshot)
- [License](#license)
- [Credits](#credits)

---

## Project Overview

DocChat Lanka allows users to upload documents (PDFs), and using advanced AI-based models like Meta LLAMA 3.1 and Groq hardware acceleration, it processes these documents into manageable text chunks. You can then query the content of these documents in natural language, and the system will provide responses that are contextually based on the document content. All queries and answers are stored and made accessible via a history feature.

This app is particularly useful for processing large amounts of textual information and retrieving concise answers efficiently, with support for complex document queries.

---

## Key Features

- **Document Upload**: Upload PDF files to be processed and stored in ChromaDB.
- **Text Chunking**: Efficiently split long documents into smaller, manageable text chunks for querying.
- **Question-Answering (Q&A)**: Ask questions about the uploaded documents and receive AI-powered answers.
- **Document History**: Track previously uploaded documents and their corresponding queries and answers.
- **Efficient Embedding Storage**: Use ChromaDB to store embeddings of documents and quickly retrieve relevant sections for answering queries.
- **Groq Hardware Acceleration**: Accelerate the Q&A process with Groq API for faster responses.

---

## Tech Stack

- **Language Model**: Meta LLAMA 3.1 (70B)
- **Hardware Acceleration**: Groq hardware API
- **Database**: ChromaDB for storing embeddings and managing document queries
- **Frameworks**: 
  - **Langchain** for Retrieval Augmented Generation (RAG)
  - **Flask** for the web application backend
- **Frontend**: Bootstrap 5.3 for a responsive and visually appealing user interface
- **Embedding Model**: HuggingFace Sentence Transformers for text embeddings
- **Document Processing**: Unstructured Python library for document parsing and text extraction from PDFs

---

## Project Architecture

1. **Document Upload**: Users upload a PDF, which is processed and stored as embeddings in ChromaDB.
2. **Text Splitter**: Documents are split into manageable chunks for faster and more accurate querying.
3. **Retrieval**: When a question is asked, the relevant document chunks are retrieved using ChromaDB and Langchain.
4. **Q&A**: The system uses Meta LLAMA 3.1 to generate a response to the user’s query, utilizing the relevant chunks from the document.
5. **Response Output**: The answer is displayed on the UI, with the option to view document history and previous queries.

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or above
- Pip (Python package installer)
- Virtualenv (optional, but recommended)
- Groq API key for hardware acceleration
- HuggingFace API token for model access

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pahinithi/DocChat-Lanka-File-Processor-Q-A-System-using-Meta-LLAMA-RAG-Groq-Langchain-LLM
   cd DocChat-Lanka
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes all necessary dependencies such as Flask, Langchain, ChromaDB, transformers, sentence-transformers, and unstructured.

### Setting Up Environment Variables

You need to set up some environment variables for Groq API and HuggingFace token.

1. **Create a `.env` file in the root directory:**

   ```bash
   touch .env
   ```

2. **Add your keys:**

   ```bash
   GROQ_API_KEY="your_groq_api_key"
   HUGGINGFACE_API_KEY="your_huggingface_api_key"
   ```

### Running the Application

After setting up the environment variables:

1. **Run the Flask application:**

   ```bash
   python main.py
   ```

2. **Access the web app:**

   Open your browser and go to `http://127.0.0.1:5000/`.

### Embedding Persistence

The embeddings of the uploaded documents are stored in the `doc_db/` folder. This allows faster retrieval and reuse of document data during the question-answering process.

---

## Usage Guide

1. **Upload a PDF**: Click the "Upload Document" button and choose a PDF file to upload. The file is parsed, and its text is split into chunks for processing.
2. **Ask Questions**: After the file is uploaded, you can type a question related to the document into the input box and click "Submit".
3. **View Responses**: The system will return an AI-generated response based on the document's content.
4. **Check History**: Click on the "History" tab to view all previously uploaded files and their respective queries and answers.

---

## Example Queries

- **"What is the conclusion of this document?"**
- **"Summarize the second chapter of the document."**
- **"List the key points discussed in the section on project management."**
- **"What are the author’s recommendations for future work?"**

---

## Project Structure

```
DocChat-Lanka/
│
├── templates/
│   ├── index.html       # Main interface for file upload and querying
│   ├── history.html     # Page displaying processed document history
│
├── main.py              # Flask backend application
├── requirements.txt     # Python dependencies file
├── .env                 # Environment variables (API keys)
├── README.md            # Readme file (this file)
└── doc_db/              # Folder for storing ChromaDB embeddings
```

---

## Future Enhancements

- **Support for more file formats**: Currently, only PDFs are supported, but we plan to add DOCX and TXT support.
- **Multi-language support**: Expanding the app to handle multilingual documents and queries.
- **Improved UI**: Enhance the user interface with interactive visualizations and improved document navigation.

---

## Screenshot

<img width="1728" alt="LLM06" src="https://github.com/user-attachments/assets/d652511f-9180-4461-abe4-0a3c1c3dc727">


<img width="1728" alt="LLM06" src="https://github.com/user-attachments/assets/755e14fe-3c5c-4bf0-8655-f3bab89f10cf">

Demo:(["https://drive.google.com/file/d/1tmUCz7K7y6rKIDPT-ZIXCpdHoaMdb-tJ/view?usp=sharing"])

---

## License

This project is licensed under the MIT License.

---

## Credits

- **Meta**: For providing the LLAMA 3.1 model used in this project.
- **Groq**: For hardware acceleration that enhances model performance.
- **Langchain & ChromaDB**: For handling the document retrieval and query processes.
- **Unstructured**: For helping with document parsing and text extraction.

Developed by [Nithilan](https://github.com/Pahinithi).  
For any questions or feedback, feel free to contact me at `nithilan32@gmail.com`.
