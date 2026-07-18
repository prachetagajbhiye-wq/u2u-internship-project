# 🎓 AI-Powered Educational Learning Platform

## Project Overview

The AI-Powered Educational Learning Platform is a web application that helps students learn using Artificial Intelligence and Retrieval-Augmented Generation (RAG).

Users can ask educational questions through a chat interface, upload learning materials, and receive AI-generated answers based on a custom knowledge base.

---

## Features

- 🤖 AI-powered educational chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using ChromaDB
- 📄 PDF document support
- 📊 CSV dataset support
- 📑 Excel file support
- 📤 Upload educational documents
- 💬 Interactive chat interface
- 📋 Copy responses
- 🗑 Clear chat
- 💡 Suggested questions
- 📚 Source citations

---

## Technology Stack

### Frontend

- React
- Vite
- CSS

### Backend

- Python
- Flask

### AI

- Google Gemini 2.5 Flash
- Sentence Transformers (all-MiniLM-L6-v2)

### Vector Database

- ChromaDB

### Document Processing

- PyMuPDF
- Pandas

---

## Project Structure

```text
u2u-internship-project/

├── frontend/
├── src/
├── data/
├── documents/
├── chroma_db/
├── reports/
├── presentation/
└── README.md
```

---

## How It Works

1. User enters a question.
2. The question is converted into an embedding.
3. ChromaDB retrieves the most relevant document chunks.
4. Retrieved context is sent to Google Gemini.
5. Gemini generates the final answer.
6. The answer and source documents are displayed.

---

## Team Members

- Pracheta Rajendra Gajbhiye
- Kunjal Praveen Divecha
- Srushti Sharad Dangre
- Mayuri Mahadev Sonwane
- Trisha Dash
- Shravani Jaiprakash Gajbhiye
- Pari Shukla
- Sachi Sachin Patil
- Ashwini Vitthalrao Lamdade
- Samiksha Sanjay More

---

## Presentation

The project presentation is available in the `presentation/` folder.

---

## Demo Video

(Add the Google Drive or YouTube link after recording.)

---

## Future Improvements

- Automatic indexing of uploaded documents
- User authentication
- Chat history
- Voice interaction
- Cloud deployment

---

## Status

Completed as part of the U2U Internship Project.