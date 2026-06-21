# Data Strategy

## Overview

This project is an AI-Powered Educational Learning Platform that combines Large Language Models (LLMs), Retrieval Augmented Generation (RAG), Vector Databases, Educational Analytics, and Adaptive Learning Systems.

The purpose of the data collection phase is to build a structured knowledge foundation that supports intelligent tutoring, document-based question answering, quiz generation, flashcard generation, study planning, and learning analytics.

---

## Data Collection Goals

The collected data must support the following platform capabilities:

- Chat with Documents
- Retrieval Augmented Generation (RAG)
- Source Citations
- Flashcard Generation
- Quiz Generation
- Adaptive Learning
- Weakness Detection
- Smart Study Planning
- Learning Analytics
- AI Learning Companion

---

## Data Categories

### 1. PDF Knowledge Base

Files:

- operating_systems_notes.pdf
- dbms_notes.pdf
- computer_networks_notes.pdf
- dsa_notes.pdf

Purpose:

The PDF documents act as the primary educational knowledge base. These files will later be parsed, cleaned, chunked, embedded, and stored inside a vector database.

Future Usage:

Upload → Parse → Chunk → Embed → Store → Retrieve → Generate Response

Supports:

- Chat with Documents
- Explain Mode
- Source Citations
- AI Learning Companion

---

### 2. Structured CSV Datasets

Files:

- educational_qa.csv
- student_performance.csv

Purpose:

CSV datasets provide structured information for analytics, evaluation, and adaptive learning.

Supports:

- Weakness Detection Engine
- Adaptive Quiz System
- Learning Analytics
- Study Planner

---

### 3. JSON Educational Content

Files:

- flashcards.json
- quiz_questions.json

Purpose:

JSON files provide structured educational content used for revision and assessment modules.

Supports:

- Flashcard Generator
- Quiz Generator
- Personalized Learning

---

### 4. Subject Mapping Dataset

File:

- subjects_topics.xlsx

Purpose:

Stores relationships between subjects, topics, and difficulty levels.

Supports:

- Smart Study Planner
- Topic Recommendation Engine
- Learning Path Generation

---

## Data Validation Strategy

To maintain dataset quality, structured datasets undergo validation before being used in downstream AI workflows.

Validation checks include:

- Missing value detection
- Duplicate record detection
- Dataset structure verification

The validation process is automated using Python and Pandas through the data_cleaning.py workflow.

---

## Future Expansion

Future versions of the platform may include:

- Previous Year Questions (PYQs)
- Multi-language Educational Content
- Student Learning Histories
- Personalized Recommendation Data
- Collaborative Learning Datasets