# Storage Schema

## Repository Data Organization

### Raw Data

Location:

data/raw/

Contains original collected datasets.

Categories:

- PDF Documents
- CSV Datasets
- JSON Datasets
- Excel Datasets

---

### Cleaned Data

Location:

data/cleaned/

Contains validated and standardized datasets prepared for model development.

---

## RAG Storage Workflow

PDF Documents
↓
Document Parsing
↓
Text Cleaning
↓
Chunking
↓
Embedding Generation
↓
Vector Database Storage
↓
Semantic Retrieval

---

## Future Database Entities

The complete platform is expected to store:

- Users
- Documents
- Embeddings
- Chats
- Notes
- Flashcards
- Quizzes
- Quiz Results
- Study Plans
- PYQs
- Evaluation Metrics

---

## Vector Database Metadata

Each stored chunk will maintain:

- Chunk ID
- Document Name
- Source Reference
- Page Number
- Subject
- Upload Timestamp

This metadata enables source citation, retrieval tracking, and explainable AI responses.